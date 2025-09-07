from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd
import os

def translate_text(model, tokenizer, text, target_lang):
    """Translate text to target language using HunYuan MT-7B model"""
    
    # Create message in the required format
    messages = [
        {"role": "user", "content": f"Translate the following segment into {target_lang}, without additional explanation.\n\n{text}"},
    ]
    
    # Apply chat template
    tokenized_chat = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=False,
        return_tensors="pt"
    )
    
    # Generate translation with recommended parameters
    outputs = model.generate(
        tokenized_chat.to(model.device), 
        max_new_tokens=2048,
        top_k=20,
        top_p=0.6,
        repetition_penalty=1.05,
        temperature=0.7,
        do_sample=True
    )
    
    # Decode output
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the generated response (after the input)
    input_text = tokenizer.decode(tokenized_chat[0], skip_special_tokens=True)
    if input_text in output_text:
        translation = output_text.replace(input_text, "").strip()
    else:
        translation = output_text.strip()
    
    return translation

def main():
    print("Loading Tencent HunYuan MT-7B model...")
    
    model_name_or_path = "tencent/Hunyuan-MT-7B"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto")
    
    print("Model loaded successfully!\n")
    
    # Load Excel file
    excel_file = "sample_to_translate.xlsx"
    print(f"Reading {excel_file}...")
    df = pd.read_excel(excel_file)
    
    # Language mapping
    lang_mapping = {
        'fr_translation': 'French',
        'es_translation': 'Spanish', 
        'de_translation': 'German',
        'cn_translation': 'Chinese'
    }
    
    print(f"Found {len(df)} texts to translate\n")
    
    # Process each row
    for idx, row in df.iterrows():
        english_text = row['en_translation']
        print(f"Processing {idx+1}/{len(df)}: {english_text}")
        
        # Translate to each target language
        for col_name, lang_name in lang_mapping.items():
            # Skip if translation already exists
            if pd.notna(row[col_name]) and row[col_name].strip():
                print(f"  {lang_name}: Already translated - {row[col_name]}")
                continue
            
            try:
                translation = translate_text(model, tokenizer, english_text, lang_name)
                df.loc[idx, col_name] = translation
                print(f"  {lang_name}: {translation}")
            except Exception as e:
                print(f"  {lang_name}: Translation failed - {e}")
                df.loc[idx, col_name] = f"ERROR: {str(e)}"
        
        print("-" * 60)
    
    # Save updated Excel file
    output_file = "sample_to_translate_hunyuan_translations.xlsx"
    df.to_excel(output_file, index=False)
    print(f"\nTranslations saved to {output_file}")
    
    # Print summary
    print("\nTranslation Summary:")
    for col_name, lang_name in lang_mapping.items():
        completed = df[col_name].notna().sum()
        total = len(df)
        print(f"{lang_name}: {completed}/{total} completed")

if __name__ == "__main__":
    main()