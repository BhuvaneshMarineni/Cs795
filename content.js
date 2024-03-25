// Content script to listen for keypress events and log word timings
document.addEventListener("keydown", function(event) {
    // Check if the key pressed is a space (indicating the end of a word)
    if (event.key === " ") {
        let currentTime = new Date().getTime();
        let word = getPreviousWord();
        console.log("Sending message from content script:", { action: "logWordTime", word: word, time: currentTime });
        chrome.runtime.sendMessage({ action: "logWordTime", word: word, time: currentTime });
    }
});

// Function to get the word preceding the cursor position
function getPreviousWord() {
    let selection = window.getSelection();
    let range = selection.getRangeAt(0);
    range.setStart(range.startContainer, 0);
    let precedingText = range.toString().split(/\s+/).pop();
    return precedingText.trim();
}
