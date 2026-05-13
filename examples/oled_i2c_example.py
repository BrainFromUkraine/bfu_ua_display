"""
BFU UA Display - SSD1306 OLED I2C Example
==========================================

This example demonstrates how to use the BFU UA Display library
with an SSD1306 OLED display connected via I2C.

Hardware Setup:
- ESP32 board
- SSD1306 OLED display (128x64 pixels)
- I2C connection:
  - SCL -> GPIO 22
  - SDA -> GPIO 21
  - VCC -> 3.3V
  - GND -> GND

Author: BFU Electronics
License: MIT
"""

from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from bfu_ua_display import ua_text, ua_text_center, ua_text_scaled
import time


# Initialize I2C and OLED display
# Adjust pins according to your ESP32 board
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)


def example_basic_text():
    """Example 1: Basic Ukrainian text rendering"""
    print("Example 1: Basic text")
    oled.fill(0)
    
    ua_text(oled, "ПРИВІТ!", 0, 0)
    ua_text(oled, "Hello World", 0, 10)
    ua_text(oled, "Україна 2026", 0, 20)
    
    oled.show()
    time.sleep(3)


def example_centered_text():
    """Example 2: Centered text"""
    print("Example 2: Centered text")
    oled.fill(0)
    
    ua_text_center(oled, "УКРАЇНА", 10)
    ua_text_center(oled, "BFU Electronics", 28)
    ua_text_center(oled, "2026", 46)
    
    oled.show()
    time.sleep(3)


def example_scaled_text():
    """Example 3: Scaled text (2x size)"""
    print("Example 3: Scaled text")
    oled.fill(0)
    
    ua_text_scaled(oled, "ПРИВІТ", 10, 10, scale=2)
    ua_text(oled, "Normal size text", 0, 40)
    
    oled.show()
    time.sleep(3)


def example_full_alphabet():
    """Example 4: Display Ukrainian alphabet"""
    print("Example 4: Ukrainian alphabet")
    
    # Uppercase
    oled.fill(0)
    ua_text_center(oled, "UPPERCASE:", 0)
    ua_text(oled, "АБВГҐДЕЄЖЗ", 0, 12)
    ua_text(oled, "ИІЇЙКЛМНОП", 0, 22)
    ua_text(oled, "РСТУФХЦЧШЩ", 0, 32)
    ua_text(oled, "ЬЮЯ", 0, 42)
    oled.show()
    time.sleep(4)
    
    # Lowercase
    oled.fill(0)
    ua_text_center(oled, "lowercase:", 0)
    ua_text(oled, "абвгґдеєжз", 0, 12)
    ua_text(oled, "иіїйклмноп", 0, 22)
    ua_text(oled, "рстуфхцчшщ", 0, 32)
    ua_text(oled, "ьюя", 0, 42)
    oled.show()
    time.sleep(4)


def example_mixed_content():
    """Example 5: Mixed Ukrainian and English"""
    print("Example 5: Mixed content")
    oled.fill(0)
    
    ua_text(oled, "ESP32 + OLED", 0, 0)
    ua_text(oled, "Температура:", 0, 12)
    ua_text(oled, "25.5C", 70, 12)
    ua_text(oled, "Вологість:", 0, 24)
    ua_text(oled, "60%", 70, 24)
    ua_text(oled, "Статус: OK", 0, 40)
    
    oled.show()
    time.sleep(3)


def example_scrolling_text():
    """Example 6: Scrolling text animation"""
    print("Example 6: Scrolling text")
    
    text = "ПРИВІТ УКРАЇНО! "
    text_width = len(text) * 6  # Approximate width
    
    for offset in range(128 + text_width):
        oled.fill(0)
        ua_text(oled, text, 128 - offset, 28)
        oled.show()
        time.sleep(0.03)


def example_multi_line():
    """Example 7: Multi-line text display"""
    print("Example 7: Multi-line text")
    oled.fill(0)
    
    lines = [
        "BFU UA Display",
        "Бібліотека для",
        "відображення",
        "українського",
        "тексту на OLED"
    ]
    
    y = 2
    for line in lines:
        ua_text(oled, line, 0, y)
        y += 10
    
    oled.show()
    time.sleep(4)


def example_clear_background():
    """Example 8: Text with background clearing"""
    print("Example 8: Background clearing")
    
    # Draw some background pattern
    for i in range(0, 128, 4):
        oled.line(i, 0, i, 64, 1)
    oled.show()
    time.sleep(1)
    
    # Draw text with cleared background
    ua_text(oled, "CLEAR BG", 20, 28, color=1, bg_color=0, clear_bg=True)
    oled.show()
    time.sleep(3)


def run_all_examples():
    """Run all examples in sequence"""
    print("\n" + "="*40)
    print("BFU UA Display - Examples")
    print("="*40 + "\n")
    
    examples = [
        example_basic_text,
        example_centered_text,
        example_scaled_text,
        example_full_alphabet,
        example_mixed_content,
        example_scrolling_text,
        example_multi_line,
        example_clear_background,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"Error in {example.__name__}: {e}")
        time.sleep(0.5)
    
    # Final message
    oled.fill(0)
    ua_text_center(oled, "ДЯКУЄМО!", 20)
    ua_text_center(oled, "Thank you!", 35)
    oled.show()
    
    print("\n" + "="*40)
    print("Examples completed!")
    print("="*40)


# Run examples when script is executed
if __name__ == "__main__":
    run_all_examples()
