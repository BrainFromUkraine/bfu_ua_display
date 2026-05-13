# bfu_ua_display: Ukrainian Text Rendering Library for MicroPython

## Summary

Add `bfu_ua_display` package - a lightweight library for rendering Ukrainian text on displays commonly used with ESP32 and MicroPython projects.

## What the Package Does

`bfu_ua_display` provides Ukrainian alphabet support for MicroPython displays. Standard MicroPython display libraries (like `framebuf.text()`) do not include Ukrainian characters (А, Б, В, Г, Ґ, Д, Е, Є, Ж, З, И, І, Ї, Й, etc.), making it impossible to display Ukrainian text properly. This library solves that problem with a custom 5x7 bitmap font containing all 33 Ukrainian letters (uppercase and lowercase).

## Why It Is Useful

- **Language Support**: Enables Ukrainian language support in embedded MicroPython projects
- **Educational**: Used in Ukrainian maker community and educational content
- **Lightweight**: Optimized for ESP32 memory constraints (~2-3 KB)
- **Display Agnostic**: Works with any display supporting the `pixel()` method
- **Production Ready**: Clean, modular architecture with comprehensive documentation

## Supported Hardware/Display Interface

**Tested Displays:**
- SSD1306 OLED (128x64, 128x32) via I2C/SPI

**Compatible With:**
- Any display implementing `pixel(x, y, color)` method
- Optional `fill_rect()` for optimization
- Optional `show()` for buffered displays

**Target Platforms:**
- ESP32 (primary)
- Any MicroPython-compatible board with display support

## Public API

The package exports three main functions:

```python
from bfu_ua_display import ua_text, ua_text_center, ua_text_scaled
```

### Functions

**`ua_text(display, text, x, y, color=1, bg_color=0, clear_bg=False)`**
- Render text at specified position with Ukrainian character support
- Returns: Total width of rendered text in pixels

**`ua_text_center(display, text, y, color=1, bg_color=0, clear_bg=False, display_width=128)`**
- Render text centered horizontally on the display
- Returns: X coordinate where text was rendered

**`ua_text_scaled(display, text, x, y, scale=2, color=1, bg_color=0, clear_bg=False)`**
- Render text with scaling (2x, 3x, etc.)
- Returns: Total width of rendered text in pixels

## Basic Usage Example

```python
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from bfu_ua_display import ua_text, ua_text_center

# Initialize display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Draw Ukrainian text
ua_text(oled, "ПРИВІТ УКРАЇНО!", 0, 0)
ua_text_center(oled, "BFU Electronics", 28)

# Update display
oled.show()
```

## Supported Characters

- **Ukrainian Alphabet**: All 33 letters (А-Я, а-я including Ґ, Є, І, Ї, Й)
- **English Alphabet**: A-Z, a-z
- **Numbers**: 0-9
- **Symbols**: Common punctuation and special characters

## License

MIT License - Compatible with MicroPython's license

## Additional Information

- **Repository**: https://github.com/BrainFromUkraine/bfu_ua_display
- **Documentation**: Comprehensive README with examples
- **Version**: 0.1.0
- **Author**: BFU Electronics
- **Community**: Used in Ukrainian educational YouTube content about ESP32 and MicroPython

## Package Structure

```
micropython/bfu_ua_display/
├── manifest.py              # Package metadata
├── README.md                # Full documentation
├── LICENSE                  # MIT License
└── bfu_ua_display/
    ├── __init__.py          # Public API exports
    ├── font5x7.py           # 5x7 bitmap font with Ukrainian characters
    ├── text_engine.py       # Core rendering functions
    └── utils.py             # Utility functions
```

## Testing

The package has been tested on:
- ESP32 with MicroPython v1.19+
- SSD1306 OLED displays (I2C interface)
- Real-world projects and educational content

## Notes

This package fills a gap in the MicroPython ecosystem by providing proper Ukrainian language support for embedded displays, making MicroPython more accessible to Ukrainian developers and students.
