import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = tuple(pyautogui.size())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 12.0
video_output = cv2.VideoWriter("output.avi", fourcc, fps, SCREEN_SIZE)
record_seconds = 10

Xs = [0,8,6,14,12,4,2,0]
Ys = [0,2,4,12,14,6,8,0]

# for i in range(int(record_seconds * fps)):   
while True: 
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    video_output.write(frame)
    image = cv2.resize(frame, (960, 540))   
    cv2.imshow("screenshot", image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
video_output.release()