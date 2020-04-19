const websocketConnection = new WebSocket("ws://" + window.location.hostname + ":3000");
const videoStream = document.getElementById("video-stream");
const videoStreamPort = 8081;

Chart.platform.disableCSSInjection = true;

videoStream.src = "http://" + window.location.hostname + ":" + videoStreamPort;

class Main {
    fired = {};
    commands = {
        ArrowUp: "forward",
        ArrowDown: "backward",
        ArrowLeft: "left",
        ArrowRight: "right"
    }

    constructor() {
        this.logger = new Logger();
        document.querySelectorAll(".control-button").forEach((button) => {
            button.onmousedown = () => {
                const key = button.id;
                if(!this.fired[key]) {
                    if(key in this.commands) {
                        this.fired[key] = true;
                        this.sendCommand(this.commands[key]);
                    }
                }
            }
            button.onmouseup = () => {
                const key = button.id;
                if(this.fired[key]) {
                    if(key in this.commands) {
                        this.fired[key] = false;
                        this.sendCommand("stop_" + this.commands[key]);
                    }
                }
            }
        })

        document.addEventListener("keydown", (event) => {
            const key = event.key;

            if(!this.fired[key]) {
                if(key in this.commands) {
                    this.fired[key] = true;
                    console.log("yeah")
                    this.sendCommand(this.commands[key]);
                }
            }
        })

        document.addEventListener("keyup", (event) => {
            const key = event.key;

            if(key in this.commands) {
                this.fired[event.key] = false;
                this.sendCommand("stop_" + this.commands[key]);
            }
        })

        websocketConnection.onmessage = this.handleMessage;

        this.signalLevelDisplay = document.getElementById("signal-level")
        this.signalQualityDisplay = document.getElementById("signal-quality")
    }

    handleMessage = (event) => {
        let message = event.data;
        message.split(" ").forEach(arg => {
            if(arg.includes("=")) {
                let key = arg.split("=")[0]
                let value = arg.split("=")[1]

                if(key === "level") {
                    this.signalLevelDisplay.innerText = "Signal Level: " + value
                }else if(key == "Quality") {
                    this.signalQualityDisplay.innerText = "Signal Quality: " + value
                }
            }
        })
    }

    sendCommand(command) {
        this.logger.log("Send command:" + command)
        websocketConnection.send("command:" + command);
    }
}

class Logger {
    constructor() {
        this.logMessages = new Array()
        this.console = document.getElementById("debug-console")
    }

    log(message) {
        this.console.innerText = ""

        let date = new Date().toLocaleTimeString()
        this.logMessages.push(`[${date}]: ${message}`)
        this.logMessages.forEach((message) => {
            this.console.innerText += message + "\n"
        })

        if(Math.abs(this.console.clientHeight - window.outerHeight) < 100) {
            this.console.innerText = ""
            this.logMessages = new Array()
            this.log("Cleaned log")
        }
    }
}

new Main();