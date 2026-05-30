import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('const probWordsDB = [')
end_idx = content.find('];', start_idx) + 2

if start_idx != -1 and end_idx != -1:
    db_content = content[start_idx:end_idx]
    
    with open('words.js', 'w', encoding='utf-8') as f:
        f.write('// Aici adaugi noile cuvinte sub forma: { c: "varianta_corectă", w: "varianta_greșită" }\n')
        f.write(db_content)
        f.write('\n')
        
    new_content = content[:start_idx] + content[end_idx:]
    
    # insert <script src="words.js"></script> before the first <script> tag at the end
    script_idx = new_content.rfind('<script>')
    if script_idx != -1:
        new_content = new_content[:script_idx] + '<script src="words.js"></script>\n' + new_content[script_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Extracted to words.js successfully')
else:
    print('Could not find probWordsDB')
