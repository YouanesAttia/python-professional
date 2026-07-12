from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": "Hello from Flask", "status": "running"}

if __name__ == "__main__":
    app.run(debug=True)