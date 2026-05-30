import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

buttons_html_old = """
<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; margin-bottom: 25px;">
  <button onclick="document.getElementById('score-sinonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #10b981, #059669); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3); font-weight: bold; flex: 1; min-width: 200px;">✏️ Exerciții – Sinonime</button>
  <button onclick="document.getElementById('score-antonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #e11d48, #be123c); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(225, 29, 72, 0.3); font-weight: bold; flex: 1; min-width: 200px;">⚔️ Exerciții – Antonime</button>
  <button onclick="document.getElementById('score-omonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3); font-weight: bold; flex: 1; min-width: 200px;">👯 Exerciții – Omonime</button>
  <button onclick="document.getElementById('score-paronime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #a855f7, #9333ea); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(168, 85, 247, 0.3); font-weight: bold; flex: 1; min-width: 200px;">🔤 Exerciții – Paronime</button>
</div>
"""

buttons_html_new = """
<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; margin-bottom: 25px;">
  <button onclick="document.getElementById('score-sinonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #10b981, #059669); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3); font-weight: bold; flex: 1; min-width: 200px;">✏️ Exerciții – Sinonime</button>
  <button onclick="document.getElementById('score-antonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #e11d48, #be123c); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(225, 29, 72, 0.3); font-weight: bold; flex: 1; min-width: 200px;">⚔️ Exerciții – Antonime</button>
  <button onclick="document.getElementById('score-omonime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3); font-weight: bold; flex: 1; min-width: 200px;">👯 Exerciții – Omonime</button>
  <button onclick="document.getElementById('score-paronime').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #a855f7, #9333ea); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(168, 85, 247, 0.3); font-weight: bold; flex: 1; min-width: 200px;">🔤 Exerciții – Paronime</button>
  <button onclick="document.getElementById('score-omofone').scrollIntoView({behavior: 'smooth', block: 'center'})" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border: none; padding: 12px 20px; border-radius: 50px; font-size: 1.1rem; cursor: pointer; box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3); font-weight: bold; flex: 1; min-width: 200px;">🎧 Exerciții – Omofone</button>
</div>
"""

if buttons_html_old.strip() in content:
    content = content.replace(buttons_html_old.strip(), buttons_html_new.strip())
else:
    print("Could not find the old buttons HTML block.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added Omofone button')
