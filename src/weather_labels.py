import numpy as np
import process_y as py
import cv2

###################################
#### Constants ###################

TRAIN_JPG = "../data/train-jpg"
TRAIN_TIFF = "../data/train-tif-v2"

##################################

weather_labels = ["cloudy", "partly_cloudy", "haze", "clear"]
Y = py.selected_columns(weather_labels)
Y = Y[(Y.T != 0).any()]

X = []
for i in Y.index:
    print "Read Image: ", i
    img = cv2.imread(TRAIN_TIFF + '/train_'+ str(i) +'.tif', cv2.IMREAD_UNCHANGED)
    X.append(img)

X = np.array(X)

np.save('../data/x_train_tif_weather.npy', X)
np.save('../data/y_train_weather.npy', Y)

X = []
for i in Y.index:
    print "Read Image: ", i
    img = cv2.imread(TRAIN_JPG + '/train_'+ str(i) +'.jpg', cv2.IMREAD_UNCHANGED)
    X.append(img)

np.save('../data/x_train_jpg_weather.npy', X)
