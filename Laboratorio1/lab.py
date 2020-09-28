import cv2

def menuFruta():
    print("------ Seleccione la Imagen que desea usar --------")
    print("Seleccione su opción: ")
    print("1) Banano")
    print("2) Sandia")
    print("3) Cereza")
    print("4) Durazno")
    print("5) Madarina")
    print("6) Rambutan")
    print("0) Salir")
    print("---------------------------------------------------")

    while True:
        opt = input("Opción: ")

        if opt == '1': #banano
            archivo = "Laboratorio1\\frutas\\banano.png"
            menuTran(archivo)
            break
        elif opt == '2': #sandia
            archivo = "Laboratorio1\\frutas\\sandia.png"
            menuTran(archivo)
            break
        elif opt == '3': #cereza
            archivo = "Laboratorio1\\frutas\\cereza.png"
            menuTran(archivo)
            break
        elif opt == '4': #durazno
            archivo = "Laboratorio1\\frutas\\durazno.png"
            menuTran(archivo)
            break
        elif opt == '5': #mandarina
            archivo = "Laboratorio1\\frutas\\mandarina.png"
            menuTran(archivo)
            break
        elif opt == '6': #rambutan
            archivo = "Laboratorio1\\frutas\\rambutan.png"
            menuTran(archivo)
            break
        elif opt == '0':
            break
        else:
            print("Esa opción no existe")

def menuTran(archivo):
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
            region(archivo)
            break
        elif opt == '4':
            redimensionar(archivo)
            break
        elif opt == '6':
            suavizar(archivo)
            break
        elif opt == '1':
            getPixel(archivo)
            break
        elif opt == '3':
            resizeLibre(archivo)
            break
        elif opt == '5':
            rotarImagen(archivo)
            break
        elif opt == '0':
            menuFruta()
            break
        else:
            print("Esa opción no existe")

def region(archivo):
    print("------ Región de una imagen ------")
    fruta = cv2.imread(archivo)
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    ix = int(input("Inicio X: "))
    iy = int(input("Inicio Y: "))
    fx = int(input("Fin X: "))
    fy = int(input("Fin Y: "))

    roi = fruta[iy:fy, ix:fx]

    cv2.imshow("Region", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar(roi, 2)
    menuFruta()

def redimensionar(archivo):
    print("------ Redimensionar imagen ------")
    fruta = cv2.imread(archivo)
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    size = int(input("Tamaño a redimensionar: "))

    r = size / fruta.shape[1]
    dim = (size, int(fruta.shape[0] * r))
    resized = cv2.resize(fruta, dim)

    cv2.imshow("Redimension", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar(resized, 4)
    menuFruta()

def suavizar(archivo):
    print("------ Suavizado Gaussiano ------")
    fruta = cv2.imread(archivo)
    print("Tamaño: "+ str(fruta.shape[0])+"x"+str(fruta.shape[1]))

    blur = int(input("Intensidad del suavizado (debe ser impar): "))

    blurred = cv2.GaussianBlur(fruta, (blur, blur), 0)

    cv2.imshow("Suavizado", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar(blurred, 6)
    menuFruta()

def getPixel(archivo):
    print("------ RGB de Pixel ------")

    fruta = cv2.imread(archivo)

    x = int(input("Posicion X: "))
    y = int(input("Posicion Y: "))

    (B, G, R) = fruta[x, y]

    print("R={}, G={}, B={}".format(R, G, B))
    menuFruta()

def resizeLibre(archivo):
    print("------ Resize de imagen libre ------")

    fruta = cv2.imread(archivo)

    w = int(input("Ancho: "))
    h = int(input("Alto: "))

    resized = cv2.resize(fruta, (w, h))

    cv2.imshow("Resize Libre", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar(resized, 3)
    menuFruta()

def rotarImagen(archivo):
    print("------ Rotacion de la imagen ------")

    fruta = cv2.imread(archivo)
    w = fruta.shape[1]
    h = fruta.shape[0]
    center = (w // 2, h // 2)

    angulo = int(input("Angluo de rotacion: "))
    M = cv2.getRotationMatrix2D(center, angulo, 1.0)

    rotated = cv2.warpAffine(fruta, M, (w, h))

    cv2.imshow("Rotado", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar(rotated, 5)
    menuFruta()


def guardar(imagen, tipo):
    if tipo == 1:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info1.png', imagen)
    elif tipo == 2:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info2.png', imagen)
    elif tipo == 3:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info3.png', imagen)
    elif tipo == 4:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info4.png', imagen)
    elif tipo == 5:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info5.png', imagen)
    elif tipo == 6:
        cv2.imwrite('C:\\Users\\carlo\\OneDrive\\Escritorio\\Info6.png', imagen)


menuFruta()