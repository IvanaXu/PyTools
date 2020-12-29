# -*-coding:utf-8-*-
# @auth Ivan
# @time 2020-12-29
# @goal Test dlib

import dlib
import cv2 as cv

modelv = "_81"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(f"093.shape_predictor{modelv}_face_landmarks.dat")

def f_xy(images):
    result = []
    cv_face = detector(cv.cvtColor(images, cv.COLOR_BGR2GRAY), 1)
    for face in cv_face:
        shape = predictor(images, face)
        for pt in shape.parts():
            result.append((pt.y, pt.x))
    return result

pi = "093.Test_IN.jpg"
op = "093.Test_OT.jpg"
img = cv.imread(pi)
for if_xy in f_xy(img):
    y, x = if_xy
    if 0 <= x < 112 and 0 <= y < 112:
        img[y-1:y+1,x-1:x+1] = 0

cv.imwrite(op, img)
