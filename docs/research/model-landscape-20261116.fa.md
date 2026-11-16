# کاتالوگ پژوهشی مدل‌های DEC — همتای فارسی بررسی‌شده
**تاریخ:** ۱۶ نوامبر ۲۰۲۶ | **شواهد:** عمدتاً E0 بر پایهٔ منابع سازنده؛ اجرای محلی محدود و مستقل ثبت‌شده است.

> این جدول به‌عنوان نسخهٔ فارسی کاتالوگ اصلی تهیه شده است: نام مدل، گروه، مشخصات فنی، محدودیت و نشانی منبع برای تک‌تک مدخل‌ها حفظ می‌شود. اعداد و ادعاهای سازندگان آزمایش مستقل DEC نیستند. در این بازنویسی ترتیب و ساختار ستون‌ها برای خوانایی فارسی یکسان‌سازی شده است.

## وضعیت آزمون محلی
- تنها نتایج محدود MiniCPM5-2B Q4_K_M روی sal-ai در متن اولیه ارجاع شده‌اند: ۷۴ درخواست شامل ۵۲ آزمون خودکار اصلی، ۱۰ مورد کیفی و ۱۲ کنترل؛ ۴۴ موفقیت خودکار از ۵۲ اصلی و ۸ شکست. یادداشت اولیه با تقسیم‌بندی متفاوت `44 PASS / 20 FAIL` مرتبط با تمام ۷۴ مورد بوده است؛ این دسته‌بندی را نباید با نتیجهٔ اصلی یکی دانست.
- دادهٔ خام خصوصی داخل مخزن عمومی منتشر نشده و رتبه‌بندی سایر مدل‌ها منوط به کیفیت سنجی یکسان است.

## فهرست کامل مدخل‌ها به تفکیک دور پژوهش

### الف — مدل‌های عمومی و اولویت‌دار برای CPU

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| OpenBMB | MiniCPM5-2B | Dense حدود ۲٫۵۲ میلیارد پارامتر؛ Thinking، ابزار و Context تا ۱۳۱k؛ نامزد آزمون CPU | کیفیت و سرعت اجرای واقعی، وابسته به Runtime و تنظیمات است. | https://huggingface.co/openbmb/MiniCPM5-2B |
| Liquid AI | LFM3-1.7B | مدل Hybrid کوچک ۱٫۷میلیاردی برای استنتاج CPU؛ خط مبنای محلی | استنتاج موفق، اثبات انتخاب نهایی یا برتری تخصصی نیست. | https://huggingface.co/LiquidAI |
| SparkLLM/XHToken | Spark-X2.6-1.7B | معماری Hybrid با توجه محلی و کامل، نسخه‌های Base و GGUF، ۱٫۷میلیارد پارامتر | نامزد اولویت P0؛ اجرای کنترل‌شده نیاز است. | https://huggingface.co/XHToken/Spark-X2.6-1.7B |
| SparkLLM/XHToken | Spark-X2.6-4B | نسخهٔ ۴٫۱میلیاردی Hybrid با Sliding/Full Attention و GGUF | نامزد P0؛ وزن و Context باید با منابع سرور سنجیده شود. | https://huggingface.co/XHToken/Spark-X2.6-4B |
| IBM | Granite 4.2-3B | مدل Dense سه‌میلیاردی IBM با استدلال و ابزار؛ مجوز Apache-2.0 | نامزد P0 و نه گزینهٔ برگزیده. | https://www.ibm.com/granite/docs/models/granite/ |
| IFM/MBZUAI | K2-Horizon-0.9B | مدل Dense حدود ۹۰۰میلیون‌پارامتری، تقطیر معلم، Context ادعایی ۱۲۸k و دادهٔ باز آموزش | تناسب سرویس‌دهی و Backend باید بررسی شود. | https://huggingface.co/IFM/K2-Horizon-0.9B |
| IFM/MBZUAI | K2-Horizon-3.7B | هستهٔ Dense در کلاس ۳٫۷میلیاردی با Context ادعایی ۵۱۲k و آموزش باز | تعداد کل پارامتر و RAM واقعی ممکن است متفاوت باشد. | https://huggingface.co/IFM/K2-Horizon-3.7B |
| NVIDIA | Nemotron Labs Dory1.0-4B | مدل چهاربلیاردی بازگشتیِ عمق نهفته با محاسبهٔ داخلی قابل تنظیم؛ GGUF Q5_K_M و Context تا ۲۵۶k | مدل پژوهش محاسبهٔ تطبیقی؛ اجرای CPU باید آزموده شود. | https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-GGUF |
| Gensyn | Open-1B SFT/Base | خانوادهٔ حدود ۱میلیاردی Gensyn با انتشار مراحل مختلف آموزش و Checkpoint | پارامتر دقیق هر نسخه و امکان بازآموزی بررسی شود. | https://huggingface.co/Gensyn/open-1b-sft |
| Swiss AI | Apertus 1.5-8B | مدل چندوجهی ۸میلیاردی Swiss AI، Thinking اختیاری، شفافیت آموزش و مجوز Apache-2.0 | بیشتر رقیب/مرجع پژوهشی است تا گزینهٔ نخست سخت‌افزار محدود. | https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes |

