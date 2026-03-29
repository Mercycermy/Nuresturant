import re
import os

html_path = 'c:/Users/zuko/Documents/a/Nuresturant/index.html'
help_path = 'c:/Users/zuko/Documents/a/Nuresturant/help.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. SVGs for Events
svg_birthday = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
svg_private = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10l-1.5 13H8.5L7 4z"/></svg>'
svg_custom = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'

html = html.replace('<h3>Birthday Parties</h3>', f'<div class="event-icon">{svg_birthday}</div>\\n                    <h3>Birthday Parties</h3>')
html = html.replace('<h3>Private Parties</h3>', f'<div class="event-icon">{svg_private}</div>\\n                    <h3>Private Parties</h3>')
html = html.replace('<h3>Custom Parties</h3>', f'<div class="event-icon">{svg_custom}</div>\\n                    <h3>Custom Parties</h3>')

# 2. Remove Footer Links from index.html
links_to_remove = [
    '<li><a href="#">Food & Beverage Services</a></li>',
    '<li><a href="#">Delivery & Takeaway Services</a></li>',
    '<li><a href="#">Private Dining & Special Occasions</a></li>'
]
for link in links_to_remove:
    # also try with varying whitespace
    html = re.sub(r'<li>\s*<a href="#">' + re.escape('Food & Beverage Services') + r'</a>\s*</li>', '', html)
    html = re.sub(r'<li>\s*<a href="#">' + re.escape('Delivery & Takeaway Services') + r'</a>\s*</li>', '', html)
    html = re.sub(r'<li>\s*<a href="#">' + re.escape('Private Dining & Special Occasions') + r'</a>\s*</li>', '', html)

# 3. Create Menu Tabs if not already present
if '<div class="menu-tabs"' not in html:
    categories = re.findall(r'<h3 class="category-title">(.*?)</h3>', html)
    if categories:
        tabs_html = '<div class="menu-tabs" data-anim="fade-up">\n'
        for i, cat in enumerate(categories):
            active_class = ' active' if i == 0 else ''
            target_id = cat.lower().replace(' ', '-')
            tabs_html += f'    <button class="menu-tab-btn{active_class}" data-target="{target_id}">{cat}</button>\n'
            # Update the menu category div with ID
            old_div = f'<div class="menu-category" data-anim="fade-up">\n        <h3 class="category-title">{cat}</h3>'
            new_div = f'<div id="{target_id}" class="menu-category{" active" if i==0 else ""}" data-anim="fade-up">\n        <h3 class="category-title">{cat}</h3>'
            html = html.replace(old_div, new_div)
            
        tabs_html += '</div>\n'
        html = html.replace('<div class="full-menu-container">', tabs_html + '<div class="full-menu-container">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 4. Update Help.html Socials 
if os.path.exists(help_path):
    with open(help_path, 'r', encoding='utf-8') as f:
        help_html = f.read()
    
    socials_pattern = re.compile(r'<div class="social-links">.*?</div>', re.DOTALL)
    new_socials = '''<div class="social-links">
                        <a href="https://tiktok.com/@numigbet" target="_blank" class="social-link" title="TikTok">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.34 2.88 2.88 0 0 1 2.31-4.53 2.84 2.84 0 0 1 1.05.19V9.07a6.29 6.29 0 0 0-1.12-.1 6.33 6.33 0 0 0-5.12 9.87A6.33 6.33 0 0 0 9.17 22a6.34 6.34 0 0 0 6.13-6.68v-6.3a8.27 8.27 0 0 0 4.63 1.54V7.1a5.18 5.18 0 0 0-1.34-.41z"/>
                            </svg>
                        </a>
                    </div>'''
    help_html = socials_pattern.sub(new_socials, help_html)
    with open(help_path, 'w', encoding='utf-8') as f:
        f.write(help_html)
        
print("Successfully modified index.html and help.html")
