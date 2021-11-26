import cv2
import numpy as np
import pyautogui
import ctypes

#OBTIENE TAMAÑO DE LA PANTALLA
def screen_s():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    dimensions = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)
    return dimensions

#FORMATO PARA CREACIÓN DE VIDEO
screen_size = screen_s()
fourcc = cv2.VideoWriter_fourcc(*"avc1")
out = cv2.VideoWriter("prueba.mp4", fourcc, 20.0, (screen_size))

while True:
    #CAPTURA DE PANTALLA
    img = pyautogui.screenshot()
    #TRADUCIMOS CAPTURA A UN ARRAY QUE PUEDA LEER "cv2"
    frame = np.array(img)
    #CONVERTIMOS "frame" DE FORMATO "BGR" A "RGB".
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #AÑADIMOS "frame" AL FUTURO VÍDEO.
    out.write(frame)

    #MOSTRAMOS CAPTURA DE PANTALLA ACTUAL
    # cv2.imshow("screenshot", frame)

    #SI PULSAMOS "esc" FINALIZA EL PROCESO.
    if cv2.waitKey(1) == 27:
        print("END")
        break

#CERRAMOS TODAS LAS VENTANAS
cv2.destroyAllWindows()
#CREAMOS VÍDEO.
out.release()
