var ppsrpQ = document.getElementById('ppsrp_quantity').value;
var ppsrpQQ = 1;
ppsrpPrice = parseInt(ppsrpQ) * parseInt(ppsrpQQ)
srp = ppsrpPrice / 2
document.getElementById('ppsrpPrice').value = "PP "+ srp  + " (50%)" + " + " + "SRP "+ srp  + " (50%)";
document.getElementById('ppsrpTotal').value = "PP "+ (srp + (srp * 0.10))  + " + " + "SRP "+ (srp + (srp * 0.10));

$('.ppsrp_c').on('change input', function(){

	var ppsrpQ = document.getElementById('ppsrp_quantity').value;
    var ppsrpQQ = 1;
    ppsrpPrice = parseInt(ppsrpQ) * parseInt(ppsrpQQ)
    srp = ppsrpPrice / 2
    document.getElementById('ppsrpPrice').value = "PP "+ srp  + " (50%)" + " + " + "SRP "+ srp  + " (50%)";
    document.getElementById('ppsrpTotal').value = "PP "+ (srp + (srp * 0.10))  + " + " + "SRP "+ (srp + (srp * 0.10));

});




