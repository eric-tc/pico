document.addEventListener('DOMContentLoaded', function() {
    


    var TmpSpecificDate=null;

  var selectedPathologyid="1";
  console.log("selectedPathology");

  
  const jsonTimeline= '{{timeline_pathology | safe}}';
  var timelineByName=null;
  
  console.log("jsonTimeline",jsonTimeline);
  if(jsonTimeline.length>0){

    timelineByName = JSON.parse(jsonTimeline);
  }


  function createDatePicker(){

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
      },
      beforeShowDay: customBeforeShowDay
      // Add more options as needed
  });
    
  }
  function changeDefaultDate(){

    console.log("CHANGE DEFAULT DATE");

    TmpSpecificDate= getSpecificDate(timelineByName[selectedPathologyid]);
    
    //Rimuove tutte le impostazioni di default. In questo modo il calendario si posiziona nella data
    //TmpSpecificDate
    $("#datepicker").datepicker("destroy");  
    createDatePicker();

  }

  function getSpecificDate(week_to_add) {
    // Function body

    var week_to_add_int= parseInt(week_to_add);

    console.log(week_to_add_int);

    if(isNaN(week_to_add_int)){

      console.log("NO WEEK TO ADD");
      week_to_add_int=0;
    }
   
    var daysToAdd = parseInt(week_to_add_int)*7;
    var check_if_default = "{{ check_if_default|lower }}";
    var specificDate;
    
    if(check_if_default==1){
      console.log("CHECK_IF_DEFAULT");
      
      var default_date="{{default_date}}"

      console.log("CHECK_IF_DEFAULT",default_date);
      console.log("CHECK_IF_DEFAULT",check_if_default);
      
      var dateComponent = default_date.split(" ")[0];
      var dateComponents = default_date.split("-");

      // Create Date object
      specificDate =  new Date(
        parseInt(dateComponents[0], 10),
        parseInt(dateComponents[1], 10) - 1, // JavaScript months are 0-indexed
        parseInt(dateComponents[2], 10)
        );
        console.log("Default date",default_date);

    }else{
      
      console.log("Current Date");
      specificDate=new Date();
    
    }
    
    console.log("specificDate",specificDate);
    console.log("specificDate daysToAdd",daysToAdd);
    specificDate.setDate(specificDate.getDate() + daysToAdd);

    console.log("specificDate",specificDate);
    return specificDate;
  }

  

  function customBeforeShowDay(d){
    var daysBefore= 3;
    var daysAfter=  4;
    

    if(timelineByName !=null ){
      //quando creo il primo controllo, i valori delle settimane da aggiungere sono dinamici in base
       //a quello che sceglie l'utente dal form
       
       console.log("SELECT DATE TIMELINE ",timelineByName[selectedPathologyid]);
           console.log("SELECT DATE TIMELINE ",timelineByName); 
           console.log("SELECT DATE TIMELINE ",selectedPathologyid);
       TmpSpecificDate= getSpecificDate(timelineByName[selectedPathologyid]);
    
    }else{

       TmpSpecificDate= getSpecificDate("{{week_to_add}}");

    }
   

    //Devo inizializzare il valore delle date con la data specifica dell'intervento altrimenti non funziona
    //Inizializzando la data con new Date() viene preso il mese di riferimento corrente e non quello futuro
    var beforeDate = new Date(TmpSpecificDate);
    var afterDate = new Date(TmpSpecificDate);      

    beforeDate.setDate(TmpSpecificDate.getDate() - daysBefore);
    afterDate.setDate(TmpSpecificDate.getDate() + daysAfter);
   
    
    // Check if the current date is within the specified range
    return [true, beforeDate <= d && d <= afterDate ? "calendar-highlight" : ""];      

  }

 

    $(function () {
        // Define the start and end dates
        // Initialize Datepicker

        if(timelineByName !=null ){
          
          //quando creo il primo controllo, i valori delle settimane da aggiungere sono dinamici in base
           //a quello che sceglie l'utente dal form 

           console.log("SELECT DATE TIMELINE ",timelineByName[selectedPathologyid]);
           console.log("SELECT DATE TIMELINE ",timelineByName); 
           console.log("SELECT DATE TIMELINE ",selectedPathologyid);
           TmpSpecificDate= getSpecificDate(timelineByName[selectedPathologyid]);
        
        }else{
    
           TmpSpecificDate= getSpecificDate("{{week_to_add}}");
    
        }

        createDatePicker();
       
    });
    $(function () {
    
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

});