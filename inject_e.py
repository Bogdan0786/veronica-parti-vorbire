import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('litera_e.html', 'r', encoding='utf-8') as f:
    e_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="prob-3"' in line:
        for j in range(i, i+10):
            if '<div style="text-align:center' in lines[j]:
                start_del = j
                for k in range(j, j+10):
                    if '</div>' in lines[k]:
                        end_del = k
                        # replace the lines
                        lines[start_del:end_del+1] = [e_content + '\n']
                        break
                break
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Injected successfully')
