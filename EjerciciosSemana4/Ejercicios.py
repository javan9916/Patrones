import cv2
import math
import numpy as np

img = cv2.imread("EjerciciosSemana4\\2image1.jpg")

def menu():
    print("------ Ejercicios ------")
    print("Seleccione su opción: ")
    print("1) Color Balance")
    print("2) Green Screen Matting")
    print("3) Photo Effects")
    print("0) Salir")
    print("---------------------------------------------------")

    while True:
        opt = input("Opción: ")

        if opt == '1':
            color_balance()
            break
        elif opt == '2':
            pixeldiff()
            break
        elif opt == '3':
            photo_effects()
            break
        elif opt == '0':
            break
        else:
            print("Esa opción no existe")

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()

def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix

def simplest_cb(img, percent_list):
    half_percents = []

    y,m,c = cv2.split(img)
    colors = [y,m,c]

    for index in range(len(percent_list)):
        half_percents.append(percent_list[index] / 200.0)

    out_channels = []
    for index,channel in enumerate(colors):
        half_percent = half_percents[index]
        assert len(channel.shape) == 2
        # find the low and high precentile values (based on the input percentile)
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1

        flat = np.sort(flat)

        n_cols = flat.shape[0]

        low_val  = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil(n_cols * (1.0 - half_percent))]

        # saturate below the low percentile and above the high percentile
        thresholded = apply_threshold(channel, low_val, high_val)
        # scale the channel
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

def pixeldiff():

    img1 = cv2.imread("EjerciciosSemana4\\verdeVacio.png")
    img2 = cv2.imread("EjerciciosSemana4\\verdeMano.png")
    diff = cv2.absdiff(img1, img2)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 1
    imask =  mask>th

    canvas = np.zeros_like(img2, np.uint8)
    canvas[imask] = img2[imask]

    cv2.imshow("Difference", canvas)
    cv2.waitKey(0)
    return

def color_balance():
    print("Inserte los porcentajes de cada color: ")

    cyan = int(input("Cyan: "))
    magenta = int(input("Magenta: "))
    yellow = int(input("Yellow: "))

    out = simplest_cb(img, [yellow, magenta, cyan])

    cv2.imshow("Before", img)
    cv2.imshow("After", out)
    cv2.waitKey(0)


def photo_effects():
    
    new_image = np.zeros(img.shape, img.dtype)
    img.convertTo(new_image, -1, 2, 0)

    cv2.imshow('Original Image', img)
    cv2.imshow('New Image', new_image)
    # Wait until user press some key
    cv2.waitKey()


menu()
