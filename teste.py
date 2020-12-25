
import cv2

from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

#webcam =  cv2.resize(captura, (1366, 768))

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Pupila Esquerda:  " + str(left_pupil), (20, 135), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Pupila Direita: " + str(right_pupil), (20, 195), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    text = ""

    if gaze.is_blinking():
        text = "Piscou"
        print("piscou", str(right_pupil))
    elif gaze.is_right():
        text = "Direita"
    elif gaze.is_left():
        text = "Esquerda"
    elif gaze.is_center():
        text = "Centro"

    cv2.putText(frame, text, (20, 90), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)


    cv2.imshow("Lemyson-test1", frame)

    if cv2.waitKey(1) == 27:
        break
