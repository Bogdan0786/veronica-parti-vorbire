import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

exercises = '''
  <h2 class="section-title" style="color:#d97706; margin-top:40px;">🎮 Exersează Numeralul!</h2>
  
  <div class="exercise-card" style="border-color:#d97706; background:white; padding:20px; border-radius:15px; border-left:6px solid #d97706; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:20px;">
    <div class="q-num" style="color:#d97706; font-weight:bold; margin-bottom:10px;">Exercițiul 1 - Alege răspunsul corect</div>
    <div class="question" style="font-size:1.2rem; margin-bottom:15px;">Care dintre aceste cuvinte este un numeral?</div>
    <div class="options" style="display:flex; gap:10px; flex-wrap:wrap;">
      <button class="option-btn" onclick="checkOption(this,'num1',false,'Numeral')" style="flex:1; min-width:100px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">verde</button>
      <button class="option-btn" onclick="checkOption(this,'num1',true,'Numeral')" style="flex:1; min-width:100px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">șapte</button>
      <button class="option-btn" onclick="checkOption(this,'num1',false,'Numeral')" style="flex:1; min-width:100px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">cântă</button>
    </div>
    <div class="feedback" id="fb-num1" style="margin-top:15px; font-weight:bold; font-size:1.1rem;"></div>
  </div>

  <div class="exercise-card" style="border-color:#b45309; background:white; padding:20px; border-radius:15px; border-left:6px solid #b45309; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:20px;">
    <div class="q-num" style="color:#b45309; font-weight:bold; margin-bottom:10px;">Exercițiul 2 - Alege răspunsul corect</div>
    <div class="question" style="font-size:1.2rem; margin-bottom:15px;">Ce fel de numeral este cuvântul „primul”?</div>
    <div class="options" style="display:flex; gap:10px; flex-wrap:wrap;">
      <button class="option-btn" onclick="checkOption(this,'num2',true,'Numeral')" style="flex:1; min-width:150px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">Numeral ordinal</button>
      <button class="option-btn" onclick="checkOption(this,'num2',false,'Numeral')" style="flex:1; min-width:150px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">Numeral cardinal</button>
      <button class="option-btn" onclick="checkOption(this,'num2',false,'Numeral')" style="flex:1; min-width:150px; padding:12px; font-size:1.1rem; border-radius:8px; border:2px solid #e5e7eb; background:white; cursor:pointer; transition:0.2s;">Nu este numeral</button>
    </div>
    <div class="feedback" id="fb-num2" style="margin-top:15px; font-weight:bold; font-size:1.1rem;"></div>
  </div>
'''

# Find the end of the numeral section.
# We will replace `</div>\n  <button class="back-btn" onclick="showSection('home')">⬅️ Înapoi</button>\n</section>\n\n<!-- ══════════════ ARTICOLUL`
# Wait, let's just insert it before `<button class="back-btn" onclick="showSection('home')">⬅️ Înapoi</button>` of the numeral section.

insert_str = '<button class="back-btn" onclick="showSection(\'home\')">⬅️ Înapoi</button>\n</section>\n\n<!-- ══════════════ ARTICOLUL'
if insert_str in content:
    content = content.replace(insert_str, exercises + '\n  ' + insert_str)
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added exercises to Numeral')
