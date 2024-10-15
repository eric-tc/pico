// Datepicker event for the datepicker in the form
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