import sys

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_words = '''  { c: "rucsac", w: "ruzsac / ruczac" },
  { c: "vise (imagini în somn)", w: "visuri (imagini în somn)" },
  { c: "visuri (idealuri)", w: "vise (idealuri)" },
  { c: "chitare", w: "chitări" },
  { c: "va veni", w: "v-a veni" },
  { c: "ați", w: "a-ți (când e verb auxiliar)" },
'''

end_idx = content.rfind(']')
if end_idx != -1:
    content = content[:end_idx] + new_words + content[end_idx:]

with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

row_prob_1 = '''          <tr>
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Rucsac</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Ruzsac / Ruczac</td>
            <td style="padding: 15px; color: #444;">Din germană (Rucksack). Se scrie și se pronunță cu „cs”, nu „z” sau „cz”.</td>
          </tr>'''

for i, line in enumerate(lines):
    if 'Topogan</td>' in line:
        for j in range(i, i+10):
            if '</tr>' in lines[j]:
                lines.insert(j+1, row_prob_1)
                break
        break

row_prob_2 = '''          <tr style="background-color: #fdf2f8;">
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Vise / Visuri</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Vise / Visuri (confundate)</td>
            <td style="padding: 15px; color: #444;">Avem ambele plurale, dar cu sensuri diferite! <b>Vise</b> = imagini din timpul somnului. <b>Visuri</b> = idealuri, dorințe mărețe.</td>
          </tr>
          <tr>
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Chitare</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Chitări</td>
            <td style="padding: 15px; color: #444;">Forma corectă și acceptată conform DOOM este „chitare”. (Ex: Două chitare).</td>
          </tr>'''

for i, line in enumerate(lines):
    if 'Complee</td>' in line:
        for j in range(i, i+10):
            if '</tr>' in lines[j]:
                lines.insert(j+1, row_prob_2)
                break
        break

row_prob_3 = '''          <tr>
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Epocă, Elicopter</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Iepocă, Ielicopter</td>
            <td style="padding: 15px; color: #444;">Neologismele NU primesc acel „i” în față! Se pronunță exact cu „E” curat, cum se scriu.</td>
          </tr>'''

for i, line in enumerate(lines):
    if 'Elev' in line and 'Ecran' in line:
        for j in range(i, i+10):
            if '</tr>' in lines[j]:
                lines.insert(j+1, row_prob_3)
                break
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Updated everything')