### ب — عامل‌ها، کدنویسی و اسناد

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Microsoft | FrogNano-4B-2609 | عامل نرم‌افزاری Microsoft برای عملیات در سطح Repository و پس‌آموزش RL؛ متن‌محور | کارایی واقعی عامل و محدودهٔ استفادهٔ اعلام‌شده جدا سنجیده شود. | https://huggingface.co/microsoft/FrogNano-4B-2609 |
| Microsoft | Mage-VL-Cowork | مدل حدود ۴میلیاردی مبتنی بر تصویر برای تعامل GUI و Terminal | عامل چندوجهی است، نه LLM عمومی. | https://huggingface.co/microsoft/Mage-VL-Cowork |
| Microsoft | Fara1.5-4B | مدل حدود ۴میلیاردی عامل مرورگر و رابط بصری | نباید به‌عنوان خط مبنای عمومی کوچک تلقی شود. | https://huggingface.co/microsoft/Fara1.5-4B |
| Ai2 | TMax-2B and TMax-4B | عامل‌های Terminal در اندازه‌های ۲ و ۴میلیارد با آموزش DPPO و مجوز Apache-2.0 | آزمون موفقیت ابزار و بازگشت از خطا لازم است. | https://huggingface.co/allenai/tmax-2b |
| Ai2 | Bolmo-1B | مدل یک‌میلیاردی Byte-level آموزش‌دیده مجدد بر پایهٔ مدل قدیمی‌تر | پژوهش پیش‌آموزش است، نه چت‌بات معمول. | https://huggingface.co/allenai/Bolmo-1B |
| Ai2 | AstaBrief-8B | مدل هشت‌میلیاردی تهیهٔ گزارش علمی همراه استناد و دادهٔ آموزشی باز | نامزد تحقیق LDI/RAG و صحت ارجاع. | https://huggingface.co/blog/allenai/astabrief |
| H Company | Holo-3.1-0.8B | عامل رایانه‌ای چندوجهی در کلاس ۸۰۰میلیون پارامتر | برای وظیفهٔ خاص GUI مقایسه شود. | https://huggingface.co/Hcompany/Holo-3.1-0.8B |
| H Company | Holotron4 Nano | MoE چندوجهی با حدود ۳۰میلیارد وزن کل و ۳میلیارد پارامتر فعال | RAM لازم تابع وزن کل است؛ CPU محدود ممکن است نامناسب باشد. | https://huggingface.co/Hcompany/Holotron4-30B-A3B |
| Upstage | Solar Mini 4 | مدل چندزبانه و عامل‌محور MoE؛ ادعای سازنده حدود ۳۵میلیارد کل و ۳میلیارد فعال | مشخصات و مصرف وزن کل مستقلاً اعتبارسنجی شوند. | https://huggingface.co/upstage |

