// script.js

const convertButton = document.getElementById("convert-button");
const textInput = document.getElementById("text-input");
const videoOutput = document.getElementById("video-output");
const languageSelect = document.getElementById("language-select");

convertButton.addEventListener("click", () => {
    const text = textInput.value;
    const lang = languageSelect.value;

    // Send a request to the Python script on the server
    fetch('http://127.0.0.1:5000/convert', {
        method: 'POST',
        body: JSON.stringify({ text, lang }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.blob())
    .then(blob => {
        const videoURL = URL.createObjectURL(blob);
        videoOutput.src = videoURL;
    });
});
