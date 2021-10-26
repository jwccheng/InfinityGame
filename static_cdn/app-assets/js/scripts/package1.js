//Change Package Listing Total

var ppQ = document.getElementById('pp_quantity').value;
var ppQQ = 1;
ppPrice = parseInt(ppQ) * parseInt(ppQQ)

document.getElementById('ppPrice').value = ppPrice  + " + (10%)";
document.getElementById('ppTotal').value = (ppPrice + (ppPrice * 0.10));

$('.pp_c').on('change input', function(){
    
	var ppQ = document.getElementById('pp_quantity').value;
    var ppQQ = 1;
    ppPrice = parseInt(ppQ) * parseInt(ppQQ)
    document.getElementById('ppPrice').value = ppPrice  + " + (10%)";
    document.getElementById('ppTotal').value = (ppPrice + (ppPrice * 0.10));

});
