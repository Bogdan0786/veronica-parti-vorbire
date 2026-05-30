import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hardcoded HTML text
content = content.replace(
    'Veronica îți va arăta 10 cuvinte, iar tu trebuie să alegi varianta corectă.', 
    'Veronica îți va arăta 20 de cuvinte și propoziții, iar tu trebuie să alegi varianta corectă.'
)
content = content.replace(
    '<div style="font-size: 1.1rem; color: #666; margin-bottom: 15px; font-weight: bold;">Întrebarea <span id="game-q-num">1</span> din 10</div>',
    '<div style="font-size: 1.1rem; color: #666; margin-bottom: 15px; font-weight: bold;">Întrebarea <span id="game-q-num">1</span> din 20</div>'
)
content = content.replace(
    '<p id="game-end-msg" style="font-size: 1.3rem; color: #444; margin-bottom: 25px;">Ai răspuns corect la 8 din 10 cuvinte!</p>',
    '<p id="game-end-msg" style="font-size: 1.3rem; color: #444; margin-bottom: 25px;">Ai răspuns corect la 16 din 20 cuvinte!</p>'
)

# Replace JS state
old_js = """let gameQuestions = [];
let currentQuestionIndex = 0;
let gameScore = 0;
let isAnswered = false;"""

new_js = """let gameQuestionPool = [];
let gameQuestions = [];
let currentQuestionIndex = 0;
let gameScore = 0;
let isAnswered = false;"""

content = content.replace(old_js, new_js)

old_start = """function startGame() {
  document.getElementById('game-start-screen').style.display = 'none';
  document.getElementById('game-end-screen').style.display = 'none';
  document.getElementById('game-play-screen').style.display = 'block';
  
  let shuffled = [...probWordsDB].sort(() => 0.5 - Math.random());
  gameQuestions = shuffled.slice(0, 10);
  
  currentQuestionIndex = 0;
  gameScore = 0;
  
  loadQuestion();
}"""

new_start = """function startGame() {
  document.getElementById('game-start-screen').style.display = 'none';
  document.getElementById('game-end-screen').style.display = 'none';
  document.getElementById('game-play-screen').style.display = 'block';
  
  if (gameQuestionPool.length < 20) {
      gameQuestionPool = [...probWordsDB].sort(() => 0.5 - Math.random());
  }
  
  gameQuestions = gameQuestionPool.splice(0, 20);
  
  currentQuestionIndex = 0;
  gameScore = 0;
  
  loadQuestion();
}"""

content = content.replace(old_start, new_start)

# Update endgame check
old_next = """setTimeout(() => {
    currentQuestionIndex++;
    if (currentQuestionIndex < 10) {
      loadQuestion();
    } else {
      endGame();
    }
  }, 1500);"""

new_next = """setTimeout(() => {
    currentQuestionIndex++;
    if (currentQuestionIndex < 20) {
      loadQuestion();
    } else {
      endGame();
    }
  }, 1500);"""
  
content = content.replace(old_next, new_next)

# Update endgame function
old_end = """document.getElementById('game-end-msg').innerText = `Ai răspuns corect la ${gameScore} din 10 cuvinte!`;

  if (gameScore > 7) {"""

new_end = """document.getElementById('game-end-msg').innerText = `Ai răspuns corect la ${gameScore} din 20 exerciții!`;

  if (gameScore >= 16) {"""

content = content.replace(old_end, new_end)

# Also update the gameScore === 10 check for perfect score (changed to 20)
content = content.replace('if (gameScore === 10) {', 'if (gameScore === 20) {')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Game logic updated for 20 words and no repeats.")
