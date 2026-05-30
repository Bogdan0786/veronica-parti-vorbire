import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update buttons
buttons = [
    ('score-sinonime', 'div-sinonime'),
    ('score-antonime', 'div-antonime'),
    ('score-omonime', 'div-omonime'),
    ('score-paronime', 'div-paronime'),
    ('score-omofone', 'div-omofone')
]

for score_id, div_id in buttons:
    old_onclick = f"onclick=\"document.getElementById('{score_id}').scrollIntoView({{behavior: 'smooth', block: 'center'}})\""
    new_onclick = f"onclick=\"document.getElementById('{div_id}').style.display='block'; document.getElementById('{score_id}').scrollIntoView({{behavior: 'smooth', block: 'center'}})\""
    content = content.replace(old_onclick, new_onclick)

# Wrap sections
sections = [
    ("✏️ Exerciții – Sinonime", "div-sinonime", "reward-sinonime"),
    ("✏️ Exerciții – Antonime", "div-antonime", "reward-antonime"),
    ("✏️ Exerciții – Omonime", "div-omonime", "reward-omonime"),
    ("✏️ Exerciții – Paronime", "div-paronime", "reward-paronime"),
    ("✏️ Exerciții – Omofone", "div-omofone", "reward-omofone")
]

for title_text, div_id, reward_id in sections:
    # Find the start (h3 title)
    title_pattern = rf"(<h3 class='exercises-title'[^>]*>{title_text}</h3>)"
    content = re.sub(title_pattern, rf'<div id="{div_id}" style="display:none; margin-top:20px;">\n\1', content)
    
    # Find the end (end of reward div)
    # The reward div looks like:
    # <div class='reward' id='reward-sinonime'>
    # <div class='reward-stars'>⭐⭐⭐⭐⭐</div>
    # <h2>🏆 Felicitări, Veronica!</h2>
    # <p>Ai terminat exercițiile pentru Sinonime!</p>
    # </div>
    reward_pattern = rf"(<div class='reward' id='{reward_id}'>.*?</div>\s*)"
    # Note: re.sub with re.DOTALL is needed if there are newlines
    content = re.sub(reward_pattern, r'\1</div>\n', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Wrapped exercises in hidden divs and updated buttons')
