from flask import Flask
app = Flask(__name__)

# openssl req -x509 -nodes -days 36500 -newkey rsa:2048 -keyout key.pem -out cert.pem  -subj "/CN=sb_testserver.herokuapp.com"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))