import cv2 as cv
import mediapipe as mp
import time
import math

import serial
ser = serial.Serial('/dev/ttyACM0',9600)
capt = cv.VideoCapture(0)

mpHands =mp.solutions.hands
hands = mpHands.Hands()
mydraw = mp.solutions.drawing_utils
cTime =0
pTime = 0
while 1:
    isTrue,frame = capt.read()
    imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    res = hands.process(imgRGB)

    if res.multi_hand_landmarks:
        for handLMS in res.multi_hand_landmarks:
            for id, lm in enumerate(handLMS.landmark):
                h,w,c = frame.shape
                cx,cy = int(lm.x*w), int(lm.y * h)

                if id == 4:
                    # print(f"x={cx} \ny={cy} \n --------------------" )
                    cv.circle(frame, (cx, cy), 15, (255, 0, 0), cv.FILLED)
                    cy4 = cy
                    cx4= cx
                if id == 8:
                    # print(f"x={cx} \ny={cy} \n --------------------" )
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                    cy8 = cy
                    cx8 = cx
                if id == 20:
                    # print(f"x={cx} \ny={cy} \n --------------------" )
                    cv.circle(frame, (cx, cy), 15, (100, 100, 255), cv.FILLED)
                    cy20 = cy
                    cx20 = cx

                if id == 12:
                    # print(f"x={cx} \ny={cy} \n --------------------" )
                    cv.circle(frame, (cx, cy), 15, (100, 0, 255), cv.FILLED)
                    cy12 = cy

                if id == 16:
                    # print(f"x={cx} \ny={cy} \n --------------------" )
                    cv.circle(frame, (cx, cy), 15, (50, 50, 255), cv.FILLED)
                    cy16 = cy
            mydraw.draw_landmarks(frame, handLMS, mpHands.HAND_CONNECTIONS)
        dis = math.sqrt(abs(cx4 - cx8) ^ 2 + abs(cy4 - cy8) ^ 2)
        cv.putText(frame, str(int(dis)), (10, 70), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)

        if cy4 > cy20 and cy4 < cy8 and cy4 < cy12 and cy4 < cy16:
            ser.write(b'1')
            print("Led")

        elif cx4 > cx8 and cx4>cx20 and dis > 6 and cy4 < cy20:
            print("Servo L")
            ser.write(b'3')

        elif cx4< cx8 and cx4<cx8 and dis > 6 :
            print("Servo R")
            ser.write(b'4')

        elif dis < 6 :
            ser.write(b'2')
            print("Buzzer")


        else:
            ser.write(b'7')
            print("NONE")
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.imshow("video",frame)
    if cv.waitKey(20)&0xFF==ord('d'):
        break

capt.release()
cv.destroyAllWindows()
