﻿# Toddler Fall Detection

This repository contains a Toddler Fall Detection System implemented using Flask, OpenPifPaf for pose estimation, and an LSTM deep neural network. The system aims to detect and alert caregivers in the event of a fall by analyzing the toddler's body pose. We have created a Flask App in which you can either use your own camera to detect falls in real time or you can upload a video.

## Classes

The system classifies the toddler's body pose into the following four classes:

1. **Normal**: This class represents a normal body pose where no fall is detected.

2. **No Fall**: This class indicates that a potential fall was not detected, and detects the toddler's body pose.

3. **Fall Warning**: This class indicates a fall warning situation where the toddler's body pose suggests an imminent fall but hasn't fallen yet.

4. **Fall**: This class indicates that a fall has been detected based on the toddler's body pose.

## Installation

1. Clone this repository:
```bash
https://github.com/Chaitreya/Toddler-Fall-Detection.git
```

2. Change to the project directory:
```bash
cd Toddler-Fall-Detection
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application by running the following command:
```bash
python flaskApp.py
```

2. Access the application by opening a web browser and navigating to http://localhost:5000.

3. Follow the instructions provided on the web interface to upload a video file or stream video from a connected camera.
  
4. The system will process the video frames, perform pose estimation using OpenPifPaf, and analyze the toddler's body pose using the LSTM deep neural network.
