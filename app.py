import os
import asyncio
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import warnings

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')
warnings.filterwarnings("ignore", category=UserWarning, module="pyowm")

process = None
writer = None


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('start')
def start():
    global process, writer

    async def run_subprocess():
        global process, writer
        process = await asyncio.create_subprocess_exec(
            'python', 'run.py',
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )
        writer = process.stdin

        while True:
            line = await process.stdout.readline()
            if not line:
                break
            decoded = line.decode()
            print(f'[EMIT]: {decoded.strip()}')
            socketio.emit('output', decoded)

    def thread_target():
        asyncio.run(run_subprocess())

    threading.Thread(target=thread_target).start()


@socketio.on('input')
def receive_input(data):
    global writer
    if writer is not None:
        try:
            writer.write(data.encode())
        except Exception as e:
            print(f"[ERROR] Failed to write to process: {e}")


if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        allow_unsafe_werkzeug=True
    )
