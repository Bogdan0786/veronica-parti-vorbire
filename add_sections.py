import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix onclick for Numeral and Articol
# Look for the cards
numeral_pattern = r'<button class="fairy-card" onclick="showSection\(\'exercitii\'\)">(?=\s*<div class="fc-num" style="background:#f59e0b;">5</div>)'
articol_pattern = r'<button class="fairy-card" onclick="showSection\(\'exercitii\'\)">(?=\s*<div class="fc-num" style="background:#8b5cf6;">6</div>)'

content = re.sub(numeral_pattern, '<button class="fairy-card" onclick="showSection(\'numeral\')">', content)
content = re.sub(articol_pattern, '<button class="fairy-card" onclick="showSection(\'articol\')">', content)

# Create the sections
new_sections = """
<!-- ══════════════ NUMERALUL ══════════════ -->
<section class="section" id="numeral">
  <div class="content-box" style="background: linear-gradient(to right, #fef3c7, #fffbeb); border-left: 6px solid #f59e0b;">
    <h2 style="color: #92400e; display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 2rem;">🧙‍♂️</span> Numeralul
    </h2>
    <p style="font-size: 1.2rem; color: #444; margin-bottom: 20px;">
      Numeralul este partea de vorbire flexibilă care exprimă <strong>un număr</strong>, <strong>numărul obiectelor</strong> sau <strong>ordinea</strong> acestora prin numărare.
    </p>
    
    <h3 style="color: #d97706; margin-top: 20px;">Tipuri principale:</h3>
    <ul style="list-style: none; padding: 0; font-size: 1.1rem; color: #444;">
      <li style="margin-bottom: 10px;">🔢 <strong>Numeral cardinal</strong>: exprimă un număr exact (<em>unu, doi, trei, o sută</em>).<br><span style="color:#6b7280; font-size:1rem;">Exemplu: Am mâncat <strong>două</strong> mere.</span></li>
      <li style="margin-bottom: 10px;">🥇 <strong>Numeral ordinal</strong>: exprimă ordinea obiectelor (<em>primul, al doilea, a treia</em>).<br><span style="color:#6b7280; font-size:1rem;">Exemplu: El a sosit <strong>primul</strong> la concurs.</span></li>
    </ul>

    <div style="background: white; padding: 15px; border-radius: 10px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
      <h4 style="color: #ea580c; margin-bottom: 10px;">💡 Câteva capcane:</h4>
      <p style="font-size: 1rem; color: #444; margin-bottom: 0;">Spunem corect: „ora <strong>două</strong>” (nu „ora doi”), „clasa a <strong>două</strong>sprezecea” (nu „a doisprezecea”), dar „etajul <strong>al doilea</strong>”.</p>
    </div>
  </div>
  <button class="back-btn" onclick="showSection('home')">⬅️ Înapoi</button>
</section>

<!-- ══════════════ ARTICOLUL ══════════════ -->
<section class="section" id="articol">
  <div class="content-box" style="background: linear-gradient(to right, #ede9fe, #f5f3ff); border-left: 6px solid #8b5cf6;">
    <h2 style="color: #5b21b6; display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 2rem;">📜</span> Articolul
    </h2>
    <p style="font-size: 1.2rem; color: #444; margin-bottom: 20px;">
      Articolul este partea de vorbire flexibilă care <strong>însoțește un substantiv</strong> pentru a arăta în ce măsură obiectul denumit de acesta este cunoscut vorbitorilor. Nu are înțeles de sine stătător!
    </p>

    <h3 style="color: #7c3aed; margin-top: 20px;">Cele două tipuri principale:</h3>
    <div style="display: flex; flex-direction: column; gap: 15px;">
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <strong>📌 Articolul hotărât</strong> (arată că obiectul este bine cunoscut)
        <p style="margin: 5px 0 0 0; color: #666; font-size: 1rem;">Se lipește la sfârșitul cuvântului: băiat<strong>ul</strong>, fat<strong>a</strong>, pom<strong>ii</strong>, cărți<strong>le</strong>.</p>
      </div>
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <strong>❓ Articolul nehotărât</strong> (arată că obiectul nu este precis cunoscut)
        <p style="margin: 5px 0 0 0; color: #666; font-size: 1rem;">Stă în fața cuvântului (separat): <strong>un</strong> băiat, <strong>o</strong> fată, <strong>niște</strong> pomi, <strong>niște</strong> cărți.</p>
      </div>
    </div>
  </div>
  <button class="back-btn" onclick="showSection('home')">⬅️ Înapoi</button>
</section>

"""

# Insert before Exerciții Mari
insert_target = '<!-- ══════════════ EXERCIȚII MARI ══════════════ -->'
if insert_target in content:
    content = content.replace(insert_target, new_sections + insert_target)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Numeral and Articol sections")
