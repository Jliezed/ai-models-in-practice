# Translation Models

This directory contains machine translation implementations using state-of-the-art models from Hugging Face.

## Models

### Tencent HunYuan MT-7B
- **Model**: `tencent/Hunyuan-MT-7B`
- **Type**: Large Language Model for Machine Translation
- **Parameters**: 7 billion
- **Supported Languages**: Multi-language translation including Chinese, French, Spanish, German, and more

## Features

- Batch translation from Excel files
- Multi-language support (French, Spanish, German, Chinese)
- Resume capability (skips already translated entries)
- Error handling and progress tracking
- Excel file input/output

## Use Cases

- **Bulk Translation**: Translate large datasets of text from Excel files
- **Multi-language Content Creation**: Generate translations for documentation, marketing materials, or educational content
- **Research & Analysis**: Translate datasets for cross-linguistic studies
- **Localization**: Prepare content for international markets

## Usage

### Prerequisites

Install required dependencies:
```bash
pip install transformers torch pandas openpyxl
```

### Running the Translation Script

1. **Prepare your Excel file** with the following structure:
   - Column `en_translation`: English text to translate
   - Columns `fr_translation`, `es_translation`, `de_translation`, `cn_translation`: Will be filled with translations

2. **Run the script**:
   ```bash
   cd nlp/translation
   python translation-tencent-hunyuan-mt-7b.py
   ```

3. **Output**: The script will create `sample_to_translate_hunyuan_translations.xlsx` with all translations filled in.

### Script Features

- **Progress Tracking**: Shows current item being processed (e.g., "Processing 15/55")
- **Resume Capability**: If translation is interrupted, re-running will skip already completed translations
- **Error Handling**: Failed translations are marked with error messages
- **Summary Report**: Final count of completed translations per language

### Performance Notes

- The 7B parameter model requires significant GPU memory
- Each translation takes several seconds depending on hardware
- For 55 texts × 4 languages = 220 total translations
- Consider running in batches for very large datasets

## File Structure

```
nlp/translation/
├── README.md
├── translation-tencent-hunyuan-mt-7b.py    # Main translation script
├── sample_to_translate.xlsx                 # Input Excel file (55 entries)
└── sample_to_translate_hunyuan_translations.xlsx  # Output with translations
```
