import numpy as np
from joblib import load
from PIL import Image

model = load('training/logistic_regression.joblib')

MAPPING = {
    0: 'no_mask',
    1: 'mask'
}


def classifier(image):
    predict = round(float(model.predict([np.array(Image.open(image).resize((200, 200))).reshape(-1)])))

    return MAPPING[predict]
