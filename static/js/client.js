const socket = io();
const term = new Terminal({ scrollback: 1000 });
term.open(document.getElementById('terminal'));


let inputBuffer = "";
let isActive = false;


function startApp() {
    term.clear();
    socket.emit("start");
    term.focus();
    isActive = true;

    setTimeout(() => {
        term.focus();
    }, 50);
}


term.onData(data => {
    if (!isActive) return;

    if (data === "\r") {
        socket.emit("input", inputBuffer + "\n");
        inputBuffer = "";
    } else if (data === "\u007F") {
        if (inputBuffer.length > 0) {
            inputBuffer = inputBuffer.slice(0, -1);
            term.write('\b \b');
        }
    } else {
        inputBuffer += data;
        term.write(data);
    }
});


socket.on("output", data => {
    term.write(data, () => {
        term.scrollToBottom();

        if (data.includes("Program is completed!")) {
            isActive = false;
        }
    });
});
