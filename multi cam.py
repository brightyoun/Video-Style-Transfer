import cv2
import numpy as np

cap = cv2.VideoCapture()
cap.open("C:\\Users\\MLV\\Documents\\oCam\\00002.mp4")

cap2 = cv2.VideoCapture()
cap2.open("C:\\Users\\MLV\\Documents\\oCam\\00002_res.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_002.avi', fourcc, 30.0, (1280, 480))

count = 0
str_input = "INPUT (GT)"
str_output = "AI OUTPUT"

str_input_font = cv2.FONT_HERSHEY_PLAIN

while(cap.isOpened()):
    count += 1
    try:
        if count % 2 == 0:
            ret, frame1 = cap.read()
            ret, frame2 = cap2.read()
            frame1 = cv2.resize(frame1, (640, 480)) #1080 720
            cv2.putText(frame1, str_input, (20, 40), str_input_font, 2, (0, 0, 255), 2)
            frame2 = cv2.resize(frame2, (640, 480))  # 1080 720
            cv2.putText(frame2, str_output, (20, 40), str_input_font, 2, (255, 0, 0), 2)


            # 다중 창!
            numpy_horizontal_concat = np.concatenate((frame1, frame2), axis=1)
            #numpy_horizontal_concat = img

            out.write(numpy_horizontal_concat)
            cv2.imshow('frame', numpy_horizontal_concat)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if count == 7700:
                break
    except Exception as e:
        print("오우야 : ", count)
        print(str(e))

cap.release()
cap2.release()
cv2.destroyAllWindows()