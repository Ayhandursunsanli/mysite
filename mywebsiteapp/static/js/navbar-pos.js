
// navbar pozisyonu ve yukarı butonu için

window.onscroll = function() {
    scrollFunction();
    calcScrollValue();
};

function scrollFunction() {
    var navbar = document.querySelector(".navbar");

    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        navbar.style.width = "100%";
        navbar.style.position = "fixed";
        navbar.style.top = "0";
        navbar.style.borderRadius = "0";
        navbar.style.boxShadow = "rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px";
        navbar.style.background = "linear-gradient(180deg, rgba(7,28,77,1) 9%, rgba(33,79,133,1) 100%) !important";
    } else {
        navbar.style.width = "80%";
        navbar.style.position = "absolute";
        navbar.style.top = "30px";
        navbar.style.borderRadius = "30px";
        navbar.style.boxShadow = "none";
        navbar.style.background = "none";
    }
}

function calcScrollValue() {
    let scrollProgress = document.getElementById("progress");
    let pos = document.documentElement.scrollTop;
    let calcHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);
    if (pos > 100) {
        scrollProgress.style.display = "grid";
    } else {
        scrollProgress.style.display = "none";
    }
    scrollProgress.addEventListener("click", () => {
        document.documentElement.scrollTop = 0;
    });
    scrollProgress.style.background = `conic-gradient(#06a3da ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;
}

window.onload = function() {
    calcScrollValue();
    window.onscroll = function() {
        scrollFunction();
        calcScrollValue();
    };
};