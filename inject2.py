import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add nav button in the top menu
nav_btn_anchor = '''onclick="showSection('substantiv')">📦 Substantiv</button>'''
nav_btn_insert = '''onclick="showSection('substantiv')">📦 Substantiv</button>
  <button class="tab-btn"        id="tab-articol" style="background:linear-gradient(135deg,#c026d3,#e879f9)" onclick="showSection('articol')">📝 Articol</button>'''
html = html.replace(nav_btn_anchor, nav_btn_insert)

# 2. Add menu card in the home grid
menu_card_anchor = '''<span class="big-emoji">📦</span><h2>Substantivul</h2><p>Numele lucrurilor, ființelor și locurilor</p>
    </button>'''
menu_card_insert = '''<span class="big-emoji">📦</span><h2>Substantivul</h2><p>Numele lucrurilor, ființelor și locurilor</p>
    </button>
    <button class="menu-card" style="background:linear-gradient(135deg,#c026d3,#e879f9)" onclick="showSection('articol')">
      <div class="done-badge" id="done-articol">✅</div>
      <span class="big-emoji">📝</span><h2>Articolul</h2><p>Hăinuța substantivului</p>
    </button>'''
html = html.replace(menu_card_anchor, menu_card_insert)

# 3. Add the content section just before PRONUME
section_html = '''
<!-- ══════════════ ARTICOLUL ══════════════ -->
<div id="sec-articol" class="content-section" style="display:none;">
  <h2 class="section-title" style="color:#c026d3;">📝 Articolul</h2>
  
  <div class="def-box" style="border-left-color:#c026d3;">
    <span class="def-icon">📌</span>
    <strong>Articolul</strong> este „hăinuța” care se așează mereu pe lângă un <em>substantiv</em>! El ne ajută să ne dăm seama dacă știm sau nu exact despre ce obiect vorbim. De obicei, stă lipit la sfârșit sau vine imediat în față.
  </div>

  <div class="info-grid">
    <div class="info-card" style="background:linear-gradient(135deg,#c026d3,#d946ef)"><span class="emoji">🎯</span><h3>Hotărât</h3><p>Obiectul este precis, cunoscut. Stă <strong>la final</strong>: băiat<strong>ul</strong>, fat<strong>a</strong>, pom<strong>ii</strong>.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#d946ef,#e879f9)"><span class="emoji">❓</span><h3>Nehotărât</h3><p>Un obiect la întâmplare. Stă <strong>în față</strong>: <strong>un</strong> băiat, <strong>o</strong> fată, <strong>niște</strong> pomi.</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#e879f9,#f0abfc)"><span class="emoji">🔑</span><h3>Posesiv (Genitival)</h3><p>Arată al cui este obiectul: <strong>al</strong>, <strong>a</strong>, <strong>ai</strong>, <strong>ale</strong> (ex: cartea <em>a</em> fetei).</p></div>
    <div class="info-card" style="background:linear-gradient(135deg,#f0abfc,#f5d0fe)"><span class="emoji">👉</span><h3>Demonstrativ (Adjectival)</h3><p>Arată pe care anume: <strong>cel</strong>, <strong>cea</strong>, <strong>cei</strong>, <strong>cele</strong> (ex: băiatul <em>cel</em> înalt).</p></div>
  </div>
  
  <div class="tip-box" style="background:#fae8ff; border-color:#d946ef; color:#86198f;">
      💛 <strong>Trucul Veronicăi:</strong> Gândește-te la el ca la o etichetă! Fără el, cuvântul pare gol!
  </div>

  <h3 class="exercises-title" style="color:#d946ef;">✏️ Exerciții – Articolul</h3>
  <div class="score-bar" id="score-articol">⭐ Puncte: <span class="score-num" id="pts-articol">0</span> / <span id="total-articol">4</span>
    <div class="progress-wrap"><div class="progress-fill" id="prog-articol"></div></div>
  </div>
  <div class="exercise-card" style="border-color:#d946ef;">
    <div class="q-num" style="color:#d946ef;">Exercițiul 1</div>
    <div class="question">În expresia „un câine”, ce fel de articol este „un”?</div>
    <div class="options">
      <button class="option-btn" onclick="checkOption(this,'a1',false,'articol')">Hotărât</button>
      <button class="option-btn" onclick="checkOption(this,'a1',true,'articol')">Nehotărât</button>
      <button class="option-btn" onclick="checkOption(this,'a1',false,'articol')">Posesiv</button>
      <button class="option-btn" onclick="checkOption(this,'a1',false,'articol')">Demonstrativ</button>
    </div>
    <div class="feedback" id="fb-a1"></div>
  </div>
  <div class="exercise-card" style="border-color:#d946ef;">
    <div class="q-num" style="color:#d946ef;">Exercițiul 2</div>
    <div class="question">Ce articol este în cuvântul „băiatul”?</div>
    <div class="options">
      <button class="option-btn" onclick="checkOption(this,'a2',false,'articol')">Nehotărât (un)</button>
      <button class="option-btn" onclick="checkOption(this,'a2',true,'articol')">Hotărât (-ul)</button>
      <button class="option-btn" onclick="checkOption(this,'a2',false,'articol')">Posesiv (al)</button>
      <button class="option-btn" onclick="checkOption(this,'a2',false,'articol')">Nu are articol</button>
    </div>
    <div class="feedback" id="fb-a2"></div>
  </div>
  <div class="exercise-card" style="border-color:#d946ef;">
    <div class="q-num" style="color:#d946ef;">Exercițiul 3</div>
    <div class="question">Care este articolul posesiv din propoziția: „Jucăria este a fetei.”?</div>
    <div class="options">
      <button class="option-btn" onclick="checkOption(this,'a3',false,'articol')">Jucăria</button>
      <button class="option-btn" onclick="checkOption(this,'a3',false,'articol')">este</button>
      <button class="option-btn" onclick="checkOption(this,'a3',true,'articol')">a</button>
      <button class="option-btn" onclick="checkOption(this,'a3',false,'articol')">fetei</button>
    </div>
    <div class="feedback" id="fb-a3"></div>
  </div>
  <div class="exercise-card" style="border-color:#d946ef;">
    <div class="q-num" style="color:#d946ef;">Exercițiul 4</div>
    <div class="question">Care este articolul demonstrativ: „băiatul cel curajos”?</div>
    <div class="options">
      <button class="option-btn" onclick="checkOption(this,'a4',false,'articol')">băiatul</button>
      <button class="option-btn" onclick="checkOption(this,'a4',true,'articol')">cel</button>
      <button class="option-btn" onclick="checkOption(this,'a4',false,'articol')">curajos</button>
      <button class="option-btn" onclick="checkOption(this,'a4',false,'articol')">-ul</button>
    </div>
    <div class="feedback" id="fb-a4"></div>
  </div>
</div>

'''
html = html.replace('<!-- ══════════════ PRONUME ══════════════ -->', section_html + '\n<!-- ══════════════ PRONUME ══════════════ -->')

# 4. Update qCounts
html = html.replace('const qCounts={\n  Substantiv:4,', 'const qCounts={\n  articol:4, Substantiv:4,')

# 5. Update mp3Map
html = html.replace('const mp3Map = {\n  \'acasă\':', 'const mp3Map = {\n  \'articol\': \'articol.mp3\',\n  \'articolul\': \'articol.mp3\',\n  \'acasă\':')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
