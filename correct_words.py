import json
import re

with open('words.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to extract the array, modify it, and write it back.
# The array starts at `const probWordsDB = [` and ends at `];`

start_idx = content.find('[')
end_idx = content.rfind(']')

array_str = content[start_idx:end_idx+1]
# Some keys don't have quotes, let's fix that for JSON parsing if needed, but it's simpler to just do string replacements.

content = content.replace('{ c: "abțibild", w: "abțiguib" }', '{ c: "abțibild", w: "acțibild" }')
content = content.replace('{ c: "șnițel", w: "șnițel (cu s)" }', '{ c: "șnițel", w: "snițel" }')
content = content.replace('{ c: "complee", w: "compleuri" }', '{ c: "compleuri", w: "complee" }')
content = content.replace('{ c: "ouă", w: "ouăle" }', '{ c: "ouă", w: "ouo" }')
content = content.replace('{ c: "roșcove", w: "roșcove" }', '{ c: "roșcove", w: "roșcoave" }')
content = content.replace('{ c: "rucsac", w: "ruzsac / ruczac" }', '{ c: "rucsac", w: "ruczac" }')

# Removals:
content = re.sub(r'\s*\{\s*c:\s*"reper",\s*w:\s*"reper \(accent greșit\)"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"șasiu",\s*w:\s*"șasiu \(accent greșit\)"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"vadră",\s*w:\s*"vadră \(accent\)"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"făraș",\s*w:\s*"făraș \(accent\)"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"chibrit",\s*w:\s*"chibrite"\s*\},\n', '\n', content)
content = re.sub(r'\s*\{\s*c:\s*"chitare",\s*w:\s*"chitări"\s*\},\n', '\n', content)

with open('words.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated words.js")

# Let's count the number of words left
with open('words.js', 'r', encoding='utf-8') as f:
    final_content = f.read()

count = final_content.count('{ c:')
print(f"Total words: {count}")

