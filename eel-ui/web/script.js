async function getGreetingFromPython() {
    getElementById("title").innerText = await eel.greet_html()();
}

document.getElementById('btn').addEventListener('click', () => {
    getGreetingFromPython()
})