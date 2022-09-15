from flask import Flask, request, render_template, jsonify
from Decoding import decode
from prediction import Predict

app = Flask(__name__)

class Classfier_App:
    def __init__(self):
        self.file_name = "Test_image.jpg"
        self.Classifier = Predict(self.file_name)


@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predictRoute():
    img_str = request.json['image']
    decode.decodeImage(img_str, obj.file_name)
    results = obj.Classifier.predict_dogcat()
    return jsonify(results)


if __name__ == "__main__":
    obj = Classfier_App()
    app.run(host='127.0.0.1', port=8000, debug=True)
