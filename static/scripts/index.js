let index = 0;
    const images = document.querySelectorAll(".banner-img");

    function showBanner(i) {
        images.forEach((img, idx) => {
            img.style.display = idx === i ? "block" : "none";
        });
    }

    document.getElementById("next").addEventListener("click", () => {
        index = (index + 1) % images.length;
        showBanner(index);
    });

    document.getElementById("prev").addEventListener("click", () => {
        index = (index - 1 + images.length) % images.length;
        showBanner(index);
    });

    setInterval(() => {
        index = (index + 1) % images.length;
        showBanner(index);
        bookSlider();
    }, 5000);

// const bookShelfs = document.querySelectorAll('.category-items');
//
// function bookSlider() {
//     for (const shelf of bookShelfs) {
//         const books = shelf.querySelectorAll('.book')
//
//         if (books.length > 3) {
//             const firstBook = shelf.querySelectorAll('.book')[0];
//             const forthBook = shelf.querySelectorAll('.book')[3];
//
//             shelf.style.transition = 'transform 1s ease';
//             shelf.style.transform = 'translateX(-23vw)';
//             firstBook.style.transition = 'opacity 1s ease';
//             firstBook.style.opacity = '0';
//             forthBook.style.transition = 'opacity 1s ease';
//             forthBook.style.opacity = '1';
//
//
//             setTimeout(() => {
//                 shelf.style.transition = 'none';
//                 shelf.style.transform = 'translateX(0)';
//                 firstBook.style.transition = 'none';
//                 firstBook.style.opacity = '1';
//                 forthBook.style.transition = 'none';
//                 forthBook.style.opacity = '0';
//                 shelf.appendChild(firstBook);
//             }, 1000);
//         }
//     }
// }
