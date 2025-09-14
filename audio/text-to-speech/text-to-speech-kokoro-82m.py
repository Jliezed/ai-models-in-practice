from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import torch
import pandas as pd
import random
import os

# Language mapping to Kokoro lang_codes
language_mapping = {
    'English': 'a',           # American English
    'Spanish': 'e',           # Spanish
    'French': 'f',            # French
    'Italian': 'i',           # Italian
    'Japanese': 'j',          # Japanese
    'Chinese (Mandarin)': 'z', # Mandarin Chinese
    'Portuguese': 'p',        # Brazilian Portuguese
    'Hindi': 'h',             # Hindi
    # Unsupported languages will default to American English
    'German': 'a',
    'Dutch': 'a', 
    'Russian': 'a',
    'Korean': 'a',
    'Arabic': 'a'
}

# All available voices by language code
voices_by_language = {
    'a': {  # American English
        'female': ['af_heart', 'af_alloy', 'af_aoede', 'af_bella', 'af_jessica', 
                  'af_kore', 'af_nicole', 'af_nova', 'af_river', 'af_sarah', 'af_sky'],
        'male': ['am_adam', 'am_echo', 'am_eric', 'am_fenrir', 'am_liam', 
                'am_michael', 'am_onyx', 'am_puck', 'am_santa']
    },
    'b': {  # British English
        'female': ['bf_alice', 'bf_emma', 'bf_isabella', 'bf_lily'],
        'male': ['bm_daniel', 'bm_fable', 'bm_george', 'bm_lewis']
    },
    'e': {  # Spanish
        'female': ['ef_dora'],
        'male': ['em_alex', 'em_santa']
    },
    'f': {  # French
        'female': ['ff_siwis'],
        'male': []
    },
    'h': {  # Hindi
        'female': ['hf_alpha', 'hf_beta'],
        'male': ['hm_omega', 'hm_psi']
    },
    'i': {  # Italian
        'female': ['if_sara'],
        'male': ['im_nicola']
    },
    'j': {  # Japanese
        'female': ['jf_alpha', 'jf_gongitsune', 'jf_nezumi', 'jf_tebukuro'],
        'male': ['jm_kumo']
    },
    'p': {  # Brazilian Portuguese
        'female': ['pf_dora'],
        'male': ['pm_alex', 'pm_santa']
    },
    'z': {  # Mandarin Chinese
        'female': ['zf_xiaobei', 'zf_xiaoni', 'zf_xiaoxiao', 'zf_xiaoyi'],
        'male': ['zm_yunjian', 'zm_yunxi', 'zm_yunxia', 'zm_yunyang']
    }
}

def get_random_voice(lang_code):
    """Get a random voice for the given language code"""
    if lang_code not in voices_by_language:
        lang_code = 'a'  # fallback to American English
    
    all_voices = voices_by_language[lang_code]['female'] + voices_by_language[lang_code]['male']
    return random.choice(all_voices) if all_voices else 'af_heart'

# Read Excel file
excel_file = '/Users/jliez/PycharmProjects/ai-models-in-practice/audio/text-to-speech/data/sample_text_to_speech.xlsx'
df = pd.read_excel(excel_file)

print(f"Processing {len(df)} texts from Excel file...")
print(f"Languages found: {', '.join(df['Language'].unique())}")

# Create output directory
output_dir = 'generated_audio'
os.makedirs(output_dir, exist_ok=True)

# Process each row in the Excel file
for index, row in df.iterrows():
    language = row['Language']
    text = row['Text']
    
    # Get language code and voice
    lang_code = language_mapping.get(language, 'a')
    voice = get_random_voice(lang_code)
    
    print(f"\n--- Processing row {index + 1} ---")
    print(f"Language: {language} -> lang_code: '{lang_code}'")
    print(f"Voice: {voice}")
    print(f"Text: {text[:100]}...")
    
    # Create pipeline for this language
    pipeline = KPipeline(lang_code=lang_code)
    
    # Generate audio
    generator = pipeline(
        text, voice=voice,
        speed=1, split_pattern=r'\n+'
    )
    
    # Process generated audio
    for i, (gs, ps, audio) in enumerate(generator):
        filename = f"{output_dir}/row_{index+1:02d}_{language.replace(' ', '_').replace('(', '').replace(')', '')}_{voice}.wav"
        
        print(f"  Saving: {filename}")
        print(f"  Graphemes: {gs[:50]}...")
        print(f"  Phonemes: {ps[:50]}...")
        
        # Display audio (only autoplay first part of first row)
        display(Audio(data=audio, rate=24000, autoplay=(index==0 and i==0)))
        
        # Save audio file
        sf.write(filename, audio, 24000)

print(f"\nCompleted processing all texts! Audio files saved in '{output_dir}' directory.")