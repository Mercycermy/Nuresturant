import os

css_append = """
/* ═══════ PREMIUM VISUAL UPGRADES (WHY US, EVENTS, GALLERY) ═══════ */

/* 1. WHY US (.feature-card) */
.features-grid {
    gap: 40px;
}
.feature-card {
    background: linear-gradient(160deg, rgba(20,20,20,0.9), rgba(10,10,10,0.9));
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 40px 30px;
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    z-index: 1;
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 50%; height: 100%;
    background: linear-gradient(to right, transparent, rgba(201,169,110,0.05), transparent);
    transform: skewX(-20deg);
    transition: all 0.7s;
    z-index: -1;
}
.feature-card:hover {
    transform: translateY(-10px);
    border-color: rgba(201,169,110,0.4);
    box-shadow: 0 15px 40px rgba(201,169,110,0.15), inset 0 0 20px rgba(201,169,110,0.02);
}
.feature-card:hover::before {
    left: 200%;
}
.feature-number {
    font-size: 4rem;
    font-family: 'Playfair Display', serif;
    background: linear-gradient(45deg, var(--gold), #f3e5ab);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    opacity: 0.15;
    position: absolute;
    top: -10px; right: 15px;
    transition: all 0.4s;
}
.feature-card:hover .feature-number {
    opacity: 0.3;
    transform: scale(1.1);
}

/* 2. EVENTS (.event-card) */
.event-card {
    background: linear-gradient(135deg, rgba(22,22,22,0.95), rgba(8,8,8,0.95));
    border: 1px solid rgba(201,169,110,0.1);
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    transition: all 0.4s ease;
    position: relative;
}
.event-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 10%; right: 10%;
    height: 3px;
    background: var(--gold);
    border-radius: 3px 3px 0 0;
    transform: scaleX(0);
    transform-origin: center;
    transition: transform 0.4s ease;
}
.event-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(201,169,110,0.2);
    border-color: rgba(201,169,110,0.5);
}
.event-card:hover::after {
    transform: scaleX(1);
}
.event-card ul li {
    position: relative;
    padding-left: 25px;
    margin-bottom: 15px;
}
.event-card ul li::before {
    content: '✦';
    position: absolute;
    left: 0;
    color: var(--gold);
    font-size: 1.1rem;
    line-height: inherit;
}

/* 3. GALLERY (.gallery-grid & item) */
.gallery-grid {
    display: block !important; /* override grid to use masonry column-count */
    column-count: 3;
    column-gap: 25px;
}
@media (max-width: 900px) {
    .gallery-grid { column-count: 2; }
}
@media (max-width: 500px) {
    .gallery-grid { column-count: 1; }
}
.gallery-item {
    position: relative;
    margin-bottom: 25px;
    break-inside: avoid;
    border-radius: 12px;
    overflow: hidden;
    cursor: pointer;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.5s;
    filter: sepia(30%) grayscale(40%) contrast(1.1);
}
.gallery-item::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, transparent 30%, rgba(0,0,0,0.6));
    opacity: 1;
    transition: opacity 0.5s;
    pointer-events: none;
}
.gallery-item::before {
    content: '⤢';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) scale(0.5);
    color: var(--gold);
    font-size: 3rem;
    opacity: 0;
    z-index: 2;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    pointer-events: none;
}
.gallery-item:hover img {
    transform: scale(1.1);
    filter: sepia(0%) grayscale(0%) contrast(1.2);
}
.gallery-item:hover::after {
    opacity: 0;
}
.gallery-item:hover::before {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
}
"""

with open('c:/Users/zuko/Documents/a/Nuresturant/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
    
print("Successfully appended CSS styling.")
