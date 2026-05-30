import re

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Removals
content = re.sub(r'\s*\{\s*c:\s*"sindroame",\s*w:\s*"sindromuri"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"sloganuri",\s*w:\s*"slogane"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"pieri",\s*w:\s*"pierii"\s*\},\n', '\n', content)

# Modifications
content = content.replace(
    '{ c: "Te rog, nu înnoada șireturile așa!", w: "Te rog, nu înoada șireturile așa!" }',
    '{ c: "Băiatul înnoadă șireturile.", w: "Băiatul înoadă șireturile." }'
)

content = content.replace(
    '{ c: "A intrat dintr-o dată pe ușă.", w: "A intrat dintro dată pe ușă." }',
    '{ c: "A intrat dintr-odată pe ușă.", w: "A intrat dintr-o dată pe ușă." }'
)

with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied final rigorous DOOM2 checks!")
