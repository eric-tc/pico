document.getElementById("pathology_form").addEventListener("submit", function(event) {
    // Get the value of the 'data_intervento' field
    let dataIntervento = document.getElementById("generic-datepicker").value;
    let errorMessage = document.getElementById("error-message");

    // If the field is empty, show an error message and prevent form submission
    if (!dataIntervento.trim()) {
        //alert("Please provide a value for Data Intervento.");
        errorMessage.textContent = "Necessario fornire un valore per la Data Intervento.";
        errorMessage.style.display = "block";  // Show the error message
        event.preventDefault(); // Prevent form submission
    }
});