"""
BFU UA Display - Приклад роботи з OLED дисплеєм SSD1306 через I2C
==================================================================

Цей приклад демонструє, як використовувати бібліотеку BFU UA Display
з OLED дисплеєм SSD1306, підключеним через I2C.

Підключення обладнання:
- Плата ESP32
- OLED дисплей SSD1306 (128x64 пікселі)
- Підключення I2C:
  - SCL -> GPIO 22
  - SDA -> GPIO 21
  - VCC -> 3.3V
  - GND -> GND

Автор: BFU Electronics
Ліцензія: MIT
"""

from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from bfu_ua_display import ua_text, ua_text_center, ua_text_scaled
import time


# Ініціалізація I2C та OLED дисплея
# Налаштуйте піни відповідно до вашої плати ESP32
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)


def priklad_1_prostiy_tekst():
    """Приклад 1: Базове відображення українського тексту"""
    print("Приклад 1: Простий текст")
    oled.fill(0)  # Очищаємо дисплей (заповнюємо чорним)
    
    # Виводимо різні рядки тексту
    ua_text(oled, "ПРИВІТ!", 0, 0)
    ua_text(oled, "Hello World", 0, 10)
    ua_text(oled, "Україна 2026", 0, 20)
    
    oled.show()  # Оновлюємо дисплей
    time.sleep(3)


def priklad_2_tsentrovaniy_tekst():
    """Приклад 2: Центрований текст"""
    print("Приклад 2: Центрований текст")
    oled.fill(0)
    
    # Текст автоматично центрується по горизонталі
    ua_text_center(oled, "УКРАЇНА", 10)
    ua_text_center(oled, "BFU Electronics", 28)
    ua_text_center(oled, "2026", 46)
    
    oled.show()
    time.sleep(3)


def priklad_3_masshtabovaniy_tekst():
    """Приклад 3: Масштабований текст (подвійний розмір)"""
    print("Приклад 3: Масштабований текст")
    oled.fill(0)
    
    # Виводимо текст у подвійному розмірі
    ua_text_scaled(oled, "ПРИВІТ", 10, 10, scale=2)
    ua_text(oled, "Звичайний розмір", 0, 40)
    
    oled.show()
    time.sleep(3)


def priklad_4_ukrainska_abetka():
    """Приклад 4: Відображення української абетки"""
    print("Приклад 4: Українська абетка")
    
    # Великі літери
    oled.fill(0)
    ua_text_center(oled, "ВЕЛИКІ ЛІТЕРИ:", 0)
    ua_text(oled, "АБВГҐДЕЄЖЗ", 0, 12)
    ua_text(oled, "ИІЇЙКЛМНОП", 0, 22)
    ua_text(oled, "РСТУФХЦЧШЩ", 0, 32)
    ua_text(oled, "ЬЮЯ", 0, 42)
    oled.show()
    time.sleep(4)
    
    # Малі літери
    oled.fill(0)
    ua_text_center(oled, "малі літери:", 0)
    ua_text(oled, "абвгґдеєжз", 0, 12)
    ua_text(oled, "иіїйклмноп", 0, 22)
    ua_text(oled, "рстуфхцчшщ", 0, 32)
    ua_text(oled, "ьюя", 0, 42)
    oled.show()
    time.sleep(4)


def priklad_5_zmishaniy_vmiist():
    """Приклад 5: Змішаний український та англійський текст"""
    print("Приклад 5: Змішаний вміст")
    oled.fill(0)
    
    # Імітація виводу даних з датчиків
    ua_text(oled, "ESP32 + OLED", 0, 0)
    ua_text(oled, "Температура:", 0, 12)
    ua_text(oled, "25.5C", 70, 12)
    ua_text(oled, "Вологість:", 0, 24)
    ua_text(oled, "60%", 70, 24)
    ua_text(oled, "Статус: OK", 0, 40)
    
    oled.show()
    time.sleep(3)


def priklad_6_prokrutka_tekstu():
    """Приклад 6: Анімація прокрутки тексту"""
    print("Приклад 6: Прокрутка тексту")
    
    text = "ПРИВІТ УКРАЇНО! "
    text_width = len(text) * 6  # Приблизна ширина тексту
    
    # Прокручуємо текст справа наліво
    for offset in range(128 + text_width):
        oled.fill(0)
        ua_text(oled, text, 128 - offset, 28)
        oled.show()
        time.sleep(0.03)


def priklad_7_bagatoryad():
    """Приклад 7: Багаторядковий текст"""
    print("Приклад 7: Багаторядковий текст")
    oled.fill(0)
    
    # Список рядків для виводу
    lines = [
        "BFU UA Display",
        "Бібліотека для",
        "відображення",
        "українського",
        "тексту на OLED"
    ]
    
    # Виводимо кожен рядок з відступом
    y = 2
    for line in lines:
        ua_text(oled, line, 0, y)
        y += 10
    
    oled.show()
    time.sleep(4)


def priklad_8_ochyshchennya_fonu():
    """Приклад 8: Текст з очищенням фону"""
    print("Приклад 8: Очищення фону")
    
    # Малюємо фоновий візерунок
    for i in range(0, 128, 4):
        oled.line(i, 0, i, 64, 1)
    oled.show()
    time.sleep(1)
    
    # Виводимо текст з очищеним фоном
    ua_text(oled, "ЧИСТИЙ ФОН", 15, 28, color=1, bg_color=0, clear_bg=True)
    oled.show()
    time.sleep(3)


def zapustyty_vsi_pryklady():
    """Запустити всі приклади по черзі"""
    print("\n" + "="*40)
    print("BFU UA Display - Приклади")
    print("="*40 + "\n")
    
    # Список всіх прикладів
    pryklady = [
        priklad_1_prostiy_tekst,
        priklad_2_tsentrovaniy_tekst,
        priklad_3_masshtabovaniy_tekst,
        priklad_4_ukrainska_abetka,
        priklad_5_zmishaniy_vmiist,
        priklad_6_prokrutka_tekstu,
        priklad_7_bagatoryad,
        priklad_8_ochyshchennya_fonu,
    ]
    
    # Виконуємо кожен приклад
    for priklad in pryklady:
        try:
            priklad()
        except Exception as e:
            print(f"Помилка в {priklad.__name__}: {e}")
        time.sleep(0.5)
    
    # Фінальне повідомлення
    oled.fill(0)
    ua_text_center(oled, "ДЯКУЄМО!", 20)
    ua_text_center(oled, "Thank you!", 35)
    oled.show()
    
    print("\n" + "="*40)
    print("Приклади завершено!")
    print("="*40)


# Запускаємо приклади при виконанні скрипта
if __name__ == "__main__":
    zapustyty_vsi_pryklady()