### ضمیمهٔ ۳ — جست‌وجوی تکمیلی ۱۶ نوامبر

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Meta | MobileMoE-S/M/L Base, SFT, QAT (NINE released checkpoints) | ۹ Checkpoint رسمی Meta در اندازهٔ S/M/L و گونه‌های Base، SFT و QAT؛ معماری Expert تنک برای اجرای موبایل | مجوز FAIR غیرتجاری، Kernel اختصاصی، Context برابر ۸k، تمرکز انگلیسی و عدم آمادگی پیش‌فرض Ollama. | https://huggingface.co/facebook/models |
| Apple | AFM 3 Core 3B Dense | مدل Dense سه‌میلیاردی Apple؛ مرجع معماری نسل سوم مدل‌های بنیادین | اختصاصی؛ وزن قابل دانلود رسمی برای این نسخه در این بررسی احراز نشده است. | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |
| Apple | AFM 3 Core Advanced, 20B total / 1–4B active | معماری Apple با ۲۰میلیارد وزن کل، ۱ تا ۴میلیارد فعال، صفحه‌بندی Expert متناسب با Prompt | اختصاصی و وابسته به سخت‌افزار؛ نامزد اجرای sal-ai نیست. | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |
| Kog AI | Laneformer 2B (2.3B) | مدل حدود ۲٫۳میلیاردی Kog با تمرکز بر کاهش تأخیر کدنویسی و معماری Runtime | Context چهار هزار؛ سود وابسته به Runtime اختصاصی و شرایط مجوز Tokenizer Llama2. | https://huggingface.co/blog/kogai/kog-laneformer-2b-the-latency-first-model |
| Norwegian National Library (NbAiLab) | Borealis 2 E2B preview | پیش‌نمایش مدل چندزبانهٔ منطقه‌ای از کتابخانهٔ ملی نروژ برای پژوهش آموزش کنترل‌شده | مجوز و تمرکز زبان‌های نوردیک؛ کاربرد فارسی اثبات نشده. | https://huggingface.co/NbAiLab/borealis2-e2b-preview |
| FrontiersMind | Lumma-Fev-4B-v2 | Head تصمیم احتمالاتی نوع‌دار و غیرمولد؛ مناسب مطالعهٔ تصمیم مستقل DEC | چت‌بات یا LLM خط مبنا نیست؛ سازنده و بنچمارک‌ها نیازمند بررسی مستقل. | https://huggingface.co/blog/FrontiersMind/lumma-fev-27b-v2 |
| JOSIE-2 community researchers | JOSIE-2 2B/4B/9B | مدل‌های ۲، ۴ و ۹میلیاردی مشتق از Qwen3.5 با پس‌آموزش پالایش‌شده | ادعاهای جامعهٔ پژوهشی نیاز به ممیزی مستقل دارند. | https://huggingface.co/blog/Goekdeniz-Guelmez/josie-2-technical-report-curated-post-training-for |

### ضمیمهٔ ۴ — راستی‌آزمایی چهارم منابع

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| JetBrains | Mellum2.1-12B-A2.5B-Thinking | MoE JetBrains با ۱۲میلیارد وزن، ۲٫۵میلیارد فعال، ۶۴ Expert با Top-8، ۲۸ لایه، Context تا ۱۳۱۰۷۲؛ GGUFهای Q4_K_M حدود ۸٫۱GB و MXFP4_MOE حدود ۷GB | مجوز Apache-2.0؛ دستورات CPU سازنده وجود دارد، ولی اجرای همین نسخه در sal-ai تأیید نشده است. | ارجاع در کاتالوگ مبدأ |

