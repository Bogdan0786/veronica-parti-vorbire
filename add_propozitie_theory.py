import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update buttons
content = content.replace(
    '<button class="fairy-card" onclick="showSection(\'propozitie\')">\n    <div class="fc-num" style="background:#ef4444;">1</div>\n    <div class="fc-char">👑</div>\n    <div class="fc-label" style="color:#b91c1c;">Predicatul</div>',
    '<button class="fairy-card" onclick="showSection(\'predicat\')">\n    <div class="fc-num" style="background:#ef4444;">1</div>\n    <div class="fc-char">👑</div>\n    <div class="fc-label" style="color:#b91c1c;">Predicatul</div>'
)

content = content.replace(
    '<button class="fairy-card" onclick="showSection(\'propozitie\')">\n    <div class="fc-num" style="background:#3b82f6;">2</div>\n    <div class="fc-char">👤</div>\n    <div class="fc-label" style="color:#1d4ed8;">Subiectul</div>',
    '<button class="fairy-card" onclick="showSection(\'subiect\')">\n    <div class="fc-num" style="background:#3b82f6;">2</div>\n    <div class="fc-char">👤</div>\n    <div class="fc-label" style="color:#1d4ed8;">Subiectul</div>'
)

content = content.replace(
    '<button class="fairy-card" onclick="showSection(\'propozitie\')">\n    <div class="fc-num" style="background:#10b981;">3</div>\n    <div class="fc-char">🎀</div>\n    <div class="fc-label" style="color:#047857;">Atributul</div>',
    '<button class="fairy-card" onclick="showSection(\'atribut\')">\n    <div class="fc-num" style="background:#10b981;">3</div>\n    <div class="fc-char">🎀</div>\n    <div class="fc-label" style="color:#047857;">Atributul</div>'
)

content = content.replace(
    '<button class="fairy-card" onclick="showSection(\'propozitie\')">\n    <div class="fc-num" style="background:#f59e0b;">4</div>\n    <div class="fc-char">🧩</div>\n    <div class="fc-label" style="color:#b45309;">Complementul</div>',
    '<button class="fairy-card" onclick="showSection(\'complement\')">\n    <div class="fc-num" style="background:#f59e0b;">4</div>\n    <div class="fc-char">🧩</div>\n    <div class="fc-label" style="color:#b45309;">Complementul</div>'
)

