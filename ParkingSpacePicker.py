import cv2
import pickle

# width, height = 107, 48
# width, height = 20, 150

# posList = []

try:
    with open('CarParkPos_image6', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos_image6', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('image6.jpg')
    # for pos in posList:
    #     print("singh--",pos)
    #     cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    if len(posList)%2 == 0 :
        print("shubham",posList)
        for i in range(0,len(posList),2):
            x1,x2 = posList[i]
            x3,x4 = posList[i+1]
            pos = (x1,x2)
            cv2.rectangle(img,pos, (x1 + (x3-x1), x2 + (x4-x2)), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)