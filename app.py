import os
from flask import Flask, render_template, request, send_from_directory
from predictor import check


author = 'TEAM DELTA'

app = Flask(__name__, static_folder="static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template('upload.html')


@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(APP_ROOT, 'images'), filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    results = []
    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)

        status, contours, confidence = check(filename)
        results.append({'filename': filename, 'status': status, 'contours': contours, 'confidence': confidence})

    return render_template('complete.html', results=results)

if __name__ == "__main__":
    app.run(port=4555, debug=True)
