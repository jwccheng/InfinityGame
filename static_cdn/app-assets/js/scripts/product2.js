document.getElementById('pprp_quantity_a').value = 1;
var pprpQ = document.getElementById('pprp_quantity').value;
var mem = document.getElementById('pprp_quantity_q').value;
if (mem == "OUTLET"){
    var pprpQQ = 10;
}
else{
    var pprpQQ = 1;
}
var pprpQA = document.getElementById('pprp_quantity_a').value;
pprpPrice = parseInt(pprpQ) * parseInt(pprpQQ) * parseInt(pprpQA)
rp = pprpPrice / 2
document.getElementById('pprpTotal').value = "PP "+ (rp)  + " + " + "RP "+ (rp);

$('.pprp_c').on('change input', function(){

    var pprpQ = document.getElementById('pprp_quantity').value;
    var mem = document.getElementById('pprp_quantity_q').value;
    if (mem == "OUTLET"){
        var pprpQQ = 10;
    }
    else{
        var pprpQQ = 1;
    }
    var pprpQA = document.getElementById('pprp_quantity_a').value;
    pprpPrice = parseInt(pprpQ) * parseInt(pprpQQ) * parseInt(pprpQA)
    rp = pprpPrice / 2
    document.getElementById('pprpTotal').value = "PP "+ (rp)  + " + " + "RP "+ (rp);
});




