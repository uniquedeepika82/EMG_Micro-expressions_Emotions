
# filters.py
# Digital filters for EMG signal processing

from scipy.signal import butter, lfilter, iirnotch
import numpy as np

def bandpass_filter(data, fs=1000, lowcut=20.0, highcut=450.0, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

def notch_filter(data, fs=1000, freq=50.0, Q=30.0):
    w0 = freq / (fs / 2)
    b, a = iirnotch(w0, Q)
    return lfilter(b, a, data)

def full_wave_rectify(data):
    return np.abs(data)
