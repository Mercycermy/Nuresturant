/**
 * Nu Restaurant Landing Page scripts
 */

// Mobile menu toggle
function toggleMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    const hamburger = document.querySelector('.hamburger');
    mobileMenu.classList.toggle('open');

    // Animate hamburger
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
    if (mobileMenu.classList.contains('open')) {
        toggleMenu();
    }
}

// Sticky Navbar on scroll
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Reveal on scroll (Intersection Observer)
const revealElements = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    const fades = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
    fades.forEach(el => observer.observe(el));
};

// Smooth scroll for anchor links
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
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
};


// Gallery Lightbox Logic
let currentImageIndex = 0;
const galleryImages = [
    { src: 'images/visual.png', caption: 'Authentic Kitfo Platter' },
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
    document.body.style.overflow = 'hidden'; // Prevent scrolling
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
}

function changeLightboxImage(step) {
    currentImageIndex += step;
    if (currentImageIndex >= galleryImages.length) currentImageIndex = 0;
    if (currentImageIndex < 0) currentImageIndex = galleryImages.length - 1;

    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');

    // Add a small fade effect during transition
    lightboxImg.style.opacity = '0';
    setTimeout(() => {
        lightboxImg.src = galleryImages[currentImageIndex].src;
        lightboxCaption.textContent = galleryImages[currentImageIndex].caption;
        lightboxImg.style.opacity = '1';
    }, 150);
}

// Close lightbox on click outside the image
document.getElementById('lightbox').addEventListener('click', (e) => {
    if (e.target.id === 'lightbox') {
        closeLightbox();
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    revealElements();
    setupSmoothScroll();
});
