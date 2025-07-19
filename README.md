

Face Detection Application

A simple and interactive web-based face detection app built with Streamlit, using both OpenCV and MediaPipe as face detection options. Upload an image and detect faces with just a few clicks!

 Features

* ✅ Upload an image (`.jpg`, `.jpeg`, `.png`)
* ✅ Select face detection method: `OpenCV` or `MediaPipe`
* ✅ View the image with detected faces highlighted
* ✅ Real-time processing directly in the browser using Streamlit

 Requirements

Install dependencies using `pip`:

bash
pip install -r requirements.txt


requirements.txt

txt
opencv-python
numpy
streamlit
Pillow
mediapipe



 How It Works

 Face Detection Methods

 1. OpenCV

* Uses Haar Cascade Classifier (`haarcascade_frontalface_default.xml`)
* Detects faces in grayscale images
* Draws rectangles around detected faces

 2. MediaPipe

* Uses `mediapipe.solutions.face_detection`
* Detects faces with a more modern model
* Annotates faces using MediaPipe’s drawing utilities


 Usage

Run the Streamlit app using:`bash
streamlit run face_detection_app.py


Then open the browser at the displayed URL (usually `http://localhost:8501/`).


 


 Author

Emad Salib Fahmy Ibrahim 
🔗 [LinkedIn](https://www.linkedin.com/in/emad-salib-ab4968248)
📧 [emad@example.com](mailto:emad@example.com)





