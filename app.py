#importing the required libraries
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils.file_reader import read_file
from summarizer.abstractive import abstractive_summary
from summarizer.keypoints import extract_keypoints

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder to save uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    keypoints = []

    # If user submits the form
    if request.method == 'POST':
        input_text = request.form.get('input_text')  # Get text input from UI
        uploaded_file = request.files.get('file')  # Get uploaded file from UI

        # If a file is uploaded, save it and read its content
        if uploaded_file and uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)
            input_text = read_file(filepath)  # Read file content

        # If there is input text (either from form or file), generate summary and key points
        if input_text:
            summary = abstractive_summary(input_text)  # Create summary by using abstractive.py
            keypoints = extract_keypoints(summary)  # Get key points by using keypoints.py

    return render_template('index.html', summary=summary, keypoints=keypoints)  # Show result inthe UI

if __name__ == '__main__':
    app.run(debug=True)  # Run the app
