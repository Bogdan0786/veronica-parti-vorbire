// ================================================================
// BAZA DE DATE - SPÂNZURĂTOAREA
// ================================================================
// Format: ["cuvânt", "indiciu pentru jucător"]
//
// ✅ CUM SĂ ADAUGI CUVINTE NOI:
//    1. Deschide acest fișier în Notepad sau orice editor de text.
//    2. Adaugă o linie nouă ÎNAINTE de "];" de la final.
//    3. Formatul este: ["cuvântul", "Indiciu descriptiv; parte de vorbire"],
//    4. Salvează fișierul. Gata!
//
// EXEMPLU:
//    ["prietenie", "Sinonimul lui 'amiciție'; substantiv"],
//
// CATEGORII RECOMANDATE PENTRU INDICIU:
//    - Sinonimul lui '...'
//    - Antonimul lui '...'
//    - Paronimul lui '...'
//    - Parte de vorbire: substantiv / verb / adjectiv / adverb
//    - Descriere scurtă
// ================================================================

const HANGMAN_WORDS = [

  // ── SUBSTANTIVE ─────────────────────────────────────────────
  ["soare",       "Sinonimul lui 'astru luminos'; substantiv"],
  ["noapte",      "Antonimul cuvântului 'zi'; substantiv"],
  ["iubire",      "Sinonimul lui 'dragoste'; substantiv"],
  ["dușman",      "Antonimul lui 'prieten'; substantiv"],
  ["lumină",      "Antonimul lui 'întuneric'; substantiv"],
  ["copil",       "Paronimul lui 'copil' este 'capil'; substantiv"],
  ["școală",      "Loc unde înveți carte; substantiv"],
  ["carte",       "Sinonimul lui 'volum'; substantiv"],
  ["creion",      "Instrument de scris cu grafit; substantiv"],
  ["masă",        "Paronimul lui 'masă' este 'rasă'; substantiv"],
  ["casă",        "Sinonimul lui 'locuință'; substantiv"],
  ["apă",         "Sinonimul lui 'undă'; substantiv"],
  ["foc",         "Antonimul lui 'îngheț' ca efect; substantiv"],
  ["pădure",      "Sinonimul lui 'codru'; substantiv"],
  ["munte",       "Antonimul lui 'vale' ca formă de relief; substantiv"],
  ["mare",        "Corp mare de apă sărată; substantiv"],
  ["vânt",        "Sinonimul lui 'adierea aerului'; substantiv"],
  ["ploaie",      "Antonimul lui 'secetă' ca fenomen; substantiv"],
  ["iarnă",       "Anotimpul cu zăpadă; substantiv"],
  ["primăvară",   "Antonimul toamnei; substantiv"],
  ["vară",        "Anotimpul cel mai cald; substantiv"],
  ["toamnă",      "Anotimpul în care cad frunzele; substantiv"],
  ["animal",      "Sinonimul lui 'ființă'; substantiv"],
  ["floare",      "Sinonimul lui 'blossom' în română; substantiv"],
  ["culoare",     "Sinonimul lui 'nuanță'; substantiv"],
  ["prietenie",   "Sinonimul lui 'amiciție'; substantiv"],
  ["bucurie",     "Antonimul lui 'tristețe'; substantiv"],
  ["speranță",    "Sinonimul lui 'nădejde'; substantiv"],

  // ── ADJECTIVE ────────────────────────────────────────────────
  ["fericit",     "Sinonimul lui 'bucuros'; adjectiv"],
  ["trist",       "Antonimul lui 'vesel'; adjectiv"],
  ["frumos",      "Antonimul lui 'urât'; adjectiv"],
  ["bogat",       "Antonimul lui 'sărac'; adjectiv"],
  ["rapid",       "Sinonimul lui 'iute'; adjectiv"],
  ["lent",        "Antonimul lui 'rapid'; adjectiv"],
  ["cald",        "Antonimul lui 'rece'; adjectiv"],
  ["albastru",    "Culoarea cerului; adjectiv"],
  ["roșu",        "Culoarea sângelui; adjectiv"],
  ["galben",      "Culoarea soarelui; adjectiv"],
  ["verde",       "Culoarea ierbii; adjectiv"],
  ["negru",       "Antonimul lui 'alb'; adjectiv"],
  ["alb",         "Antonimul lui 'negru'; adjectiv"],
  ["mic",         "Antonimul lui 'mare' (dimensiune); adjectiv"],
  ["greu",        "Antonimul lui 'ușor'; adjectiv"],
  ["ușor",        "Antonimul lui 'greu'; adjectiv"],
  ["vechi",       "Antonimul lui 'nou'; adjectiv"],
  ["nou",         "Antonimul lui 'vechi'; adjectiv"],
  ["bun",         "Antonimul lui 'rău'; adjectiv"],
  ["rău",         "Antonimul lui 'bun'; adjectiv"],
  ["larg",        "Antonimul lui 'îngust'; adjectiv"],
  ["îngust",      "Antonimul lui 'larg'; adjectiv"],
  ["înalt",       "Antonimul lui 'scund'; adjectiv"],
  ["scund",       "Antonimul lui 'înalt'; adjectiv"],
  ["tare",        "Antonimul lui 'moale'; adjectiv"],
  ["moale",       "Antonimul lui 'tare'; adjectiv"],
  ["dulce",       "Antonimul lui 'amar'; adjectiv"],
  ["amar",        "Antonimul lui 'dulce'; adjectiv"],
  ["curat",       "Antonimul lui 'murdar'; adjectiv"],
  ["murdar",      "Antonimul lui 'curat'; adjectiv"],
  ["plin",        "Antonimul lui 'gol'; adjectiv"],
  ["gol",         "Antonimul lui 'plin'; adjectiv"],
  ["viu",         "Antonimul lui 'mort'; adjectiv"],
  ["zgomotos",    "Antonimul lui 'liniștit'; adjectiv"],
  ["liniștit",    "Antonimul lui 'zgomotos'; adjectiv"],
  ["generos",     "Antonimul lui 'zgârcit'; adjectiv"],
  ["curajos",     "Antonimul lui 'fricos'; adjectiv"],

  // ── VERBE ────────────────────────────────────────────────────
  ["a alerga",    "Sinonimul verbului 'a fugi'; verb"],
  ["a citi",      "Sinonimul verbului 'a lectura'; verb"],
  ["a plânge",    "Antonimul verbului 'a râde'; verb"],
  ["a munci",     "Sinonimul verbului 'a lucra'; verb"],
  ["a dormi",     "Sinonimul verbului 'a se odihni'; verb"],
  ["a cumpăra",   "Antonimul verbului 'a vinde'; verb"],
  ["a urca",      "Antonimul verbului 'a coborî'; verb"],
  ["a deschide",  "Antonimul verbului 'a închide'; verb"],
  ["a găsi",      "Antonimul verbului 'a pierde'; verb"],
  ["a întări",    "Sinonimul verbului 'a consolida'; verb"],
  ["a ajuta",     "Sinonimul verbului 'a sprijini'; verb"],
  ["a întreba",   "Sinonimul verbului 'a chestiona'; verb"],
  ["a răspunde",  "Sinonimul verbului 'a replica'; verb"],
  ["a vedea",     "Sinonimul verbului 'a zări'; verb"],
  ["a auzi",      "Sinonimul verbului 'a percepe sonor'; verb"],
  ["a simți",     "Sinonimul verbului 'a percepe'; verb"],
  ["a gândi",     "Sinonimul verbului 'a cugeta'; verb"],
  ["a ști",       "Sinonimul verbului 'a cunoaște'; verb"],
  ["a iubi",      "Sinonimul verbului 'a îndrăgi'; verb"],
  ["a ura",       "Antonimul verbului 'a iubi'; verb"],
  ["a vorbi",     "Sinonimul verbului 'a comunica'; verb"],
  ["a tăcea",     "Antonimul verbului 'a vorbi'; verb"],
  ["a merge",     "Sinonimul verbului 'a umbla'; verb"],
  ["a veni",      "Antonimul verbului 'a pleca'; verb"],
  ["a pleca",     "Antonimul verbului 'a veni'; verb"],
  ["a începe",    "Antonimul verbului 'a termina'; verb"],
  ["a termina",   "Antonimul verbului 'a începe'; verb"],
  ["a câștiga",   "Antonimul verbului 'a pierde'; verb"],
  ["a pierde",    "Antonimul verbului 'a câștiga'; verb"],
  ["a naște",     "Antonimul verbului 'a muri'; verb"],
  ["a ierta",     "Sinonimul verbului 'a scuza'; verb"],
  ["a proteja",   "Sinonimul verbului 'a apăra'; verb"],
  ["a înțelege",  "Sinonimul verbului 'a pricepe'; verb"],
  ["a aminti",    "Sinonimul verbului 'a rememora'; verb"],
  ["a privi",     "Sinonimul verbului 'a se uita'; verb"],
  ["a zâmbi",     "Sinonimul verbului 'a surâde'; verb"],
  ["a plimba",    "Sinonimul verbului 'a se preumbla'; verb"],
  ["a crește",    "Antonimul verbului 'a scădea'; verb"],
  ["a scădea",    "Antonimul verbului 'a crește'; verb"],
  ["a construi",  "Sinonimul verbului 'a edifica'; verb"],
  ["a distruge",  "Antonimul verbului 'a construi'; verb"]

  // ── ADAUGĂ CUVINTE NOI AICI ──────────────────────────────────
  // Copiază formatul de mai sus și adaugă câte rânduri dorești!
  // Nu uita virgula după fiecare linie (cu excepția ultimei)!

];
