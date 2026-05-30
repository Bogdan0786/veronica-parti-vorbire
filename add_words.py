import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if 'probWordsDB = [' in content:
    content = content.replace(
        'probWordsDB = [',
        'probWordsDB = [\n  { c: "mostră", w: "monstră" },'
    )

new_rows = '''          <tr style="background-color: #fdf2f8;">
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Serviciu</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Servici</td>
            <td style="padding: 15px; color: #444;">Deși în vorbirea curentă se folosește des „servici”, forma corectă acceptată de DOOM este „serviciu”.</td>
          </tr>
          <tr>
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Mostră</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Monstră</td>
            <td style="padding: 15px; color: #444;">Provine din latinescul „monstrare” (a arăta), dar în limba română a pierdut „n”-ul. „Monstră” este greșit (se confundă cu monstrul).</td>
          </tr>'''

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'Astă seară / Aseară</td>' in line:
        for j in range(i, i+10):
            if '</tr>' in lines[j]:
                lines.insert(j+1, new_rows)
                break
        break

content = '\n'.join(lines)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated database and table 1')
