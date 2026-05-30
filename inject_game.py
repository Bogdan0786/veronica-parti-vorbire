import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

ui_content = '''    <button class="tab-btn" onclick="showProb('prob-4')" style="background:linear-gradient(135deg,#3b82f6,#2563eb); width: 100%; max-width: 600px; padding: 15px; font-size: 1.1rem; white-space: normal; line-height: 1.3; margin-top: 10px;">4. Provocarea cuvintelor (JOC)</button>
'''

prob4_content = '''
  <div id="prob-4" class="prob-content" style="display:none; text-align:center;">
    <h3 style="color:#2563eb; text-align:center; margin-bottom: 15px;">🎮 Provocarea Cuvintelor</h3>
    
    <div id="game-start-screen" style="padding: 30px; background:white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
       <p style="font-size: 1.2rem; color: #444; margin-bottom: 20px;">Ești gata să-ți testezi cunoștințele? Veronica îți va arăta 10 cuvinte, iar tu trebuie să alegi varianta corectă.</p>
       <button class="tab-btn" onclick="startGame()" style="background:linear-gradient(135deg,#3b82f6,#2563eb); font-size:1.3rem; padding:12px 35px;">▶️ Începe Jocul!</button>
    </div>

    <div id="game-play-screen" style="display:none; padding: 20px; background:white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
       <div style="font-size: 1.1rem; color: #666; margin-bottom: 15px; font-weight: bold;">Întrebarea <span id="game-q-num">1</span> din 10</div>
       <h4 style="font-size: 1.5rem; color: #1e40af; margin-bottom: 25px;">Care este varianta corectă?</h4>
       
       <div style="display:flex; justify-content:center; gap: 15px; flex-wrap: wrap;">
         <button id="btn-opt-1" class="tab-btn" onclick="checkAnswer(1)" style="background:linear-gradient(135deg,#64748b,#475569); min-width: 250px; font-size:1.2rem; padding:15px; text-transform:none;">Varianta A</button>
         <button id="btn-opt-2" class="tab-btn" onclick="checkAnswer(2)" style="background:linear-gradient(135deg,#64748b,#475569); min-width: 250px; font-size:1.2rem; padding:15px; text-transform:none;">Varianta B</button>
       </div>
       <div id="game-feedback" style="margin-top: 20px; font-size: 1.2rem; font-weight: bold; min-height: 30px;"></div>
    </div>

    <div id="game-end-screen" style="display:none; padding: 30px; background:white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
       <div id="game-end-emoji" style="font-size: 4rem; margin-bottom: 10px;">🏆</div>
       <h3 id="game-end-title" style="font-size: 2rem; color: #1e40af; margin-bottom: 15px;">Felicitări!</h3>
       <p id="game-end-msg" style="font-size: 1.3rem; color: #444; margin-bottom: 25px;">Ai răspuns corect la 8 din 10 cuvinte!</p>
       <button class="tab-btn" onclick="startGame()" style="background:linear-gradient(135deg,#10b981,#059669); font-size:1.2rem; padding:12px 30px;">🔄 Joacă din nou</button>
    </div>
  </div>
'''

