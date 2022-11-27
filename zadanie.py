import cv2
import numpy as np

cap = cv2.VideoCapture('video.MP4')

fourcc = cv2.VideoWriter_fourcc(*'mpv4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)
out = cv2.VideoWriter('GreenBlueVideo.mp4', fourcc, 50.0, size, True)


while(1):

    # Take each frame
    _, frame = cap.read()

    # konwersja BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # zakres niebieskiego w HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # maska niebieska
    mask_b = cv2.inRange(hsv,lower_blue,upper_blue)

    # zakres czerwonego w HSV

    lower_red = np.array([159, 50, 70])
    upper_red = np.array([180, 255, 255])

    # maska czerwona
    mask_r = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask_b + mask_r

    # ekstrakcja obrazu tam gdzie piksele pokrywają sie z maską

    vid = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('mask', mask)
    cv2.imshow('video', vid)
    out.write(vid)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
print("Video saved successfully.")
cv2.destroyAllWindows()
