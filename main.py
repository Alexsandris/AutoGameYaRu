import time
import pyautogui
import cv2
import numpy as np

# Задержка в 3 секунды
time.sleep(10)

# Получение текущего изображения экрана
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# Обнаружение красного цвета
red_lower = np.array([0, 0, 150], np.uint8)
red_upper = np.array([100, 100, 255], np.uint8)
red_mask = cv2.inRange(screenshot, red_lower, red_upper)
blue_lower = np.array([82, 125, 153], np.uint8)
blue_upper = np.array([219, 147, 255], np.uint8)
blue_mask = cv2.inRange(screenshot, blue_lower, blue_upper)
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours1, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Поиск самого большого контура красного цвета
largest_contour = max(contours, key=cv2.contourArea)
largest_contour_blue = max(contours1, key=cv2.contourArea)

# Определение координат центра контура
M = cv2.moments(largest_contour)
center_x = int(M["m10"] / M["m00"])
center_y = int(M["m01"] / M["m00"])

M_blue = cv2.moments(largest_contour_blue)
center_x_blue = int(M_blue["m10"] / M_blue["m00"])
center_y_blue = int(M_blue["m01"] / M_blue["m00"])

# Перемещение курсора мыши в найденные координаты

#pyautogui.moveTo(center_x_blue, center_y_blue)
# Нажатие левой кнопки мыши

#pyautogui.mouseDown()
#pyautogui.mouseUp()


pyautogui.moveTo(center_x, center_y)

pyautogui.mouseDown()
pyautogui.mouseUp()
