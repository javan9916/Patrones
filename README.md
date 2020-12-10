# Patrones

Repositorio del curso Introducción al Reconocimiento de Patrones

## Laboratorio 1

![Infografia](https://cdn.discordapp.com/attachments/708362688014844008/757781519317205052/Transformaciones.png)

En este laboratorio se pidieron 6 transformaciones, todas ejecutables a través de un menú de consola. Si bien el enunciado llamaba a usar las mismas imágenes que se trabajaron en el repositorio personal, se decidió usar otras imágenes de internet para tener más variedad de imágenes de mejor calidad.

Se manejó la interfaz a través de dos menús, el primero donde se escoge la imagen que se desea alterar y el segundo donde se escoge el cambio a aplicar; una vez se han pasado los menús, se piden los datos necesarios según la tranformación escogida.

### Despliegue el R,G,B de un pixel para un x,y proporcionado por el usuario

Para esta función, se cargó la imagen a través de OpenCV, donde luego se seleccionó un pixel específico (en las coordenadas dadas) con la capacidad de la librería de aislar pixeles.

```python
    x = int(input("Posicion X: "))
    y = int(input("Posicion Y: "))

    (B, G, R) = fruta[x, y]

    print("R={}, G={}, B={}".format(R, G, B))
```

### Extraer una región de una imagen una region (ROI) se deben solicitar los dos pares (x,y)inicio y fin y desplegar la imagen recortada. Muestre primero la imagen original

Mediante OpenCV es posible seleccionar una región específica de la imagen cargada, lo que resulta en un recorte del área marcada.

```python
    ix = int(input("Inicio X: "))
    iy = int(input("Inicio Y: "))
    fx = int(input("Fin X: "))
    fy = int(input("Fin Y: "))

    roi = fruta[iy:fy, ix:fx]
```

### Permita ajustar el tamaño de una imagen solicitando nueva dimensión en pixles y muestrela imagen resultante

Mediante la función resize() de OpenCV, se realiza el cambio de formato de la imagen según las dimensiones dadas por el usuario, lo que resulta en una nueva imagen con la resolución deseada.

```python
    w = int(input("Ancho: "))
    h = int(input("Alto: "))

    resized = cv2.resize(fruta, (w, h))
```
### Redimencione una imagen pero sin alterar el aspecto

Gracias a formulas matemáticas, se recibe una de las dimensiones de la igmane deseada (el ancho en este caso), se calcula la proporción de diferencia, con esta proporción se calcula la altura que deberá tener la imagen para preservar el aspecto original y se realiza el resize.

```python
    size = int(input("Tamaño a redimensionar: "))

    r = size / fruta.shape[1]
    dim = (size, int(fruta.shape[0] * r))
    resized = cv2.resize(fruta, dim)
```
### Rote una imagen la cantidad de grados que el usuario requiera

Para la rotación de la imagen se debe calcular el centro de esta (dividiendo el alto y el ancho en dos), con el centro y la medida de ángulos que el usuario desea rotar la imagen se genera una matrís de rotación, la cual es usada para generar mediante la función warpAffine() la imagen rotada.

```python
    w = fruta.shape[1]
    h = fruta.shape[0]
    center = (w // 2, h // 2)

    angulo = int(input("Angluo de rotacion: "))
    M = cv2.getRotationMatrix2D(center, angulo, 1.0)

    rotated = cv2.warpAffine(fruta, M, (w, h))
```

### Suavizar una imagen mediante un blur con un kernel Gaussiano

Mediante la funcion GaussianBlur() de OpenCV se realiza un difuminado gaussiano con la intensidad deteminana por el usuario.

```python
    blur = int(input("Intensidad del suavizado (debe ser impar): "))

    blurred = cv2.GaussianBlur(fruta, (blur, blur), 0)
```


## Infografía Perceptron
![InforPercep](https://cdn.discordapp.com/attachments/708362688014844008/772969360636772372/InfografiaPatronesPerceptor.png)
