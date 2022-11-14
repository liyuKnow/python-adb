// Onclick of the button
document.querySelector("#pull_btn").onclick = function () {
    // Call python's random_python function
    eel.push_file()(function (number) {
        // Update the div with a random number returned by python
        document.querySelector("#devices_list").innerHTML = number;
    })
}

document.getElementById("push_btn").onclick(() => {
    document.getElementById("devices_list").innerHTML = "Push Is up"
});



document.querySelector("#push_btn").onclick = function () {
    eel.pull_file()(function (number) {
        document.querySelector("#devices_list").innerHTML = number;
    })
}