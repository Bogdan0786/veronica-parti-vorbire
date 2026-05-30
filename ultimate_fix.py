import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the broken half container at the top
broken_top_start = content.find('<div class="fairy-row" id="propozitie-cards-container" style="display:none;">')
if broken_top_start != -1:
    meadow_start = content.find('<div class="meadow-strip">', broken_top_start)
    if meadow_start != -1:
        content = content[:broken_top_start] + content[meadow_start:]

# 2. Remove the orphaned bottom chunk
orphan_start = content.find('    <div class="fc-char">👤</div>')
if orphan_start != -1:
    orphan_end = content.find('<!-- ══════════════ NUMERALUL ══════════════ -->', orphan_start)
    if orphan_end != -1:
        # Include the preceding blank lines or broken button
        btn_start = content.rfind('<button', max(0, orphan_start - 100), orphan_start)
        if btn_start != -1:
            content = content[:btn_start] + content[orphan_end:]
        else:
            content = content[:orphan_start] + content[orphan_end:]

# 3. Insert the perfect propozitie-cards-container exactly before meadow-strip
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

meadow_start2 = content.find('<div class="meadow-strip">')
if meadow_start2 != -1:
    content = content[:meadow_start2] + correct_container + content[meadow_start2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed layout once and for all!")
