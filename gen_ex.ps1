$out = ""

function makeEx($title, $color, $border, $idPrefix, $catName, $questions) {
  $global:out += "<h3 class="exercises-title" style="color:$color;margin-top:40px;">✏️ Exerciții – $title</h3>
"
  $global:out += "<div class="score-bar" id="score-$catName">⭐ Puncte: <span class="score-num" id="pts-$catName">0</span> / <span id="total-$catName">10</span>"
  $global:out += "<div class="progress-wrap"><div class="progress-fill" id="prog-$catName"></div></div></div>
"
  
  $i = 1
  foreach ($q in $questions) {
    $qId = "$idPrefix$i"
    $global:out += "<div class="exercise-card" style="border-color:$border;">"
    $global:out += "<div class="q-num" style="color:$color;">Exercițiul $i</div>"
    $global:out += "<div class="question">$($q.q)</div><div class="options">"
    foreach ($o in $q.opts) {
      $isC = if ($o -eq $q.ans) { "true" } else { "false" }
      $global:out += "<button class="option-btn" onclick="checkOption(this,'$qId',$isC,'$catName')">$o</button>"
    }
    $global:out += "</div><div class="feedback" id="fb-$qId"></div></div>
"
    $i++
  }
  $global:out += "<button class="reset-btn" onclick="resetSection('$catName')">🔄 Resetează $title</button>"
  $global:out += "<div class="reward" id="reward-$catName">"
  $global:out += "<div class="reward-stars">⭐⭐⭐⭐⭐</div><h2>🏆 Felicitări, Veronica!</h2><p>Ai terminat exercițiile pentru $title!</p></div>
"
}

$q_sin = @(
  @{q='Care este sinonimul pentru "vesel"?'; ans='bucuros'; opts=@('trist','bucuros','supărat','înalt')},
  @{q='Sinonimul lui "zăpadă" este:'; ans='nea'; opts=@('apă','ploaie','nea','gheață')},
  @{q='Ce cuvânt înseamnă același lucru cu "amic"?'; ans='prieten'; opts=@('dușman','prieten','coleg','străin')},
  @{q='Sinonim pentru "a alerga":'; ans='a fugi'; opts=@('a merge','a sta','a dormi','a fugi')},
  @{q='Sinonim pentru "steag":'; ans='drapel'; opts=@('hârtie','drapel','băț','tricou')},
  @{q='Sinonim pentru "scund":'; ans='mic'; opts=@('înalt','mare','mic','gras')},
  @{q='Sinonim pentru "a privi":'; ans='a se uita'; opts=@('a asculta','a se uita','a mirosi','a simți')},
  @{q='Sinonim pentru "dar":'; ans='cadou'; opts=@('jucărie','cadou','carte','dulce')},
  @{q='Sinonim pentru "teamă":'; ans='frică'; opts=@('curaj','frică','bucurie','râs')},
  @{q='Sinonim pentru "a zice":'; ans='a spune'; opts=@('a asculta','a tăcea','a spune','a citi')}
)
makeEx 'Sinonime' '#10b981' '#10b981' 'vs' 'sinonime' $q_sin

$q_ant = @(
  @{q='Antonimul pentru "alb":'; ans='negru'; opts=@('roșu','negru','gri','galben')},
  @{q='Antonimul pentru "mare":'; ans='mic'; opts=@('uriaș','mic','înalt','rotund')},
  @{q='Antonimul pentru "cald":'; ans='rece'; opts=@('fierbinte','răcoros','rece','soare')},
  @{q='Antonimul pentru "a râde":'; ans='a plânge'; opts=@('a zâmbi','a chicoti','a plânge','a sta')},
  @{q='Antonimul pentru "zi":'; ans='noapte'; opts=@('dimineață','seară','noapte','amiază')},
  @{q='Antonimul pentru "bun":'; ans='rău'; opts=@('drăguț','rău','dulce','amar')},
  @{q='Antonimul pentru "înalt":'; ans='scund'; opts=@('mare','scund','lung','gros')},
  @{q='Antonimul pentru "devreme":'; ans='târziu'; opts=@('târziu','acum','niciodată','mâine')},
  @{q='Antonimul pentru "aproape":'; ans='departe'; opts=@('lângă','aici','departe','sus')},
  @{q='Antonimul pentru "nou":'; ans='vechi'; opts=@('strălucitor','vechi','curat','frumos')}
)
makeEx 'Antonime' '#e11d48' '#e11d48' 'va' 'antonime' $q_ant

