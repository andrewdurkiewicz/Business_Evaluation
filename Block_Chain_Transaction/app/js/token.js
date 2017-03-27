$(document).ready(function() {
var currentDeed;
$("#deployDeed button").click(function() {
    var prop_addr = $('#deployDeed input').val();
    Deed.deploy([prop_addr]).then(function(deployedDeed) {
      currentDeed = deployedDeed;
      $("#deployDeed .result").append("<br>D33D deployed with identifier: " + deployedDeed.address);
    });
});
$("#useDeed button").click(function() {
    var address = $('#useDeed input').val();
    currentDeed = new EmbarkJS.Contract({
      abi: Deed.abi,
      address: address
    });
});
web3.eth.getAccounts(function(err, accounts) {
    $('#queryBalance input').val(accounts[0]);
  });
$('#queryBalance button').click(function() {
    var address = $('#queryBalance input').val();
    currentDeed.getOwner().then(function(balance) {
      $('#queryBalance .result').html(balance.toString());
    });
  });
$('#transfer button').click(function() {
    var address = $('#transfer .address').val();
    // var string = $('#transfer .string').val();
    currentDeed.newOwner(address).then(function() {
      $('#transfer .result').html('Done!');
    });;
  });
$('#accountDisplay button').click(function() {
      var accounts = web3.eth.accounts
      // var string = $('#transfer .string').val();
      // currentDeed.newOwner(address).then(function() {
        $('#transfer .result').html(accounts[0].toString());
      // });;
    });

});
