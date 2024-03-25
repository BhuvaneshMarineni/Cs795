// popup.js

document.addEventListener('DOMContentLoaded', function () {
  chrome.storage.local.get('loggedData', function (result) {
    const loggedData = result.loggedData || [];
    const logList = document.getElementById('logList');
    
    logList.innerHTML = '';

    loggedData.forEach(function (entry) {
      const li = document.createElement('li');
      li.textContent = entry.message + ' - ' + entry.time + ' - ' + entry.url;
      logList.appendChild(li);
    });
  });
});
