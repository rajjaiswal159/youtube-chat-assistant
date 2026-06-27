const processBtn = document.getElementById("processBtn");
const sendBtn = document.getElementById("sendBtn");
const questionInput = document.getElementById("question");
const result = document.getElementById("result");

// Process Video
processBtn.addEventListener("click", async () => {

    result.innerHTML = "<p>Processing video...</p>";

    try {

        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        const response = await fetch("http://127.0.0.1:8000/process", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                video_url: tab.url
            })

        });

        const data = await response.json();

        result.innerHTML = `<p>${data.message}</p>`;

    }

    catch (error) {

        result.innerHTML = "<p>Failed to process video.</p>";

    }

});


// Chat
sendBtn.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question) return;

    result.innerHTML += `<p><b>You:</b> ${question}</p>`;

    questionInput.value = "";

    result.innerHTML += `<p><b>AI:</b> Thinking...</p>`;

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        result.lastElementChild.innerHTML =
            `<b>AI:</b> ${data.answer}`;

    }

    catch (error) {

        result.lastElementChild.innerHTML =
            "<b>AI:</b> Error occurred.";

    }

});