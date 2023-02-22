import cv2
import pytesseract

# Inicializace kamery
cap = cv2.VideoCapture(0)

# Načtení fontu pro český jazyk
font = cv2.FONT_HERSHEY_TRIPLEX
font_scale = 1
font_color = (255, 255, 255)
line_type = 2

# Časovač pro snímkování každou sekundu
timer = cv2.getTickCount()
fps = 1

# Neustálé čtení snímků z kamery
while True:
    current_time = cv2.getTickCount()
    time_diff = current_time - timer
    if time_diff > 1000 / fps:
        timer = current_time
        # Čtení aktuálního snímku
        ret, frame = cap.read()

        # Konverze snímku do černobílé
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Aplikace prahování pro zvýraznění textu
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Použití funkce pytesseract pro převod textu z obrázku do textu v Pythonu
        text = pytesseract.image_to_string(img, lang='ces')

        # Vykreslení snímku s vyznačeným textem
        cv2.putText(frame, text, (30, 30), font, font_scale, font_color, line_type, cv2.LINE_AA)

        # Zobrazení snímku
        cv2.imshow('frame', frame)

    # Kontrola stisknuté klávesy pro ukončení aplikace
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Uvolnění kamery a zničení oken
cap.release()
cv2.destroyAllWindows()
