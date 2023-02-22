# Text recognition from webcam using OpenCV and Tesseract OCR

This project demonstrates how to perform real-time text recognition from a webcam using OpenCV and Tesseract OCR in Python. The captured images from the webcam are processed using OpenCV to extract the text regions, and then the Tesseract OCR engine is used to recognize the text in the regions.

## Dependencies

- Python 3
- OpenCV 4
- Tesseract OCR
- pytesseract module
- imutils module

To install OpenCV, you can use pip:

`pip3 install opencv-python-headless`


Tesseract OCR can be installed from the official website:

- [Tesseract OCR Installation](https://tesseract-ocr.github.io/tessdoc/Installation.html)

On macOS:

`brew install tesseract`

[Download language model](https://github.com/tesseract-ocr/tessdata_best/raw/main/ces.traineddata)

`export TESSDATA_PREFIX=path-to-language-model`

Change the path-to-language-model with real folder.



You can install the pytesseract and imutils modules using pip:

``
pip3 install pytesseract
pip3 install imutils
``


## Usage

To run the application, run the following command:

`python3 main.py`


When the application starts, it will capture images from the webcam and display the recognized text on the screen.

## Configuration

You can configure the language of the recognized text by modifying the `lang` parameter in the `image_to_string` function in the `text_recognition.py` file. By default, it is set to `'ces'` for English.

You can also configure the font used for displaying the text by modifying the `font_path` variable in the `text_recognition.py` file. By default, it is set to `'arial.ttf'`.

## Credits

This project is based on the following tutorial:

- [Real-time OCR in Python with Tesseract and OpenCV](https://www.pyimagesearch.com/2018/09/17/real-time-ocr-in-python-with-tesseract-and-opencv/)
