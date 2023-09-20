console.log('test')

function hamMenu() {
    menu = document.getElementById('menu-popup');

    if (menu.style.height === "100vh") {
        menu.style.height = "0px";
    } else {
        menu.style.height = "100vh";
    }
}