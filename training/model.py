from os import walk

import numpy as np
from PIL import Image
from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def dataset_generator(label):
    mapping = {
        'no_mask': 0,
        'mask': 1
    }

    mapping_id = mapping[label]
    inputs = []

    for (base_path, _, filenames) in walk('dataset/' + str(mapping_id)):
        for filename in filenames:
            x.append(np.array(Image.open(base_path + '/' + filename).resize((200, 200))).reshape(-1))

    labels = [mapping_id for _ in range(len(x))]
    return inputs, labels


no_mask_images, no_mask_y = dataset_generator('no_mask')
mask_images, mask_y = dataset_generator('mask')

x = no_mask_images + mask_images
y = no_mask_y + mask_y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

lr = LogisticRegression()
lr.fit(x_train, y_train)

print(f"Train accuracy is: #{lr.score(x_train, y_train)}")
print(f"Test accuracy is: #{lr.score(x_test, y_test)}")
dump(lr, 'logistic_regression.joblib')
