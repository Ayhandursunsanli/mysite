

// Loading ekranını gösterme fonksiyonu
function showLoadingScreen() {
    var loadingScreen = document.getElementById('animation-container-parent');
    loadingScreen.style.opacity = 1;
}

// Belirli bir süre sonra loading ekranını gizle ve içeriği gösterme fonksiyonu
function hideLoadingScreen() {
    var loadingScreen = document.getElementById('animation-container-parent');
    loadingScreen.style.transition = 'opacity 0.3s ease-out'; // Transition efektini ekle
    loadingScreen.style.opacity = 0;

    setTimeout(function() {
        loadingScreen.style.display = 'none';
        loadingScreen.style.transition = ''; // Transition'ı kaldır
    }, 300); // Opaklık değeri değiştikten sonra loading ekranını gizle (0.3 saniye)
}

// Sayfa yüklendiğinde direkt olarak loading ekranını göster
showLoadingScreen();

// Belirli bir süre sonra içeriği göster
setTimeout(function() {
    // Burada içeriğinizi görünür yapmak için gerekli kodları ekleyebilirsiniz
    // Örneğin: document.body.style.display = 'block'; veya içeriğin başka bir öğesi
    hideLoadingScreen();
}, 1000); // 3 saniye (3000 milisaniye) sonra loading ekranını gizle






