from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>DevOps Made Simple</title>
        <style>
          body {
            background-color: lightyellow;
            font-family: Arial, sans-serif;
            padding: 50px;
            font-size: 24px;
          }
        </style>
      </head>
      <body>
        <h1>Welcome to Devops Made Simple</h1>
        <p>version-2</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
