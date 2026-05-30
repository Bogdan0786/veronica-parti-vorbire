import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change onclick
content = content.replace("onclick=\"showSection('propozitie')\"", "onclick=\"togglePropozitieCards()\"")

# Add the new container right before NUMERALUL section
new_cards = """
<div class="fairy-row" id="propozitie-cards-container" style="display:none;">
  <button class="fairy-card" onclick="showSection('propozitie')">
    <div class="fc-num" style="background:#ef4444;">1</div>
    <div class="fc-char">👑</div>
    <div class="fc-label" style="color:#b91c1c;">Predicatul</div>
    <div class="fc-desc">arată ce face subiectul (acțiunea).</div>
  </button>
  <button class="fairy-card" onclick="showSection('propozitie')">
    <div class="fc-num" style="background:#3b82f6;">2</div>
    <div class="fc-char">👤</div>
    <div class="fc-label" style="color:#1d4ed8;">Subiectul</div>
    <div class="fc-desc">arată cine face acțiunea.</div>
  </button>
  <button class="fairy-card" onclick="showSection('propozitie')">
    <div class="fc-num" style="background:#10b981;">3</div>
    <div class="fc-char">🎀</div>
    <div class="fc-label" style="color:#047857;">Atributul</div>
    <div class="fc-desc">determină (explică) un substantiv.</div>
  </button>
  <button class="fairy-card" onclick="showSection('propozitie')">
    <div class="fc-num" style="background:#f59e0b;">4</div>
    <div class="fc-char">🧩</div>
    <div class="fc-label" style="color:#b45309;">Complementul</div>
    <div class="fc-desc">determină (ajută) un verb.</div>
  </button>
</div>
"""

# Insert before NUMERALUL
insert_target = '<!-- ══════════════ NUMERALUL ══════════════ -->'
if insert_target in content:
    content = content.replace(insert_target, new_cards + '\n' + insert_target)

# Add JS toggle function
js_target = 'function toggleFairyCards() {'
js_addition = """
function togglePropozitieCards() {
  const container = document.getElementById('propozitie-cards-container');
  if (container.style.display === 'none') {
    container.style.display = 'flex';
  } else {
    container.style.display = 'none';
  }
}
"""
if js_target in content:
    content = content.replace(js_target, js_addition + '\n' + js_target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added propozitie cards and toggle script")
