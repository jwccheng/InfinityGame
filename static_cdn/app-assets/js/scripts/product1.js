//Change Package Listing Total
document.getElementById('pp_quantity_a').value = 1;
var ppQ = document.getElementById('pp_quantity').value;
var mem = document.getElementById('pp_quantity_q').value;
if (mem == "OUTLET"){
    var ppQQ = 10;
}
else{
    var ppQQ = 1;
}
var ppQA = document.getElementById('pp_quantity_a').value;
ppPrice = parseInt(ppQ) * parseInt(ppQQ) * parseInt(ppQA)
document.getElementById('ppTotal').value = (ppPrice);

$('.pp_c').on('change input', function(){
    
	var ppQ = document.getElementById('pp_quantity').value;
    var mem = document.getElementById('pp_quantity_q').value;
    if (mem == "OUTLET"){
        var ppQQ = 10;
    }
    else{
        var ppQQ = 1;
    }
    var ppQA = document.getElementById('pp_quantity_a').value;
    ppPrice = parseInt(ppQ) * parseInt(ppQQ) * parseInt(ppQA)  
    document.getElementById('ppTotal').value = (ppPrice);

});