# New sections content
new_sections = """
<!-- 👑 PREDICATUL -->
<section class="section" id="predicat">
  <button class="home-btn" onclick="goTopAndHome()">🏠 Acasă</button>
  <h2 class="section-title" style="color:#ef4444;">👑 Predicatul</h2>
  <p class="section-subtitle">Inima propoziției, care ne spune ce se întâmplă!</p>
  <div class="def-box" style="background:linear-gradient(135deg,#fef2f2,#fee2e2);border-left:8px solid #ef4444;">
    <strong>💡 Definiție:</strong> Predicatul este partea principală de propoziție care arată <strong>ce face, ce este sau cum este subiectul</strong>.<br><br>
    🎯 <strong>Întrebări:</strong> <em>Ce face? Cine este? Ce este? Cum este?</em>
  </div>
  <div class="info-grid">
    <div class="info-card" style="background:linear-gradient(135deg,#ef4444,#f87171)"><span class="emoji">🏃</span><h3>Acțiune</h3><p>Băiatul <strong>aleargă</strong>.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#f87171,#fca5a5)"><span class="emoji">⭐</span><h3>Stare</h3><p>Fata <strong>este veselă</strong>.</p></div>
  </div>
  <div class="tip-box">💛 <strong>Trucul Veronicăi:</strong> Fără predicat, nu există propoziție! Caută mereu verbul mai întâi!</div>
</section>

<!-- 👤 SUBIECTUL -->
<section class="section" id="subiect">
  <button class="home-btn" onclick="goTopAndHome()">🏠 Acasă</button>
  <h2 class="section-title" style="color:#3b82f6;">👤 Subiectul</h2>
  <p class="section-subtitle">Eroul principal al propoziției!</p>
  <div class="def-box" style="background:linear-gradient(135deg,#eff6ff,#dbeafe);border-left:8px solid #3b82f6;">
    <strong>💡 Definiție:</strong> Subiectul este partea principală de propoziție care arată <strong>cine face acțiunea</strong> exprimată de predicat.<br><br>
    🎯 <strong>Întrebări:</strong> <em>Cine? Ce?</em> (adresate predicatului)
  </div>
  <div class="info-grid">
    <div class="info-card" style="background:linear-gradient(135deg,#3b82f6,#60a5fa)"><span class="emoji">👧</span><h3>Exemplu</h3><p><strong>Veronica</strong> citește.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#60a5fa,#93c5fd)"><span class="emoji">🐶</span><h3>Exemplu</h3><p><strong>Câinele</strong> latră.</p></div>
  </div>
  <div class="tip-box">💛 <strong>Trucul Veronicăi:</strong> Subiectul stă mereu în cazul Nominativ! El comandă verbului cum să se acorde!</div>
</section>

<!-- 🎀 ATRIBUTUL -->
<section class="section" id="atribut">
  <button class="home-btn" onclick="goTopAndHome()">🏠 Acasă</button>
  <h2 class="section-title" style="color:#10b981;">🎀 Atributul</h2>
  <p class="section-subtitle">Decorațiunea perfectă pentru substantive!</p>
  <div class="def-box" style="background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-left:8px solid #10b981;">
    <strong>💡 Definiție:</strong> Atributul este partea secundară de propoziție care <strong>determină un substantiv</strong> sau un înlocuitor al acestuia, adăugându-i detalii.<br><br>
    🎯 <strong>Întrebări:</strong> <em>Care? Ce fel de? Al, a, ai, ale cui? Câți? Câte?</em>
  </div>
  <div class="info-grid">
    <div class="info-card" style="background:linear-gradient(135deg,#10b981,#34d399)"><span class="emoji">🍎</span><h3>Ce fel de?</h3><p>Măr <strong>roșu</strong>.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#34d399,#6ee7b7)"><span class="emoji">🎒</span><h3>Al cui?</h3><p>Ghiozdanul <strong>băiatului</strong>.</p></div>
  </div>
  <div class="tip-box">💛 <strong>Trucul Veronicăi:</strong> Atributul stă întotdeauna pe lângă un cuvânt-obiect (substantiv). Dacă descrie o acțiune (un verb), atunci este complement!</div>
</section>

<!-- 🧩 COMPLEMENTUL -->
<section class="section" id="complement">
  <button class="home-btn" onclick="goTopAndHome()">🏠 Acasă</button>
  <h2 class="section-title" style="color:#f59e0b;">🧩 Complementul</h2>
  <p class="section-subtitle">Piesa de puzzle care completează verbul!</p>
  <div class="def-box" style="background:linear-gradient(135deg,#fffbeb,#fef3c7);border-left:8px solid #f59e0b;">
    <strong>💡 Definiție:</strong> Complementul este partea secundară de propoziție care <strong>determină un verb</strong>, un adjectiv sau un adverb, arătând obiectul, locul, timpul sau modul acțiunii.<br><br>
    🎯 <strong>Întrebări:</strong> <em>Pe cine? Ce? Unde? Când? Cum? Din ce cauză?</em>
  </div>
  <div class="info-grid">
    <div class="info-card" style="background:linear-gradient(135deg,#f59e0b,#fbbf24)"><span class="emoji">📖</span><h3>Pe cine/Ce?</h3><p>Citesc <strong>o carte</strong>.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#fbbf24,#fcd34d)"><span class="emoji">🏡</span><h3>Unde? Când?</h3><p>Mergem <strong>acasă</strong> <strong>astăzi</strong>.</p></div>
  </div>
  <div class="tip-box">💛 <strong>Trucul Veronicăi:</strong> Complementul este prietenul bun al verbului! Îți dă mereu detalii suplimentare despre cum, când sau unde se întâmplă lucrurile.</div>
</section>
"""

# Find the old #propozitie section and replace it with the new sections
start_idx = content.find('<!-- 🌟 PROPOZIȚIE 🌟 -->')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_sections + content[end_idx + 10:]
else:
    # Append if not found
    print("Could not find old propozitie section, appending to end.")
    content += new_sections

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated propozitie buttons and sections')
