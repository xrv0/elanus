const websocketConnection = new WebSocket("ws://" + window.location.hostname + ":3000");
const videoStream = document.getElementById("video-stream");
const videoStreamPort = 8081;

const fired = {};
const commands = {
    ArrowUp: "forward",
    ArrowDown: "backward",
    ArrowLeft: "left",
    ArrowRight: "right"
}

document.querySelectorAll(".control-button").forEach((button) => {
    button.onmousedown = () => {
        const key = button.id;
        if(!fired[key]) {
            if(key in commands) {
                fired[key] = true;
                sendCommand(commands[key]);
            }
        }
    }
    button.onmouseup = () => {
        const key = button.id;
        if(!fired[key]) {
            if(key in commands) {
                fired[key] = true;
                sendCommand(commands[key]);
            }
        }
    }
})

document.addEventListener("keydown", (event) => {
    const key = event.key;

    if(!fired[key]) {
        if(key in commands) {
            fired[key] = true;
            sendCommand(commands[key]);
        }
    }
})

document.addEventListener("keyup", (event) => {
    const key = event.key;

    if(key in commands) {
        fired[event.key] = false;
        sendCommand("stop_" + commands[key]);
    }
})

function sendCommand(command) {
    websocketConnection.send("command:" + command);
}

websocketConnection.onopen = () => {
    websocketConnection.send("get:signal")
}

websocketConnection.onmessage = (event) => {
    console.log(event.data)
}

videoStream.src = "http://" + window.location.hostname + ":" + videoStreamPort;