### ضمیمهٔ ۶ — شناسایی نظام‌مند

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Tencent Hunyuan | Hy-MT2-1.8B | مترجم تخصصی حدود ۱٫۸میلیاردی Tencent با فارسی، ادعای ۳۳ زبان، AngelSlim 1.25-bit حدود ۴۴۰MB و ۱٫۵× سرعت | وزن رسمی BF16/GGUF و Apache-2.0؛ باید کیفیت فنی EN↔FA و تعارض تعداد زبان‌ها آزموده شود. | ارجاع در کاتالوگ مبدأ |
| Preferred Networks + NICT | PLaMo 3 Translate 0.8B & 2B | مترجم دو اندازهٔ ۰٫۸ و ۲میلیاردی با پشتیبانی ادعایی ۵۳ زبان از جمله فارسی و Glossary؛ جمع Context ورودی/خروجی تا ۳۲۷۶۸ | نسخه‌های BF16/GGUF/MLX/NVFP4؛ مجوز Community و اجرای کد اختصاصی باید بررسی شود. | ارجاع در کاتالوگ مبدأ |
| Preferred Networks + NICT | PLaMo 3 0.8B Finance Instruct | نسخهٔ ۸۰۰میلیونی تخصص مالی؛ نمونهٔ تخصصی‌سازی حوزه | مدل عمومی امنیت سایبری و خانوادهٔ پایهٔ مستقل نیست. | ارجاع در کاتالوگ مبدأ |
| Bilibili Index Team | Index-Translate-2B | مترجم Qwen3.5-derived با پشتیبانی ادعایی ۱۵۰ زبان و قیود سبک، Glossary، JSON و Markdown؛ نسخهٔ ترجمهٔ بصری هم دارد | وزن رسمی Apache-2.0؛ پشتیبانی فهرستی جایگزین آزمون کیفیت فارسی نیست. | ارجاع در کاتالوگ مبدأ |
| Bilibili Index Team | Index-Translate-Omni-2B | ترجمهٔ متن و تصویر به همراه گفتار/ASR چینی-انگلیسی از خانوادهٔ Index-Translate | مجوز صریح در کارت بررسی‌شده مشخص نبود؛ گفتار آن به معنی پشتیبانی صوتی ۱۵۰ زبان نیست. | ارجاع در کاتالوگ مبدأ |
| Amazon | ALoDLM-1.7B | مدل Diffusion پوشانده و حلقه‌ای تطبیقی مبتنی بر Qwen3 با حالت نهفتهٔ ماندگار، تخصیص محاسبهٔ سطح توکن و توقف یادگرفتنی | وزن/کد رسمی CC-BY-NC-4.0؛ جریان Ollama خودرگرسیو عادی نیست و سرعت CPU اثبات نشده. | ارجاع در کاتالوگ مبدأ |
| Amazon / Strands Agents | Strands Decider 2B (Qwen3.5 v1 2610) | LoRA روی Qwen3.5-2B-Base با Head خروجی نوع‌دار برای بله/خیر، چندکلاسه، رتبه‌ای و Confidence | Adapter، دستور آموزش، داده و کد رسمی با Apache-2.0؛ جایگزین مولد متن نیست. | ارجاع در کاتالوگ مبدأ |
| NVIDIA | Nemotron 3.5 Parse 0.631B | مدل حدود ۶۳۱میلیون‌پارامتری با Encoder تصویر و mBART ده‌لایه برای متن، ترتیب خواندن، جدول، نمودار، Bounding Box و کلاس معنایی | وزن/کد رسمی OpenMDW-1.1؛ عملکرد GPU سازنده به CPU قابل تعمیم نیست. | ارجاع در کاتالوگ مبدأ |
| Baidu | Unlimited-OCR-2 | OCR چندوجهی مبتنی بر مدل دید-زبان برای استخراج ساختاریافتهٔ سند | وزن رسمی Safetensors و کد اختصاصی با MIT؛ اندازه، CPU و فارسی باید سنجیده شوند. | ارجاع در کاتالوگ مبدأ |
| Jina AI | jina-ocr-v1 | OCR چندزبانه و فهم سند با معماری مشتق از DeepSeek-VL | وزن Safetensors و CC-BY-NC-4.0؛ CPU و کیفیت فارسی آزموده نشده. | ارجاع در کاتالوگ مبدأ |

### ضمیمهٔ ۷ — حفظ دامنهٔ اصلی پژوهش

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Nanbeige (Kanzhun/China) | Nanbeige4.2-3B | Transformer حلقه‌ای سه‌میلیاردی آموزش‌دیده از صفر با ۲۸تریلیون توکن، loopSplit و Attention عمقی، n-gram Embedding، Thinking قابل تنظیم و ابزار XML/JSON؛ Context ادعایی ۲۵۶k | وزن Apache-2.0 و کد سفارشی؛ RAM/Latency CPU تأیید نشده. | https://huggingface.co/Nanbeige/Nanbeige4.2-3B، https://huggingface.co/Nanbeige/Nanbeige4.2-3B-Base |
| Ant Group inclusionAI | Ling-3.0-tiny | MoE هیبرید KDA/MLA با نسبت ۳:۱، ۷٫۹میلیارد کل/۱٫۳میلیارد فعال، ۱۲۸ Expert انتخابی با Top-8 و یک Expert مشترک، حالت سریع/Thinking | وزن MIT و GGUF Q4_K_M حدود ۴٫۸۲GB؛ نتایج Mac/DGX سازنده جایگزین CPU نیست. | https://huggingface.co/inclusionAI/Ling-3.0-tiny، https://huggingface.co/inclusionAI/Ling-3.0-tiny-GGUF |
| Ant Group inclusionAI | LemonDecider 4B v3 | Head تصمیم نوع‌دار مشتق از Qwen3.5-4B، خروجی ۲۵۵ گزینه، بدون متن آزاد، تقسیم بازگشتی سؤال و Chunk ورودی ۸۱۹۲ | وزن Apache-2.0 با کد سفارشی؛ احتمال خروجی برای دامنهٔ DEC نیاز به کالیبراسیون دارد. | https://huggingface.co/inclusionAI/LemonDecider |
| Ant Group inclusionAI | SingGuard-2B | طبقه‌بند چندوجهی ریسک متن و تصویر با سیاست ورودی در Runtime و ارزیابی سریع/تحلیل عمیق | GGUF Q4 حدود ۱٫۱۱GB به‌علاوهٔ Projector؛ جایگزین موتور مستقل اعمال سیاست نیست. | https://huggingface.co/inclusionAI/SingGuard-2b-GGUF |
| Tencent | WeVisDoc-2B / 4B | مدل صفحهٔ تصویر به Markdown و جدول LaTeX مشتق از Qwen3-VL؛ سازنده امتیاز 95.06/95.38 در OmniDocBench v1.6 گزارش می‌کند | وزن Apache-2.0؛ اجرای رسمی vLLM/GPU و کیفیت OCR فارسی/CPU بررسی نشده. | https://huggingface.co/tencent/WeVisDoc-2B |
| Ant Group inclusionAI | SingVL-S1-4B | مدل دید-زبان کلاس ۴میلیاردی منتشرشده در سازمان Ant در نوامبر ۲۰۲۶ | نیازمند بررسی عمیق Model Card؛ فقط صف کشف. | https://huggingface.co/inclusionAI/models |
| Xiaomi | MiMo series recent releases | خانوادهٔ Xiaomi شامل MoEهای بسیار بزرگ و مشتق‌های تقطیری حدود ۹میلیاردی | هر مدل باید جدا بررسی شود؛ پارامتر فعال با وزن مقیم یکی نیست. | ارجاع در کاتالوگ مبدأ |

