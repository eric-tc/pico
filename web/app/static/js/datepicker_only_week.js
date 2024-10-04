//Datepicker: Input parameter week_to_add. Need to be defined before calling this file

document.addEventListener('DOMContentLoaded', function () {


    function createDatePicker() {

        $("#datepicker").datepicker({
            dateFormat: 'dd-mm-yy', // Set the date format
            changeMonth: true,
            defaultDate: TmpSpecificDate,
            changeYear: true,
            showOn: "button", // Show the Datepicker when clicking the button
            buttonText: "",
            beforeShow: function (input, inst) {
                // Prevent the calendar from showing on focus
                if (!$("#datepicker").prop("disabled")) {
                    $.datepicker._clearDate(input);
                }
                
                //DataIntervento
                TmpSpecificDate= new Date(DataIntervento);
                
                var week_to_add_int = parseInt(week_to_add);
                
                //Altirmenti tutte le volte che si apre il calendario la data viene aggiornata delle week_to_add
                TmpSpecificDate.setDate(TmpSpecificDate.getDate() + week_to_add_int * 7);
                
                //Aggiorna la data corrente di dove sarà mostrato il calendario
                $(input).datepicker('setDate', TmpSpecificDate);
                console.log("beforeShow", TmpSpecificDate);
                
            },
            beforeShowDay: customBeforeShowDay
            // Add more options as needed
        });

    }



    function customBeforeShowDay(d) {
        
        console.log("DataIntervento", DataIntervento);
        console.log("TmpSpecificDate", TmpSpecificDate);
        
        var daysBefore = 3;
        var daysAfter = 4;

        //Devo inizializzare il valore delle date con la data specifica dell'intervento altrimenti non funziona
        //Inizializzando la data con new Date() viene preso il mese di riferimento corrente e non quello futuro
        var beforeDate = new Date(TmpSpecificDate);
        var afterDate = new Date(TmpSpecificDate);

        beforeDate.setDate(TmpSpecificDate.getDate() - daysBefore);
        afterDate.setDate(TmpSpecificDate.getDate() + daysAfter);


        // Check if the current date is within the specified range
        return [true, beforeDate <= d && d <= afterDate ? "calendar-highlight" : ""];

    }

    //INIT //DataIntervento non deve mai cambiare altrimenti ogni volta che si apre il calendario la data cambia
    // valore DataIntervento settato nel generic_datepicker.js
    var TmpSpecificDate = new Date(DataIntervento);

    console.log("DataIntervento", TmpSpecificDate);
     //Week to add variable che deve essere definita prima di richiamare questo file
    console.log("SELECT DATE TIMELINE ", week_to_add);
  
    createDatePicker();



    $("#timepicker").timepicker({
        timeFormat: 'HH:mm',
        controlType: 'select',
        oneLine: true,
        showButtonPanel: true,
        showTimezone: false,
        showHour: true,
        showMinute: true,
        showSecond: false,
        showMillisec: false,
        showMicrosec: false,
    });


});