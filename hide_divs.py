import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'id="prob-1"' in line and 'class="prob-content"' in line:
        if 'style="display:none;"' not in line:
            lines[i] = line.replace('class="prob-content"', 'class="prob-content" style="display:none;"')
    if 'id="prob-2"' in line and 'class="prob-content"' in line:
        if 'style="display:none;"' not in line:
            lines[i] = line.replace('class="prob-content"', 'class="prob-content" style="display:none;"')
    if 'id="prob-3"' in line and 'class="prob-content"' in line:
        if 'style="display:none;"' not in line:
            lines[i] = line.replace('class="prob-content"', 'class="prob-content" style="display:none;"')
    if 'id="prob-4"' in line and 'class="prob-content"' in line:
        pass # Already has display:none

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
    
print("Updated display styles")
