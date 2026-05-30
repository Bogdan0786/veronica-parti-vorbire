import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

end_idx = content.find('</html>')
if end_idx != -1:
    content = content[:end_idx + 7]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Truncated duplicate content correctly.")
else:
    print("Could not find </html>")
