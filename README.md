# 🤖 AI Models in Practice

A curated collection of practical AI model implementations and examples for real-world applications.

---

## 📋 Available Models

### 🎵 Audio Processing

#### Text-to-Speech
- **📄 `audio/text-to-speech/text-to-speech-kokoro-82m.py`**
  - **Model**: Kokoro 82M
  - **Purpose**: Generate natural speech from text
  - **Languages**: English, Spanish, French, Italian, Japanese, Chinese (Mandarin), Portuguese, Hindi
  - **Features**: Multiple voice options, batch processing from Excel files

### 🌐 Natural Language Processing

#### Machine Translation
- **📄 `nlp/translation/translation-tencent-hunyuan-mt-7b.py`**
  - **Model**: Tencent HunYuan MT-7B
  - **Purpose**: High-quality multi-language translation
  - **Languages**: English → French, Spanish, German, Chinese
  - **Features**: Batch translation from Excel files

---

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-models-in-practice
   ```

2. **Set up environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run a model**
   ```bash
   # Text-to-Speech example
   python audio/text-to-speech/text-to-speech-kokoro-82m.py

   # Translation example
   python nlp/translation/translation-tencent-hunyuan-mt-7b.py
   ```

---

## 📁 Project Structure

```
ai-models-in-practice/
├── 🎵 audio/
│   └── text-to-speech/
│       ├── text-to-speech-kokoro-82m.py
│       └── data/
├── 🌐 nlp/
│   └── translation/
│       ├── translation-tencent-hunyuan-mt-7b.py
│       └── data/
└── 📖 README.md
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
