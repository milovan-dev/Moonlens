document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll(".category-section");
    const navLinks = document.querySelectorAll(".gallery-filters .filter-btn");

    if (navLinks.length === 0) return;

    let isScrollingTo = false; // Zastavica koja sprečava sudar sa skrolom

    // 1. Ručni klik: odmah postavi aktivnu klasu i pauziraj observer na trenutak
    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            isScrollingTo = true;
            
            navLinks.forEach(l => l.classList.remove("active"));
            this.classList.add("active");

            // Dozvoli observeru da ponovo radi tek kada se skrolovanje završi
            setTimeout(() => {
                isScrollingTo = false;
            }, 800);
        });
    });

    if (sections.length === 0) return;

    // 2. Automatsko praćenje skrola (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: "-20% 0px -50% 0px", 
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        if (isScrollingTo) return; // Ako smo kliknuli dugme, ignoriši observer dok klizi

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute("id");
                
                navLinks.forEach(link => link.classList.remove("active"));
                
                const activeLink = document.querySelector(`.gallery-filters .filter-btn[href="#${id}"]`);
                if (activeLink) {
                    activeLink.classList.add("active");
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Ako je korisnik na samom vrhu, aktiviraj "Sve" dugme
    window.addEventListener("scroll", () => {
        if (isScrollingTo) return;

        if (window.scrollY < 150) {
            navLinks.forEach(link => link.classList.remove("active"));
            const sveBtn = document.querySelector('.gallery-filters .filter-btn[href="#gallery-top"]');
            if (sveBtn) sveBtn.classList.add("active");
        }
    });
});


// Lightbox funkcionalnost za slike
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImg");
    const closeBtn = document.querySelector(".modal-close");

    if (!modal) return;

    // Klik na bilo koju sliku u galeriji
    document.querySelectorAll(".gallery-image").forEach(img => {
        img.style.cursor = "pointer"; // Pokazuje da je slika klikabilna
        img.addEventListener("click", function () {
            modal.style.display = "flex";
            modal.style.alignItems = "center";
            modal.style.justifyContent = "center";
            modalImg.src = this.src;
        });
    });

    // Zatvaranje na klik X dugme
    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    // Zatvaranje na klik bilo gde van slike
    modal.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });

    // Zatvaranje na taster ESC na tastaturi
    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
            modal.style.display = "none";
        }
    });
});