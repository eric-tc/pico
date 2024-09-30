$(document).ready(function() {
    $("#datepicker").datepicker({
        dateFormat: 'dd-mm-yy',
        changeMonth: true,
        defaultDate: Date(),
        changeYear: true,
        showOn: "button",
        buttonText: ""
    });
});