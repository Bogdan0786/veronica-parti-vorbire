import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update toggleFairyCards
old_toggle1 = """function toggleFairyCards() {
  const container = document.getElementById('fairy-cards-container');
  if (container.style.display === 'none') {
    container.style.display = 'flex';
  } else {
    container.style.display = 'none';
  }
}"""
new_toggle1 = """function toggleFairyCards() {
  const container = document.getElementById('fairy-cards-container');
  const propContainer = document.getElementById('propozitie-cards-container');
  if (container.style.display === 'none') {
    container.style.display = 'flex';
    if(propContainer) propContainer.style.display = 'none';
  } else {
    container.style.display = 'none';
  }
}"""
content = content.replace(old_toggle1, new_toggle1)

# Update togglePropozitieCards
old_toggle2 = """function togglePropozitieCards() {
  const container = document.getElementById('propozitie-cards-container');
  if (container.style.display === 'none') {
    container.style.display = 'flex';
  } else {
    container.style.display = 'none';
  }
}"""
new_toggle2 = """function togglePropozitieCards() {
  const container = document.getElementById('propozitie-cards-container');
  const fairyContainer = document.getElementById('fairy-cards-container');
  if (container.style.display === 'none') {
    container.style.display = 'flex';
    if(fairyContainer) fairyContainer.style.display = 'none';
  } else {
    container.style.display = 'none';
  }
}"""
content = content.replace(old_toggle2, new_toggle2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated JS toggles to be mutually exclusive")
