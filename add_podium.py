import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS to head
css = '''
    /* PODIUM */
    .game-end-flex { display: flex; flex-wrap: wrap; justify-content: space-around; gap: 30px; align-items: center; }
    .podium-wrapper { display: flex; align-items: flex-end; gap: 10px; margin-top: 20px; justify-content: center; }
    .podium-container { display: flex; align-items: flex-end; gap: 4px; }
    .podium-spot { display: flex; flex-direction: column; align-items: center; }
    .p-char { font-size: 3.5rem; animation: bounce 2s infinite; }
    .p-step { width: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; color: white; border-radius: 8px 8px 0 0; box-shadow: inset 0 2px 5px rgba(255,255,255,0.4); }
    .step-1 { height: 120px; background: linear-gradient(135deg, #fbbf24, #d97706); }
    .step-2 { height: 80px; background: linear-gradient(135deg, #94a3b8, #64748b); }
    .step-3 { height: 50px; background: linear-gradient(135deg, #b45309, #78350f); }
    .p-off { font-size: 3rem; margin-bottom: 0px; filter: grayscale(50%); display:flex; align-items:flex-end; padding-bottom:10px; }
'''

if '/* PODIUM */' not in content:
    content = content.replace('  </style>', css + '\n  </style>')

# Replace game-end-screen content
new_end_screen = '''<div id="game-end-screen" style="display:none; padding: 30px; background:white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
<div class="game-end-flex">
  <div style="flex: 1; min-width: 250px; text-align: center;">
    <div id="game-end-emoji" style="font-size: 4rem; margin-bottom: 10px;">🏆</div>
    <h3 id="game-end-title" style="font-size: 2rem; color: #1e40af; margin-bottom: 15px;">Felicitări!</h3>
    <p id="game-end-msg" style="font-size: 1.3rem; color: #444; margin-bottom: 25px;">Ai răspuns corect la 8 din 10 cuvinte!</p>
    <button class="tab-btn" onclick="startGame()" style="background:linear-gradient(135deg,#10b981,#059669); font-size:1.2rem; padding:12px 30px;">🔄 Joacă din nou</button>
  </div>
  <div style="flex: 1; min-width: 250px;">
    <div class="podium-wrapper">
      <div class="podium-container">
        <div class="podium-spot spot-2">
          <div class="p-char" id="p-char-2">👦</div>
          <div class="p-step step-2">2</div>
        </div>
        <div class="podium-spot spot-1">
          <div class="p-char" id="p-char-1">👧</div>
          <div class="p-step step-1">1</div>
        </div>
        <div class="podium-spot spot-3">
          <div class="p-char" id="p-char-3">👱‍♀️</div>
          <div class="p-step step-3">3</div>
        </div>
      </div>
      <div class="p-off" id="p-char-off" style="display:none;">👧😭</div>
    </div>
  </div>
</div>
</div>'''

# Regex to replace `<div id="game-end-screen".*?</div>\n</section>`
# We will just replace from `<div id="game-end-screen"` until `</section>`
start_idx = content.find('<div id="game-end-screen"')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_end_screen + '\n' + content[end_idx:]

# Modify endGame logic
end_logic = '''
  const charV = '👧';
  const charB = '👦';
  const charG = '👱‍♀️';

  let p1 = document.getElementById('p-char-1');
  let p2 = document.getElementById('p-char-2');
  let p3 = document.getElementById('p-char-3');
  let pOff = document.getElementById('p-char-off');
  
  pOff.style.display = 'none';

  if (gameScore === 10) {
    p1.innerText = charV;
    p2.innerText = charB;
    p3.innerText = charG;
  } else if (gameScore === 9) {
    p1.innerText = charB;
    p2.innerText = charV;
    p3.innerText = charG;
  } else if (gameScore === 8) {
    p1.innerText = charB;
    p2.innerText = charG;
    p3.innerText = charV;
  } else {
    p1.innerText = charB;
    p2.innerText = charG;
    p3.innerText = '🧑';
    pOff.innerText = '👧😢';
    pOff.style.display = 'block';
  }
}'''

content = content.replace("document.getElementById('game-end-msg').innerText += ' dar ești pe drumul cel bun!';\n  }\n}", "document.getElementById('game-end-msg').innerText += ' dar ești pe drumul cel bun!';\n  }" + end_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated podium logic")
