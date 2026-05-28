const fs = require('fs');
let out = '';

function makeEx(title, color, border, idPrefix, catName, questions) {
  out += <h3 class="exercises-title" style="color:;margin-top:40px;">?? Exerci?ii – </h3>;
  out += <div class="score-bar" id="score-">? Puncte: <span class="score-num" id="pts-">0</span> / <span id="total-">10</span>;
  out += <div class="progress-wrap"><div class="progress-fill" id="prog-"></div></div></div>;
  
  questions.forEach((q, i) => {
    let qId = idPrefix + (i+1);
    out += <div class="exercise-card" style="border-color:;">;
    out += <div class="q-num" style="color:;">Exerci?iul </div>;
    out += <div class="question"></div>;
    out += <div class="options">;
    q.opts.forEach(o => {
      let isC = (o === q.ans).toString();
      out += <button class="option-btn" onclick="checkOption(this,'',,'')"></button>;
    });
    out += </div><div class="feedback" id="fb-"></div></div>;
  });
  out += <button class="reset-btn" onclick="resetSection('')">?? Reseteaza </button>;
  out += <div class="reward" id="reward-">;
  out += <div class="reward-stars">?????</div><h2>?? Felicitari, Veronica!</h2><p>Ai terminat exerci?iile pentru !</p></div>;
}

// Sinonime (10)
makeEx('Sinonime', '#10b981', '#10b981', 'vs', 'sinonime', [
  {q:'Care este sinonimul pentru "vesel"?', ans:'bucuros', opts:['trist','bucuros','suparat','înalt']},
  {q:'Sinonimul lui "zapada" este:', ans:'nea', opts:['apa','ploaie','nea','ghea?a']},
  {q:'Ce cuvânt înseamna acela?i lucru cu "amic"?', ans:'prieten', opts:['du?man','prieten','coleg','strain']},
  {q:'Sinonim pentru "a alerga":', ans:'a fugi', opts:['a merge','a sta','a dormi','a fugi']},
  {q:'Sinonim pentru "steag":', ans:'drapel', opts:['hârtie','drapel','ba?','tricou']},
  {q:'Sinonim pentru "scund":', ans:'mic', opts:['înalt','mare','mic','gras']},
  {q:'Sinonim pentru "a privi":', ans:'a se uita', opts:['a asculta','a se uita','a mirosi','a sim?i']},
  {q:'Sinonim pentru "dar":', ans:'cadou', opts:['jucarie','cadou','carte','dulce']},
  {q:'Sinonim pentru "teama":', ans:'frica', opts:['curaj','frica','bucurie','râs']},
  {q:'Sinonim pentru "a zice":', ans:'a spune', opts:['a asculta','a tacea','a spune','a citi']}
]);

// Antonime (10)
makeEx('Antonime', '#e11d48', '#e11d48', 'va', 'antonime', [
  {q:'Antonimul pentru "alb":', ans:'negru', opts:['ro?u','negru','gri','galben']},
  {q:'Antonimul pentru "mare":', ans:'mic', opts:['uria?','mic','înalt','rotund']},
  {q:'Antonimul pentru "cald":', ans:'rece', opts:['fierbinte','racoros','rece','soare']},
  {q:'Antonimul pentru "a râde":', ans:'a plânge', opts:['a zâmbi','a chicoti','a plânge','a sta']},
  {q:'Antonimul pentru "zi":', ans:'noapte', opts:['diminea?a','seara','noapte','amiaza']},
  {q:'Antonimul pentru "bun":', ans:'rau', opts:['dragu?','rau','dulce','amar']},
  {q:'Antonimul pentru "înalt":', ans:'scund', opts:['mare','scund','lung','gros']},
  {q:'Antonimul pentru "devreme":', ans:'târziu', opts:['târziu','acum','niciodata','mâine']},
  {q:'Antonimul pentru "aproape":', ans:'departe', opts:['lânga','aici','departe','sus']},
  {q:'Antonimul pentru "nou":', ans:'vechi', opts:['stralucitor','vechi','curat','frumos']}
]);

