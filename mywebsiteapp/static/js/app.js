
const texts = [
    "İletişime geç...",
    "Sosyal medya hesaplarımı takip et...",

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





