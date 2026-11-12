---
doc_id: DEC-DOC-021
language: fa
title: "بررسی مدل‌های پایه جدید DEC با تمرکز بر Tool Calling، LoRA و ارتباط نهفته"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# بررسی مدل‌های پایه جدید DEC با تمرکز بر Tool Calling، LoRA و ارتباط نهفته

**وضعیت:** بررسی منبع‌محور ۱۸ گزینه؛ این گزارش هیچ اجرای جدید یا انتخاب نهایی هسته را ادعا نمی‌کند. آزمون‌های انتخاب مدل از این پس **فقط انگلیسی** خواهند بود. مستندات طبق سیاست پروژه به هر دو زبان تولید می‌شوند. نامزدهایی که قبلاً در محیط DEC اجرا شده‌اند، فقط در همان دامنه محدود E1 ارزیابی شده‌اند؛ نامزدهای جدید هنوز E0 هستند.

## 1. نیازمندی‌های Gate انتخاب

هسته باید (۱) پیروی دقیق از دستور انگلیسی، (۲) فراخوانی ساختاریافته ابزار واقعی از طریق API و اجرای چرخه کامل، (۳) عدم فراخوانی ابزار نامرتبط، (۴) ابزار و خروجی قابل اعتبارسنجی، (۵) آموزش LoRA/QLoRA روی وزن مرجع با مجوز روشن، (۶) تعویض دو Adapter آموزش‌دیده بدون بارگذاری مجدد Base، (۷) دسترسی قابل آزمون به Hidden States و مدیریت صحیح KV/Recurrent State، (۸) مصرف RAM/VRAM و زمان قابل کنترل، و (۹) حقوق توزیع و تجاری‌سازی قابل دفاع داشته باشد. مجوز، امنیت، سازگاری و حقوق مالکیت *Gate سخت* هستند؛ نمره متوسط نمی‌تواند نقص آن‌ها را جبران کند.

## 2. گروه‌های اولویت

- **آزمون فوری پیشنهادی**: Qwen3.5-2B, MiniCPM5-2B, Granite 4.2-3B, Qwen3.5-4B, Raon-1 nano, QVAC BotPsy-0.8B
- **کنترل داخلی موجود**: LFM3-1.7B, Qwen2.5-3B-Instruct
- **مقایسه مرحله دوم**: Qwen3-1.7B, Ministral 3 3B Instruct, Gemma 4 E2B-it, Nemotron 3 Nano 4B, K2-Horizon-3.7B, Qwen3-4B-Instruct-2507
- **پژوهش یا ابزار جانبی**: Granite 4.0 H-1B, Ternary Bonsai 2 4B, FunctionGemma 270M, LFM2.5-24B-A2B

## 3. فهرست مستند گزینه‌ها

