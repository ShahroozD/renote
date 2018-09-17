//=====================================









//=============================================================
//=====================  getUrlVars  ==========================
//=============================================================

var getUrlVars = function (){
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;

};



//=============================================================
//======================  mapfixed  ===========================
//=============================================================

var mapfixed = function() {
  setTimeout(function() {
    center = map1.getCenter()
    google.maps.event.trigger(map1, "resize");
    map1.setCenter(center);

    center = map2.getCenter()
    google.maps.event.trigger(map2, "resize");
    map2.setCenter(center);
  }, 100);
}





//=============================================================
//======================  addCommas  ===========================
//=============================================================
function addCommas(nStr){
  if (nStr) {
    nStr = nStr.toString();
    nStr = nStr.replace(/,/g, "");
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
      return x1 + x2
  }
  else {
      return""
  }

}
