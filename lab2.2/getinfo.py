from flask import Flask
import random

app = Flask(__name__)
names = dict()

@app.route("/")
def index():
    return """
        Hi, bro!<br>
        Use <b>config</b> for get all host names.<br>
        Use <b>config/hostname</b> for get all ip addresses in host.
    """

@app.route("/config")
def config():
    return "<br>".join(names.keys())

@app.route("/config/<host>")
def hostname(host):
    return "<br>".join(names[host])

if __name__ == "__main__":
    # TODO Lab 1.6
    # Вместо данных из лабы 1.6 генерируется случайный набор данных
    for i in range(0, 10):
        ips = set()
        for j in range(0, 10):
            ips.add(f"{random.randint(1, 128)}.{random.randint(1, 128)}.{random.randint(1, 128)}.{random.randint(1, 128)}")
        names[f"host_{i}"] = ips
    app.run(port=7777, debug=True)
