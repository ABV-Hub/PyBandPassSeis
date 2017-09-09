from scipy.signal import butter, lfilter, lfilter_zi

def butter_bandpass(lowcut, highcut, fs, order=6):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs):
    b, a = butter_bandpass(lowcut, highcut, fs, order=6)
    y_first = lfilter(b, a, data)
    y_secon = lfilter(b, a, y_first[::-1])  #It's because the filter delay, AJ
    y= y_secon[::-1]
    return y
