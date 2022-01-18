import cv2
import numpy as np
import imutils

sciezka_proto = "MobileNetSSD_deploy.prototxt"
sciezka_modelu = "MobileNetSSD_deploy.caffemodel"
detektor = cv2.dnn.readNetFromCaffe(prototxt=sciezka_proto, caffeModel=sciezka_modelu)

KLASY = ["background", "aeroplane", "bicycle", "bird", "boat",
         "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
         "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
         "sofa", "train", "tvmonitor"]


def main():
    # obraz = cv2.imread('ludzie.jpg')
    obraz = cv2.imread('ludzie2.jpg')
    obraz = imutils.resize(obraz, width=600)

    (H, W) = obraz.shape[:2]

    blob = cv2.dnn.blobFromImage(obraz, 0.007843, (W, H), 127.5)

    detektor.setInput(blob)
    wykrycia_ludzi = detektor.forward()

    for i in np.arange(0, wykrycia_ludzi.shape[2]):
        pewnosc = wykrycia_ludzi[0, 0, i, 2]
        if pewnosc > 0.5:
            idx = int(wykrycia_ludzi[0, 0, i, 1])

            if KLASY[idx] != "person":
                continue

            zaznaczenie = wykrycia_ludzi[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = zaznaczenie.astype("int")

            cv2.rectangle(obraz, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imshow("Wynik", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
