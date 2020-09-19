import cv2
import numpy as np
from matplotlib import pyplot as plt

def menu():
    print("------ Transformación de imágenes con OpenCV ------")
    print("Seleccione su opción: ")
    print("1) RGB de un pixel")
    print("2) Región de una imagen")
    print("3) Ajustar tamaño de imagen")
    print("4) Redimensionar imagen")
    print("5) Rotar imagen")
    print("6) Suavizar imagen")
    print("0) Salir")
    print("---------------------------------------------------")

    while True:
        opt = input("Opción: ")

        if opt == '2':
            region()
            break
        elif opt == '4':
            redimensionar()
            break
        elif opt == '6':
            suavizar()
            break
        elif opt == '0':
            break
        else:
            print("Esa opción no existe")

def region():
    print("------ Región de una imagen ------")
    fruta = cv2.imread("C:\\Users\\Javier\\Patrones\\Laboratorio1\\frutas\\banano.png")
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    ix = int(input("Inicio X: "))
    iy = int(input("Inicio Y: "))
    fx = int(input("Fin X: "))
    fy = int(input("Fin Y: "))

    roi = fruta[iy:fy, ix:fx]

    cv2.imshow("Region", roi)
    cv2.waitKey(0)

    menu()

def redimensionar():
    print("------ Redimensionar imagen ------")
    fruta = cv2.imread("C:\\Users\\Javier\\Patrones\\Laboratorio1\\frutas\\banano.png")
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    size = int(input("Tamaño a redimensionar: "))

    r = size / fruta.shape[1]
    dim = (size, int(fruta.shape[0] * r))
    resized = cv2.resize(fruta, dim)

    cv2.imshow("Redimension", resized)
    cv2.waitKey(0)

    menu()

def suavizar():
    print("------ Suavizado Gaussiano ------")
    fruta = cv2.imread("C:\\Users\\Javier\\Patrones\\Laboratorio1\\frutas\\banano.png")
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    blur = int(input("Intensidad del suavizado (debe ser impar): "))

    blurred = cv2.GaussianBlur(fruta, (blur, blur), 0)

    cv2.imshow("Suavizado", blurred)
    cv2.waitKey(0)

    menu()

menu()