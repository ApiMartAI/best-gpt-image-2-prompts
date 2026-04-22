"""
多语言翻译字典。

每个 locale 包含：
- 顶部语言切换徽章：flag / label / verb / color
- UI 文案：所有 section 标题、段落、标签

翻译文案大量参考了原 `awesome-gpt-image-2-prompts` 项目的多语言 README（CC BY 4.0），
我们根据新的 README 结构（画廊 + 详情双区）做了精简和调整。
"""

# 语言顺序 = 顶部徽章顺序
LOCALE_ORDER = [
    "en", "es", "pt", "ja", "ko", "de", "fr", "tr", "zh-TW", "zh-CN", "ru",
]

# 每个 locale 对应 APIMart 站点的路径前缀。
# apimart.ai 实际支持：/ (英文默认，空 slug) /zh /ja /ko /ru
# 其他未原生支持的语言（es/pt/de/fr/tr/zh-TW）回落到英文默认路径。
LOCALE_SLUGS = {
    "en": "",       # 英文用根路径
    "es": "", "pt": "", "de": "", "fr": "", "tr": "",  # 未原生支持，回落英文
    "ja": "ja",
    "ko": "ko",
    "ru": "ru",
    "zh-CN": "zh",
    "zh-TW": "zh",  # apimart 未区分繁简，统一走 /zh
}


def readme_filename(locale: str) -> str:
    """locale 对应的 README 文件名。英文为默认 README.md。"""
    return "README.md" if locale == "en" else f"README_{locale}.md"


