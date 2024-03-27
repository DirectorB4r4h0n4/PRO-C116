import cv2

# Leer la imagen
img = cv2.imread("solar-system.jpg")

# Agregar texto debajo de cada planeta
cv2.putText(img, "Sun", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.putText(img, "Mercury", (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Venus", (170, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Earth", (270, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Mars", (370, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Jupiter", (550, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Saturn", (750, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Uranus", (950, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)
cv2.putText(img, "Neptune", (1090, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (155, 155, 155), 2)

# Mostrar la imagen
cv2.imshow("Output", img)
cv2.waitKey(0)

# Guardar la imagen final
cv2.imwrite("Solar_systemwithname.jpg", img)
