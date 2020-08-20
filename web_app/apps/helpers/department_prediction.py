import pickle
import sys

from web_app.add_paths import path

with open(path + '/web_app/apps/helpers/vocab.pickle', 'rb') as f:
    model = pickle.load(f)


def model_prediction(complaint):
    return model.predict(complaint)

