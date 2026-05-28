import os
import asyncio
import edge_tts

async def gen_audio(text, filename):
    communicate = edge_tts.Communicate(text, "ro-RO-AlinaNeural", rate="+15%", pitch="+25Hz")
    await communicate.save(filename)

async def main():
    items = {
        "greeting.mp3": "Bună Veronica! Ești gata să învățăm împreună? Iupi!",
        "acasa.mp3": "Acasă",
        "substantiv.mp3": "Substantivul",
        "pronume.mp3": "Pronumele",
        "verb.mp3": "Verbul",
        "adjectiv.mp3": "Adjectivul",
        "adverb.mp3": "Adverbul",
        "prepozitie.mp3": "Prepoziția",
        "conjunctie.mp3": "Conjuncția",
        "interjectie.mp3": "Interjecția",
        "exercitii.mp3": "Exerciții Mari",
        "vocabular.mp3": "Vocabular, Relații Semantice",
    }
    for file, text in items.items():
        print(f"Generating {file}...")
        await gen_audio(text, file)

asyncio.run(main())
