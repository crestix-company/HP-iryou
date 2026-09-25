from pathlib import Path
import html,json,os,hashlib
ROOT=Path(__file__).parent
OUT=ROOT/'dist'
BASE_PATH=os.environ.get('SITE_BASE_PATH','').rstrip('/')
if BASE_PATH and (not BASE_PATH.startswith('/') or '..' in BASE_PATH):
 raise ValueError('SITE_BASE_PATH must be an absolute URL path prefix')
services=[
{'slug':'medical-target-plus','name':'Medical Target +','tag':'ターゲティング広告','short':'比較・検討のタイミングを、逃さない。','desc':'診療圏や関心に合わせて配信対象を設計。医院を検討する方へ、貴院の特徴を届けます。','color':'navy','visual':'target'},
{'slug':'medical-map','name':'Medical Map','tag':'MEO・Googleマップ運用','short':'地域の検索から、来院のきっかけを。','desc':'医院情報の整備から投稿・口コミ返信、順位の確認まで。Googleマップの運用を継続的に支えます。','color':'','visual':'map'},
{'slug':'medical-map-plus','name':'Medical Map +','tag':'Googleマップ広告','short':'いま近くで探している人に、届ける。','desc':'地域と診療科に合わせて広告を配信。Googleマップで医院を探す患者さまとの接点をつくります。','color':'violet','visual':'mapad'},
{'slug':'survey-plus','name':'アンケートプラス','tag':'患者アンケート・口コミ支援','short':'患者さまの声を、医院の力に。','desc':'来院後の声を集め、院内改善と口コミの接点へ。患者体験を知る仕組みを整えます。','color':'teal','visual':'survey'},
{'slug':'line-plus','name':'LINEプラス','tag':'LINE拡張ツール・運用支援','short':'来院した、その先もつながる。','desc':'タグ管理、配信の自動化、予約への案内まで。LINE拡張ツールで、患者さまとの接点を整えます。','color':'green','visual':'line'},
{'slug':'mynavi-clinic','name':'マイナビクリニックナビ','tag':'メディア掲載支援','short':'医院の魅力に、出会う場所を増やす。','desc':'地域・診療科で医院を探す方へ、紹介記事でアプローチ。掲載に向けた準備を支援します。','color':'sand','visual':'media'}]
def visual(s):
 return f'<div class="product-visual from-pdf"><img src="/assets/{s["slug"]}.webp" alt="{s["name"]} サービス資料" width="1440" height="810" loading="lazy"></div>'
def card(s):
 title='<span class="title-part">マイナビ</span><wbr><span class="title-part">クリニックナビ</span>' if s['slug']=='mynavi-clinic' else s['name']
 jp=' jp' if s['slug'] in ['survey-plus','line-plus','mynavi-clinic'] else ''
 return f'<a class="product-card reveal" href="/services/{s["slug"]}/">{visual(s)}<div class="card-body"><span class="product-tag">{s["tag"]}</span><h3 class="{jp}">{title}</h3><p>{s["desc"]}</p><div class="card-bottom">サービスを詳しく見る<span class="arrow-circle" aria-hidden="true">↗</span></div></div></a>'
def cta():
 return '<section class="contact-band"><div class="wrap contact-inner"><div><div class="eyebrow">CONTACT</div><h2>Let’s talk.</h2><p class="contact-heading">クリニックの次の一歩を、ここから。</p><p>いまの課題や、これから実現したいことをお聞かせください。</p></div><a class="contact-link" href="/contact/"><span>お問い合わせ</span><span class="contact-arrow" aria-hidden="true">↗</span></a></div></section>'
def navigation(current):
 links=[('/products/','PRODUCTS','プロダクト'),('/development/','DEVELOPMENT','AI開発'),('/consulting/','CONSULTING','Webコンサルティング'),('/company/','COMPANY','会社情報'),('/contact/','CONTACT','お問い合わせ')]
 result=[]
 for href,english,label in links:
  active=current==href or (href=='/products/' and current.startswith('/services/'))
  attrs=' class="nav-contact"' if href=='/contact/' else ''
  if active:attrs+=f' aria-current="{"page" if current==href else "location"}"'
  result.append(f'<a href="{href}"{attrs}><span class="nav-en">{english}</span><span class="nav-ja">{label}</span></a>')
 return ''.join(result)

def breadcrumb(label):
 return f'<div class="wrap breadcrumb"><a href="/">トップ</a><span>/</span><span>{label}</span></div>'

def page(title,desc,body,current='/'):
 css_revision=hashlib.sha256((OUT/'style.css').read_bytes()).hexdigest()[:10]
 js_revision=hashlib.sha256((OUT/'app.js').read_bytes()).hexdigest()[:10]
 icon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="%230869ed"/><path d="M29 12a12 12 0 1 0 0 16" fill="none" stroke="white" stroke-width="5"/></svg>'
 service_links=''.join(f'<a href="/services/{s["slug"]}/">{s["name"]}</a>' for s in services)
 return f'''<!doctype html><html lang="ja"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | CRESTIX</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#ffffff"><meta property="og:title" content="{html.escape(title)} | CRESTIX"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><link rel="icon" type="image/svg+xml" href='{icon.replace("<svg", "data:image/svg+xml,<svg", 1)}'><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="/style.css?v={css_revision}"><script defer src="/app.js?v={js_revision}"></script></head><body><a class="skip" href="#main">本文へ移動</a><header class="header"><div class="wrap header-inner"><a class="brand" href="/" aria-label="CRESTIX トップ"><img src="/assets/crestix-logo.png" alt="CRESTIX" width="152" height="42"><span class="brand-note">PRODUCTS &amp;<br>WEB CONSULTING</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation" aria-label="メニューを開く">☰</button><nav class="nav" id="navigation" aria-label="メインナビゲーション">{navigation(current)}</nav></div></header><main id="main">{body}</main><footer class="footer corporate-footer"><div class="wrap"><div class="footer-directory"><div class="footer-identity"><a href="/" aria-label="CRESTIX トップ"><img src="/assets/crestix-logo.png" alt="CRESTIX" width="152" height="43" loading="lazy"></a><p>クリニックの成長を、<br>AIとデジタルで。</p><span>株式会社Crestix</span></div><nav class="footer-service-nav" aria-label="サービス一覧"><a class="footer-nav-title" href="/products/">PRODUCTS &amp; SERVICES ↗</a><div>{service_links}</div></nav><nav class="footer-corporate-nav" aria-label="企業・事業情報"><span class="footer-nav-title">CRESTIX</span><a href="/development/">AIを活用した開発</a><a href="/consulting/">Webコンサルティング</a><a href="/company/">会社情報</a><a href="/contact/">お問い合わせ</a></nav></div><div class="footer-bottom"><span>© 2026 Crestix Inc.</span><a href="https://www.crestix.jp/privacy.html" target="_blank" rel="noopener">プライバシーポリシー ↗</a><a href="#main">PAGE TOP ↑</a></div><div class="footer-wordmark" aria-hidden="true">CRESTIX</div></div></footer></body></html>'''

def write(path,title,desc,body):
 p=OUT/path
 p.parent.mkdir(parents=True,exist_ok=True)
 current='/' if str(path)=='index.html' else '/'+str(path).removesuffix('index.html')
 document=page(title,desc,body,current)
 p.write_text(document.replace('href="/',f'href="{BASE_PATH}/').replace('src="/',f'src="{BASE_PATH}/'))
