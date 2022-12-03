import cv2
image="solar-system.jpg"
cv2.imshow("picture",image)
image=cv2.imread("solar-system.jpg")
cv2.waitKey(0)
cv2.putText(image,
            "Sun"
            (20,300),
            fontFace=cv2,
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            fontScale=1,
            color=(225,225,225)
            )