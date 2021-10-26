//Change Package Listing Total
document.getElementById('w_quantity').value = 100;

var selV = document.getElementById('wSelect').value;
    var fee = 0
    var msg = " [5% FEE]"
    if (selV === "BANK-TRANSFER") {
        fee = 0.05
        msg = " [5% FEE]"
      }
    if (selV === "USDT-WALLET") {
        fee = 0.03
        msg = " [3% FEE]"
      }

var wQ = document.getElementById('w_quantity').value;
wAmount = parseInt(wQ);
document.getElementById('wTotal').value = (wAmount - (wAmount * fee)) + msg;

$('.withdrawal_p').on('change input ', function(){

    var selV = document.getElementById('wSelect').value;
    var fee = 0
    var msg = " [5% FEE]"
    if (selV === "BANK-TRANSFER") {
        fee = 0.05
        msg = " [5% FEE]"
      }
    if (selV === "USDT-WALLET") {
        fee = 0.03
        msg = " [3% FEE]"
      }
    
	var wQ = document.getElementById('w_quantity').value;
    wAmount = parseInt(wQ)
    document.getElementById('wTotal').value = (wAmount - (wAmount * fee)) + msg;

});
