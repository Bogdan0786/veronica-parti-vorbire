import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Gramatica<br>limbii române', 'Părțile de<br>vorbire')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted scroll-title to Părțile de vorbire')
