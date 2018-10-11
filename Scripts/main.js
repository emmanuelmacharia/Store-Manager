function navtab(evnt, navigate) {

    var n, content, sidenav;

    content = document.getElementsByClassName('content');
    for (n = 0; n < content.length; n++) {
        content[n].style.display = "none";
    }

    sidenav = document.getElementsByClassName('sidenav');

    for (n = 0; n < sidenav.length; n++) {
        sidenav[n].className.replace(' active', '');
    }

    document.getElementById(navigate).style.display = 'flex';

    evnt.currentTarget.className += " active";

}

document.getElementById('default').click();
