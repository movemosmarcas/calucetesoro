import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Testimonial 1
new_t1_text = """<div class="testimonial-info">
                        <p class="testimonial-quote">"Ha sido una experiencia maravillosa, ha llenado todas las expectativas y nos encontramos muy felices con el nivel profesional y humano"</p>
                        <h4 class="testimonial-name">Sonia Gómez, Residente</h4>
                    </div>"""
html = re.sub(r'<div class="testimonial-info">\s*<p class="testimonial-quote">"Uno est.*?</div>', new_t1_text, html, flags=re.DOTALL)

# Replace Testimonial 2
new_t2_text = """<div class="testimonial-info">
                        <p class="testimonial-quote">"Amo todo de Hábitat, es una gran comunidad con personas amables, un equipo amigable, se lo recomiendo a todos mis amigos y personas que conozco"</p>
                        <h4 class="testimonial-name">Alcira Trujillo, Residente</h4>
                    </div>"""
html = re.sub(r'<div class="testimonial-info">\s*<p class="testimonial-quote">"Mis padres.*?</div>', new_t2_text, html, flags=re.DOTALL)

# Also update the video thumbnails based on screenshots (we will use placeholders or try to find them)
# Let's check images first.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
