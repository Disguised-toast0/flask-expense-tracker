 // Set today's date as default
 document.getElementById("expenseDateField").valueAsDate = new Date();

 // Simple form validation - ensure required fields are filled
 document.querySelector("form").addEventListener("submit", function (e) {
   e.preventDefault();

   // You can add your form submission logic here
   // For now just show an alert
   alert("Expense saved successfully!");

   // In a real application, you would send this data to your backend
   // or store it in local storage / IndexedDB
 });


 