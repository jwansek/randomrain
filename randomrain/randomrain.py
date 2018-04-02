import cv2
import numpy as np
import argparse
from pyimagesearch import imutils
import time

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", help = "Path to the video file. If ignored, use webcam.")
args = vars(parser.parse_args())

times = []
count = 5

def draw_fps(frame, times, count):
    times.append(time.time())
    if len(times) >= count:
        times = times[-count:]
        fps = "%.2f FPS" % (count/(times[-1] - times[0]))
        cv2.putText(frame, fps, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_AA)
        
def draw_pts(frame, pts, minx, miny):
    xs = []
    ys = []
    for pt in pts:
        for x, y in pt:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            print(sum(map(int, str(int((y*x) % 7000)))))


if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    cap, img = camera.read()

    if args.get("video") and not cap:
        break

    img = imutils.resize(img, width = 600)
    orig = img.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.erode(img, kernel = None, iterations = 2)
    img = cv2.dilate(img, kernel = None, iterations  = 2)
    img = cv2.inRange(img, 0, 100)
    pts = cv2.findNonZero(img)
    
    draw_pts(orig, pts, None, None)



    
    
    draw_fps(orig, times, count)

    cv2.imshow("Press 'q' to exit", orig)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()


