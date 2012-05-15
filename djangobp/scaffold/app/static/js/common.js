function loadGeoLocation(form, onSuccess) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            form.latitude.value = position.coords.latitude;
            form.longitude.value = position.coords.longitude;
            if (position.address)
                form.address.value = position.address.city + ' ' + position.address.street;
            if (onSuccess) onSuccess(form)
        }, function(error) {
            form.latitude.value = 37.422006;
            form.longitude.value = -122.084095;
            if (onSuccess) onSuccess(form)
            // TODO notify locatino error, not alert. flash?
        });
    }
}

function getCookie ( cookieName ) {
  var results = document.cookie.match ( '(^|;) ?' + cookieName + '=([^;]*)(;|$)' );

  if ( results )
    return unescape(results[2]);
  else
    return null;
}

function setCookie( name, value, expires, path, domain, secure ) {
// set time, it's in milliseconds
    var today = new Date();
    today.setTime( today.getTime() );

    /*
     if the expires variable is set, make the correct
     expires time, the current script below will set
     it for x number of days, to make it for hours,
     delete * 24, for minutes, delete * 60 * 24
     */
    if ( expires ) {
        expires = expires * 1000 * 60 * 60 * 24;
    }
    var expires_date = new Date( today.getTime() + (expires) );

    document.cookie = name + "=" +escape( value ) +
        ( ( expires ) ? ";expires=" + expires_date.toGMTString() : "" ) +
        ( ( path ) ? ";path=" + path : "" ) +
        ( ( domain ) ? ";domain=" + domain : "" ) +
        ( ( secure ) ? ";secure" : "" );
}

function setTab(tabIndex) {
    $('.tabs li').removeClass('active')
    $('.tabs li')[tabIndex].className = 'active';
    setCookie('tab', '' + tabIndex, null, '/');
}

function initTab() {
    var tab = getCookie('tab');
    var tabIndex = tab ? parseInt(tab) : 0;
    $('.tabs li')[tabIndex].className = 'active';
}