function changeImage(src) {
    document.getElementById('mainProductImage').src = src;
}
// Ensure smooth horizontal scrolling on mobile
const thumbnailImages = document.getElementById('thumbnail-images');
thumbnailImages.addEventListener('wheel', (evt) => {
    if (window.innerWidth <= 768) {
        evt.preventDefault();
        thumbnailImages.scrollLeft += evt.deltaY;
    }
});