### ضمیمهٔ ۸ — استارتاپ‌ها، Edge، حافظه و Runtime

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Prism ML / US | Ternary-Bonsai-2 (2B, 4B, 9B) | VLM با وزن زبانی سه‌ارزشی در اندازه‌های ۲/۴/۹میلیارد؛ بخش زبانی 2B در GGUF حدود PTQ1_0=0.43GB، PQ2_0=0.52GB، Q2_0=0.55GB در برابر FP16 نزدیک 3.8GB | اجرای CPU با llama.cpp ادعا شده؛ RAM برج دید و نسخهٔ Build باید بررسی شود. | https://huggingface.co/prism-ml/Ternary-Bonsai-2-2B-gguf |
| Klein ML / startup | KV1-1.2B | مشتق LFM2.5-1.2B با آموزش آگاه از KV فشرده BQ2_0 حدود ۲٫۵بیت/مقدار؛ در Context ۳۲k، KV یک توالی از ۳۸۴MiB به ۶۰MiB رسیده است | وزن BF16 جداست؛ Backend اختصاصی KV1.cpp لازم؛ امتیاز تجمیعی ۷۵٫۸٪ افت MMLU-Pro را پنهان می‌کند. | https://huggingface.co/klein-ml/KV1-1.2B |
| MemTensor / China | MemT-1.0-Nano | مدل حافظهٔ بومی با حدود ۳۶میلیارد کل/۳میلیارد فعال، حالت محلی و Hyper-memory، دروازهٔ خواندن/نوشتن/فراموشی، ادعای کاهش ۶۶برابری State در تاریخچهٔ ۱۲۸k | وزن کل همچنان لازم است؛ کد سفارشی Transformers؛ بهره‌وری CPU اثبات نشده. | https://huggingface.co/MemTensor/MemT-1.0-Nano |
| KRAFTON / South Korea | Raon-1-mini-preview | مدل MoE حدود ۳۰میلیارد کل/۴میلیارد فعال با توجه خطی و آموزش از صفر؛ GGUF/MLX و Apache-2.0 | نسخهٔ Preview با تمرکز کره‌ای/انگلیسی؛ ۴میلیارد فعال به معنی ۴میلیارد وزن مقیم نیست. | https://huggingface.co/KRAFTON/Raon-1-mini-preview |
| Ant Group inclusionAI / China | Ming-3.0-tts-0.5B | مدل TTS Dense حدود ۵۰۰میلیونی با DiT، Tokenizer صوت و Encoder گوینده، هفت زبان در کارت سازنده | MIT و Runtime اختصاصی؛ فارسی در هفت زبان رسمی نیست. | https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B |
| Ant Group inclusionAI / China | Ming-3.0-asr-tiny | ASR با Context و Hotword برای چینی/انگلیسی؛ نام tiny علی‌رغم حدود ۹میلیارد پارامتر و مخزن ۱۷٫۸GB | MIT؛ پشتیبانی فارسی ندارد و زیر یک میلیارد نیست. | https://huggingface.co/inclusionAI/Ming-3.0-asr-tiny |
| Tencent / China | Hy-Memory-30B-A3B | MoE تخصصی نوشتن و انتخاب واقعیت‌های ماندگار حافظهٔ عامل با ۳۰میلیارد کل/۳میلیارد فعال | Apache-2.0؛ خط مبنای سبک CPU نیست؛ پژوهش سیاست حافظه. | https://huggingface.co/tencent/Hy-Memory-30B-A3B |
| Academic | LayerRoute | پرش لایه تطبیقی با LoRA روی Qwen2.5-0.5B، Router حدود ۲۱٫۵هزار و LoRA حدود ۱٫۰۸میلیون پارامتر، ده Seed؛ سرعت ادعایی 1.02 تا 1.06 برابر (میانگین 1.04) | مقاله سپتامبر ۲۰۲۶؛ سود کم و با انتخاب مدل/Adapter تفاوت دارد. | https://arxiv.org/abs/2609.13682 |

