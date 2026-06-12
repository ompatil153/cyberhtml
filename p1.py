from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Python Web Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
                padding: 50px;
            }

            img {
                width: 400px;
                border: 3px solid black;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Python Web Page</h1>
        <p>This page is generated using Flask.</p>

        <img src="https://via.placeholder.com/400x250.png?text=Python+Web+Page"
             alt="Sample Image">
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)