| گزینه | معماری / اندازه | مجوز اعلام‌شده | کاربرد پیشنهادی | ریسک / ابهام |
|---|---|---|---|---|
| [Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | 2B dense/hybrid | Apache-2.0 | هسته کم‌هزینه Agent؛ مسیر Base جداگانه برای LoRA | DeltaNet/Attention hybrid؛ State و اتصال LoRA باید واقعاً آزمون شود |
| [MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B) | 2.52B dense Llama | Apache-2.0 | نامزد اصلی آزمون چند LoRA روی Base مشترک؛ دستورالعمل رسمی PEFT | Tool Parser رسمی SGLang و نسخه GGUF باید جدا بررسی شود |
| [Granite 4.2-3B](https://huggingface.co/ibm-granite/granite-4.2-3b) | 3B dense Transformer | Apache-2.0 | هسته Agent با Thinking قابل تنظیم و ساختار Dense قابل بررسی | سقف تفکر و Parser باید دقیق کنترل شوند؛ آموزش LoRA در محیط ما آزمایش نشده |
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | 4B hybrid DeltaNet | Apache-2.0 | مرجع توانمندتر برای ارزیابی کیفیت ابزار و دستور | آموزش با GPU شش‌گیگابایتی و دسترسی به State بدون ارزیابی تضمین نیست |
| [Raon-1 nano](https://huggingface.co/KRAFTON/Raon-1-nano) | 3.1B total / 1.5B effective, hybrid | Apache-2.0 | نسل تازه ۱۱ نوامبر ۲۰۲۶؛ حافظه بازگشتی و Tool Use انگلیسی | تازه‌انتشار، کد سفارشی و پیچیدگی LoRA/State؛ ادعای سازنده E0 |
| [QVAC BotPsy-0.8B](https://qvac.tether.io/models/botpsy) | 0.8B Qwen3.5 derivative | Apache-2.0 | تخصصی‌شده برای Tool Executor یا Router سبک؛ انتشار ۱۱ نوامبر | توانایی عمومی و متخصص مشترک از کیفیت Tool Calling نتیجه نمی‌شود |
| [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | 1.73B tri-hybrid | LFM Open License v1.0 | کنترل اجرایی DEC با ۱۱/۱۲ ابزار؛ معماری کم‌مصرف و Base مشخص | رژیم مجوز تجاری و صحت State/LoRA نیازمند Gate مستقل |
| [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 1.7B dense Transformer | Apache-2.0 | مرجع ساده برای LoRA و Hidden State، با پیچیدگی کمتر از Hybrid | امتیاز Tool Calling روی سخت‌افزار DEC هنوز معلوم نیست |
| [Ministral 3 3B Instruct](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) | 3.4B language + 0.4B vision | Apache-2.0 | رقیب Dense با Function Calling و مسیر Base جداگانه | حجم واقعی و پیش‌نیاز Runtime/vision برای ۶GB باید آزمون شوند |
| [Gemma 4 E2B-it](https://huggingface.co/google/gemma-4-E2B-it) | 5.1B total / 2.3B effective | Apache-2.0 | تازه و دارای Function Calling؛ معماری Per-Layer Embedding برای مقایسه | E2B به معنای ۲B وزن ذخیره‌شده نیست؛ آموزش ۶GB اثبات نشده |
| [Nemotron 3 Nano 4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16) | 3.97B Mamba-2 + Attention | NVIDIA Nemotron Open Model License | مدل انگلیسی Agent با مرجع وضعیت بازگشتی | پشتیبانی Runtime و شرایط اختصاصی مجوز باید سنجیده شوند |
| [K2-Horizon-3.7B](https://huggingface.co/IFM/K2-Horizon-3.7B) | 3.7B core dense; embeddings extra | Apache-2.0 | مدل پژوهشی شفاف با کد و داده آموزش و ابزار | بودجه استدلال پیشنهادی طولانی و H200 با CPU-first پروژه ناهم‌راستا است |
| [Granite 4.0 H-1B](https://huggingface.co/ibm-granite/granite-4.0-h-1b) | ~1.5B total hybrid Mamba2 | Apache-2.0 | مرجع وضعیت کم‌حجم و Router؛ رقیب معماری بازگشتی | State Mamba با KV عادی یکسان نیست؛ تعویض Adapter تأیید نشده |
| [Ternary Bonsai 2 4B](https://huggingface.co/prism-ml/Ternary-Bonsai-2-4B-gguf) | 4.21B ternary language; 0.95–1.15GB weights | Apache-2.0 | روش نو برای اجرای فشرده، نه لزوماً مبنای آموزش LoRA | بسته‌بندی ویژه و Fork/Kernel؛ امکان LoRA و بازتولید نیازمند آزمون |
| [FunctionGemma 270M](https://deepmind.google/models/gemma/functiongemma/) | 270M specialized tool model | Gemma terms | مدل Router کوچک قابل تخصصی‌سازی، نه هسته استدلال | مجوز Gemma جدا؛ بدون Fine-tune کیفیت نهایی را مفروض نگیریم |
| [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | 24B total / ~2.45B active MoE | LFM Open License v1.0 | Teacher/مرجع MoE؛ برای هسته ۶GB مناسب فرض نشود | وزن همه ۲۴B پارامتر باید ذخیره شود؛ فعال‌بودن ۲B VRAM را حل نمی‌کند |
| [Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) | 4B dense Transformer | Apache-2.0 | مرجع Dense نسبتاً بالغ برای Tool Calling و PEFT | ممکن است روی GPU شش‌گیگابایتی برای LoRA نیازمند Offload باشد |
| [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) | 3B dense Transformer | qwen-research | برنده محدود ۲۲/۲۴ آزمون DEC؛ فقط کنترل تا روشن شدن مجوز | مجوز مرجع رسمی qwen-research است؛ وزن محلی و حقوق تجاری باید تطبیق شوند |

## 4. رابطه با آزمون E1 داخلی DEC

آزمون فعلی DEC برای Qwen2.5:3B امتیاز ۲۲/۲۴ و برای LFM3-1.7B امتیاز ۲۰/۲۴ را نشان داده است؛ در هر دو مورد ۱۰/۱۰ چرخه فراخوانی مثبت ابزار موفق بودند. این‌ها فقط بر یک مجموعه ۲۴‌سؤالی انگلیسی و یک اجرا با توابع مصنوعی متکی‌اند. **وزن آزموده‌شده Qwen2.5 از مخزن محلی آمده و نسخه و حقوق دقیق آن باید با مدل رسمی تطبیق شود.** مدل Qwen2.5-3B-Instruct رسمی مجوز qwen-research دارد و بدون تعیین حقوق آن نباید به هسته یک محصول تجاری تبدیل شود.

## 5. یافته‌های معماری و ریسک تصمیم

**Dense در برابر Hybrid:** مدل‌های Dense مانند MiniCPM5-2B، Granite 4.2-3B، Qwen3-1.7B و Qwen3-4B برای نخستین آزمایش تعویض LoRA و برداشت Hidden State نسبتاً ساده‌ترند. در Qwen3.5، Raon، Granite H و LFM3 حالت DeltaNet، Mamba، Convolution یا Attention ترکیبی وجود دارد؛ هیچ‌کدام به معنای اشتراک معتبر Cache میان Adapterها نیست.

**LoRA واقعی:** PEFT به‌صورت رسمی افزودن و تعویض Adapter روی Base واحد را پشتیبانی می‌کند، ولی توافق نوع Adapter، ماژول‌های هدف، رتبه، نسخه دقیق وزن و Tensor سازگاری باید آزمایش شود. خروجی موفق GGUF برای استنتاج، اثبات امکان آموزش QLoRA روی GPU شش‌گیگابایتی نیست. آزمایش PEFT باید با وزن قابل آموزش Safetensors انجام شود.

**حافظه نهفته:** Hidden State استخراج‌پذیر با `output_hidden_states=True` یک قابلیت معمول Transformers است؛ اما عبور Hidden State از یک متخصص به متخصص دیگر و استفاده مجدد از KV/SSM State پس از تغییر Adapter به‌صورت خودکار درست یا ایمن نیست. پروژه LatentMAS-SLoRA یک نمونه پژوهشی دارد، اما Adapterهای همراه آن آموزش‌دیده نیستند؛ بنابراین شاهدی بر برتری متخصص‌های LoRA نیست.

**مالکیت و حقوق تجاری:** در مدل‌های Apache-2.0 باید شرایط NOTICE، منشأ مشتقات و وابستگی‌های ثالث رعایت شود. LFM Open License v1.0 در تولید تجاری شرکت‌های با درآمد بالای ۱۰ میلیون دلار در سال نیازمند مجوز سازمانی است. مجوز qwen-research برای وزن رسمی Qwen2.5-3B-Instruct یک مانع احتمالی جدی تجاری است. مجوز NVIDIA و Gemma نیز جداگانه بررسی حقوقی می‌خواهند. مالکیت مستندات و کد نوآورانه DEC به معنای مالکیت وزن‌های شخص ثالث نیست.

## 6. فهرست انتخاب کوتاه و مسیر آزمون

**برای هسته عملیاتی Agent:** ابتدا Qwen3.5-2B، Granite 4.2-3B، Qwen3.5-4B و Raon-1 nano را در برابر LFM3-1.7B موجود بسنجید. **برای معماری چند LoRA و ارتباط نهفته:** ابتدا MiniCPM5-2B و Qwen3-1.7B (Dense)، سپس Qwen3.5-2B (Hybrid) را وارد آزمون دو Adapter کنید. **برای Router/Tool Executor فوق‌سبک:** BotPsy-0.8B در کنار FunctionGemma 270M بررسی شود. دو مسیر را بدون داشتن شواهد یکی نکنید.

## 7. حداقل پروتکل پذیرش پیشنهادی

ابتدا کنترل مجوز و انتشار دقیق وزن (Revision و SHA256)، سپس اجرای دست‌کم ۴۰ سؤال انگلیسی پیروی از دستور و ۴۰ سناریوی انگلیسی ابزار شامل موارد منفی، ابزارهای هم‌نام، آرگومان نامعتبر و درخواست چندمرحله‌ای؛ حداقل سه Seed و داوری مستقل. پس از غربالگری، روی نامزدهای باقی‌مانده دو LoRA واقعی با داده دارای حق استفاده آموزش دهید؛ بارگذاری Base یک‌باره، تغییر Adapter، آزمون عدم نشت وضعیت، صحت KV/SSM Cache و Hidden State، ثبت RAM/VRAM و آزمون Rollback الزامی باشد. وزن‌های خام و اطلاعات غیرعمومی در GitHub منتشر نشوند. این‌ها **معیارهای پیشنهادی قبل از آزمون** هستند، نه نتایج موجود.

نتیجه قطعی: هنوز هیچ مدل نهایی برای DEC انتخاب نشده است. این گزینه‌ها *نامزد تحقیقاتی* هستند؛ ادعاهای سازندگان درباره Benchmarks جایگزین آزمون یکسان روی سخت‌افزار DEC نیستند.

## 8. مراجع اصلی روش

- https://huggingface.co/docs/transformers/peft
- https://huggingface.co/docs/peft/main/quicktour
- https://huggingface.co/docs/transformers/main_classes/output
- https://github.com/Arifuzzamanjoy/latent_mas_slora
- https://huggingface.co/blog/LiquidAI/lfm3
- https://huggingface.co/blog/ibm-granite/granite-4-2

### Research evidence and reproducibility
- [Prior five-model English tools/instructions E1 test](model-english-instruction-tools.md)
- [Machine-readable catalogue](../../research/model-candidates-20261112.json)
