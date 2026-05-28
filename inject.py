import sys

with open('index.html', 'rb') as f:
    html_b = f.read()
    html = html_b.decode('utf-8', errors='ignore')

with open('vocabular_partial.html', 'rb') as f:
    vocab_b = f.read()
    # Handle possible utf-16 from powershell
    if vocab_b.startswith(b'\xff\xfe') or vocab_b.startswith(b'\xfe\xff'):
        vocab_html = vocab_b.decode('utf-16')
    else:
        vocab_html = vocab_b.decode('utf-8', errors='ignore')

# 1. Insert Vocabular HTML before JS section
idx_js = html.find('<!-- ════════════════════ JAVASCRIPT ════════════════════ -->')
html = html[:idx_js] + vocab_html + '\n\n' + html[idx_js:]

# 2. Add header button
nav_pos = html.find('id="tab-exercitii"')
nav_end = html.find('</button>', nav_pos) + 9
btn_html = '\n  <button class="tab-btn" id="tab-vocabular" style="background:linear-gradient(135deg,#f43f5e,#fb923c)" onclick="showSection(\'vocabular\')">📖 Vocabular</button>'
html = html[:nav_end] + btn_html + html[nav_end:]

# 3. Add home grid card
grid_pos = html.find('onclick="showSection(\'exercitii\')"')
grid_end = html.find('</button>', grid_pos) + 9
card_html = '\n      <button class="fairy-card" onclick="showSection(\'vocabular\')">\n        <div class="done-badge" id="done-vocabular">✅</div>\n        <div class="fc-num" style="background:#f43f5e">11</div>\n        <h3>📖 Vocabular</h3><p>Relații Semantice</p>\n      </button>'
html = html[:grid_end] + card_html + html[grid_end:]

# 4. Update JS qCounts
qc_pos = html.find('const qCounts={')
qc_end = html.find('};', qc_pos)
new_qc = 'const qCounts={\n  Substantiv:4, pronume:3, verb:4, adjectiv:3,\n  adverb:3, prepozitie:3, conjunctie:3, interjectie:3, exercitii:10,\n  sinonime:10, antonime:10, omonime:10, paronime:10, omofone:10\n'
html = html[:qc_pos] + new_qc + html[qc_end:]

# 5. Update JS sectionOf
sec_pos = html.find('function sectionOf(qid){')
sec_end = html.find('}', sec_pos) + 1
new_sec = '''function sectionOf(qid){
  if(qid.startsWith('ad')) return 'adverb';
  if(qid.startsWith('pr')) return 'prepozitie';
  if(qid.startsWith('vs')) return 'sinonime';
  if(qid.startsWith('va')) return 'antonime';
  if(qid.startsWith('vo')) return 'omonime';
  if(qid.startsWith('vp')) return 'paronime';
  if(qid.startsWith('vf')) return 'omofone';
  const map={s:'Substantiv',p:'pronume',v:'verb',a:'adjectiv',c:'conjunctie',i:'interjectie',g:'exercitii'};
  for(const [k,v] of Object.entries(map)) if(qid.startsWith(k)) return v;
  return 'exercitii';
}'''
html = html[:sec_pos] + new_sec + html[sec_end:]

# 6. Update checkAllDone to include new sections for diploma
rwd_pos = html.find("sec==='interjectie'?'Interjecție':")
if rwd_pos != -1:
    rwd_end = html.find("'Exerciții Generale'", rwd_pos)
    new_rwd = "sec==='interjectie'?'Interjecție':\n          sec==='sinonime'?'Sinonime':sec==='antonime'?'Antonime':sec==='omonime'?'Omonime':sec==='paronime'?'Paronime':sec==='omofone'?'Omofone':\n          "
    html = html[:rwd_end] + new_rwd + html[rwd_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injection complete!")
