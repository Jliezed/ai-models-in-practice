# 🎤 Advanced Text-to-Speech with Kokoro TTS

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Kokoro](https://img.shields.io/badge/🎵%20Kokoro-TTS-purple)](https://huggingface.co/kokoro)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Excel](https://img.shields.io/badge/📊%20Excel-Processing-orange)](https://openpyxl.readthedocs.io/)

> **High-quality text-to-speech generation using Kokoro TTS with bulk Excel file processing and enhanced audio output organization**

## 🚀 Features

✨ **Smart TTS Pipeline**
- 📊 **Excel Integration** - Direct Excel file processing with intelligent column detection
- 🎵 **Multi-voice Support** - Multiple voice options with customizable settings
- 📁 **Organized Output** - Structured audio file generation with descriptive naming
- 🔄 **Demo Mode** - Automatic fallback with sample texts when Excel file is missing
- 📈 **Progress Tracking** - Real-time processing status with detailed logging

## 🤖 Model Information

### 🎵 [Kokoro Text-to-Speech](https://huggingface.co/kokoro)

| Specification | Details |
|---|---|
| **🏢 Organization** | [Kokoro Team](https://huggingface.co/kokoro) |
| **🎯 Architecture** | Neural TTS Model |
| **🌐 Languages** | 9 languages (EN, JP, ZH, ES, FR, HI, IT, PT) |
| **🎤 Voices** | Multiple voice options |
| **📝 License** | Apache 2.0 |
| **🔗 HF Link** | [`kokoro`](https://huggingface.co/kokoro) |

## 🛠️ Quick Start

### 📋 Prerequisites

```bash
# Install required dependencies
pip install -r requirements.txt
```

### 🚀 Usage

#### 1️⃣ **Prepare Excel File**
Create an Excel file with this structure:

| Column | Purpose | Required |
|---|---|---|
| `text` | Text to convert to speech | ✅ Primary |
| `sentence` | Alternative text column | ⭐ Fallback |
| `content` | Alternative text column | ⭐ Fallback |
| `message` | Alternative text column | ⭐ Fallback |
| `speech` | Alternative text column | ⭐ Fallback |

#### 2️⃣ **Run Text-to-Speech**
```bash
cd audio/text-to-speech
python text-to-speech-kokoro-82m.py
```

#### 3️⃣ **Get Results**
- 📥 **Input**: `data/sample_text_to_speech.xlsx`
- 📤 **Output**: `data/generated_audio/*.wav`

## 🔧 Advanced Features

### 🎛️ **Configuration Parameters**
Customize voice and language settings:

```python
{
  "lang_code": "a",
  "voice": "af_heart",
  "audio_format": "wav",
  "sample_rate": 22050
}
```

### 🎤 **Available Voices & Languages**

#### 🇺🇸 **American English** (11F, 9M)
**Top Quality Voices:**
- `af_heart` - Heart voice (Grade A)
- `af_bella` - Bella voice (Grade A)
- `af_nicole` - Nicole voice (Grade B+)
- `af_sarah` - Sarah voice (Grade B)

#### 🇬🇧 **British English** (4F, 4M)
- `bf_emma` - Emma voice (Grade B-)
- `bm_george` - George voice (Grade C+)

#### 🇯🇵 **Japanese** (4F, 1M)
- `jf_alpha` - Alpha voice (Grade C+)
- `jf_gongitsune` - Gongitsune voice (Grade C)

#### 🇨🇳 **Mandarin Chinese** (4F, 4M)
- `zf_xiaobei` - Xiaobei voice
- `zf_xiaoni` - Xiaoni voice

#### 🇪🇸 **Spanish** (1F, 2M)
- `ef_dora` - Dora voice
- `em_alex` - Alex voice
- `em_santa` - Santa voice

#### 🇫🇷 **French** (1F)
- `ff_siwis` - Siwis voice (Grade B-)

#### 🇮🇳 **Hindi** (2F, 2M)
- `hf_alpha` - Alpha voice (Grade C)
- `hf_beta` - Beta voice (Grade C)
- `hm_omega` - Omega voice (Grade C)
- `hm_psi` - Psi voice (Grade C)

#### 🇮🇹 **Italian** (1F, 1M)
- `if_sara` - Sara voice (Grade C)
- `im_nicola` - Nicola voice (Grade C)

#### 🇧🇷 **Brazilian Portuguese** (1F, 2M)
- `pf_dora` - Dora voice
- `pm_alex` - Alex voice
- `pm_santa` - Santa voice

> **📝 Note:** Voices perform optimally with text between 100-200 tokens. Quality grades range from A (highest) to D (lowest).
>
> 🔗 **[View complete voice list and quality ratings →](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)**

### 📊 **Processing Modes**
- 🔄 **Standard Mode**: Process Excel file with text entries
- 🎯 **Demo Mode**: Use predefined sample texts
- 📈 **Batch Mode**: Process multiple texts efficiently

## ⚡ Performance & Requirements

### 💻 **System Requirements**

| Component | Minimum | Recommended |
|---|---|---|
| **🧠 RAM** | 4GB | 8GB+ |
| **🎮 GPU Memory** | Optional | 4GB+ VRAM |
| **💾 Storage** | 2GB free | 10GB+ free |
| **🐍 Python** | 3.8+ | 3.10+ |

## 📁 Project Structure

```
audio/text-to-speech/
├── 📖 README.md                           # This documentation
├── 🐍 text-to-speech-kokoro-improved.py  # Enhanced TTS script
├── 🐍 text-to-speech-kokoro-82m.py       # Original script
├── 📋 requirements.txt                    # Python dependencies
└── data/
    ├── 📊 sample_text_to_speech.xlsx      # Input Excel file
    └── generated_audio/                   # Output directory
        ├── 🎵 000_Hello_world_This_is.wav
        ├── 🎵 001_The_quick_brown_fox.wav
        └── 📋 generation_summary.txt
```

## 🔧 Troubleshooting

### 🚨 **Common Issues**

#### 📦 **Missing Dependencies**
```bash
# The script automatically checks and provides install instructions
pip install kokoro pandas openpyxl
```

#### 🎵 **Kokoro Installation**
```bash
# If kokoro-tts is not available via pip
# Check official repository for source installation
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

- 🎵 **Kokoro Team** for the exceptional [Kokoro TTS](https://huggingface.co/kokoro) model
- 🤗 **Hugging Face** for the excellent model hosting platform
- 🐼 **Pandas** team for powerful data manipulation tools
- 📊 **OpenPyXL** developers for Excel file processing capabilities