import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The appended sections start at "<!-- 👑 PREDICATUL -->"
start_appended = content.rfind('<!-- 👑 PREDICATUL -->')

if start_appended != -1 and start_appended > content.rfind('</html>'):
    # The appended text is at the very end
    new_sections = content[start_appended:]
    
    # Remove from end
    content = content[:start_appended]
    
    # Now find the old #propozitie section
    old_propozitie_start = content.find('<section class="section" id="propozitie">')
    if old_propozitie_start != -1:
        # Include the comment above it if present
        if content[old_propozitie_start-27:old_propozitie_start] == '<!-- 🌟 PROPOZIȚIE 🌟 -->\n':
            old_propozitie_start -= 27

        old_propozitie_end = content.find('</section>', old_propozitie_start)
        if old_propozitie_end != -1:
            # Replace the old propozitie section with the new sections
            content = content[:old_propozitie_start] + new_sections + '\n' + content[old_propozitie_end + 10:]
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully moved the new sections to the correct location.")
        else:
            print("Could not find end of old propozitie section.")
    else:
        print("Could not find old propozitie section.")
else:
    print("Could not find appended sections at the end.")
