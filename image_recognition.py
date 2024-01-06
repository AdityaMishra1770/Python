import sys
import threading
import cv2
from deepface import DeepFace

print(sys.executable)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
counter = 0
face_match = False
reference_img = cv2.imread("C:\\Users\\Aditya Mishra\\OneDrive\\Pictures\\Camera Roll\\WIN_20240104_02_56_13_Pro.jpg")


def check_face(word):
    global face_match
    try:
        if DeepFace.verify(word, reference_img)['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()

# import sys
# import threading
# import cv2
# from deepface import DeepFace

# print(sys.executable)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# counter = 0
# face_match = False
# reference_img = cv2.imread("C:\\Users\\Aditya Mishra\\OneDrive\\Pictures\\Camera Roll\\WIN_20240104_02_56_13_Pro.jpg")

# def check_face(frame):
#     global face_match
#     if frame is not None and reference_img is not None:
#         try:
#             if DeepFace.verify(frame, reference_img, enforce_detection=False)['verified']:
#                 face_match = True
#             else:
#                 face_match = False
#         except ValueError:
#             face_match = False
#     else:
#         face_match = False

# while True:
#     ret, frame = cap.read()
#     if ret:
#         if counter % 30 == 0:
#             try:
#                 threading.Thread(target=check_face, args=(frame.copy(),)).start()
#             except ValueError:
#                 pass
#         counter += 1

#         if face_match:
#             cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
#         else:
#             cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

#         cv2.imshow("video", frame)

#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
# cv2.destroyAllWindows()


# import cv2
# from deepface import DeepFace

# # Load the reference image
# reference_img = cv2.imread("D:\\download\\WhatsApp Image 2024-01-04 at 3.22.42 AM.jpeg")

# # Load the image to compare
# compare_img = cv2.imread("D:\\download\\WhatsApp Image 2024-01-04 at 3.22.42 AM.jpeg")

# def check_face(img1, img2):
#     try:
#         result = DeepFace.verify(img1, img2)
#         return result['verified']
#     except ValueError:
#         return False

# # Check if the faces match
# face_match = check_face(reference_img, compare_img)

# if face_match:
#     print("MATCH!")
# else:
#     print("NO MATCH!")
