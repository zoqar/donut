import numpy as np
from flask import Flask, render_template_string

app = Flask(__name__)

A, B = 0, 0

def render_frame(A, B):
    output = [[' ' for _ in range(80)] for _ in range(22)]
    zbuffer = [[0 for _ in range(80)] for _ in range(22)]
    cos_A = np.cos(A)
    sin_A = np.sin(A)
    cos_B = np.cos(B)
    sin_B = np.sin(B)

    for j in np.arange(0, 6.28, 0.07):
        for i in np.arange(0, 6.28, 0.02):
            cos_i = np.cos(i)
            sin_i = np.sin(i)
            cos_j = np.cos(j)
            sin_j = np.sin(j)
            
            circle_x = cos_j + 2
            circle_y = sin_i * circle_x * cos_A + sin_j * sin_A
            z = 1 / (sin_i * circle_x * sin_A - sin_j * cos_A + 5)
            x = int(40 + 30 * z * (cos_i * circle_x * cos_B - circle_y * sin_B))
            y = int(12 + 15 * z * (cos_i * circle_x * sin_B + circle_y * cos_B))
            if 0 <= x < 80 and 0 <= y < 22:
                if z > zbuffer[y][x]:
                    zbuffer[y][x] = z
                    luminance_index = int(8 * ((cos_j * cos_i * sin_B - cos_j * sin_i * sin_A - sin_j * cos_A * cos_i * sin_B - sin_j * sin_A * sin_i * cos_B) + 5))
                    luminance_index = max(0, min(11, luminance_index))  # Ensure the index is within range
                    output[y][x] = ".,-~:;=!*#$@"[luminance_index]

    frame = "\n".join("".join(row) for row in output)
    return frame

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>3D Donut</title>
            <style>
                body { font-family: monospace; white-space: pre; margin: 0; padding: 20px; }
                pre { line-height: 1; }
            </style>
        </head>
        <body>
            <pre id="donut"></pre>
            <script>
                var A = 0;
                var B = 0;
                function updateDonut() {
                    fetch('/frame').then(response => response.text()).then(data => {
                        document.getElementById('donut').innerText = data;
                    });
                    A += 0.1;  // Increase the increment for faster rotation
                    B += 0.05;  // Increase the increment for faster rotation
                }
                setInterval(updateDonut, 10);  // Reduce the delay to 10 milliseconds for smoother updates
                updateDonut();  // Initial call to start the loop
            </script>
        </body>
        </html>
    ''')

@app.route('/frame')
def frame():
    global A, B
    frame_data = render_frame(A, B)
    A += 0.1  # Increase the increment for faster rotation
    B += 0.05  # Increase the increment for faster rotation
    return frame_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
