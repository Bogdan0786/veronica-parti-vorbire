import sys

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

end_idx = content.rfind(']')
if end_idx != -1:
    content = content[:end_idx] + '  { c: "pancartă", w: "pancardă" },\n  { c: "tobogan", w: "topogan" }\n' + content[end_idx:]

with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

new_rows = '''          <tr>
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Pancartă</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Pancardă</td>
            <td style="padding: 15px; color: #444;">Provine din franceză (pancarte). Varianta cu „d” (pancardă) este incorectă.</td>
          </tr>
          <tr style="background-color: #fdf2f8;">
            <td style="padding: 15px; font-weight: bold; color: #15803d;">Tobogan</td>
            <td style="padding: 15px; color: #dc2626; text-decoration: line-through;">Topogan</td>
            <td style="padding: 15px; color: #444;">Deși foarte multă lume folosește varianta cu „p” din obișnuință, cuvântul corect este scris cu „b” (din fr. toboggan).</td>
          </tr>'''

lines = html_content.split('\n')
for i, line in enumerate(lines):
    if 'Monstră</td>' in line:
        for j in range(i, i+10):
            if '</tr>' in lines[j]:
                lines.insert(j+1, new_rows)
                break
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Updated both words.js and index.html')
