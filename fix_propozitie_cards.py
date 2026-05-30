import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We will find and remove all occurrences of the broken propozitie-cards-container fragments.
# Fragment 1: The broken start before meadow-strip
p1_start = content.find('<div class="fairy-row" id="propozitie-cards-container" style="display:none;">')
if p1_start != -1:
    p1_end = content.find('<div class="meadow-strip">', p1_start)
    if p1_end != -1:
        # Remove this fragment
        content = content[:p1_start] + content[p1_end:]

# Fragment 2: The remaining buttons somewhere in the file
p2_start = content.find('    <div class="fc-char">👤</div>\n    <div class="fc-label" style="color:#1d4ed8;">Subiectul</div>')
if p2_start != -1:
    # Go back to the <button class="fairy-card" onclick="showSection('subiect')">
    p2_btn_start = content.rfind('<button class="fairy-card" onclick="showSection(\'subiect\')">', 0, p2_start)
    p2_end = content.find('</div>\n<!-- ══════════════ NUMERALUL ══════════════ -->', p2_btn_start)
    if p2_end != -1:
        # Include the </div> that closes propozitie-cards-container if it's there
        content = content[:p2_btn_start] + content[p2_end + 6:]
    else:
        # Just find the end of the 4th button
        p2_end = content.find('</button>', content.find('showSection(\'complement\')', p2_btn_start)) + 9
        content = content[:p2_btn_start] + content[p2_end:]

# 2. Re-insert the proper propozitie-cards-container exactly before meadow-strip
correct_container = """<div class="fairy-row" id="propozitie-cards-container" style="display:none;">
  <button class="fairy-card" onclick="showSection('predicat')">
    <div class="fc-num" style="background:#ef4444;">1</div>
    <div class="fc-char">👑</div>
    <div class="fc-label" style="color:#b91c1c;">Predicatul</div>
    <div class="fc-desc">arată ce face subiectul (acțiunea).</div>
  </button>
  <button class="fairy-card" onclick="showSection('subiect')">
    <div class="fc-num" style="background:#3b82f6;">2</div>
    <div class="fc-char">👤</div>
    <div class="fc-label" style="color:#1d4ed8;">Subiectul</div>
    <div class="fc-desc">arată cine face acțiunea.</div>
  </button>
  <button class="fairy-card" onclick="showSection('atribut')">
    <div class="fc-num" style="background:#10b981;">3</div>
    <div class="fc-char">🎀</div>
    <div class="fc-label" style="color:#047857;">Atributul</div>
    <div class="fc-desc">determină (explică) un substantiv.</div>
  </button>
  <button class="fairy-card" onclick="showSection('complement')">
    <div class="fc-num" style="background:#f59e0b;">4</div>
    <div class="fc-char">🧩</div>
    <div class="fc-label" style="color:#b45309;">Complementul</div>
    <div class="fc-desc">determină (ajută) un verb.</div>
  </button>
</div>
"""

meadow_start = content.find('<div class="meadow-strip">')
if meadow_start != -1:
    content = content[:meadow_start] + correct_container + content[meadow_start:]
else:
    print("WARNING: meadow-strip not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored propozitie-cards-container cleanly.")
