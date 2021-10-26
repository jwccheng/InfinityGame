document.getElementById('ppsrp_quantity_a').value = 1;
var ppsrpQ = document.getElementById('ppsrp_quantity').value;
var mem = document.getElementById('ppsrp_quantity_q').value;
if (mem == "OUTLET"){
    var ppsrpQQ = 10;
}
else{
    var ppsrpQQ = 1;
}
var ppsrpQA = document.getElementById('ppsrp_quantity_a').value;
ppsrpPrice = parseInt(ppsrpQ) * parseInt(ppsrpQQ) * parseInt(ppsrpQA)

srp = ppsrpPrice / 2
document.getElementById('ppsrpTotal').value = "PP "+ (srp) + " + " + "SRP "+ (srp);

$('.ppsrp_c').on('change input', function(){

	var ppsrpQ = document.getElementById('ppsrp_quantity').value;
    var mem = document.getElementById('ppsrp_quantity_q').value;
    if (mem == "OUTLET"){
        var ppsrpQQ = 10;
    }
    else{
        var ppsrpQQ = 1;
    }
    var ppsrpQA = document.getElementById('ppsrp_quantity_a').value;
    ppsrpPrice = parseInt(ppsrpQ) * parseInt(ppsrpQQ) * parseInt(ppsrpQA)
    srp = ppsrpPrice / 2
    document.getElementById('ppsrpTotal').value = "PP "+ (srp) + " + " + "SRP "+ (srp);

});




