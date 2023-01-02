//const close = document.querySelector('.close');
//const card = document.querySelector('.card');

//close.addEventListener('click', function(){
//   card.style.display = 'none';
//});

// dom traversal
const close = document.querySelectorAll('.close');

// for( let i = 0; i < close.length; i++){
//     close[i].addEventListener('click', function(e){
//         //alert('tombol ke-' + i)
//         e.target.parentElement.style.display = 'none';
//     });

// }

close.forEach(function(el) {
    el.addEventListener('click', function(e) {
        e.target.parentElement.style.display = 'none';
    });
});


(function() {

    var infoBar = document.querySelector(".cookies-infobar");
    var btnAccept = document.querySelector("#cookies-infobar-close");

    // Check if user has already accepted the notification
    if (wasAccepted()) {
        hideInfobar();
        return;
    }

    //listen for the click event on Accept button
    btnAccept.addEventListener("click", function(e) {
        e.preventDefault();
        hideInfobar();
        saveAcceptInCookies(7);
    });

    //hide cookie info bar
    function hideInfobar() {
        infoBar.className = infoBar.classList.value + " cookies-infobar_accepted";
    }

    // Check if user has already accepted the notification
    function wasAccepted() {
        return checkCookie() === "1";
    }

    // get cookie
    function checkCookie() {
        var name = "cookieInfoHidden=";
        var cookies = document.cookie.split(';');

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            while (cookie.charAt(0) == ' ') {
                cookie = cookie.substring(1);
            }

            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        return "";
    };

    //save cookie
    function saveAcceptInCookies(daysOfValidity) {
        var now = new Date();
        var time = now.getTime() + (daysOfValidity * 24 * 60 * 60 * 1000);
        var newTime = new Date(now.setTime(time));

        newTime = newTime.toUTCString();

        document.cookie = "cookieInfoHidden=1; expires=" + newTime + "; path=/";
    }

})();