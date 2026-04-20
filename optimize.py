import sys
import re

file_path = r'c:\Users\EduPe\.gemini\antigravity\scratch\peccinin\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make scroll event listeners passive
content = content.replace("window.addEventListener('scroll', () => {", "window.addEventListener('scroll', () => {") # Just to check, but let's do a better replace
content = re.sub(r"window\.addEventListener\('scroll',\s*\(\)\s*=>\s*\{", r"window.addEventListener('scroll', () => {", content)
content = re.sub(r"\}\);\s*// ---- Form submit ----", "}, { passive: true });\n    \n    // ---- Form submit ----", content)
# It's safer to use multi_replace for precise patching. Let's just do standard Python replacements.

content = content.replace("});\n    \n    // ---- Mobile menu ----", "}, { passive: true });\n    \n    // ---- Mobile menu ----")
content = content.replace("});\n    \n    // ---- Active nav link on scroll ----", "}, { passive: true });\n    \n    // ---- Active nav link on scroll ----")
content = content.replace("});\n    });\n  </script>", "}, { passive: true });\n    });\n  </script>")

# Zoom SVG Cleanup
zoom_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>'

svg_defs = """
  <!-- Reusable SVGs -->
  <svg width="0" height="0" style="display: none;">
    <defs>
      <symbol id="icon-zoom" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/>
      </symbol>
    </defs>
  </svg>
"""

content = content.replace(zoom_svg, '<svg width="22" height="22"><use href="#icon-zoom" /></svg>')

if '<!-- Reusable SVGs -->' not in content:
    content = content.replace('<body>\n', '<body>\n' + svg_defs)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Optimization complete')
