import cv2
import pickle
import cvzone
import numpy as np

# Video feed
# cap = cv2.VideoCapture('carPark.mp4')
# cap = cv2.imread('parking_lot.jpg')
cap = cv2.imread('image10.jpg')

# with open('parking_lot_pos', 'rb') as f:
#     posList = pickle.load(f)

with open('CarParkPos_image6', 'rb') as f:
    posList = pickle.load(f)

# width, height = 107, 48


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for i in range(0, len(posList), 2):
        x1, x2 = posList[i]
        x3, x4 = posList[i + 1]
        width = abs((x3 - x1))
        height = abs((x4 - x2))
        # width = (x3 - x1)
        # height = (x2 - x4)
        pos = (x1, x2)

        x, y = pos

        # imgCrop = imgPro[y:y + height, x:x + width]

        imgCrop = imgPro[x2:x4, x1:x3]

        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        # print("shubham---", y + height, x + width,count)

        # cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 1)
        # cvzone.putTextRect(img,str(count),(x,y+height-10),scale=1,thickness = 1, offset = 1)

        if count < 1000:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{int(len(posList)/2)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0, 200, 0))

        # cv2.rectangle(img, pos, (x1 + (x3 - x1), x2 + (x4 - x2)), (255, 0, 255), 2)


while True:
    img = cap
    print("@@@@@@@@@@@@@@@",img)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    # checkParkingSpace(imgThreshold)
    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageBlur", imgThreshold)
    # cv2.imshow("ImageThres", imgMedian)
    # cv2.imshow("imgDilate", imgDilate)
    cv2.waitKey(10)