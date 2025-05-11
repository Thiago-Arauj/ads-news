// Prevent on Click Scroll page to top
const links = document.querySelectorAll("span.read-more-button");
for(link of links) {
    link.setAttribute("onclick", "return false;");
}

// Carousel
const mainCarousel = document.querySelector('#main-carousel');
const carousel = new bootstrap.Carousel(mainCarousel, {
  interval: 4000,
  touch: true
})