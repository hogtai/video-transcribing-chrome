document.getElementById('start-btn').addEventListener('click', function() {
    // Extract the audio from the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.tabCapture.capture({ audio: true, video: false }, function(stream) {
        console.log(stream);
        // Convert the audio to text using the Google Speech Recognition API
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-US';
        recognition.onresult = function(event) {
          var interim_transcript = '';
          var final_transcript = '';
          for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
              final_transcript += event.results[i][0].transcript;
            } else {
              interim_transcript += event.results[i][0].transcript;
            }
          }
          // Display the transcribed text in the popup UI
          document.getElementById('transcription').innerHTML = final_transcript;
        };
        recognition.start();
      });
    });
  });
