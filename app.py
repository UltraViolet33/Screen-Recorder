import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = tuple(pyautogui.size())

fourcc = cv2.VideoWriter_fourcc(*"XVID")

fps = 12.0

video_output = cv2.VideoWriter("output.avi", fourcc, fps, SCREEN_SIZE)

record_seconds = 10


for i in range(int(record_seconds * fps)):    
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_output.write(frame)
    # cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
video_output.release()