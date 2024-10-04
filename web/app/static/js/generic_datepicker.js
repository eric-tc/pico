document.addEventListener('DOMContentLoaded', function () {


    $("#generic-datepicker").datepicker({
        dateFormat: 'dd-mm-yy', // Set the date format
        showOn: "button", // Show the Datepicker when clicking the button
        buttonText: "",
        beforeShow: function (input, inst) {
            // Prevent the calendar from showing on focus
            console.log("beforeShow");
        },
        onSelect: function(dateText) {
            console.log("onSelect", dateText);

            const [day, month, year] = dateText.split('-');

            DataIntervento= new Date(year, month - 1, day);
            console.log("onSelect", DataIntervento);
        }
        // Add more options as needed
    });

});