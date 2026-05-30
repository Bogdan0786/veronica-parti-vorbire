import re

new_sentences = """
  { c: "Eu am o mostră de parfum.", w: "Eu am o monstră de parfum." },
  { c: "Acesta are repercusiuni grave.", w: "Acesta are repercursiuni grave." },
  { c: "Muncitorul conduce un excavator.", w: "Muncitorul conduce un escavator." },
  { c: "Am făcut zece genuflexiuni.", w: "Am făcut zece genoflexiuni." },
  { c: "Mi-am cumpărat un tricou bleumarin.", w: "Mi-am cumpărat un tricou bleu-marin." },
  { c: "El este proprietarul casei.", w: "El este propietarul casei." },
  { c: "Am stabilit un itinerar clar.", w: "Am stabilit un itinerariu clar." },
  { c: "Vii la mine astă-seară?", w: "Vii la mine astă seară?" },
  { c: "Băiatul așază paharul pe masă.", w: "Băiatul așează paharul pe masă." },
  { c: "Voiam să merg la film.", w: "Vroiam să merg la film." },
  { c: "Am cumpărat două aragaze.", w: "Am cumpărat două aragazuri." },
  { c: "Nu au atins aceste bareme.", w: "Nu au atins aceste baremuri." },
  { c: "Am obținut numeroase succese.", w: "Am obținut numeroase succesuri." },
  { c: "Am găsit trei monede vechi.", w: "Am găsit trei monezi vechi." },
  { c: "S-a ascuns după boschete.", w: "S-a ascuns după boscheți." },
  { c: "Pe stradă sunt multe pancarte.", w: "Pe stradă sunt multe pancărți." },
  { c: "Zidarii au adus noi vopsele.", w: "Zidarii au adus noi vopseluri." },
  { c: "Fata se înșală amarnic.", w: "Fata se înșeală amarnic." },
  { c: "Ea creează rochii de seară.", w: "Ea crează rochii de seară." },
  { c: "Te rog, nu înnoada șireturile așa!", w: "Te rog, nu înoada șireturile așa!" },
  { c: "Băiatul merge la cursuri de înot.", w: "Băiatul merge la cursuri de înnot." },
  { c: "Ne vedem deseară în parc.", w: "Ne vedem de seară în parc." },
  { c: "Nu a fost nicidecum vina ei.", w: "Nu a fost nici de cum vina ei." },
  { c: "Niciun om nu a venit.", w: "Nici un om nu a venit." },
  { c: "A fost odată un prinț.", w: "A fost o dată un prinț." },
  { c: "Ne vom întâlni altădată.", w: "Ne vom întâlni altă dată." },
  { c: "Te rog să nu fii supărat.", w: "Te rog să nu fi supărat." },
  { c: "Nu fi obraznic!", w: "Nu fii obraznic!" },
  { c: "Fii cuminte la școală!", w: "Fi cuminte la școală!" },
  { c: "Tu știi lecția la istorie?", w: "Tu ști lecția la istorie?" },
  { c: "Ți-ar plăcea o înghețată?", w: "Țiar plăcea o înghețată?" },
  { c: "Sper să aibă noroc.", w: "Sper să aibe noroc." },
  { c: "Sper să vină mai repede.", w: "Sper să vie mai repede." },
  { c: "A refuzat să dea înapoi.", w: "A refuzat să deie înapoi." },
  { c: "Băiatul este foarte respectuos.", w: "Băiatul este foarte respectos." },
  { c: "Ai făcut o greșeală mare.", w: "Ai făcut o greșală mare." },
  { c: "Poliția a prins acel delincvent.", w: "Poliția a prins acel delicvent." },
  { c: "Fetița are o panglică roșie.", w: "Fetița are o pamblică roșie." },
  { c: "Am un abțibild cu o mașină.", w: "Am un acțibild cu o mașină." },
  { c: "Am mâncat un sandviș cu șuncă.", w: "Am mâncat un sanviș cu șuncă." },
  { c: "Azi la prânz avem șnițel.", w: "Azi la prânz avem snițel." },
  { c: "Copiii au plecat la joacă.", w: "Copii au plecat la joacă." },
  { c: "Aceștia sunt miniștrii țării.", w: "Aceștia sunt miniștri țării." },
  { c: "Cartea pe care o citesc este lungă.", w: "Cartea care o citesc este lungă." },
  { c: "Bunicul a primit un salariu mare.", w: "Bunicul a primit un salar mare." },
  { c: "El se duce zilnic la serviciu.", w: "El se duce zilnic la servici." },
  { c: "Ochii ei sunt albaștri.", w: "Ochii ei sunt albaștrii." },
  { c: "Băieții s-au dus la munte.", w: "Băieții sau dus la munte." },
  { c: "A intrat dintr-o dată pe ușă.", w: "A intrat dintro dată pe ușă." },
  { c: "Pisica se ascunde dedesubt.", w: "Pisica se ascunde dedesupt." }
"""

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

end_bracket = content.rfind(']')
if end_bracket != -1:
    content = content[:end_bracket] + new_sentences + content[end_bracket:]
    
with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added 50 new sentences!")
