---
doc_id: DEC-DOC-005
language: fa
title: "پیشینه علمی و پروژه‌های واقعی مرجع"
version: 0.1.0
date: 2026-11-12
evidence_level: E0
publication_status: public-research-draft
---

# پیشینه پژوهش و مقایسه گزینه‌های موجود

این متن **مرور گزینش‌شده فنی** از مقاله اصلی، کارت رسمی مدل، مستندات تولیدکننده و کد عمومی تا تاریخ ۲۰۲۶-۱۱-۱۲ است. متاآنالیز نظام‌مند یا بازتولید مستقل ادعاهای بنچمارک نیست. [کاتالوگ دوزبانه منابع](../../research/catalogue.json) ارجاع‌های ماشین‌خوان را دارد.

## مدل‌های کوچک و معماری‌های عصبی

| گزینه | ارتباط با DEC | محدودیت |
|---|---|---|
| [MiniCPM5 1B/2B](https://github.com/OpenBMB/MiniCPM) | معماری Dense سازگار با Llama، راهنمای LoRA/QLoRA، Think، GGUF و تقطیر گزارش‌شده چند معلم | شورای نهفته آماده ندارد؛ فارسی آزموده نشده |
| [Qwen3.5 0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | معماری ترکیبی DeltaNet و Attention با اندازه کوچک | سازگاری LoRA/Runtime و کیفیت فارسی نیازمند آزمون است |
| [Granite 4.0 H](https://huggingface.co/ibm-granite/granite-4.0-h-1b) | ترکیب Mamba-2 و Attention برای استدلال و نقش‌های کنترلی | وضعیت بازگشتی معادل KV Cache Transformer نیست |
| [LFM3](https://huggingface.co/LiquidAI/LFM3-1.7B) | خانواده دارای هسته مشترک و نسخه‌های تخصصی | مجوز وزن و دسترسی به آموزش و Runtime نیازمند کنترل است |
| [RWKV-7](https://github.com/BlinkDL/RWKV-LM) / [Mamba](https://github.com/state-spaces/mamba) | وضعیت بازگشتی فشرده و محاسبه کم‌مصرف | وضعیت آن‌ها مستقیماً با Hidden State هسته LoRA سازگار نیست |
| [BitNet](https://github.com/microsoft/BitNet) | وزن بومی کم‌بیت و Kernel اختصاصی | معماری ۱٫۵۸ بیت بومی معادل Quantization عادی Q4 نیست |

**قاعده:** انتشار وزن و کد، به‌تنهایی نشان‌دهنده کیفیت فارسی/انگلیسی فنی یا امکان آموزش روی GPU با حافظه محدود نیست.

## همکاری نهفته و حافظه

- [LatentMAS (ICML 2026)](https://proceedings.mlr.press/v306/zou26k.html): آزمایش حافظه کاری نهفته مشترک.
- [Interlat (ACL 2026)](https://aclanthology.org/2026.acl-long.1248/): ارتباط Hidden State و سازگارسازی عامل‌ها.
- [LatCom (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1068/): فشرده‌سازی انتقال نهفته پرهزینه.
- [Cache-to-Cache (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/474ada926b331d78f06d95e8913111cc-Abstract-Conference.html): Projection/Fusion قابل آموزش روی KV جفت‌های مدل آزموده‌شده؛ **پژوهش چندسروری معوق است**.
- [LRAgent (ICML 2026)](https://proceedings.mlr.press/v306/jeon26b.html): اشتراک بخش پایه و تحلیل هزینه KV وابسته به LoRA.
- [Agent Primitives](https://github.com/haibojin001/AgentPrimitives): ماژول‌های Review/Vote/Plan/Organize با KV سازگار؛ وضعیت اجرای کامل باید دوباره بررسی شود.
- [LatentMAS-SLoRA](https://github.com/Arifuzzamanjoy/latent_mas_slora): نمونه اجرایی تعویض LoRA و ارتباط نهفته؛ **Adapterهای نقشی عرضه‌شده آموزش‌ندیده‌اند**. نتایج محدود نویسنده، نتیجه DEC نیست.

این پروژه‌ها امکان بخش‌هایی از ایده را نشان می‌دهند، اما هیچ‌یک کل سامانه DEC یا مدل عصبی یکپارچه تأییدشده با همکاری نهفته را آماده ارائه نمی‌کند.

## ابزارها و محصولات

- [PEFT](https://github.com/huggingface/peft)، [Unsloth](https://github.com/unslothai/unsloth) و [TRL](https://huggingface.co/docs/trl/main/index): ابزارهای آموزش LoRA و پژوهش پس‌آموزش.
- [llama.cpp](https://github.com/ggml-org/llama.cpp): اجرای محلی GGUF/CPU؛ [vLLM](https://github.com/vllm-project/vllm) و [SGLang](https://github.com/sgl-project/sglang): استنتاج بهینه با قیود سخت‌افزاری.
- [LangGraph](https://github.com/langchain-ai/langgraph)، [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) و [CrewAI](https://github.com/crewAIInc/crewAI): کنترل جریان ساختاریافته Agentها؛ **نه انتقال نهفته عصبی خودکار**.
- [LMCache](https://github.com/LMCache/LMCache): مدیریت ذخیره KV سازگار؛ نه حافظه استدلال مشارکتی.
- [pgvector](https://github.com/pgvector/pgvector) و [LightRAG](https://github.com/HKUDS/LightRAG): گزینه‌های بازیابی در مقایسه با بستر اسناد موجود؛ جایگزینی بی‌آزمون مجاز نیست.
- [AutoGen](https://github.com/microsoft/autogen)، [LoRAX](https://github.com/predibase/lorax) و [S-LoRA](https://github.com/S-LoRA/S-LoRA) با هشدار نگهداری/آرشیو مواجه‌اند؛ عمدتاً مرجع تاریخی هستند.

## اثر پیشینه علمی بر نوآوری

LoRA، MoE، اشتراک Cache، پیام نهفته و Orchestration به‌صورت مستقل پیشینه گسترده دارند. نوآوری احتمالی DEC باید **یک مکانیزم درونی متمایز و آموزش‌پذیر** با اثر تجربی مستقل باشد. پیش از انتشار سازوکار اختراعی ثبت‌نشده بررسی حقوقی ضرورت دارد. حضور نام در کاتالوگ به معنی انتخاب برای نصب نیست.

[کاتالوگ](../../research/catalogue.json) · [آزمایش‌های برنامه‌ریزی‌شده](../../research/experiment-register.json) · [روش‌شناسی](methods.md) · [نتایج](results.md). هر رکورد در زمینه DEC فعلاً E0 است.
