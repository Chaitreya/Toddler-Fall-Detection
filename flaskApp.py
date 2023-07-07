from flask import Flask, render_template, request
from fall_detector import FallDetector
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'videos'
DEFAULT_CONSEC_FRAMES = 10

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detect')
def detect():
    return render_template('fall.html')

@app.route('/access-webcam',methods=['GET'])
def access_webcam():
    fall_detector = FallDetector()
    fall_detector.begin()
    
    return render_template('fall.html')

@app.route('/run-video',methods=['POST'])
def run_video():
    if 'videoFile' in request.files:
        video_file = request.files['videoFile']
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
        video_file.save(video_path)

        fall_detector_script = 'fall_detector.py'
        command = f'python {fall_detector_script} --resize=640x480 --video="{video_path}"'

        subprocess.run(command, shell=True)
        os.remove(video_path)

        return render_template('fall.html')

    return "No video file uploaded."


if __name__ == '__main__':
    app.run(debug=True)