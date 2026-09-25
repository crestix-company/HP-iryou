from pathlib import Path
from build import OUT, services, card, write, breadcrumb, cta


def build_corporate():
    home = '''
<section class="hero corporate-home-hero">
  <img class="hero-art" src="/assets/hero.webp" alt="" width="1536" height="1024" fetchpriority="high">
  <div class="wrap hero-inner">
    <div class="eyebrow">CLINIC GROWTH PARTNER</div>
    <h1>クリニックの成長を、<br><em>AIとデジタルで。</em></h1>
    <p class="hero-copy">クリニック向けプロダクトと、Webコンサルティング。<br>AIを活かした開発・分析・制作で、<br>医院の集患と、患者さまとの接点づくりを支えます。</p>
    <div class="hero-actions"><a class="button" href="/products/">サービスを見る<span class="arrow" aria-hidden="true">↗</span></a><a class="text-link" href="/company/">Crestixについて<span aria-hidden="true">↗</span></a></div>
  </div>
  <span class="hero-side">CRESTIX — PRODUCTS &amp; WEB CONSULTING</span>
</section>
<section class="section home-business">
  <div class="wrap">
    <div class="section-head reveal"><div><div class="eyebrow">OUR BUSINESS</div><h2>プロダクトと戦略で、<br>医院の次の一歩を。</h2></div><p>必要な仕組みを届けること。<br>その仕組みを、医院の成長につなげること。<br>Crestixは、その両方に取り組みます。</p></div>
    <div class="business-grid">
      <a class="business-card reveal" href="/products/">
        <div class="business-art product-collage" aria-hidden="true"><img src="/assets/medical-map.webp" alt="" width="1440" height="810" loading="lazy"><img src="/assets/medical-target-plus.webp" alt="" width="1440" height="810" loading="lazy"><img src="/assets/line-plus.webp" alt="" width="1440" height="810" loading="lazy"></div>
        <div class="business-card-copy"><span class="business-label">01 / PRODUCTS &amp; SERVICES</span><h3>クリニック向けプロダクト</h3><p>地図検索、広告、口コミ、LINE、メディア。<br>6つのサービスで、患者さまとの接点を整えます。</p><span class="business-card-link">プロダクト一覧へ<span class="arrow-circle" aria-hidden="true">↗</span></span></div>
      </a>
      <a class="business-card reveal" href="/consulting/">
        <div class="business-art"><img class="business-photo" src="/assets/consulting.webp" alt="データをもとに医院の施策を検討する様子" width="1536" height="1024" loading="lazy"></div>
        <div class="business-card-copy"><span class="business-label">02 / WEB CONSULTING</span><h3>Webコンサルティング</h3><p>医院の課題を整理し、戦略から実行・改善へ。<br>専属コンサルタントが、次の一手を設計します。</p><span class="business-card-link">Webコンサルティングへ<span class="arrow-circle" aria-hidden="true">↗</span></span></div>
      </a>
    </div>
  </div>
</section>
<section class="home-links"><div class="wrap home-links-grid">
  <a class="destination-card development-destination reveal" href="/development/"><div class="eyebrow">AI &amp; DEVELOPMENT</div><h2>AIを活かした、<br>つくる力。</h2><p>設計・実装・改善にAIを活用。<br>医院の課題を、使える仕組みに。</p><span>AIを活用した開発<span class="arrow-circle" aria-hidden="true">↗</span></span><div class="destination-symbol" aria-hidden="true">AI<span>+</span></div></a>
  <a class="destination-card company-destination reveal" href="/company/"><div class="eyebrow">COMPANY</div><h2>医療の可能性を、<br>デジタルでひらく。</h2><p>クリニックの隣で、考え続ける。<br>Crestixの考え方と会社情報をご紹介します。</p><span>私たちについて<span class="arrow-circle" aria-hidden="true">↗</span></span></a>
</div></section>
''' + cta()
    write(Path('index.html'), 'クリニックの成長を、AIとデジタルで。', 'クリニック向けプロダクトとWebコンサルティングのCrestix。AIを活かした開発・分析・制作で、医院の成長を支援します。', home)

    products = breadcrumb('プロダクト一覧') + '''
<section class="page-intro"><div class="wrap page-intro-grid"><div><div class="eyebrow">PRODUCTS &amp; SERVICES</div><h1>プロダクト一覧</h1><p class="page-lead">集患から、来院後のつながりまで。</p><p>地図検索、広告、口コミ、LINE、メディア。<br>医院の課題と患者さまの行動に合わせて、サービスを組み合わせます。</p></div><div class="service-count" aria-label="6つのサービス"><strong>06</strong><span>PRODUCTS &amp; SERVICES</span></div></div></section>
<section class="catalog-section"><div class="wrap"><div class="product-grid">''' + ''.join(card(s) for s in services) + '''</div><p class="products-note">マイナビクリニックナビは株式会社マイナビが運営するメディアです。Crestixは掲載をご支援します。</p></div></section>
<section class="detail-section"><div class="wrap choice-guide"><div><div class="eyebrow">FIND YOUR NEXT STEP</div><h2>何から始めるかも、<br>一緒に考えます。</h2></div><div><p>医院の課題によって、必要な施策や優先順位は変わります。現状を整理するところから、導入後の運用までご相談いただけます。</p><a class="text-link" href="/consulting/">Webコンサルティングを見る<span aria-hidden="true">↗</span></a></div></div></section>
''' + cta()
    write(Path('products/index.html'), 'クリニック向けプロダクト一覧', 'Medical Map、Medical Map+、Medical Target+、アンケートプラス、LINEプラス、マイナビクリニックナビ。クリニックの患者接点を支える6サービス。', products)

    development = breadcrumb('AIを活用した開発') + '''
<section class="development-hero"><div class="wrap development-hero-grid"><div><div class="eyebrow">AI &amp; DEVELOPMENT</div><h1>AIを、つくる力に。<br><span class="title-part">医院の課題を、</span><wbr><span class="title-part">仕組みに。</span></h1><p class="page-lead">AIを活用したプロダクト・Web開発</p><p>設計・実装・改善のプロセスにAIを取り入れ、担当者が内容を確認しながら形にする。医院が使いやすく、運用しやすい仕組みづくりに取り組みます。</p><a class="button" href="/contact/">開発について相談する<span class="arrow" aria-hidden="true">↗</span></a></div>
<div class="development-map" aria-label="AIと人の知見を組み合わせ、設計・実装・改善を進めます"><div class="dev-map-orbit" aria-hidden="true"></div><div class="dev-map-core"><strong>AI<span>×</span>HUMAN</strong><span>技術と、人の知見。</span></div><div class="dev-map-node node-design"><small>DESIGN</small>設計</div><div class="dev-map-node node-build"><small>DEVELOP</small>実装</div><div class="dev-map-node node-improve"><small>IMPROVE</small>改善</div><span class="dev-map-caption">BUILD FOR YOUR CLINIC</span></div></div></section>
<section class="detail-section"><div class="wrap"><div class="eyebrow">DEVELOPMENT SCOPE</div><h2>必要な体験を、必要な形で。</h2><div class="feature-list"><article class="feature reveal"><span class="num">01 / WEBSITE</span><h3>Webサイト・LP</h3><p>医院の特徴や診療内容を伝えるWebサイト、目的に合わせたLPを制作。情報設計から見せ方、問い合わせへの導線まで整えます。</p></article><article class="feature reveal"><span class="num">02 / PATIENT EXPERIENCE</span><h3>Web上の案内・導線</h3><p>診療案内、アクセス、予約方法など、患者さまが知りたい情報に迷わずたどり着ける体験を設計します。</p></article><article class="feature reveal"><span class="num">03 / CUSTOM DEVELOPMENT</span><h3>課題に合わせた個別開発</h3><p>既存のツールで対応できる範囲を整理し、医院の運用に合わせた仕組みを検討。必要な機能と開発範囲を明確にして進めます。</p></article></div></div></section>
<section class="detail-section soft"><div class="wrap"><div class="eyebrow">OUR PROCESS</div><h2>医院の目的から、開発を始める。</h2><div class="detail-flow"><div class="reveal"><b>STEP 01</b><h3>課題を整理する</h3><p>目的、利用する方、現在の運用を伺い、解決したいことを明確にします。</p></div><div class="reveal"><b>STEP 02</b><h3>仕様を設計する</h3><p>必要な機能、画面、情報の流れと、制作する範囲をすり合わせます。</p></div><div class="reveal"><b>STEP 03</b><h3>実装・確認する</h3><p>AIを開発に活用しながら、担当者が表示や動作、内容を確認します。</p></div><div class="reveal"><b>STEP 04</b><h3>運用につなげる</h3><p>医院の使い方に合わせて調整し、必要な改善や運用方法をご相談します。</p></div></div></div></section>
<section class="detail-section"><div class="wrap choice-guide"><div><div class="eyebrow">DEVELOPMENT × STRATEGY</div><h2>つくった先の、<br>活かし方まで。</h2></div><div><p>集患や予約までの患者導線を踏まえ、Webコンサルティングと開発をつなぎます。医院の目標に向かって、制作と運用を一緒に考えます。</p><a class="text-link" href="/consulting/">Webコンサルティングを見る<span aria-hidden="true">↗</span></a></div></div></section>
<section class="detail-section soft"><div class="wrap faq"><div class="eyebrow">FAQ</div><h2>開発のご相談について</h2><details><summary>つくりたいものが決まっていなくても相談できますか？</summary><p>はい。いま感じている課題や、実現したいことからお聞かせください。既存のプロダクトの活用も含めて、必要な仕組みを整理します。</p></details><details><summary>いま使っているサイトの改善も相談できますか？</summary><p>現在のサイトの構成・仕様・管理状況を確認し、対応できる範囲と進め方をご案内します。</p></details><details><summary>費用や期間はどのように決まりますか？</summary><p>必要な機能やページ数、制作範囲、既存システムの状況などを確認し、お見積もりと進行計画をご案内します。</p></details></div></section>
''' + cta()
    write(Path('development/index.html'), 'AIを活用した開発', 'AIを設計・実装・改善に活用するCrestixのプロダクト・Web開発。医院の課題に合わせ、Webサイトや必要な仕組みを形にします。', development)

    company = breadcrumb('会社情報') + '''
<section class="page-intro company-intro"><div class="wrap"><div class="eyebrow">COMPANY</div><h1>会社情報</h1><p class="page-lead">医療の可能性を、デジタルでひらく。</p></div></section>
<section class="section company-message"><div class="wrap company-message-grid"><div class="company-wordmark" aria-hidden="true">Crestix<span>TECHNOLOGY FOR CLINICS</span></div><div><div class="eyebrow">WHO WE ARE</div><h2>クリニックの隣で、<br>考え続ける会社。</h2><p>地域で見つけてもらい、医院の価値を知ってもらう。そして、来院後も必要な情報を届けていく。</p><p>株式会社Crestixは、クリニックの患者接点をデジタルでつなぐ会社です。日々の運用を支えるプロダクトと、医院ごとの課題に向き合うWebコンサルティング。その両面から、続けられる成長の仕組みをつくります。</p></div></div></section>
<section class="detail-section soft"><div class="wrap"><div class="eyebrow">OUR APPROACH</div><h2>技術を活かし、医院に向き合う。</h2><div class="feature-list"><article class="feature reveal"><span class="num">01</span><h3>クリニックを起点に。</h3><p>診療科や地域性、院内の体制を踏まえ、医院が届けたい価値と患者さまが知りたい情報をつなぎます。</p></article><article class="feature reveal"><span class="num">02</span><h3>AIと、人の知見を。</h3><p>AIを開発・分析・制作に活用。担当者が内容を確認し、医院ごとの事情に合う判断と提案につなげます。</p></article><article class="feature reveal"><span class="num">03</span><h3>運用を、ともに育てる。</h3><p>導入後のデータと現場の声をもとに改善。院内の負担に配慮しながら、継続できる運用を考えます。</p></article></div></div></section>
<section class="section company company-profile"><div class="wrap company-grid"><div><div class="eyebrow">COMPANY PROFILE</div><h2>会社概要</h2></div><dl><div><dt>会社名</dt><dd>株式会社Crestix（クレスティックス）</dd></div><div><dt>設立</dt><dd>2024年12月</dd></div><div><dt>所在地</dt><dd>〒101-0054<br>東京都千代田区神田錦町1丁目21-2<br>大手町モダンビルディング 4F</dd></div><div><dt>事業・支援領域</dt><dd>クリニック向けプロダクトの導入・運用<br>Webコンサルティング<br>AIを活用した開発・Web制作</dd></div><div><dt>お問い合わせ</dt><dd><a class="text-link" href="/contact/">お問い合わせ窓口<span aria-hidden="true">↗</span></a></dd></div></dl></div></section>
''' + cta()
    write(Path('company/index.html'), '会社情報', '株式会社Crestixの会社情報。クリニック向けプロダクト、Webコンサルティング、AIを活用した開発を通じて医院の成長を支援します。', company)
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
    print('Built corporate home, products, development, and company pages')
