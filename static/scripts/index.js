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
    }, 5000);
