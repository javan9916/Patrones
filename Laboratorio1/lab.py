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
    opt = input("Opción: ")

    print("Seleccionó "+opt)

menu()