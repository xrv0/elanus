from flask import Flask

app = Flask(__name__,
            static_url_path='',
            static_folder='../frontend')


@app.route("/")
def index():
    return app.send_static_file("index.html")


def start():
    print("Starting flask static file server...")
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    start()