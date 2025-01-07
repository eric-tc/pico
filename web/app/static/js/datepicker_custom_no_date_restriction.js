document.addEventListener('DOMContentLoaded', function () {


  $("#generic-datepicker-no-res").datepicker({
      dateFormat: 'dd-mm-yy', // Set the date format
      showOn: "button", // Show the Datepicker when clicking the button
      buttonText: "",
      changeYear: true, // Show a dropdown to control year
      yearRange: "1900:2100",
      changeMonth: true,
      beforeShow: function (input, inst) {
          // Prevent the calendar from showing on focus
          console.log("beforeShow");
      },
      onSelect: function(dateText) {

      }
      // Add more options as needed
  });

});