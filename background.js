// Background script to handle message passing
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    console.log("Received message in background script:", request);
    if (request.action === "logWordTime") {
        console.log("Word:", request.word, "Time:", request.time);
    }
});
