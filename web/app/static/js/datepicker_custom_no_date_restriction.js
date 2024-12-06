document.addEventListener('DOMContentLoaded', function () {


  $("#generic-datepicker-no-res").datepicker({
      dateFormat: 'dd-mm-yy', // Set the date format
      showOn: "button", // Show the Datepicker when clicking the button
      buttonText: "",
      beforeShow: function (input, inst) {
          // Prevent the calendar from showing on focus
          console.log("beforeShow");
      },
      onSelect: function(dateText) {

      }
      // Add more options as needed
  });

});