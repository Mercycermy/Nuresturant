import re

with open('c:/Users/zuko/Documents/a/Nuresturant/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace logos
html = html.replace('logo.png', 'logo.jpg')

# Remove menu footers entirely
html = re.sub(r'<div class="menu-footer">.*?</div>', '', html, flags=re.DOTALL)

# Replace Feature
html = html.replace('''<div class="feature-icon">🎁</div>
                    <h4>Loyalty Rewards</h4>
                    <p>Earn points on every order and redeem them for free authentic meals.</p>''', '''<div class="feature-icon">⭐</div>
                    <h4>Rate & Feedback</h4>
                    <p>Share your experience and help us improve with our built-in rating system.</p>''')

# Replace Screenshots
screenshots_old = re.search(r'<div class="screenshots-scroll">.*?<!-- Slide 3 -->.*?</div>\s+</div>', html, flags=re.DOTALL)
if screenshots_old:
    screenshots_new = '''<div class="screenshots-scroll">
                <div class="phone-mockup" style="padding: 0; background: transparent; box-shadow: none;">
                    <img src="images/image.jpg" alt="App Screenshot 1" style="width: 100%; height: 100%; object-fit: cover; border-radius: 32px; box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
                </div>
                <div class="phone-mockup" style="padding: 0; background: transparent; box-shadow: none;">
                    <img src="images/image2.jpg" alt="App Screenshot 2" style="width: 100%; height: 100%; object-fit: cover; border-radius: 32px; box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
                </div>
                <div class="phone-mockup" style="padding: 0; background: transparent; box-shadow: none;">
                    <img src="images/image3.jpg" alt="App Screenshot 3" style="width: 100%; height: 100%; object-fit: cover; border-radius: 32px; box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
                </div>
            </div>'''
    html = html.replace(screenshots_old.group(0), screenshots_new)

with open('c:/Users/zuko/Documents/a/Nuresturant/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Replaced content successfully")
