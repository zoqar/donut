import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Define environment variables for testing
FOREGROUND_COLOR = os.getenv('FOREGROUND_COLOR', 'red')  # Default to red
BACKGROUND_COLOR = os.getenv('BACKGROUND_COLOR', 'black')  # Default to black

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Color Test</title>
            <style>
                body { font-family: monospace; white-space: pre; margin: 0; padding: 20px; }
                pre { line-height: 1; }
                .colored-text {
                    color: {{ foreground_color }};
                    background-color: {{ background_color }};
                }
            </style>
        </head>
        <body>
            <pre class="colored-text">This text should be colored</pre>
        </body>
        </html>
    ''', foreground_color=FOREGROUND_COLOR, background_color=BACKGROUND_COLOR)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