### ضمیمهٔ ۹ — مهندسی مدل‌های فارسی و ایرانی

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Sina Meraji / IbnSina | IbnSina-1.5B | مدل ۱٫۴۸میلیاردی Llama-compatible با ۲۸ لایه، BPE بایتی فارسی ۳۲۷۶۸، Context ۲۰۴۸، GGUF Q4 حدود ۹۰۴MB؛ نویسنده ۳۶٫۷میلیارد توکن آموزش و ۵۱٫۵هزار گفتگو گزارش کرده است | وزن/کد Apache-2.0؛ امتیازهای ۳۱٫۸٪ ParsiNLU-MC و ۲۶٫۸٪ PersianMedQA نزدیک شانس؛ متخصص امنیت اثبات نشده؛ ادعای ۴۶میلیارد توکن باید با اجرای دقیق تفکیک شود. | https://huggingface.co/ibnsina-llm/ibnsina-1.5b |
| Sina Meraji / IbnSina | IbnSina-3B | معماری سبک Qwen3 ولی آموزش از صفر با ۴۰ لایه، d2560، GQA 20/4، Context ۲۰۴۸، ۹۹٫۶میلیارد توکن؛ Checkpoint، Optimizer، Tokenizer، MANIFEST و GGUF Q4 حدود ۱٫۸۱GB | Apache-2.0؛ نویسنده شکست بازتولید یکی از Seedهای SFT سپتامبر ۲۰۲۶ را ثبت کرده است؛ برتری اثبات نشده. | https://huggingface.co/ibnsina-llm/ibnsina-3b-checkpoints |
| Aria Haman Mehr Parseh / Haman Labs | Haman Graph-LLM 125M | مدل گراف+Transformer با ۱۲۴٬۹۷۸٬۹۵۱ پارامتر یکتا، Decoder ده‌لایه، GCN گراف واژگان ۳۱۹۹۵ گره، Context ۲۵۶؛ حدود ۳۹۶٫۹میلیون مواجهه با توکن، Runtime اختصاصی و انتشار وزن/داده/گراف | مجوز Haman 1.0 و انتشار ۱۵ ژوئیهٔ ۲۰۲۶؛ دستیار عمومی نیست و ادعای اولین معماری بومی مستقل اثبات نشده. | https://huggingface.co/aria-haman/haman-fa-article-graph-llm-125m |
| Arad Manamnaoon (individual) | Persian GPT 110M | Decoder دوازده‌لایهٔ ۱۱۰٫۴میلیونی، آموزش از صفر روی حدود ۲۴۴میلیون توکن ویکی‌پدیای فارسی، BPE32k، Context ۱۰۲۴، Perplexity ادعایی 14.52 | مدل آموزشی کوچک و فاقد دستورپذیری؛ منشأ داده و CC-BY-SA-3.0 بررسی شود. | https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch |
| Dibachain / DibaAi | Diba-2B | مدل ۲میلیاردی متمرکز بر فارسی و کدنویسی وب؛ ادعای GGUF Q4 حدود ۱٫۲GB و ۱۸توکن/ثانیه روی CPU چهار‌هسته‌ای؛ DiLLM.nano حدود ۱٫۰۲میلیون سند و ۳۷۹میلیون توکن | کارت Diba-Base دیگر هنوز 'coming soon' می‌گوید؛ فایل واقعی، نسخه و بنچمارک مستقل بررسی شود. | https://huggingface.co/DibaAi/Diba-2B |
| JibayAi | Jibay 2 | مدل حدود ۲میلیاردی مشتق Qwen3؛ سازنده عرضهٔ عمومی ژوئن ۲۰۲۶ پس از معرفی مه ۲۰۲۵ را ادعا می‌کند | ادعای بسیار بزرگ سازنده دربارهٔ مدل اختصاصی Jibay5 **تأییدنشده** است؛ وزن و مجوز واقعی باید بررسی شود. | https://huggingface.co/JibayAi/Jibay_2 |

