import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

class Predict:
    def __init__(self, file_name):
        self.file_name = file_name

    def predict_dogcat(self):
        model = tf.keras.models.load_model('eldos.h5')
        test_img = image.load_img(self.file_name, target_size=(64, 64))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)
        result = model.predict(test_img)

        if result[0][0] >= 0.5:
            prediction = 'dog'
        else:
            prediction = 'cat'

        return {"image" : prediction}
