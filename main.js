/**
 * Nu Restaurant – Interactive Scroll Animations & Interactions
 */

// ═══════ MOBILE MENU ═══════
function toggleMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    const hamburger = document.querySelector('.hamburger');
    mobileMenu.classList.toggle('open');
    const spans = hamburger.querySelectorAll('span');
    if (mobileMenu.classList.contains('open')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
    }
}

function closeMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenu.classList.contains('open')) toggleMenu();
}

// ═══════ STICKY NAVBAR ═══════
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// ═══════ INTERACTIVE SCROLL ANIMATIONS ═══════
const initScrollAnimations = () => {
    const animElements = document.querySelectorAll('[data-anim]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const delay = parseInt(el.dataset.delay || 0);
                setTimeout(() => {
                    el.classList.add('anim-visible');
                }, delay);
                observer.unobserve(el);
            }
        });
    }, {
        threshold: 0.12,
        rootMargin: '0px 0px -60px 0px'
    });

    animElements.forEach(el => {
        const anim = el.dataset.anim;
        el.style.opacity = '0';
        el.style.transition = 'opacity 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';

        switch (anim) {
            case 'fade-up':
                el.style.transform = 'translateY(40px)';
                break;
            case 'fade-left':
                el.style.transform = 'translateX(50px)';
                break;
            case 'fade-right':
                el.style.transform = 'translateX(-50px)';
                break;
            case 'fade-scale':
                el.style.transform = 'scale(0.9)';
                break;
            case 'fade-rotate':
                el.style.transform = 'rotate(-3deg) translateY(30px)';
                break;
        }

        observer.observe(el);
    });

    // Add visible state
    const style = document.createElement('style');
    style.textContent = `
        .anim-visible {
            opacity: 1 !important;
            transform: none !important;
        }
    `;
    document.head.appendChild(style);
};

// ═══════ PARALLAX SCROLL EFFECT ═══════
const initParallax = () => {
    const hero = document.getElementById('home');
    const heroImage = document.querySelector('.hero-food-card');

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        const heroH = hero ? hero.offsetHeight : 800;

        if (scrollY < heroH && heroImage) {
            const parallaxY = scrollY * 0.15;
            const parallaxScale = 1 + scrollY * 0.0002;
            heroImage.style.transform = `translateY(${parallaxY}px) scale(${parallaxScale})`;
        }
    }, { passive: true });
};

// ═══════ COUNTER ANIMATION ═══════
const animateCounters = () => {
    const counters = document.querySelectorAll('[data-count]');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.dataset.count);
                const suffix = el.textContent.replace(/[0-9]/g, '').trim() || '+';
                let current = 0;
                const step = Math.max(1, Math.floor(target / 60));
                const timer = setInterval(() => {
                    current += step;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    el.textContent = current + suffix;
                }, 25);
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(el => observer.observe(el));
};

// ═══════ SMOOTH REVEAL FOR SECTIONS ═══════
const initSectionReveal = () => {
    const sections = document.querySelectorAll('section');
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-revealed');
            }
        });
    }, { threshold: 0.05 });

    sections.forEach(s => sectionObserver.observe(s));
};

// ═══════ MAGNETIC HOVER EFFECT ON CARDS ═══════
const initMagneticCards = () => {
    const cards = document.querySelectorAll('.menu-card, .feature-card, .event-card, .testimonial-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;
            card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(800px) rotateX(0) rotateY(0) translateY(0)';
        });
    });
};

// ═══════ CURSOR GLOW EFFECT ═══════
const initCursorGlow = () => {
    const glow = document.createElement('div');
    glow.className = 'cursor-glow';
    document.body.appendChild(glow);

    const style = document.createElement('style');
    style.textContent = `
        .cursor-glow {
            position: fixed; width: 300px; height: 300px;
            background: radial-gradient(circle, rgba(201,169,110,0.06) 0%, transparent 70%);
            border-radius: 50%; pointer-events: none; z-index: 0;
            transition: transform 0.15s ease-out;
            transform: translate(-50%, -50%);
        }
    `;
    document.head.appendChild(style);

    document.addEventListener('mousemove', (e) => {
        glow.style.left = e.clientX + 'px';
        glow.style.top = e.clientY + 'px';
    });
};

// ═══════ SMOOTH ANCHOR SCROLL ═══════
const setupSmoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const navHeight = document.querySelector('nav').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });
};

// ═══════ GALLERY LIGHTBOX ═══════
let currentImageIndex = 0;
const galleryImages = [
    { src: 'images/visual.png', caption: 'Authentic Ethiopian Cuisine' },
    { src: 'images/visual1.png', caption: 'Traditional Ethiopian Dinner' },
    { src: 'images/menu.png', caption: 'Shiro Wot in Clay Pot' },
    { src: 'images/menu1.png', caption: 'Doro Wot Special' },
    { src: 'images/menu2.png', caption: 'Special Kitfo' },
    { src: 'images/about.png', caption: 'Nu Restaurant Interior' }
];

function openLightbox(index) {
    currentImageIndex = index;
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    lightboxImg.src = galleryImages[index].src;
    lightboxCaption.textContent = galleryImages[index].caption;
    lightbox.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function changeLightboxImage(step) {
    currentImageIndex += step;
    if (currentImageIndex >= galleryImages.length) currentImageIndex = 0;
    if (currentImageIndex < 0) currentImageIndex = galleryImages.length - 1;
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    lightboxImg.style.opacity = '0';
    lightboxImg.style.transform = 'scale(0.95)';
    setTimeout(() => {
        lightboxImg.src = galleryImages[currentImageIndex].src;
        lightboxCaption.textContent = galleryImages[currentImageIndex].caption;
        lightboxImg.style.opacity = '1';
        lightboxImg.style.transform = 'scale(1)';
    }, 200);
}

// Close lightbox on background click
document.getElementById('lightbox').addEventListener('click', (e) => {
    if (e.target.id === 'lightbox') closeLightbox();
});

// Close lightbox on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') changeLightboxImage(-1);
    if (e.key === 'ArrowRight') changeLightboxImage(1);
});

// ═══════ INITIALIZE EVERYTHING ═══════
document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initParallax();
    animateCounters();
    initSectionReveal();
    initMagneticCards();
    initCursorGlow();
    setupSmoothScroll();
});