| سازمان | مدل‌ها و سهم پژوهشی | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Part AI | Dorna and Dorna2: Persian adaptation of Llama3/3.1 8B, GGUF; Tooka-SBERT 0.1B/0.4B semantic models and Persian benchmark ecosystem | بومی‌سازی فارسی Llama3/3.1 هشت‌میلیاردی، GGUF، مدل‌های معنایی Tooka-SBERT حدود ۰٫۱/۰٫۴میلیارد و اکوسیستم ارزیابی فارسی | مبنای بازیابی و Embedding؛ انتشار Dorna قدیمی‌تر از شش‌ماه است. | https://huggingface.co/PartAI |
| University of Tehran | PersianMind-7B: Llama2 adaptation with Persian token extension, noncommercial terms | تخصصی‌سازی Llama2 هفت‌میلیاردی دانشگاه تهران با توسعهٔ Tokenizer فارسی | پژوهش CPT و Tokenizer قدیمی‌تر از بازه؛ محدودیت غیرتجاری. | https://huggingface.co/universitytehran/PersianMind-v1.0 |
| Hooshvare Research Lab | ParsBERT, GPT2-fa, token-classification/sentiment, summarization | مدل‌های فهم فارسی، طبقه‌بندی توکن، احساس و خلاصه‌سازی؛ مبنای Router، برچسب سند و LDI | بیشتر مدل‌ها مربوط به ۲۰۲۰ تا ۲۰۲۳ هستند. | https://huggingface.co/HooshvareLab/models |
| Hezar AI | Persian-focused BERT, OCR models/datasets, parsynth-ocr-4m released/updated around October 2026 | مدل‌های BERT فارسی و OCR، پیکرهٔ parsynth-ocr-4m با انتشار یا به‌روزرسانی حدود اکتبر ۲۰۲۶ | نامزد دادهٔ OCR فارسی LDI؛ بررسی رضایت، مجوز و نشت Train/Test. | https://huggingface.co/hezarai |
| Darsadi research lab | Zagros-1.0-Quick 30.5B MoE, 8 experts top-2, Apache-2.0 | MoE فارسی‌محور ۳۰٫۵میلیاردی با هشت Expert و Top-2 و Apache-2.0 | انتشار سپتامبر ۲۰۲۵ و خارج از بازه؛ وزن کل زیاد است. | https://huggingface.co/darsadilab/zagros-1.0-quick |

### ضمیمهٔ ۱۱ — مدل‌های تخصصی کوچک و محدودیت سرویس‌دهی

