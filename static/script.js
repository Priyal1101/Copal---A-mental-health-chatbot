// Get the HTML element where the response will be displayed
var responseElement = document.getElementById("response");

// Add an event listener to the form submit button
document.getElementById("chatbot-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the form from submitting
  var userInput = document.getElementById("user-input").value; // Get the user input
  document.getElementById("user-input").value = ""; // Clear the input field
  addMessage(userInput, "user"); // Add the user message to the chat
  // Send an AJAX request to the Flask app with the user input
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/chatbot");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function() {
    if (xhr.status === 200) {
      var response = JSON.parse(xhr.responseText).response; // Parse the response from JSON
      addMessage(response, "chatbot"); // Add the chatbot response to the chat
      responseElement.innerHTML = response; // Display the response in the HTML
    } else {
      console.log("Request failed. Returned status of " + xhr.status);
    }
  };
  xhr.send("user_input=" + userInput);
});

// Function to add a message to the chat
function addMessage(message, sender) {
  var messageElement = document.createElement("div");
  messageElement.classList.add("chatbot-message");
  if (sender === "user") {
    messageElement.innerHTML = "<p>" + message + "</p>";
  } else {
    messageElement.innerHTML = "<p><strong>Chatbot:</strong> " + message + "</p>";
  }
  document.getElementById("chatbot-messages").appendChild(messageElement);
}
