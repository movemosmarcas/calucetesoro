import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_slides = """<div class="hero-slideshow">
                <div class="hero-slide active" style="background-image: url('Imagenes/AL Caluce Med ALE_0541.jpg');"></div>
                <div class="hero-slide" style="background-image: url('Imagenes/CF1BFF68-5DA4-4A63-A7FF-D19A59F9B693_1_201_a.jpeg');"></div>
            </div>"""

html = re.sub(r'<div class="hero-slideshow">.*?</div>\s*<div class="hero-overlay">', new_slides + '\n            <div class="hero-overlay">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
