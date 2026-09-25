# Crestix — クリニック向けプロダクト・Webコンサルティング

**サイト:** https://crestix-company.github.io/HP-iryou/

AIを活かした開発・Webコンサルティングと、クリニック向け6サービスを紹介するサイトです。

## GitHub Pagesへの公開

`main` にプッシュすると、GitHub ActionsがHTMLを生成・検証し、`dist/` をGitHub Pagesへ公開します。

- 公開設定：Settings → Pages → Source → **GitHub Actions**
- ワークフロー：`.github/workflows/pages.yml`
- 公開対象：`dist/`（ルートに `index.html` を含む）
- URLのパス：`/HP-iryou/`

リポジトリのREADMEではなく、サイト本体を表示する設定です。

## 編集するファイル

| 内容 | ファイル |
| --- | --- |
| トップ・プロダクト一覧・AI開発・会社情報 | `corporate.py` |
| 共通ヘッダー／フッター・ページ生成 | `build.py` |
| サービス詳細・Webコンサル・お問い合わせ | `details.py` |
| デザイン・レスポンシブ対応 | `dist/style.css` |
| メニュー・アニメーション | `dist/app.js` |
| 画像 | `dist/assets/` |

HTMLを直接編集すると次回ビルドで上書きされます。文章は上記Pythonファイル内で編集してください。外部パッケージのインストールは不要です。

トップを入口に、プロダクト一覧、6つのサービス詳細、AI開発、Webコンサルティング、会社情報、お問い合わせを独立したURLで表示します。公開ページは12ページと404ページです。

## ローカル確認

Python 3.12以降を使用します。

```sh
python3 details.py
python3 verify.py
python3 -m http.server 49187 --directory dist
```

`http://localhost:49187/` をブラウザで開いてください。

GitHub Pagesと同じパスで生成する場合：

```sh
SITE_BASE_PATH=/HP-iryou python3 details.py
python3 verify.py --base-path /HP-iryou
```

## 掲載素材とお問い合わせ

6サービスの画像は提供資料PDFの表紙から抽出しています。原本PDF・卸価格資料は公開対象に含めていません。

お問い合わせは既存のCrestix公式フォーム、事業用メール・電話につながります。このリポジトリには送信先の認証情報や個人情報を保存する機能はありません。

既存の `www.crestix.jp` と本人限定のSites版は、このリポジトリの公開処理では変更しません。
