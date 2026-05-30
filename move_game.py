import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_btn = '    <button class="tab-btn" id="tab-joc" style="background:linear-gradient(135deg,#3b82f6,#2563eb)" onclick="showSection(\'joc\')">🎮 Provocarea Cuvintelor</button>\n'

# Find the end of nav-tabs to insert the button
nav_end_idx = -1
for i, line in enumerate(lines):
    if 'tab-problematice' in line:
        nav_end_idx = i + 1
        break

if nav_end_idx != -1:
    lines.insert(nav_end_idx, new_btn)

# Now find the prob-4 button and prob-4 div to extract
btn_prob_4_idx = -1
prob_4_start_idx = -1
prob_4_end_idx = -1

for i, line in enumerate(lines):
    if 'showProb(\'prob-4\')' in line:
        btn_prob_4_idx = i
    if '<div id="prob-4"' in line:
        prob_4_start_idx = i
        # find the matching closing div
        div_count = 0
        for j in range(i, len(lines)):
            div_count += lines[j].count('<div')
            div_count -= lines[j].count('</div')
            if div_count == 0:
                prob_4_end_idx = j
                break

if btn_prob_4_idx != -1 and prob_4_start_idx != -1 and prob_4_end_idx != -1:
    prob_4_content = lines[prob_4_start_idx:prob_4_end_idx+1]
    
    # Remove prob-4 button and div
    del lines[prob_4_start_idx:prob_4_end_idx+1]
    # adjust btn index since lines were removed if btn was after? No, btn is before.
    if btn_prob_4_idx > prob_4_end_idx:
        btn_prob_4_idx -= (prob_4_end_idx - prob_4_start_idx + 1)
    del lines[btn_prob_4_idx]
    
    # Modify prob_4_content to be a section
    prob_4_content[0] = '<section class="section" id="joc">\n'
    prob_4_content[-1] = '</section>\n'
    
    # Insert it before the last </script> or something. Let's insert before <!-- ══════════════ EXERCIȚII MARI ══════════════ --> or at the end of sections
    insert_idx = -1
    for i, line in enumerate(lines):
        if '<script src="words.js">' in line:
            insert_idx = i
            break
            
    if insert_idx != -1:
        for j, l in enumerate(prob_4_content):
            lines.insert(insert_idx + j, l)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Moved game to main page')
