// BANNER
// Slider de imágenes del banner
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  const slides = document.querySelectorAll(".banner .slide");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 4000); // Cambiar imagen cada 4 segundos
}

// Botones prev/next del banner
const prevBanner = document.querySelector(".banner .prev");
const nextBanner = document.querySelector(".banner .next");

prevBanner.addEventListener("click", () => {
  slideIndex--;
  if (slideIndex < 1) {
    slideIndex = document.querySelectorAll(".banner .slide").length;
  }
  showSlides();
});

nextBanner.addEventListener("click", () => {
  slideIndex++;
  if (slideIndex > document.querySelectorAll(".banner .slide").length) {
    slideIndex = 1;
  }
  showSlides();
});

// FIN BANNER

// JavaScript para cerrar el menú desplegable al hacer clic fuera de él
document.addEventListener("click", function (event) {
  if (!event.target.closest(".header .nav, .dropdown-menu")) {
    document.querySelectorAll(".dropdown-menu").forEach(function (dropdown) {
      dropdown.style.display = "none";
    });
  }
});

// JavaScript para mostrar el menú desplegable al pasar el mouse
document.addEventListener("DOMContentLoaded", function () {
  const dropdownToggle = document.querySelectorAll(".dropdown-toggle");

  dropdownToggle.forEach((toggle) => {
    const dropdownMenu = toggle.nextElementSibling;

    toggle.addEventListener("mouseenter", function () {
      dropdownMenu.style.display = "block";
    });

    toggle.addEventListener("mouseleave", function () {
      dropdownMenu.style.display = "none";
    });

    dropdownMenu.addEventListener("mouseenter", function () {
      dropdownMenu.style.display = "block";
    });

    dropdownMenu.addEventListener("mouseleave", function () {
      dropdownMenu.style.display = "none";
    });
  });
});

// Fin JavaScript para cerrar el menú desplegable al hacer clic fuera de él

//SLIDER DE NOTICIAS
//SLIDER DE NOTICIAS//SLIDER DE NOTICIAS

let newsSlideIndex = 0; // Cambio: Renombré slideIndex a newsSlideIndex para evitar conflictos
const newsSlides = document.querySelectorAll(".post-slider .slide");
const totalNewsSlides = newsSlides.length;

function showNewsSlide(index) {
  // Ocultar todos los slides
  newsSlides.forEach((slide) => {
    slide.classList.remove("active");
  });
  // Mostrar el slide actual
  newsSlides[index].classList.add("active");
}

function nextNewsSlide() {
  newsSlideIndex++;
  if (newsSlideIndex >= totalNewsSlides) {
    newsSlideIndex = 0;
  }
  showNewsSlide(newsSlideIndex);
}

function prevNewsSlide() {
  newsSlideIndex--;
  if (newsSlideIndex < 0) {
    newsSlideIndex = totalNewsSlides - 1;
  }
  showNewsSlide(newsSlideIndex);
}

// Mostrar el primer slide al cargar la página
showNewsSlide(newsSlideIndex);

// Botones del slider
const prevNewsButton = document.querySelector(".post-slider .prev-news");
const nextNewsButton = document.querySelector(".post-slider .next-news");

// Event listeners para los botones
prevNewsButton.addEventListener("click", prevNewsSlide);
nextNewsButton.addEventListener("click", nextNewsSlide);

// Automatizar el slider cada 4 segundos
setInterval(nextNewsSlide, 4000); // Cambio: Usé setInterval para automatizar el cambio de slides

//FIN DE SLIDER DE NOTICIAS

//FIN DE SLIDER DE NOTICIAS
