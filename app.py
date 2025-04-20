import os

from flask import Flask, render_template, request, send_file, redirect, url_for, abort

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    files = os.listdir('uploads')
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', message='no file selected')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', message='no file ')

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return index()


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # noinspection PyTypeChecker
    return send_file(file_path, as_attachment=True)


@app.route('/delete/<filename>', methods=['GET'])
def delete_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(file_path)
        return redirect(url_for('index'))
    except Exception as e:
        return render_template('index.html', message=e)
    

@app.route('/view/<filename>', methods=['GET'])
def view_file(filename):
    # noinspection PyBroadException
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            # noinspection PyTypeChecker
            return send_file(file_path)
        else:
            abort(404)
            
    except Exception as e:
        return index()


//manikanta
//mani
//new
//nam
//km
//mk
//as

if __name__ == '__main__':
    app.run(debug=True)
