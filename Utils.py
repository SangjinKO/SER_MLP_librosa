from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from sklearn.externals import joblib
import librosa
import librosa.display
import scipy.io.wavfile as wav
import pyaudio
import wave

from Config import Config

def load_model(load_model_name: str):

    model_path = 'Models/' + load_model_name + '.m'
    model = joblib.load(model_path)

    return model
