const socket = io();

const term = new Terminal({
    cols: 180,
    rows: 30,
    scrollback: 1000,
});
term.open(document.getElementById('terminal'));
term.focus();

let inputBuffer = "";

function startApp() {
    term.clear();
    inputBuffer = "";
    socket.emit("start");

    setTimeout(() => {
        term.focus();
    }, 50);
}

term.onData(data => {
    if (data === "\r") {
        term.write("\r\n");
        socket.emit("input", inputBuffer + "\n");
        inputBuffer = "";
    } else if (data === "\u007F") {
        // Backspace
        if (inputBuffer.length > 0) {
            inputBuffer = inputBuffer.slice(0, -1);
            term.write("\b \b");
        }
    } else {
        inputBuffer += data;
        term.write(data);
    }
});

socket.on("output", data => {
    term.write(data);
    term.scrollToBottom();
});