$q_omo = @(
  @{q='"Sare" din propoziția "Băiatul sare mingea" este:'; ans='verb'; opts=@('condiment','verb','substantiv')},
  @{q='"Sare" din "Am pus sare în mâncare" este:'; ans='condiment (substantiv)'; opts=@('verb','condiment (substantiv)','adjectiv')},
  @{q='"Broască" (animal) și "broască" (la ușă) sunt:'; ans='Omonime'; opts=@('Sinonime','Antonime','Omonime')},
  @{q='"Corn" (de mâncat) și "corn" (de animal) sunt:'; ans='Omonime'; opts=@('Omofone','Omonime','Antonime')},
  @{q='"Liliac" (floare) și "liliac" (animal) sunt:'; ans='Omonime'; opts=@('Sinonime','Omonime','Paronime')},
  @{q='"Ochi" (corp) și "ochi" (de aragaz) sunt:'; ans='Omonime'; opts=@('Omonime','Sinonime','Omofone')},
  @{q='Ce sunt omonimele?'; ans='Se scriu la fel, sens diferit'; opts=@('Sens opus','Același sens','Se scriu la fel, sens diferit')},
  @{q='"Leu" (animal) și "leu" (bani) sunt:'; ans='Omonime'; opts=@('Antonime','Omonime','Sinonime')},
  @{q='"Somn" (pește) și "somn" (de dormit) sunt:'; ans='Omonime'; opts=@('Omofone','Omonime','Paronime')},
  @{q='"Nouă" (cifră) și "nouă" (haina nouă) sunt:'; ans='Omonime'; opts=@('Omonime','Sinonime','Antonime')}
)
makeEx 'Omonime' '#2563eb' '#2563eb' 'vo' 'omonime' $q_omo

$q_par = @(
  @{q='Cuvintele "oral" și "orar" sunt:'; ans='Paronime'; opts=@('Omonime','Paronime','Antonime')},
  @{q='"Familiar" înseamnă:'; ans='Cunoscut'; opts=@('De familie','Cunoscut','Străin')},
  @{q='"Familial" înseamnă:'; ans='De familie'; opts=@('De familie','Cunoscut','Depărtat')},
  @{q='Ce sunt paronimele?'; ans='Seamănă ca formă, sens diferit'; opts=@('Același sens','Sens opus','Seamănă ca formă, sens diferit')},
  @{q='"Eminent" (bun) și "iminent" (care stă să se întâmple) sunt:'; ans='Paronime'; opts=@('Sinonime','Paronime','Omofone')},
  @{q='El este foarte ... (cunoscut/prietenos) cu noi.'; ans='familiar'; opts=@('familial','familiar')},
  @{q='Medicul a recomandat un tratament ... (pe gură).'; ans='oral'; opts=@('orar','oral')},
  @{q='Am un ... foarte încărcat la școală azi.'; ans='orar'; opts=@('oral','orar')},
  @{q='Sărbătoarea a avut un caracter ... (de familie).'; ans='familial'; opts=@('familiar','familial')},
  @{q='Paronimele se deosebesc prin:'; ans='1-2 sunete'; opts=@('Sunt identice','1-2 sunete','Au sens opus')}
)
makeEx 'Paronime' '#a855f7' '#a855f7' 'vp' 'paronime' $q_par

$q_omf = @(
  @{q='Cuvintele "sa" și "s-a" sunt:'; ans='Omofone'; opts=@('Omonime','Omofone','Antonime')},
  @{q='Cum scrii corect? Fata a luat cartea ...'; ans='sa'; opts=@('sa','s-a')},
  @{q='Cum scrii corect? El ... dus la școală.'; ans='s-a'; opts=@('sa','s-a')},
  @{q='"Mai" (luna) și "m-ai" (m-ai strigat) sunt:'; ans='Omofone'; opts=@('Omonime','Paronime','Omofone')},
  @{q='Cum scrii corect? De ce ... supărat?'; ans='m-ai'; opts=@('mai','m-ai')},
  @{q='Cum scrii corect? Suntem în luna ...'; ans='mai'; opts=@('mai','m-ai')},
  @{q='"Neam" (rude) și "ne-am" (ne-am dus) sunt:'; ans='Omofone'; opts=@('Omofone','Sinonime','Antonime')},
  @{q='Cum scrii corect? Noi ... jucat în parc.'; ans='ne-am'; opts=@('neam','ne-am')},
  @{q='Cum scrii corect? Avem un ... mare și unit.'; ans='neam'; opts=@('neam','ne-am')},
  @{q='Ce sunt omofonele?'; ans='Se aud la fel, se scriu diferit'; opts=@('Se scriu și aud la fel','Se aud la fel, se scriu diferit')}
)
makeEx 'Omofone' '#f59e0b' '#f59e0b' 'vf' 'omofone' $q_omf

$global:out += "</section>"
Add-Content "vocabular_partial.html" $global:out -Encoding UTF8
Write-Output "Exercises generated with PS."
