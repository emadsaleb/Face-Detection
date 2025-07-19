
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import mediapipe as mp

st.title('Face Detection Application')

upload = st.file_uploader('Upload an Image...', type = ['png', 'jpeg', 'jpg'])

options = st.selectbox('Choose Face Detection Method:', ('OpenCV', 'Mediapipe'))
#using opencv for face detection
def detect_face_opencv(img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #model
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #CONVERT IMAGE TO GRAY IMAGE
    faces = face_cascade.detectMultiScale(gray) #detect many faces

    #draw box around face result from opencv model
    for x,y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+ w, y + h), (255, 20, 90), 3)
        return img




#detect faces using mediapipe
def detect_face_mediapipe(img):
    mp_face_detection = mp.solutions.face_detection #model for face detection
    mp_drawing = mp.solutions.drawing_utils
    
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

        results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.detections:
            for i in results.detections:
                mp_drawing.draw_detection(img, i)

    return img
        
if upload is not None:
    image = Image.open(upload) #read image
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if options == 'OpenCV':
        result = detect_face_opencv(image)

    elif options == 'Mediapipe':
        result = detect_face_mediapipe(image)

    st.image(result, use_container_width= True, channels = 'BGR')
