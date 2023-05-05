import cv2 as cv
import mediapipe as mp
import time
import math
import pyautogui as pg
capt = cv.VideoCapture(0)

mpHands =mp.solutions.hands
hands = mpHands.Hands()
mydraw = mp.solutions.drawing_utils




while 1:
    isTrue,frame = capt.read()
    imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    res = hands.process(imgRGB)
    if res.multi_hand_landmarks:
        for handLMS in res.multi_hand_landmarks:
            for id, lm in enumerate(handLMS.landmark):
                h,w,c = frame.shape
                cx,cy = int(lm.x*w), int(lm.y * h)

                if id ==4:
                    #print(f"x={cx} \ny={cy} \n --------------------" )
                    cx4 = cx
                    cy4 = cy
                if id ==8:
                    #print(f"x={cx} \ny={cy} \n --------------------" )
                    cx8 = cx
                    cy8 = cy


            mydraw.draw_landmarks(frame,handLMS, mpHands.HAND_CONNECTIONS)

        CB = cy8 -cy4
        AB = cx8 - cx4
        pg.moveTo(cx8*3, cy8*3)
        d = math.sqrt(pow(AB,2)+pow(CB,2))
        if(abs(cx4 - cx8) < 20):
            pg.click()
       

    cv.imshow("video",frame)
    if cv.waitKey(20)&0xFF==ord('d'):
        break

capt.release()
cv.destroyAllWindows()