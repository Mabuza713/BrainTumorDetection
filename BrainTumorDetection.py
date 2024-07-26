import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
import configparser

class BrainTumorDetection:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        
        
        self.modelBin = load_model("BrainTumorBinary20.keras")
        self.modelCat = load_model("BrainTumorCategorical20.keras")
        self.size = int(config.get("General", "size"))
    
    def PrepareImage(self, image):
        image = cv2.imread(image)
        image = Image.fromarray(image)
        image = image.resize((self.size, self.size))
        image = np.array(image)
        
        input = np.expand_dims(image, axis=0)
        result = self.modelCat.predict_step(input)
        result = result.numpy()
        print(result[0, 0])

test = BrainTumorDetection()
test.PrepareImage("pred\\pred45.jpg") # There is tumor = 0
test.PrepareImage("pred\\pred42.jpg") # There is no tumor = 1