// Omonime (10)
makeEx('Omonime', '#2563eb', '#2563eb', 'vo', 'omonime', [
  {q:'"Sare" din propozi?ia "Baiatul sare mingea" este:', ans:'verb', opts:['condiment','verb','substantiv']},
  {q:'"Sare" din "Am pus sare în mâncare" este:', ans:'condiment (substantiv)', opts:['verb','condiment (substantiv)','adjectiv']},
  {q:'"Broasca" (animal) ?i "broasca" (la u?a) sunt:', ans:'Omonime', opts:['Sinonime','Antonime','Omonime']},
  {q:'"Corn" (de mâncat) ?i "corn" (de animal) sunt:', ans:'Omonime', opts:['Omofone','Omonime','Antonime']},
  {q:'"Liliac" (floare) ?i "liliac" (animal) sunt:', ans:'Omonime', opts:['Sinonime','Omonime','Paronime']},
  {q:'"Ochi" (parte a corpului) ?i "ochi" (de aragaz) sunt:', ans:'Omonime', opts:['Omonime','Sinonime','Omofone']},
  {q:'Ce sunt omonimele?', ans:'Se scriu la fel, sens diferit', opts:['Sens opus','Acela?i sens','Se scriu la fel, sens diferit']},
  {q:'"Leu" (animal) ?i "leu" (bani) sunt:', ans:'Omonime', opts:['Antonime','Omonime','Sinonime']},
  {q:'"Somn" (pe?te) ?i "somn" (de dormit) sunt:', ans:'Omonime', opts:['Omofone','Omonime','Paronime']},
  {q:'"Noua" (cifra) ?i "noua" (haina noua) sunt:', ans:'Omonime', opts:['Omonime','Sinonime','Antonime']}
]);

// Paronime (10)
makeEx('Paronime', '#a855f7', '#a855f7', 'vp', 'paronime', [
  {q:'Cuvintele "oral" ?i "orar" sunt:', ans:'Paronime', opts:['Omonime','Paronime','Antonime']},
  {q:'"Familiar" înseamna:', ans:'Cunoscut', opts:['De familie','Cunoscut','Strain']},
  {q:'"Familial" înseamna:', ans:'De familie', opts:['De familie','Cunoscut','Departat']},
  {q:'Ce sunt paronimele?', ans:'Seamana ca forma, sens diferit', opts:['Acela?i sens','Sens opus','Seamana ca forma, sens diferit']},
  {q:'"Eminent" (foarte bun) ?i "iminent" (care sta sa se întâmple) sunt:', ans:'Paronime', opts:['Sinonime','Paronime','Omofone']},
  {q:'Alege forma corecta: El este foarte ... (cunoscut/prietenos) cu noi.', ans:'familiar', opts:['familial','familiar']},
  {q:'Alege forma corecta: Medicul a recomandat un tratament ... (pe gura).', ans:'oral', opts:['orar','oral']},
  {q:'Alege forma corecta: Am un ... foarte încarcat la ?coala azi.', ans:'orar', opts:['oral','orar']},
  {q:'Alege forma corecta: Sarbatoarea a avut un caracter ... (de familie).', ans:'familial', opts:['familiar','familial']},
  {q:'Paronimele se deosebesc prin:', ans:'1-2 sunete', opts:['Sunt identice','1-2 sunete','Au sens opus']}
]);

// Omofone (10)
makeEx('Omofone', '#f59e0b', '#f59e0b', 'vf', 'omofone', [
  {q:'Cuvintele "sa" ?i "s-a" sunt:', ans:'Omofone', opts:['Omonime','Omofone','Antonime']},
  {q:'Cum se scrie corect? "Fata a luat cartea ..."', ans:'sa', opts:['sa','s-a']},
  {q:'Cum se scrie corect? "El ... dus la ?coala."', ans:'s-a', opts:['sa','s-a']},
  {q:'"Mai" (luna) ?i "m-ai" (m-ai strigat) sunt:', ans:'Omofone', opts:['Omonime','Paronime','Omofone']},
  {q:'Cum se scrie corect? "De ce ... suparat?"', ans:'m-ai', opts:['mai','m-ai']},
  {q:'Cum se scrie corect? "Suntem în luna ..."', ans:'mai', opts:['mai','m-ai']},
  {q:'"Neam" (rude) ?i "ne-am" (ne-am dus) sunt:', ans:'Omofone', opts:['Omofone','Sinonime','Antonime']},
  {q:'Cum se scrie corect? "Noi ... jucat în parc."', ans:'ne-am', opts:['neam','ne-am']},
  {q:'Cum se scrie corect? "Avem un ... mare ?i unit."', ans:'neam', opts:['neam','ne-am']},
  {q:'Ce sunt omofonele?', ans:'Se aud la fel, se scriu diferit', opts:['Se scriu ?i se aud la fel','Se aud la fel, se scriu diferit']}
]);

out += </section>;
fs.appendFileSync('vocabular_partial.html', out);
console.log('Exercises generated.');
