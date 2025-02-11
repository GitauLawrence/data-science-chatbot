const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
let typingIndicator = null; // Global variable to hold the typing indicator

// Function to add a message to the chat history
function addMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(`${sender}-message`);

    // Add avatar for bot messages only
    if (sender === 'bot') {
        const avatarDiv = document.createElement('div');
        avatarDiv.classList.add('bot-avatar-container'); // Add a class for styling
        avatarDiv.innerHTML = `<img src="avatar.png" alt="Bot Avatar" class="bot-avatar">`; // Use the image file
        messageDiv.appendChild(avatarDiv);
    } else if (sender === 'user') {  // Add user avatar
        const avatarDiv = document.createElement('div');
        avatarDiv.classList.add('user-avatar-container');
        // Use a different image/SVG for the user
        avatarDiv.innerHTML = `<img src="user-avatar.png" alt="User Avatar" class="user-avatar">`;
        messageDiv.appendChild(avatarDiv);
    }

    messageDiv.innerHTML += `<p>${message}</p>`; // Use innerHTML to allow for HTML tags

    chatHistory.appendChild(messageDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to bottom
}

//Function to show typing indicator
function showTypingIndicator() {
    // Only add if it doesn't exist
    if (!typingIndicator) {
        typingIndicator = document.createElement('div');
        typingIndicator.classList.add('typing-indicator');
        typingIndicator.innerHTML = '<span></span><span></span><span></span>';
        chatHistory.appendChild(typingIndicator);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
}

// Function to hide typing indicator
function hideTypingIndicator() {
    if (typingIndicator) {
        chatHistory.removeChild(typingIndicator);
        typingIndicator = null; // Reset the variable
    }
}

// Function to create and display quick reply buttons
function displayQuickReplies(buttons) {
  const quickRepliesDiv = document.createElement('div');
  quickRepliesDiv.classList.add('quick-replies');
  buttons.forEach(button => {
    const buttonElement = document.createElement('button');
    buttonElement.textContent = button.title;
    buttonElement.addEventListener('click', () => {
        // Send the payload as the user message
        sendMessageToRasa(button.payload);
        //Remove the quick replies after one is clicked
        quickRepliesDiv.remove();

    });
    quickRepliesDiv.appendChild(buttonElement);
  });

  chatHistory.appendChild(quickRepliesDiv);
  chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the bottom

}


// Function to send a message to the Rasa server
async function sendMessageToRasa(message) {
    const rasa_url = 'http://localhost:5005/webhooks/rest/webhook'; // Your Rasa server URL

    try {
        const response = await fetch(rasa_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                sender: 'user', // Use a consistent sender ID
                message: message,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error('Error sending message to Rasa:', error);
        addMessage('bot', 'Error: Could not connect to the Rasa server.');
        return [];  // Return an empty array on error
    }
}

// Event listener for the send button
sendButton.addEventListener('click', async () => { // Use async here
    const message = userInput.value.trim();
    if (message) {
        addMessage('user', message);
        userInput.value = '';
        showTypingIndicator(); // Show typing indicator

        const rasaResponse = await sendMessageToRasa(message);  // Await the response

        hideTypingIndicator(); // Hide typing indicator

        if (rasaResponse && rasaResponse.length > 0) {
            rasaResponse.forEach(response => {
                if(response && response.text){
                    addMessage('bot', response.text);
                }
                 // Check for quick replies (buttons)
                if (response.buttons) {
                    displayQuickReplies(response.buttons);
                }
            });
        }
    }
});

// Event listener for pressing Enter in the input field
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendButton.click(); // Simulate a button click
        event.preventDefault(); // Prevent default behavior
    }
});