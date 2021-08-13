from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/admin/Pictures'


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['myfile']
        filename = secure_filename(f.fileanme)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))


@app.route('uploaded/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
