import re

new_sentences = """
  { c: "Afară s-a înnorat puternic.", w: "Afară s-a înorat puternic." },
  { c: "A început să se înnopteze.", w: "A început să se înopteze." },
  { c: "Hainele s-au înnegrit de fum.", w: "Hainele s-au înegrit de fum." },
  { c: "Vrea să-și înnoiască garderoba.", w: "Vrea să-și înoiască garderoba." },
  { c: "Nu vreau să te înnebunesc cu asta.", w: "Nu vreau să te înebunesc cu asta." },
  { c: "Gestul lui l-a înnobilat.", w: "Gestul lui l-a înobilat." },
  { c: "Mașina s-a înnămolit pe drum.", w: "Mașina s-a înămolit pe drum." },
  { c: "Cerul este tare înnegurat azi.", w: "Cerul este tare înegurat azi." },
  { c: "El are un talent înnăscut la desen.", w: "El are un talent înăscut la desen." },
  { c: "Peștele înoată foarte rapid.", w: "Peștele înnoată foarte rapid." },
  { c: "Competiția de înot a fost grea.", w: "Competiția de înnot a fost grea." }
"""

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

end_bracket = content.rfind(']')
if end_bracket != -1:
    content = content[:end_bracket] + new_sentences + content[end_bracket:]
    
with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added double-n words!")
