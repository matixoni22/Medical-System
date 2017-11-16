$(document).ready(function(){
    $( "#birthpicker" ).datepicker();
    $( "#datepicker" ).datepicker();
    $("#timepicker").timepicker({ 'timeFormat': 'H:i' });
    $("#ssn").mask("999-999-999");

    
});

function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
};