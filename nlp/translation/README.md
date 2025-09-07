# 🌍 Machine Translation with HunYuan MT-7B

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-4.21%2B-yellow)](https://huggingface.co/transformers/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Model](https://img.shields.io/badge/🤗%20Model-HunYuan%20MT--7B-orange)](https://huggingface.co/tencent/Hunyuan-MT-7B)

> **State-of-the-art machine translation using Tencent's HunYuan MT-7B model for bulk Excel file processing**

## 🚀 Features

✨ **Smart Translation Pipeline**
- 📊 **Excel Integration** - Direct Excel file processing with automatic column mapping
- 🔄 **Resume Capability** - Intelligent skip of already translated entries  
- 🎯 **Multi-language Support** - French, Spanish, German, Chinese translations
- 📈 **Progress Tracking** - Real-time translation progress with detailed logging
- ⚡ **Error Recovery** - Graceful error handling with detailed error reporting

## 🤖 Model Information

### 🏆 [Tencent HunYuan MT-7B](https://huggingface.co/tencent/Hunyuan-MT-7B)

| Specification | Details |
|---|---|
| **🏢 Organization** | [Tencent](https://huggingface.co/tencent) |
| **📊 Parameters** | 7 Billion |
| **🎯 Architecture** | Causal Language Model |
| **🌐 Languages** | 100+ languages supported |
| **📝 License** | Apache 2.0 |
| **🔗 HF Link** | [`tencent/Hunyuan-MT-7B`](https://huggingface.co/tencent/Hunyuan-MT-7B) |

## 🎯 Use Cases

| Use Case | Description | Best For |
|---|---|---|
| 📚 **Bulk Translation** | Process large Excel datasets | Research, Data Analysis |
| 🌐 **Content Localization** | Multi-language content creation | Marketing, Documentation |
| 🔬 **Research Studies** | Cross-linguistic analysis | Academic Research |
| 🏢 **Enterprise Solutions** | International business content | Corporate Communications |

## 🛠️ Quick Start

### 📋 Prerequisites

```bash
# Install required dependencies
pip install transformers torch pandas openpyxl
```

### 🚀 Usage

#### 1️⃣ **Prepare Excel File**
Create an Excel file with this structure:

| Column | Purpose | Required |
|---|---|---|
| `en_translation` | English source text | ✅ Required |
| `fr_translation` | French translations | ⭐ Auto-filled |
| `es_translation` | Spanish translations | ⭐ Auto-filled |
| `de_translation` | German translations | ⭐ Auto-filled |
| `cn_translation` | Chinese translations | ⭐ Auto-filled |

#### 2️⃣ **Run Translation**
```bash
cd nlp/translation
python translation-tencent-hunyuan-mt-7b.py
```

#### 3️⃣ **Get Results**
- 📥 **Input**: `sample_to_translate.xlsx`
- 📤 **Output**: `sample_to_translate_hunyuan_translations.xlsx`

## 🔧 Advanced Features

### 🎛️ **Configuration Parameters**
The script uses Tencent's recommended inference parameters:

```python
{
  "top_k": 20,
  "top_p": 0.6,
  "repetition_penalty": 1.05,
  "temperature": 0.7,
  "max_new_tokens": 2048
}
```

### 📊 **Progress Monitoring**
- 📈 **Real-time Progress**: `Processing 15/55: Hello, world!`
- ✅ **Skip Existing**: `French: Already translated - Bonjour le monde!`
- ❌ **Error Tracking**: `German: Translation failed - CUDA out of memory`
- 📋 **Final Summary**: `French: 55/55 completed`

## ⚡ Performance & Requirements

### 💻 **System Requirements**

| Component | Minimum | Recommended |
|---|---|---|
| **🧠 RAM** | 16GB | 32GB+ |
| **🎮 GPU Memory** | 8GB VRAM | 16GB+ VRAM |
| **💾 Storage** | 15GB free | 30GB+ free |
| **🐍 Python** | 3.8+ | 3.10+ |

### ⏱️ **Performance Metrics**
- **📊 Dataset Size**: 55 texts × 4 languages = 220 translations
- **⏰ Processing Time**: ~2-5 seconds per translation (GPU-dependent)
- **🔄 Total Time**: ~20-40 minutes for full dataset

## 📁 Project Structure

```
nlp/translation/
├── 📖 README.md                                    # This documentation
├── 🐍 translation-tencent-hunyuan-mt-7b.py       # Main translation script
├── 📊 sample_to_translate.xlsx                     # Input Excel (55 entries)
├── ✅ sample_to_translate_hunyuan_translations.xlsx # Output with translations
└── 📋 requirements_hunyuan.txt                     # Python dependencies
```

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🏢 **Tencent** for the incredible [HunYuan MT-7B](https://huggingface.co/tencent/Hunyuan-MT-7B) model
- 🤗 **Hugging Face** for the excellent [Transformers](https://huggingface.co/transformers/) library
- 🐼 **Pandas** team for powerful data manipulation tools

---

<div align="center">

**🌟 Star this repo if you find it helpful! 🌟**

Made with ❤️ using [HunYuan MT-7B](https://huggingface.co/tencent/Hunyuan-MT-7B)

</div>