LOCALES: dict[str, dict] = {
    "en": {
        "badge_flag": "🇺🇸", "badge_label": "English", "badge_verb": "Default_Source", "badge_color": "111111",
        "tagline": "A curated gallery of high-quality GPT-Image-2 prompts.",
        "apimart_pitch": "Unified access to the world's top AI models — at up to 70% off official pricing.",
        "note_title": "Powered by **[APIMart](https://apimart.ai)**",
        "note_body": "One API for every top AI model. Click any image below to open the same prompt on APIMart and generate instantly.",
        "note_cta": "Try GPT-Image-2 now →",
        "footer_heading": "🚀 Ready to generate?",
        "footer_cta": "Try GPT-Image-2 on APIMart →",
        "footer_link_docs": "API Docs",
        "footer_link_models": "Browse All Image Models",
        "intro_heading": "Introduction",
        "intro_body": (
            "Welcome to **best-gpt-image-2-prompts** — a visual, gallery-first collection of "
            "GPT-Image-2 prompt cases across portraits, posters, character sheets, UI mockups "
            "and community experiments."
        ),
        "intro_hint": "Browse the [Gallery](#gallery) to find a visual style you like, then click any thumbnail to jump to the full prompt.",
        "intro_note": "> Content is adapted from the community collection at <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>. All prompts credit their original authors.",
        "news_heading": "News",
        "news_items": [
            "- **April 22, 2026:** Initial gallery-first layout with {total} curated cases across {cats} categories.",
        ],
        "gallery_heading": "Gallery",
        "gallery_tip": "> 💡 Click any thumbnail to jump to the full prompt in the [Prompts](#prompts) section.",
        "section_portrait": "Portrait & Photography Cases",
        "section_poster": "Poster & Illustration Cases",
        "section_character": "Character Design Cases",
        "section_ui": "UI & Social Media Mockup Cases",
        "section_comparison": "Comparison & Community Examples",
        "prompts_heading": "Prompts",
        "output_label": "Output",
        "output_alt": "Output image",
        "prompt_label": "Prompt",
        "by_label": "by",
        "ack_heading": "Acknowledge",
        "ack_body": (
            "This project builds on the community's collective effort. Prompt authors are "
            "credited on each case; please follow the links to their original posts."
        ),
        "license_heading": "License",
        "license_body": "This project is licensed under the Creative Commons Attribution 4.0 International License — see [LICENSE](LICENSE).",
    },
    "zh-CN": {
        "badge_flag": "🇨🇳", "badge_label": "简体中文", "badge_verb": "查看", "badge_color": "ef476f",
        "tagline": "一份精选的 GPT-Image-2 高质量提示词画廊。",
        "apimart_pitch": "一站式接入全球顶级 AI 模型，价格低至官方的 30%。",
        "note_title": "由 **[APIMart](https://apimart.ai)** 提供支持",
        "note_body": "一个 API 接入所有顶级 AI 模型。点击下方任意图像，即可在 APIMart 打开对应提示词并直接生成。",
        "note_cta": "立即体验 GPT-Image-2 →",
        "footer_heading": "🚀 准备好生成图像了吗？",
        "footer_cta": "在 APIMart 体验 GPT-Image-2 →",
        "footer_link_docs": "API 文档",
        "footer_link_models": "浏览所有图像模型",
        "intro_heading": "简介",
        "intro_body": (
            "欢迎来到 **best-gpt-image-2-prompts** —— 一个以画廊优先的 GPT-Image-2 "
            "提示词案例集，覆盖人像、海报、角色设计、UI 原型及社区实验等场景。"
        ),
        "intro_hint": "浏览 [Gallery](#gallery) 找到喜欢的视觉风格，点击任意缩略图即可跳转到完整提示词。",
        "intro_note": "> 内容改编自社区 <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>，所有提示词均保留原作者署名。",
        "news_heading": "最新动态",
        "news_items": [
            "- **2026 年 4 月 22 日：** 首个画廊版发布，收录 {total} 个精选案例，覆盖 {cats} 个分类。",
        ],
        "gallery_heading": "画廊",
        "gallery_tip": "> 💡 点击任意缩略图，即可跳转到 [提示词详情](#prompts) 区域。",
        "section_portrait": "人像与摄影案例",
        "section_poster": "海报与插画案例",
        "section_character": "角色设计案例",
        "section_ui": "UI 与社交媒体截图案例",
        "section_comparison": "模型对比与社区案例",
        "prompts_heading": "提示词详情",
        "output_label": "输出效果",
        "output_alt": "输出图像",
        "prompt_label": "提示词",
        "by_label": "作者",
        "ack_heading": "致谢",
        "ack_body": "本项目基于社区集体努力搭建。每个案例下方均署名原作者，欢迎点击链接访问其原始发布。",
        "license_heading": "许可协议",
        "license_body": "本项目采用 Creative Commons Attribution 4.0 International 许可协议 —— 详见 [LICENSE](LICENSE)。",
    },
    "zh-TW": {
        "badge_flag": "🇨🇳", "badge_label": "繁體中文", "badge_verb": "查看", "badge_color": "8338ec",
        "tagline": "一份精選的 GPT-Image-2 高品質提示詞畫廊。",
        "apimart_pitch": "一站式接入全球頂級 AI 模型，價格低至官方的 30%。",
        "note_title": "由 **[APIMart](https://apimart.ai)** 提供支援",
        "note_body": "一個 API 接入所有頂級 AI 模型。點擊下方任意圖像，即可在 APIMart 打開對應提示詞並直接生成。",
        "note_cta": "立即體驗 GPT-Image-2 →",
        "footer_heading": "🚀 準備好生成圖像了嗎？",
        "footer_cta": "在 APIMart 體驗 GPT-Image-2 →",
        "footer_link_docs": "API 文件",
        "footer_link_models": "瀏覽所有圖像模型",
        "intro_heading": "簡介",
        "intro_body": (
            "歡迎來到 **best-gpt-image-2-prompts** —— 一個以畫廊優先的 GPT-Image-2 "
            "提示詞案例集，涵蓋人像、海報、角色設計、UI 原型與社群實驗等場景。"
        ),
        "intro_hint": "瀏覽 [Gallery](#gallery) 找到喜歡的視覺風格，點擊任意縮圖即可跳到完整提示詞。",
        "intro_note": "> 內容改編自社群 <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>，所有提示詞均保留原作者署名。",
        "news_heading": "最新動態",
        "news_items": [
            "- **2026 年 4 月 22 日：** 首個畫廊版發布，收錄 {total} 個精選案例，涵蓋 {cats} 個分類。",
        ],
        "gallery_heading": "畫廊",
        "gallery_tip": "> 💡 點擊任意縮圖，即可跳到 [提示詞詳情](#prompts) 區域。",
        "section_portrait": "人像與攝影案例",
        "section_poster": "海報與插畫案例",
        "section_character": "角色設計案例",
        "section_ui": "UI 與社群媒體截圖案例",
        "section_comparison": "模型比較與社群案例",
        "prompts_heading": "提示詞詳情",
        "output_label": "輸出效果",
        "output_alt": "輸出圖像",
        "prompt_label": "提示詞",
        "by_label": "作者",
        "ack_heading": "致謝",
        "ack_body": "本專案基於社群集體努力搭建。每個案例下方均署名原作者，歡迎點擊連結造訪其原始發布。",
        "license_heading": "授權協議",
        "license_body": "本專案採用 Creative Commons Attribution 4.0 International 授權協議 —— 詳見 [LICENSE](LICENSE)。",
    },
    "ja": {
        "badge_flag": "🇯🇵", "badge_label": "日本語", "badge_verb": "表示", "badge_color": "52b788",
        "tagline": "厳選された GPT-Image-2 高品質プロンプトギャラリー。",
        "apimart_pitch": "主要 AI モデルへのワンストップ API アクセス。公式料金から最大 70% オフ。",
        "note_title": "**[APIMart](https://apimart.ai)** で動作",
        "note_body": "すべての主要 AI モデルに 1 つの API で接続。以下の画像をクリックすると、APIMart で同じプロンプトを開いてすぐに生成できます。",
        "note_cta": "今すぐ GPT-Image-2 を試す →",
        "footer_heading": "🚀 画像を生成する準備はできましたか？",
        "footer_cta": "APIMart で GPT-Image-2 を試す →",
        "footer_link_docs": "API ドキュメント",
        "footer_link_models": "すべての画像モデルを見る",
        "intro_heading": "紹介",
        "intro_body": (
            "**best-gpt-image-2-prompts** へようこそ。ポートレート、ポスター、キャラクターシート、"
            "UI モックアップ、コミュニティ実験にまたがる GPT-Image-2 プロンプト事例を、"
            "ギャラリー形式でまとめています。"
        ),
        "intro_hint": "[Gallery](#gallery) から好きなビジュアルスタイルを探し、サムネイルをクリックすると完全なプロンプトに移動できます。",
        "intro_note": "> コンテンツはコミュニティ <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe> から改編したもので、すべてのプロンプトは原作者を明記しています。",
        "news_heading": "最新情報",
        "news_items": [
            "- **2026年4月22日:** ギャラリー優先レイアウトの初版を公開。{cats} カテゴリ、合計 {total} 事例を収録。",
        ],
        "gallery_heading": "ギャラリー",
        "gallery_tip": "> 💡 サムネイルをクリックすると、[プロンプト詳細](#prompts) にジャンプします。",
        "section_portrait": "ポートレートと写真の事例",
        "section_poster": "ポスターとイラストの事例",
        "section_character": "キャラクターデザイン事例",
        "section_ui": "UI とソーシャルメディアモックアップ事例",
        "section_comparison": "比較とコミュニティ事例",
        "prompts_heading": "プロンプト詳細",
        "output_label": "出力",
        "output_alt": "出力画像",
        "prompt_label": "プロンプト",
        "by_label": "by",
        "ack_heading": "謝辞",
        "ack_body": "本プロジェクトはコミュニティの集合的な努力の上に成り立っています。各事例には原作者を明記しており、リンクから原投稿をご確認ください。",
        "license_heading": "ライセンス",
        "license_body": "本プロジェクトは Creative Commons Attribution 4.0 International ライセンスで提供されます。詳細は [LICENSE](LICENSE) を参照してください。",
    },
    "ko": {
        "badge_flag": "🇰🇷", "badge_label": "한국어", "badge_verb": "보기", "badge_color": "4ea8de",
        "tagline": "엄선된 GPT-Image-2 고품질 프롬프트 갤러리.",
        "apimart_pitch": "주요 AI 모델에 대한 통합 API 액세스. 공식 가격 대비 최대 70% 할인.",
        "note_title": "**[APIMart](https://apimart.ai)** 제공",
        "note_body": "모든 주요 AI 모델에 하나의 API로 연결하세요. 아래 이미지를 클릭하면 APIMart에서 동일한 프롬프트를 열어 바로 생성할 수 있습니다.",
        "note_cta": "지금 GPT-Image-2 체험하기 →",
        "footer_heading": "🚀 이미지를 생성할 준비가 되셨나요?",
        "footer_cta": "APIMart에서 GPT-Image-2 체험하기 →",
        "footer_link_docs": "API 문서",
        "footer_link_models": "모든 이미지 모델 보기",
        "intro_heading": "소개",
        "intro_body": (
            "**best-gpt-image-2-prompts** 에 오신 것을 환영합니다. 인물 사진, 포스터, 캐릭터 시트, "
            "UI 목업, 커뮤니티 실험 등 다양한 장면의 GPT-Image-2 프롬프트 사례를 "
            "갤러리 우선 방식으로 모아 놓았습니다."
        ),
        "intro_hint": "[Gallery](#gallery) 에서 마음에 드는 비주얼 스타일을 찾아, 썸네일을 클릭하면 전체 프롬프트로 이동합니다.",
        "intro_note": "> 콘텐츠는 커뮤니티 <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>를 바탕으로 각색했으며, 모든 프롬프트에 원저작자를 표기했습니다.",
        "news_heading": "최신 소식",
        "news_items": [
            "- **2026년 4월 22일:** 갤러리 우선 레이아웃의 초판을 공개. {cats} 개 카테고리, 총 {total} 개 사례 수록.",
        ],
        "gallery_heading": "갤러리",
        "gallery_tip": "> 💡 썸네일을 클릭하면 [프롬프트 상세](#prompts) 섹션으로 이동합니다.",
        "section_portrait": "인물 및 사진 사례",
        "section_poster": "포스터 및 일러스트 사례",
        "section_character": "캐릭터 디자인 사례",
        "section_ui": "UI 및 소셜 미디어 목업 사례",
        "section_comparison": "비교 및 커뮤니티 사례",
        "prompts_heading": "프롬프트 상세",
        "output_label": "결과",
        "output_alt": "출력 이미지",
        "prompt_label": "프롬프트",
        "by_label": "by",
        "ack_heading": "감사의 말",
        "ack_body": "이 프로젝트는 커뮤니티의 집단적 노력 위에 세워졌습니다. 각 사례에는 원저작자가 표기되어 있으니 링크를 통해 원 게시물을 확인하세요.",
        "license_heading": "라이선스",
        "license_body": "이 프로젝트는 Creative Commons Attribution 4.0 International 라이선스로 배포됩니다 — [LICENSE](LICENSE) 를 참조하세요.",
    },
    "de": {
        "badge_flag": "🇩🇪", "badge_label": "Deutsch", "badge_verb": "Ansehen", "badge_color": "f4a261",
        "tagline": "Eine kuratierte Galerie hochwertiger GPT-Image-2-Prompts.",
        "apimart_pitch": "Einheitlicher Zugang zu fuehrenden KI-Modellen — bis zu 70% Rabatt auf offizielle Preise.",
        "note_title": "Powered by **[APIMart](https://apimart.ai)**",
        "note_body": "Eine API fuer jedes fuehrende KI-Modell. Klicke auf ein beliebiges Bild unten, um denselben Prompt auf APIMart zu oeffnen und sofort zu generieren.",
        "note_cta": "GPT-Image-2 jetzt testen →",
        "footer_heading": "🚀 Bereit zu generieren?",
        "footer_cta": "GPT-Image-2 auf APIMart testen →",
        "footer_link_docs": "API-Dokumentation",
        "footer_link_models": "Alle Bildmodelle durchsuchen",
        "intro_heading": "Einfuehrung",
        "intro_body": (
            "Willkommen bei **best-gpt-image-2-prompts** — einer galerie-orientierten Sammlung "
            "von GPT-Image-2-Prompt-Beispielen fuer Portraets, Poster, Charakterblaetter, "
            "UI-Mockups und Community-Experimente."
        ),
        "intro_hint": "Durchstoebere die [Gallery](#gallery), um einen visuellen Stil zu finden, und klicke auf ein Vorschaubild, um zum vollstaendigen Prompt zu springen.",
        "intro_note": "> Inhalte sind aus der Community-Sammlung <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe> adaptiert; alle Prompts nennen die Originalautoren.",
        "news_heading": "Neuigkeiten",
        "news_items": [
            "- **22. April 2026:** Erste Galerie-Version mit {total} kuratierten Faellen in {cats} Kategorien veroeffentlicht.",
        ],
        "gallery_heading": "Galerie",
        "gallery_tip": "> 💡 Klicke auf ein Vorschaubild, um zum vollstaendigen Prompt im Abschnitt [Prompts](#prompts) zu springen.",
        "section_portrait": "Portraet- und Fotografie-Faelle",
        "section_poster": "Poster- und Illustrations-Faelle",
        "section_character": "Faelle zum Charakterdesign",
        "section_ui": "UI- und Social-Media-Mockup-Faelle",
        "section_comparison": "Vergleiche und Community-Beispiele",
        "prompts_heading": "Prompts",
        "output_label": "Ergebnis",
        "output_alt": "Ergebnisbild",
        "prompt_label": "Prompt",
        "by_label": "von",
        "ack_heading": "Danksagungen",
        "ack_body": "Dieses Projekt baut auf dem Gemeinschaftsbeitrag auf. Zu jedem Fall ist der Originalautor genannt; folge den Links zu den Originalposts.",
        "license_heading": "Lizenz",
        "license_body": "Dieses Projekt ist unter der Creative Commons Attribution 4.0 International Lizenz verfuegbar — siehe [LICENSE](LICENSE).",
    },
    "es": {
        "badge_flag": "🇪🇸", "badge_label": "Español", "badge_verb": "Ver", "badge_color": "ffb703",
        "tagline": "Una galeria curada de prompts GPT-Image-2 de alta calidad.",
        "apimart_pitch": "Acceso unificado a los mejores modelos de IA — hasta 70% de descuento del precio oficial.",
        "note_title": "Impulsado por **[APIMart](https://apimart.ai)**",
        "note_body": "Una API para cada modelo de IA de primera linea. Haz clic en cualquier imagen debajo para abrir el mismo prompt en APIMart y generar al instante.",
        "note_cta": "Probar GPT-Image-2 ahora →",
        "footer_heading": "🚀 Listo para generar?",
        "footer_cta": "Probar GPT-Image-2 en APIMart →",
        "footer_link_docs": "Documentacion de API",
        "footer_link_models": "Ver todos los modelos de imagen",
        "intro_heading": "Introduccion",
        "intro_body": (
            "Bienvenido a **best-gpt-image-2-prompts** — una coleccion de casos de prompts de "
            "GPT-Image-2 con enfoque de galeria, que abarca retratos, posters, hojas de "
            "personajes, maquetas de UI y experimentos de la comunidad."
        ),
        "intro_hint": "Explora la [Gallery](#gallery) para encontrar un estilo visual y haz clic en cualquier miniatura para saltar al prompt completo.",
        "intro_note": "> El contenido esta adaptado de la coleccion comunitaria en <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>; todos los prompts acreditan a sus autores originales.",
        "news_heading": "Novedades",
        "news_items": [
            "- **22 de abril de 2026:** Lanzamiento de la primera version con enfoque de galeria, con {total} casos curados en {cats} categorias.",
        ],
        "gallery_heading": "Galeria",
        "gallery_tip": "> 💡 Haz clic en cualquier miniatura para saltar al prompt completo en la seccion [Prompts](#prompts).",
        "section_portrait": "Casos de Retrato y Fotografia",
        "section_poster": "Casos de Posters e Ilustracion",
        "section_character": "Casos de Diseno de Personajes",
        "section_ui": "Casos de UI y Mockups de Redes Sociales",
        "section_comparison": "Comparativas y Ejemplos de la Comunidad",
        "prompts_heading": "Prompts",
        "output_label": "Resultado",
        "output_alt": "Imagen de resultado",
        "prompt_label": "Prompt",
        "by_label": "por",
        "ack_heading": "Agradecimientos",
        "ack_body": "Este proyecto se apoya en el esfuerzo colectivo de la comunidad. Cada caso acredita a su autor original; sigue los enlaces a las publicaciones originales.",
        "license_heading": "Licencia",
        "license_body": "Este proyecto esta bajo la licencia Creative Commons Attribution 4.0 International — ver [LICENSE](LICENSE).",
    },
    "fr": {
        "badge_flag": "🇫🇷", "badge_label": "Français", "badge_verb": "Voir", "badge_color": "e76f51",
        "tagline": "Une galerie organisee de prompts GPT-Image-2 de haute qualite.",
        "apimart_pitch": "Acces unifie aux meilleurs modeles IA — jusqu a 70 pourcent de remise sur les tarifs officiels.",
        "note_title": "Propulse par **[APIMart](https://apimart.ai)**",
        "note_body": "Une API pour chaque modele IA de premier plan. Cliquez sur n importe quelle image ci-dessous pour ouvrir le meme prompt sur APIMart et generer instantanement.",
        "note_cta": "Essayer GPT-Image-2 maintenant →",
        "footer_heading": "🚀 Pret a generer ?",
        "footer_cta": "Essayer GPT-Image-2 sur APIMart →",
        "footer_link_docs": "Documentation API",
        "footer_link_models": "Voir tous les modeles d image",
        "intro_heading": "Introduction",
        "intro_body": (
            "Bienvenue sur **best-gpt-image-2-prompts** — une collection de cas de prompts "
            "GPT-Image-2 orientee galerie, couvrant portraits, affiches, fiches de personnage, "
            "maquettes UI et experimentations de la communaute."
        ),
        "intro_hint": "Parcourez la [Gallery](#gallery) pour trouver un style visuel, puis cliquez sur une vignette pour acceder au prompt complet.",
        "intro_note": "> Le contenu est adapte de la collection communautaire sur <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>; tous les prompts creditent leurs auteurs d origine.",
        "news_heading": "Actualites",
        "news_items": [
            "- **22 avril 2026 :** Publication de la premiere version orientee galerie, avec {total} cas organises repartis en {cats} categories.",
        ],
        "gallery_heading": "Galerie",
        "gallery_tip": "> 💡 Cliquez sur une vignette pour acceder au prompt complet dans la section [Prompts](#prompts).",
        "section_portrait": "Cas de Portrait et Photographie",
        "section_poster": "Cas d Affiches et d Illustration",
        "section_character": "Cas de Design de Personnage",
        "section_ui": "Cas de Maquettes UI et Reseaux Sociaux",
        "section_comparison": "Comparaisons et Exemples de la Communaute",
        "prompts_heading": "Prompts",
        "output_label": "Resultat",
        "output_alt": "Image du resultat",
        "prompt_label": "Prompt",
        "by_label": "par",
        "ack_heading": "Remerciements",
        "ack_body": "Ce projet s appuie sur l effort collectif de la communaute. Chaque cas cite son auteur d origine; suivez les liens vers les publications originales.",
        "license_heading": "Licence",
        "license_body": "Ce projet est distribue sous la licence Creative Commons Attribution 4.0 International — voir [LICENSE](LICENSE).",
    },
    "pt": {
        "badge_flag": "🇵🇹", "badge_label": "Português", "badge_verb": "Ver", "badge_color": "2a9d8f",
        "tagline": "Uma galeria curada de prompts GPT-Image-2 de alta qualidade.",
        "apimart_pitch": "Acesso unificado aos melhores modelos de IA — ate 70% de desconto do preco oficial.",
        "note_title": "Desenvolvido por **[APIMart](https://apimart.ai)**",
        "note_body": "Uma API para todos os melhores modelos de IA. Clique em qualquer imagem abaixo para abrir o mesmo prompt no APIMart e gerar instantaneamente.",
        "note_cta": "Experimente o GPT-Image-2 agora →",
        "footer_heading": "🚀 Pronto para gerar?",
        "footer_cta": "Experimente o GPT-Image-2 no APIMart →",
        "footer_link_docs": "Documentacao da API",
        "footer_link_models": "Ver todos os modelos de imagem",
        "intro_heading": "Introducao",
        "intro_body": (
            "Bem-vindo ao **best-gpt-image-2-prompts** — uma colecao de casos de prompts "
            "GPT-Image-2 com foco em galeria, cobrindo retratos, posters, fichas de "
            "personagens, mockups de UI e experimentos da comunidade."
        ),
        "intro_hint": "Navegue pela [Gallery](#gallery) para encontrar um estilo visual e clique em qualquer miniatura para ir ao prompt completo.",
        "intro_note": "> O conteudo foi adaptado da colecao comunitaria em <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>; todos os prompts creditam seus autores originais.",
        "news_heading": "Novidades",
        "news_items": [
            "- **22 de abril de 2026:** Lancamento da primeira versao com foco em galeria, com {total} casos curados em {cats} categorias.",
        ],
        "gallery_heading": "Galeria",
        "gallery_tip": "> 💡 Clique em qualquer miniatura para ir ao prompt completo na secao [Prompts](#prompts).",
        "section_portrait": "Casos de Retrato e Fotografia",
        "section_poster": "Casos de Poster e Ilustracao",
        "section_character": "Casos de Design de Personagem",
        "section_ui": "Casos de UI e Mockups de Redes Sociais",
        "section_comparison": "Comparacoes e Exemplos da Comunidade",
        "prompts_heading": "Prompts",
        "output_label": "Resultado",
        "output_alt": "Imagem de resultado",
        "prompt_label": "Prompt",
        "by_label": "por",
        "ack_heading": "Agradecimentos",
        "ack_body": "Este projeto se baseia no esforco coletivo da comunidade. Cada caso credita seu autor original; siga os links para as publicacoes originais.",
        "license_heading": "Licenca",
        "license_body": "Este projeto esta licenciado sob a Creative Commons Attribution 4.0 International — veja [LICENSE](LICENSE).",
    },
    "tr": {
        "badge_flag": "🇹🇷", "badge_label": "Türkçe", "badge_verb": "Görüntüle", "badge_color": "d62828",
        "tagline": "Yuksek kaliteli GPT-Image-2 promptlarinin derlenmis galerisi.",
        "apimart_pitch": "Onde gelen YZ modellerine birlesik erisim — resmi fiyatlardan yuzde 70 e varan indirim.",
        "note_title": "**[APIMart](https://apimart.ai)** tarafindan saglaniyor",
        "note_body": "Her onde gelen YZ modeli icin tek bir API. Asagidaki herhangi bir gorsele tiklayin, ayni prompt APIMart te acilsin ve aninda uretilsin.",
        "note_cta": "GPT-Image-2 yi simdi deneyin →",
        "footer_heading": "🚀 Gorsel uretmeye hazir misiniz?",
        "footer_cta": "GPT-Image-2 yi APIMart te deneyin →",
        "footer_link_docs": "API Belgeleri",
        "footer_link_models": "Tum gorsel modellere goz atin",
        "intro_heading": "Giris",
        "intro_body": (
            "**best-gpt-image-2-prompts** e hos geldiniz — portreler, posterler, karakter "
            "sayfalari, UI mockuplari ve topluluk deneylerini kapsayan, galeri odakli bir "
            "GPT-Image-2 prompt vaka koleksiyonu."
        ),
        "intro_hint": "Begendiginiz bir gorsel stil bulmak icin [Gallery](#gallery) bolumune goz atin ve tam prompta gitmek icin herhangi bir kucuk resme tiklayin.",
        "intro_note": "> Icerik, <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe> adresindeki topluluk koleksiyonundan uyarlanmistir; tum promptlar orijinal yazarlari belirtir.",
        "news_heading": "Haberler",
        "news_items": [
            "- **22 Nisan 2026:** {cats} kategoride toplam {total} derlenmis vaka iceren ilk galeri odakli sürümün yayimlanmasi.",
        ],
        "gallery_heading": "Galeri",
        "gallery_tip": "> 💡 Tam prompta ulasmak icin herhangi bir kucuk resme tiklayarak [Prompts](#prompts) bolumune gidin.",
        "section_portrait": "Portre ve Fotografcilik Vakalari",
        "section_poster": "Poster ve Illustrasyon Vakalari",
        "section_character": "Karakter Tasarimi Vakalari",
        "section_ui": "UI ve Sosyal Medya Mockup Vakalari",
        "section_comparison": "Karsilastirma ve Topluluk Ornekleri",
        "prompts_heading": "Prompts",
        "output_label": "Sonuc",
        "output_alt": "Cikti gorseli",
        "prompt_label": "Prompt",
        "by_label": "yazar",
        "ack_heading": "Tesekkurler",
        "ack_body": "Bu proje toplulugun kolektif emegine dayanir. Her vakada orijinal yazar belirtilmistir; orijinal gonderilere ulasmak icin baglantilari takip edin.",
        "license_heading": "Lisans",
        "license_body": "Bu proje Creative Commons Attribution 4.0 International lisansi ile yayinlanmistir — [LICENSE](LICENSE) dosyasina bakin.",
    },
    "ru": {
        "badge_flag": "🇷🇺", "badge_label": "Русский", "badge_verb": "Смотреть", "badge_color": "577590",
        "tagline": "Кураторская галерея высококачественных промптов GPT-Image-2.",
        "apimart_pitch": "Единый доступ к топовым ИИ-моделям — скидка до 70% от официальной цены.",
        "note_title": "Работает на **[APIMart](https://apimart.ai)**",
        "note_body": "Один API для каждой топовой ИИ-модели. Нажмите на любое изображение ниже, чтобы открыть тот же промпт на APIMart и мгновенно сгенерировать.",
        "note_cta": "Попробовать GPT-Image-2 сейчас →",
        "footer_heading": "🚀 Готовы генерировать?",
        "footer_cta": "Попробовать GPT-Image-2 на APIMart →",
        "footer_link_docs": "Документация API",
        "footer_link_models": "Все модели изображений",
        "intro_heading": "Введение",
        "intro_body": (
            "Добро пожаловать в **best-gpt-image-2-prompts** — подборку кейсов промптов "
            "GPT-Image-2 с акцентом на галерею: портреты, постеры, карточки персонажей, "
            "UI-макеты и эксперименты сообщества."
        ),
        "intro_hint": "Откройте [Gallery](#gallery), чтобы найти визуальный стиль, и нажмите на любую миниатюру, чтобы перейти к полному промпту.",
        "intro_note": "> Контент адаптирован из общественного сборника по адресу <https://waytoagi.feishu.cn/wiki/PjxpwWFXriCdQnkVXBecyGqZnIe>; все промпты указывают оригинальных авторов.",
        "news_heading": "Новости",
        "news_items": [
            "- **22 апреля 2026:** Выпуск первой галерейной версии, {total} отобранных кейсов в {cats} категориях.",
        ],
        "gallery_heading": "Галерея",
        "gallery_tip": "> 💡 Нажмите на любую миниатюру, чтобы перейти к полному промпту в разделе [Prompts](#prompts).",
        "section_portrait": "Кейсы портретов и фотографии",
        "section_poster": "Кейсы постеров и иллюстраций",
        "section_character": "Кейсы дизайна персонажей",
        "section_ui": "Кейсы UI и макетов соцсетей",
        "section_comparison": "Сравнения и примеры сообщества",
        "prompts_heading": "Промпты",
        "output_label": "Результат",
        "output_alt": "Результирующее изображение",
        "prompt_label": "Промпт",
        "by_label": "автор",
        "ack_heading": "Благодарности",
        "ack_body": "Этот проект опирается на коллективный труд сообщества. В каждом кейсе указан оригинальный автор; переходите по ссылкам к исходным публикациям.",
        "license_heading": "Лицензия",
        "license_body": "Проект распространяется под лицензией Creative Commons Attribution 4.0 International — см. [LICENSE](LICENSE).",
    },
}
