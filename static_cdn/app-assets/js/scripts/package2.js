var pprpQ = document.getElementById('pprp_quantity').value;
var pprpQQ = 1;
pprpPrice = parseInt(pprpQ) * parseInt(pprpQQ)
rp = pprpPrice / 2
document.getElementById('pprpPrice').value = "PP "+ rp  + " (50%)" + " + " + "RP "+ rp  + " (50%)";
document.getElementById('pprpTotal').value = "PP "+ (rp + (rp * 0.10))  + " + " + "RP "+ (rp + (rp * 0.10));

$('.pprp_c').on('change input', function(){

    var pprpQ = document.getElementById('pprp_quantity').value;
    var pprpQQ = 1;
    pprpPrice = parseInt(pprpQ) * parseInt(pprpQQ)
    rp = pprpPrice / 2
    document.getElementById('pprpPrice').value = "PP "+ rp  + " (50%)" + " + " + "RP "+ rp  + " (50%)";
    document.getElementById('pprpTotal').value = "PP "+ (rp + (rp * 0.10))  + " + " + "RP "+ (rp + (rp * 0.10));
});