js_code = '''
const probWordsDB = [
  { c: "repercusiune", w: "repercursiune" },
  { c: "excavator", w: "escavator" },
  { c: "genuflexiune", w: "genoflexiune" },
  { c: "bleumarin", w: "bleu-marin" },
  { c: "proprietar", w: "propietar" },
  { c: "itinerar", w: "itinerariu" },
  { c: "astă-seară", w: "astă seară" },
  { c: "așază", w: "așează" },
  { c: "voiam", w: "vroiam" },
  { c: "chibrituri", w: "chibrite" },
  { c: "aragaze", w: "aragazuri" },
  { c: "bareme", w: "baremuri" },
  { c: "succese", w: "succesuri" },
  { c: "monede", w: "monezi" },
  { c: "boschete", w: "boscheți" },
  { c: "colonei", w: "coloneli" },
  { c: "pancarte", w: "pancărți" },
  { c: "sindroame", w: "sindromuri" },
  { c: "sloganuri", w: "slogane" },
  { c: "morminte", w: "mormânturi" },
  { c: "snoabe", w: "snobe" },
  { c: "parbrize", w: "parbrizuri" },
  { c: "bairamuri", w: "bairame" },
  { c: "niveluri (stadii)", w: "nivele (stadii)" },
  { c: "refrene", w: "refrenuri" },
  { c: "feșe", w: "fașe" },
  { c: "vopsele", w: "vopseluri" },
  { c: "marmuri", w: "marmure" },
  { c: "înșală", w: "înșeală" },
  { c: "creează", w: "crează" },
  { c: "înnoadă", w: "înoadă" },
  { c: "înot", w: "înnot" },
  { c: "deseară (diseară)", w: "de seară (diseară)" },
  { c: "nicidecum", w: "nici de cum" },
  { c: "niciun (adjectiv)", w: "nici un (adjectiv)" },
  { c: "odată (cândva)", w: "o dată (cândva)" },
  { c: "altădată", w: "altă dată (în trecut)" },
  { c: "nu fi", w: "nu fii" },
  { c: "fii", w: "fi (tu)" },
  { c: "știi", w: "ști" },
  { c: "ți-ar", w: "țiar" },
  { c: "să aibă", w: "să aibe" },
  { c: "să țină", w: "să ție" },
  { c: "să vină", w: "să vie" },
  { c: "să dea", w: "să deie" },
  { c: "din cauza (de rău)", w: "datorită (de rău)" },
  { c: "respectuos", w: "respectos" },
  { c: "astmatic", w: "asmatic" },
  { c: "greșeală", w: "greșală" },
  { c: "înșelăciune", w: "înșealăciune" },
  { c: "delincvent", w: "delicvent" },
  { c: "panglică", w: "pamblică" },
  { c: "frustrare", w: "frustare" },
  { c: "abțibild", w: "abțiguib" },
  { c: "sandviș", w: "sanviș" },
  { c: "șnițel", w: "șnițel (cu s)" }, 
  { c: "mândri", w: "mândrii (nearticulat)" },
  { c: "copiii", w: "copii (articulat)" },
  { c: "miniștrii", w: "miniștri (articulat)" },
  { c: "bărbații", w: "bărbați (articulat)" },
  { c: "pe care (acuzativ)", w: "care (acuzativ)" },
  { c: "salariu", w: "salar" },
  { c: "serviciu", w: "servici" },
  { c: "albaștri", w: "albaștrii (nearticulat)" },
  { c: "v-ați", w: "va-ți" },
  { c: "s-au (verb)", w: "sau (verb)" },
  { c: "printr-un", w: "printrun" },
  { c: "dintr-o", w: "dintro" },
  { c: "aceeași (f.)", w: "aceiași (f.)" },
  { c: "așadar", w: "așa dar" },
  { c: "deodată", w: "de o dată" },
  { c: "totodată", w: "tot o dată" },
  { c: "vreun", w: "vre-un" },
  { c: "nicio", w: "nici-o" },
  { c: "dedesubt", w: "dedesupt" },
  { c: "prerie", w: "preerie" },
  { c: "clovn", w: "claun" },
  { c: "dezamăgi", w: "dezămăgi" },
  { c: "țigară", w: "țigare" },
  { c: "cireașă", w: "cireșe (la singular)" },
  { c: "gogoașă", w: "gogoșe (la singular)" },
  { c: "bancnotă", w: "bacnotă" },
  { c: "piuneză", w: "pioneză" },
  { c: "chiuvetă", w: "ghiuvetă" },
  { c: "marșarier", w: "marșalier" },
  { c: "complee", w: "compleuri" },
  { c: "reper", w: "reper (accent greșit)" },
  { c: "șasiu", w: "șasiu (accent greșit)" },
  { c: "mijloc", w: "miljoc" },
  { c: "pieri", w: "pierii" },
  { c: "vadră", w: "vadră (accent)" },
  { c: "făraș", w: "făraș (accent)" },
  { c: "ouă", w: "ouăle" },
  { c: "chibrit", w: "chibrite" },
  { c: "roșcove", w: "roșcove" }
];

let gameQuestions = [];
let currentQuestionIndex = 0;
let gameScore = 0;
let isAnswered = false;

function startGame() {
  document.getElementById('game-start-screen').style.display = 'none';
  document.getElementById('game-end-screen').style.display = 'none';
  document.getElementById('game-play-screen').style.display = 'block';
  
  let shuffled = [...probWordsDB].sort(() => 0.5 - Math.random());
  gameQuestions = shuffled.slice(0, 10);
  
  currentQuestionIndex = 0;
  gameScore = 0;
  
  loadQuestion();
}

function loadQuestion() {
  isAnswered = false;
  document.getElementById('game-feedback').innerText = '';
  document.getElementById('game-q-num').innerText = currentQuestionIndex + 1;
  
  let q = gameQuestions[currentQuestionIndex];
  let btn1 = document.getElementById('btn-opt-1');
  let btn2 = document.getElementById('btn-opt-2');
  
  btn1.style.background = 'linear-gradient(135deg,#64748b,#475569)';
  btn2.style.background = 'linear-gradient(135deg,#64748b,#475569)';
  
  if (Math.random() > 0.5) {
    btn1.innerText = q.c;
    btn1.dataset.correct = 'true';
    btn2.innerText = q.w;
    btn2.dataset.correct = 'false';
  } else {
    btn1.innerText = q.w;
    btn1.dataset.correct = 'false';
    btn2.innerText = q.c;
    btn2.dataset.correct = 'true';
  }
}

function checkAnswer(opt) {
  if (isAnswered) return;
  isAnswered = true;
  
  let btn1 = document.getElementById('btn-opt-1');
  let btn2 = document.getElementById('btn-opt-2');
  let chosenBtn = opt === 1 ? btn1 : btn2;
  
  if (chosenBtn.dataset.correct === 'true') {
    chosenBtn.style.background = 'linear-gradient(135deg,#16a34a,#15803d)';
    document.getElementById('game-feedback').innerText = '✅ Corect!';
    document.getElementById('game-feedback').style.color = '#15803d';
    gameScore++;
  } else {
    chosenBtn.style.background = 'linear-gradient(135deg,#dc2626,#b91c1c)';
    document.getElementById('game-feedback').innerText = '❌ Greșit!';
    document.getElementById('game-feedback').style.color = '#dc2626';
    if (btn1.dataset.correct === 'true') btn1.style.background = 'linear-gradient(135deg,#16a34a,#15803d)';
    if (btn2.dataset.correct === 'true') btn2.style.background = 'linear-gradient(135deg,#16a34a,#15803d)';
  }
  
  setTimeout(() => {
    currentQuestionIndex++;
    if (currentQuestionIndex < 10) {
      loadQuestion();
    } else {
      endGame();
    }
  }, 1500);
}

function endGame() {
  document.getElementById('game-play-screen').style.display = 'none';
  document.getElementById('game-end-screen').style.display = 'block';
  
  document.getElementById('game-end-msg').innerText = `Ai răspuns corect la ${gameScore} din 10 cuvinte!`;
  
  if (gameScore > 7) {
    document.getElementById('game-end-emoji').innerText = '🎉';
    document.getElementById('game-end-title').innerText = 'Felicitări!';
    document.getElementById('game-end-title').style.color = '#15803d';
    document.getElementById('game-end-msg').innerText += ' Ai un vocabular excelent!';
  } else {
    document.getElementById('game-end-emoji').innerText = '📚';
    document.getElementById('game-end-title').innerText = 'Mai ai puțin de învățat...';
    document.getElementById('game-end-title').style.color = '#ea580c';
    document.getElementById('game-end-msg').innerText += ' dar ești pe drumul cel bun!';
  }
}
'''

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '3. Capcanele cuvintelor care încep cu litera' in line:
        lines.insert(i+1, ui_content)
        break

for i, line in enumerate(lines):
    if 'function showProb' in line:
        lines.insert(i-1, prob4_content + '\n')
        break

for i, line in enumerate(lines):
    if '</script>' in line and '</body>' in lines[min(len(lines)-1, i+1)]:
        lines.insert(i, js_code + '\n')
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('UI and JS Injected successfully')
