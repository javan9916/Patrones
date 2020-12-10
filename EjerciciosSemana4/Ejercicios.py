import cv2
from PIL import Image, ImageOps  
import math
import numpy as np

apple = cv2.imread("EjerciciosSemana4\\apple.PNG")
img = cv2.imread("EjerciciosSemana4\\image1.jpg")
img1 = cv2.imread("EjerciciosSemana4\\verdeVacio.png")
img2 = cv2.imread("EjerciciosSemana4\\verdeMano.png")

def menu():
    print("------ Ejercicios ------")
    print("Seleccione su opción: ")
    print("1) Color Balance")
    print("2) Green Screen Matting")
    print("3) Photo Effects")
    print("4) Histogram equalization")
    print("5) Image Resampling")
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
        elif opt == '4':
            histo_equal()
            break
        elif opt == '5':
            resampling()
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
    print("Elija un efecto: ")
    print("1) Contraste")
    print("2) Solarize")
    print("3) Emboss")
    print("4) Sharpened")
    opt = input("Opción: ")

    if opt == '1':
        bright = 255
        contrast = 140
    
        new_image = apply_brightness_contrast(img, bright, contrast)
        
        cv2.imshow('Original Image', img)
        cv2.imshow('New Image', new_image)
        cv2.waitKey(0)
    
    elif opt == '2':
        img1 = Image.open("EjerciciosSemana4/image1.jpg")  
        img2 = ImageOps.solarize(img1, threshold = 130)  
        img2.show() 
    
    elif opt == '3':
        kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
        new_image = cv2.filter2D(img, -1, kernel)

        cv2.imshow('Original Image', img)
        cv2.imshow('New Image', new_image)
        cv2.waitKey(0)

    elif opt == '4':
        kernel = np.array([[-1, -1, -1], 
                            [-1, 9, -1], 
                            [-1, -1, -1]])
        new_image = cv2.filter2D(img, -1, kernel)

        cv2.imshow('Original Image', img)
        cv2.imshow('New Image', new_image)
        cv2.waitKey(0)
 
def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)
 
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
 
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
 
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
 
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
 
    return buf
 
def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def histogram():
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    cv2.imshow('Gray', gray)
    cv2.imshow('Histogram', equalized)
    cv2.waitKey(0)

def resampling():
    print("Elija una opción: ")
    print("1) Interpolación")
    print("2) Diezmar")
    opt = input("Opción: ")

    if opt == '1':
        interpolation()
    elif opt == '2':
        decimating()

def decimating():
    scale_ratio = 0.6
    img_resized = cv2.resize(img, None, fx=scale_ratio, fy=scale_ratio, interpolation=cv2.INTER_CUBIC)

    scale_ratio = 1.8
    low_res = cv2.resize(img_resized, None, fx=scale_ratio, fy=scale_ratio, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('Original', img)
    cv2.imshow('Low Res', low_res)
    cv2.waitKey(0)

def interpolation():
    near_img = cv2.resize(apple,None, fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST)
    bilinear_img = cv2.resize(apple,None, fx = 10, fy = 10, interpolation = cv2.INTER_LINEAR)
    bicubic_img = cv2.resize(apple,None, fx = 10, fy = 10, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('Nearest Neighbour', near_img)
    cv2.imshow('Bilinear', bilinear_img)
    cv2.imshow('Bicubic', bicubic_img)
    cv2.waitKey(0)

def histo_equal():
    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ)) 
    cv2.imshow('Histogram equal', res)
    cv2.waitKey(0)

menu()
