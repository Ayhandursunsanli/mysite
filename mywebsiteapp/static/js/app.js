
const texts = [
    "İletişime geç...",
    "Sosyal medya hesaplarını takip et...",

];

let count = 0;
let textIndex = 0;
let letterIndex = 0;
const textElement = document.querySelector('.text-animation');

function typeText() {
    textElement.textContent = texts[count].slice(0, letterIndex);
    letterIndex++;

    if (letterIndex > texts[count].length) {
        letterIndex = texts[count].length;
        setTimeout(deleteText, 1000);
        return;
    }

    setTimeout(typeText, 50);
}

function deleteText() {
    textElement.textContent = texts[count].slice(0, letterIndex);
    letterIndex--;

    if (letterIndex < 0) {
        letterIndex = 0;
        count = (count + 1) % texts.length;
        setTimeout(typeText, 500);
        return;
    }

    setTimeout(deleteText, 50);
}

typeText();



// Sayfa Haritası

$('.circle2').click(function () {
    let spWidth = $('.list-group').width();
    let spMarginRight = parseInt($('.list-group').css('margin-right'), 0);
    let w = (spMarginRight >= 0) ? -spWidth : 0;
    let cw = (w < 0) ? -w : spWidth - 22;
    
    // .list-group paneline uygun animasyonları ekleyin
    $('.list-group').animate({
        marginRight: w
    });
    $('.list-group span').animate({
        marginRight: w
    });

    // .circle butonunu hareket ettirin ve ikonları değiştirin
    $('.circle2').animate({
        right: cw
    }, function () {
        $('.fa-chevron-left').toggleClass('hide');
        $('.fa-chevron-right').toggleClass('hide');
    });
});






