import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_prop = content.find('<div class="fairy-row" id="propozitie-cards-container"')
if start_prop != -1:
    end_prop = content.find('</div>\n<!-- ══════════════ NUMERALUL ══════════════ -->', start_prop)
    if end_prop == -1:
        # Fallback if comment is not right after
        end_prop = content.find('</div>', content.find('</button>', start_prop + 100)) + 6
        
    prop_block = content[start_prop:end_prop]
    
    # Remove from old position
    content = content[:start_prop] + content[end_prop:]
    
    # Insert right before meadow-strip
    meadow_start = content.find('<div class="meadow-strip">')
    if meadow_start != -1:
        content = content[:meadow_start] + prop_block + '\n' + content[meadow_start:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully moved propozitie-cards-container to fairy-poster!")
    else:
        print("Could not find meadow-strip")
else:
    print("Could not find propozitie-cards-container")
