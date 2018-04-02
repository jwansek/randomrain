import cv2
import numpy as np
import argparse
from pyimagesearch import imutils

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", help = "Path to the video file. If ignored, use webcam.")
args = vars(parser.parse_args())

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    cap, img = camera.read()

    if args.get("video") and not cap:
        break

    img = imutils.resize(img, width = 480)

    cv2.imshow("Press 'q' to exit", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()