| توسعه‌دهنده | مدل / پروژه | ویژگی‌ها و شواهد فنی | محدودیت و نقش پژوهشی | منبع اصلی |
|---|---|---|---|---|
| Jina AI / Germany | jina-reranker-v3.5 | Reranker فهرستی حدود ۶۰۰میلیونی مبتنی بر Qwen3-0.6B با Hybrid 3L2G، رتبه‌بندی هم‌زمان پرس‌وجو و چند سند، Context تا ۱۳۱k؛ اعداد سازنده BEIR=63.20 nDCG@10 و MIRACL=74.11 | وزن رسمی BF16/GGUF؛ مجوز در نسخهٔ ثابت بررسی شود؛ P0 برای LDI و مقایسه با BGE-M3. | https://huggingface.co/jinaai/jina-reranker-v3.5 |
| Rayline / startup | ARC-1.0 | مدل تصمیم احتمالاتی Rayline حدود ۶۰۰میلیونی با Backbone مبتنی بر Qwen3.5-0.8B و ۱۲ لایهٔ ثابت مشترک؛ Headهای موفقیت، توکن، استدلال، PII، عملیات، حوزه و سؤال | وزن Apache-2.0؛ دادهٔ آموزش اصلی اختصاصی؛ vLLM معمول Headهای سفارشی را سرو نمی‌کند و Plugin تنها مرحلهٔ نخست دارد. | https://huggingface.co/rayline-ai/ARC-1.0 |
| iApp / Thailand | OpenThai-SystemOne | مدل تصمیم نوع‌دار حدود ۸۰۰میلیونی بر پایهٔ Qwen3.5-0.8B با SlotHead تا ۲۵۵ گزینه و خروجی امتیاز/بله‌خیر/انتخاب | Apache-2.0؛ آموزش تایلندی/انگلیسی با ۵میلیارد توکن ادامه‌دار؛ کالیبراسیون فارسی نامعلوم. | https://huggingface.co/iapp/OpenThai-SystemOne |
| MinimaLabs / startup | KLM 1.6 | مدل پایهٔ حدود ۹۹میلیونی Hybrid با Gated-DeltaNet و ۱۰۰میلیارد توکن آموزش ادامه‌دار از KLM1.5 | Apache-2.0 و کد سفارشی؛ دستورآموخته نیست و عامل امنیتی محسوب نمی‌شود. | https://huggingface.co/MinimaLabs/KLM-1.6 |
| iApp / Thailand | OpenThai2.0 OCR Text | OCR دو‌جزئی حدود ۱٫۰۲میلیون پارامتر: Detector از PP-OCRv6-tiny و تشخیص‌دهندهٔ CTC حدود ۵۸۷هزار؛ ONNX/OpenVINO CPU | Apache-2.0؛ ادعای ۰٫۳۹ثانیه/A4 و ۴۵۰MB RAM، فقط تایلندی/انگلیسی و نه OCR فارسی. | https://huggingface.co/iapp/OpenThai2.0-OCR-Text |
| iApp / Thailand | OpenThai2.0 OCR Markdown | Parser دید-زبان ۶۳۰٫۸میلیونی آموزش‌دیده برای تایلندی بر پایهٔ Nemotron Parse با Layout، جدول HTML و Markdown | OpenMDW-1.1؛ اجرای رسمی GPU و پشتیبانی تایلندی/انگلیسی؛ بدون آموزش تازه گزینهٔ فارسی نیست. | https://huggingface.co/iapp/OpenThai2.0-OCR-Markdown |
| Alibaba Logics / China | Logics-Parsing-V3 | Parser سند با State بازگشتی سلسله‌مراتبی میان صفحات، پیوند متن/تصویر و ادغام جدول بین صفحات؛ انتشار ۲۲ سپتامبر ۲۰۲۶ | اندازهٔ ۰٫۸میلیاردی از کاتالوگ ثالث است و باید از کارت اصلی تأیید شود؛ پژوهش LDI. | https://huggingface.co/Logics-MLLM/Logics-Parsing-V3 |
| Uraion Labs / startup | Uraion-Agent-Small | عامل کوچک مبتنی بر Qwen3.5-2B با QLoRA برای فراخوانی ابزار و Adapter ادغام‌شده | باید نسخه و نتایج ابزار مستقلاً بررسی شود. | https://huggingface.co/UraionLabs/Uraion-Agent-Small |

## مدخل‌های تکمیلی بدون جدول مستقل
- `LiquidAI/d1-2B`: مدل تصمیم تخصصی خانوادهٔ LFM3؛ https://huggingface.co/LiquidAI/d1-2B
- `MiniCPM5-2B`: نسخهٔ GGUF رسمی؛ https://huggingface.co/openbmb/MiniCPM5-2B-GGUF
- `Kog Laneformer 2B`: پژوهش تأخیر و معماری؛ https://huggingface.co/kogai/laneformer-2b-it
- `TinyLM 275M`: مدل کوچک پایه برای آموزش پژوهشی؛ https://huggingface.co/Shiv-22/tinylm
- `MobileMoE S/M/L`: Checkpointهای Base/SFT/QAT رسماً منتشر شده‌اند؛ https://huggingface.co/facebook/models

## منابع و وضعیت
- گزارش مستقل [MobileMoE](mobilemoe-technical-review-20261116.fa.md) و [Tokenizer](persian-tokenizer-20261116.fa.md) در نسخهٔ فارسی تکمیل شده‌اند.
- روش‌های ترکیب مدل‌ها در سند [همکاری مدل‌ها](composition-methods-20261116.fa.md) ثبت است و این کاتالوگ با روش اشتباه گرفته نمی‌شود.
- برخی مدخل‌های قدیمی تنها ادعای اولیهٔ سازنده‌اند؛ اصلاحیه‌ها، مجوز و وزن واقعی باید با نسخهٔ ثابت منبع کنترل شوند.
- آرشیو `SLM_CATALOG_2026-11-16.md` دست‌نخورده محفوظ است. این نسخهٔ فارسی جدول‌های منبع را به واحدهای قابل مقایسه تبدیل کرده است.

**منابع تکمیلی ردیابی‌شده:** [Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B) و [Ling-3.0-tiny](https://huggingface.co/inclusionAI/Ling-3.0-tiny)؛ هر دو در سطرهای بالا نیز توصیف شده‌اند.
