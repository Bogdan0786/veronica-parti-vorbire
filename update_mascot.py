import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace innerText with innerHTML for podium assignment
old_logic = '''const charV = '👧';
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
  }'''

new_logic = '''const charV = '<img src="veronica.png" style="width: 75px; height: auto; display: block; margin-bottom: -5px; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));">';
  const charB = '👦';
  const charG = '👱‍♀️';

  let p1 = document.getElementById('p-char-1');
  let p2 = document.getElementById('p-char-2');
  let p3 = document.getElementById('p-char-3');
  let pOff = document.getElementById('p-char-off');
  
  pOff.style.display = 'none';

  if (gameScore === 10) {
    p1.innerHTML = charV;
    p2.innerHTML = charB;
    p3.innerHTML = charG;
  } else if (gameScore === 9) {
    p1.innerHTML = charB;
    p2.innerHTML = charV;
    p3.innerHTML = charG;
  } else if (gameScore === 8) {
    p1.innerHTML = charB;
    p2.innerHTML = charG;
    p3.innerHTML = charV;
  } else {
    p1.innerHTML = charB;
    p2.innerHTML = charG;
    p3.innerHTML = '🧑';
    pOff.innerHTML = '<img src="veronica.png" style="width: 60px; height: auto; display: inline-block; filter: grayscale(80%) drop-shadow(0 4px 6px rgba(0,0,0,0.2)); margin-right: 10px;"> 😢';
    pOff.style.display = 'flex';
  }'''

if old_logic in content:
    content = content.replace(old_logic, new_logic)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated podium logic to use image')
else:
    print('Could not find old logic block')
