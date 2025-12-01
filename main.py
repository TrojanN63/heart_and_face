import cv2 as cv
import mediapipe as mp
import math
import time

video = cv.VideoCapture(0)
start_time = time.perf_counter()
mp_draw = mp.solutions.drawing_utils
mp_face = mp.solutions.face_mesh
spec_landmark = mp_draw.DrawingSpec(color=(0,255,0), thickness=0, circle_radius=0)
spec_connection = mp_draw.DrawingSpec(color=(0,0,255), thickness=2)
content = 'ypos,time,horizontal_pos,vertical_pos\n'

with mp_face.FaceMesh(refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face:
    while True:
        istrue, frame = video.read()
        frame = cv.flip(frame, 1)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results_f = face.process(frame)
        frame.flags.writeable = True
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if results_f.multi_face_landmarks:
            for face_landmark in results_f.multi_face_landmarks:
                mp_draw.draw_landmarks(frame,
                                       face_landmark,
                                       mp_face.FACEMESH_RIGHT_EYE,
                                       landmark_drawing_spec=spec_landmark,
                                       connection_drawing_spec=spec_connection)
            height, width, _ = frame.shape
            landmarks = results_f.multi_face_landmarks[0]
            lm_159 = landmarks.landmark[159]
            lm_145 = landmarks.landmark[145]
            lm_468 = landmarks.landmark[468]
            lm_33 = landmarks.landmark[33]
            lm_133 = landmarks.landmark[133]
            middle_x = (lm_133.x + lm_33.x)/2
            middle_y = (lm_145.y + lm_159.y)/2

            # print(f"LandMark 158 position: {lm_158.x},{lm_158.y},{lm_158.z}")
            (x159,y159,z159) = lm_159.x, lm_159.y, lm_159.z
            (x468,y468,z468) = lm_468.x, lm_468.y, lm_468.z
            cv.line(frame, (int(x159*width),int(y159*height)), (int(x468*width),int(y468*height)), (255,255,255), 2)
            # print(y468)
            end_time = time.perf_counter()
            timer = end_time - start_time
            pos_x = x468 - middle_x
            pos_y = y468 - middle_y
            content += f'{y468-y159},{timer},{pos_x},{pos_y}\n'
            with open('data.csv','w') as file:
                file.write(content)
        if istrue:
            cv.imshow("it's you", frame)
            if cv.waitKey(100) & 0xFF==ord('d'):
                break
        else:
            break

video.release()
cv.destroyAllWindows()
