$(document).ready(function(){
    $( "#birthpicker" ).datepicker();
    $( "#datepicker" ).datepicker();
    $("#timepicker").timepicker({ 'timeFormat': 'H:i' });
    $("#ssn").mask("999-999-999");

});