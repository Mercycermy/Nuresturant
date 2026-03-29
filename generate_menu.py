import re

menu_text = """Breakfast
Scrambled egg – 250 ETB
Chechebsa – 180 ETB
NU chechebsa – 280 ETB
Normal full – 145 ETB
Special full – 190 ETB
Kinche – 210 ETB
Bread Firfir – 180 ETB
Kategna Be ergo – 250 ETB

Fasting
Special Fasting Firfir – 340 ETB
Penne with vegetables – 210 ETB
Rice with vegetable – 230 ETB
Fasting Goulash – 230 ETB
Cooked vegetable – 230 ETB
Mulu Agelgel Fasting – 820 ETB
Gemash Agelgel Fasting – 450 ETB
Shero tegabino/lala – 260 ETB
Telba wot – 250 ETB
Telba Fitfit – 250 ETB
Suf Fitfit – 250 ETB
Shero with vegetable – 250 ETB

Meat
Derkosh Firfir – 170 ETB
Special Tibs Firfir – 510 ETB
Norma Tibs Firfir – 390 ETB
Meet Firfir – 350 ETB
Lamb Tibs – 510 ETB
Beef Tibs – 510 ETB
Kitfo – 650 ETB
Kitfo banatu – 1200 ETB
Key wot – 390 ETB
Kikel – 390 ETB
Shero bozena – 350 ETB
Shekla – 1020 ETB
Doro wot mulu – 4000 ETB
Doro wot Gemash – 2000 ETB

Fish
Fish goulash – 450 ETB
Fish cuttlet – 450 ETB
Grilled Fish – 450 ETB

Western
Shewarma – 430 ETB
Tuna pizza – 650 ETB
Margarita pizza – 580 ETB
Beef pizza – 580 ETB
Chicken pizza – 650 ETB
Bergeriza – 690 ETB
Mini pizza – 475 ETB
Lasagna – 1050 ETB
Beef burger – 520 ETB
Cheese burger – 530 ETB
Club sandwich – 540 ETB
Avocado sandwich – 535 ETB
French fries – 210 ETB

Soups
Beef Soup – 250 ETB
Fish Soup – 290 ETB
Vegetable Soup – 170 ETB
Tomato Soup – 170 ETB

Salads
Tuna salad – 240 ETB
Mixed salad – 190 ETB
Nu special Salad – 480 ETB

Desserts
Fruit punch – 240 ETB
Cream cake – 80 ETB
Fruit salad – 240 ETB
Nu Special Fruit salad Fasting – 480 ETB
Nu Special Fruit salad Non Fasting – 480 ETB

Juices
Special juice – 190 ETB
Shake – 190 ETB
Seasonal juice – 160 ETB
Orange juice – 150 ETB

Extras
Ketchup – 20 ETB
Mitmita – 20 ETB
Awaze – 30 ETB
Extra Injera – 40 ETB
Extra Bread – 20 ETB
Extra Butter – 50 ETB
Mayonnaise – 20 ETB"""

categories = menu_text.split('\n\n')
html_output = '<div class="full-menu-container">\n'

for cat in categories:
    lines = cat.strip().split('\n')
    cat_name = lines[0].strip()
    html_output += f'    <div class="menu-category" data-anim="fade-up">\n'
    html_output += f'        <h3 class="category-title">{cat_name}</h3>\n'
    html_output += f'        <div class="menu-items-list">\n'
    
    for item in lines[1:]:
        if '–' in item:
            name, price = item.split('–')
        elif '-' in item:
            name, price = item.split('-')
        else:
            continue
            
        name = name.strip()
        price = price.strip()
        html_output += f'            <div class="menu-item-row">\n'
        html_output += f'                <span class="item-name">{name}</span>\n'
        html_output += f'                <span class="item-dots"></span>\n'
        html_output += f'                <span class="item-price">{price}</span>\n'
        html_output += f'            </div>\n'
        
    html_output += f'        </div>\n'
    html_output += f'    </div>\n'

html_output += '</div>'

# Now read index.html
with open('c:/Users/zuko/Documents/a/Nuresturant/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the menu grid
import re
new_html = re.sub(r'<div class="menu-grid">.*?</div>\n        </div>\n    </section>', f'{html_output}\n        </div>\n    </section>', html, flags=re.DOTALL)

# Replace Events grid with carousel
events_grid_pattern = r'<div class="events-grid">(.*?)</div>\n        </div>\n    </section>'
events_carousel = r'<div class="events-carousel carousel-container">\n            <div class="carousel-track events-track">\1</div>\n            </div>\n        </div>\n    </section>'
new_html = re.sub(events_grid_pattern, events_carousel, new_html, flags=re.DOTALL)

# Replace Testimonials grid with carousel
test_grid_pattern = r'<div class="testimonials-grid">(.*?)</div>\n        </div>\n    </section>'
test_carousel = r'<div class="testimonials-carousel carousel-container">\n            <div class="carousel-track testimonials-track">\1</div>\n            </div>\n        </div>\n    </section>'
new_html = re.sub(test_grid_pattern, test_carousel, new_html, flags=re.DOTALL)

# Update Footer
footer_pattern = r'<div class="footer-bottom">.*?</div>'
new_footer_bottom = """<div class="footer-bottom">
                <p>&copy; 2026 Nu Restaurant. All rights reserved.</p>
                <p>Working hours: 6:00 AM – 11:00 PM</p>
                <p>Gondar, Ethiopia · 0961612461 / 0962629362 · nurestaurant2@gmail.com</p>
            </div>"""
new_html = re.sub(footer_pattern, new_footer_bottom, new_html, flags=re.DOTALL)

# Update Socials
socials_pattern = r'<div class="social-links">.*?</div>'
new_socials = """<div class="social-links">
                        <a href="https://tiktok.com/@numigbet" target="_blank" class="social-link" title="TikTok">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.34 2.88 2.88 0 0 1 2.31-4.53 2.84 2.84 0 0 1 1.05.19V9.07a6.29 6.29 0 0 0-1.12-.1 6.33 6.33 0 0 0-5.12 9.87A6.33 6.33 0 0 0 9.17 22a6.34 6.34 0 0 0 6.13-6.68v-6.3a8.27 8.27 0 0 0 4.63 1.54V7.1a5.18 5.18 0 0 0-1.34-.41z"/>
                            </svg>
                        </a>
                    </div>"""
new_html = re.sub(socials_pattern, new_socials, new_html, flags=re.DOTALL)

# Update Contact section explicitly
contact_phones_pattern = r'<h4>Phone</h4>\s*<p>\+251 962 629 362</p>'
new_contact_phones = r'<h4>Phone</h4><p>0961612461<br>0962629362</p>'
new_html = re.sub(contact_phones_pattern, new_contact_phones, new_html)

contact_email_pattern = r'<h4>Email</h4>\s*<p>info@nu-restaurant\.com</p>'
new_contact_email = r'<h4>Email</h4><p>nurestaurant2@gmail.com</p>'
new_html = re.sub(contact_email_pattern, new_contact_email, new_html)

contact_hours_pattern = r'<div class="hour-item"><span>Monday – Sunday</span><span>11:00 AM – 11:00 PM</span></div>'
new_contact_hours = r'<div class="hour-item"><span>Monday – Sunday</span><span>6:00 AM – 11:00 PM</span></div>'
new_html = re.sub(contact_hours_pattern, new_contact_hours, new_html)

with open('c:/Users/zuko/Documents/a/Nuresturant/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html successfully.")
