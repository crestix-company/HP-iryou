from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
import argparse, json

parser = argparse.ArgumentParser(description='Verify the generated website.')
parser.add_argument('--base-path', default='')
parser.add_argument('--origin', help='Optional HTTP origin for all local resource checks.')
args = parser.parse_args()
prefix = args.base_path.rstrip('/')
base = Path(__file__).parent / 'dist'

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids, self.h1 = [], set(), 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'h1':
            self.h1 += 1
        for key in ('href', 'src'):
            if key in a:
                self.refs.append(a[key])

errors, resources = [], set()
pages = list(base.rglob('*.html'))
for page in pages:
    text = page.read_text()
    doc = Document()
    doc.feed(text)
    if doc.h1 != 1:
        errors.append(f'{page}: expected exactly one h1')
    for bad in ('TODO', 'Lorem ipsum', '\ufffd'):
        if bad in text:
            errors.append(f'{page}: unfinished content {bad}')
    for ref in doc.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        path = unquote(url.path)
        if path:
            if not path.startswith(prefix + '/'):
                errors.append(f'{page}: incorrect base path: {ref}')
                continue
            target = base / path[len(prefix):].lstrip('/')
            resources.add(url.path)
        else:
            target = page
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file() or not target.stat().st_size:
            errors.append(f'{page}: missing resource: {ref}')
            continue
        if url.fragment:
            linked = Document()
            linked.feed(target.read_text())
            if unquote(url.fragment) not in linked.ids:
                errors.append(f'{page}: missing anchor: {ref}')

assert len(pages) == 10, f'Expected 10 pages, found {len(pages)}'
assert 'クリニックの成長を、' in (base / 'index.html').read_text()
assert 'AIとデジタルで。' in (base / 'index.html').read_text()
assert (base / '.nojekyll').is_file()
assert not list(base.rglob('*.pdf')), 'Source PDFs must not be published'
if args.origin:
    for path in sorted(resources):
        try:
            with urlopen(args.origin.rstrip('/') + path, timeout=20) as response:
                if response.status != 200:
                    errors.append(f'HTTP {response.status}: {path}')
        except Exception as error:
            errors.append(str(error))
print(json.dumps({'pages': len(pages), 'resources': len(resources), 'base_path': prefix,
                  'errors': errors}, ensure_ascii=False))
assert not errors
