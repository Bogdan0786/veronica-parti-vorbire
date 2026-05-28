import sys

with open('index.html', 'rb') as f:
    html_b = f.read()

# Find the end of the correct Vocabular part
marker1 = '<li>nea (nea Ion) ↔ ne-a (ne-a dat)</li>\n    </div>\n  </div>\n'.encode('utf-8')
idx1 = html_b.find(marker1)
if idx1 == -1:
    # Try with \r\n
    marker1 = '<li>nea (nea Ion) ↔ ne-a (ne-a dat)</li>\r\n    </div>\r\n  </div>\r\n'.encode('utf-8')
    idx1 = html_b.find(marker1)

if idx1 == -1:
    print("Could not find marker1!")
    sys.exit(1)
    
idx1 += len(marker1)

# Find the JS block
marker2 = '<!-- ════════════════════ JAVASCRIPT ════════════════════ -->'.encode('utf-8')
idx2 = html_b.find(marker2)

if idx2 == -1:
    print("Could not find JS block!")
    sys.exit(1)

html_part1 = html_b[:idx1]
html_part2 = html_b[idx2:]

with open('exercises.html', 'rb') as f:
    exercises_b = f.read()

repaired = html_part1 + exercises_b + b'\n' + html_part2

with open('index.html', 'wb') as f:
    f.write(repaired)

print("Repair complete!")
