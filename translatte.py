import keyboard
import pyperclip
import time
import logging
from deep_translator import MyMemoryTranslator, GoogleTranslator

# ─── SETTINGS ─────────────────────────────────────────────
HOTKEY = "ctrl+b"

# 🔒 SAFETY: Set to False to disable simulation (safer, clipboard only)
SIMULATE_SELECT_ALL = True
SIMULATE_PASTE = True

DELAY_SELECT = 0.15   # Delay after Ctrl+A
DELAY_COPY = 0.25     # Clipboard update delay after Ctrl+C
DELAY_PASTE = 0.15    # Delay before Ctrl+V
# ──────────────────────────────────────────────────────────

logging.basicConfig(level=logging.DEBUG, format="🔍 %(message)s")
last_trigger = 0.0
COOLDOWN = 0.6

def safe_translate(text: str) -> str:
    text_clean = text.strip()
    for cls in [MyMemoryTranslator, GoogleTranslator]:
        try:
            res = cls(source='tr', target='en').translate(text_clean)
            if res and len(res.strip()) > 0:
                return res.strip()
        except Exception as e:
            logging.debug(f"⚠️ {cls.__name__}: {e}")
    raise RuntimeError("Translation failed. Check your internet connection.")

def on_hotkey():
    global last_trigger
    now = time.time()
    if now - last_trigger < COOLDOWN:
        return
    last_trigger = now

    try:
        # 1. Backup current clipboard (for better user experience)
        old_clip = pyperclip.paste()

        # 2. Select all (optional)
        if SIMULATE_SELECT_ALL:
            logging.debug("⌨️ Simulating Ctrl+A...")
            keyboard.press_and_release('ctrl+a')
            time.sleep(DELAY_SELECT)

        # 3. Copy
        logging.debug("⌨️ Simulating Ctrl+C...")
        keyboard.press_and_release('ctrl+c')
        time.sleep(DELAY_COPY)

        # 4. Read from clipboard
        text = pyperclip.paste().strip()
        logging.debug(f"📋 Captured text: '{text}'")

        if not text or len(text) < 2:
            logging.warning("⚠️ Empty text. Ctrl+A/C may have failed. Try manual copy and retry.")
            return

        # 5. Translate
        logging.info("🌐 Translating...")
        translated = safe_translate(text)
        logging.info(f"✅ Result: {translated}")

        # 6. Copy translated text to clipboard
        pyperclip.copy(translated)
        time.sleep(0.05)

        # 7. Paste (optional)
        if SIMULATE_PASTE:
            logging.debug("⌨️ Simulating Ctrl+V...")
            keyboard.press_and_release('ctrl+v')
            time.sleep(DELAY_PASTE)

        # 8. Restore previous clipboard (optional, UX improvement)
        pyperclip.copy(old_clip)

    except Exception as e:
        logging.error(f"💥 ERROR: {e}")

def main():
    print("🎮 In-Game Auto Translator v5")
    print(f"🔑 Hotkey: {HOTKEY}")
    mode = "AUTOMATIC (Ctrl+A → Ctrl+C → Translate → Ctrl+V)" if SIMULATE_SELECT_ALL and SIMULATE_PASTE else "SEMI-AUTOMATIC (Clipboard only)"
    print(f"📌 Mode: {mode}")
    print("⚠️  Run as ADMIN for global hotkeys & simulation!")
    print("🛑 Exit: CTRL+C\n")

    try:
        keyboard.add_hotkey(HOTKEY, on_hotkey, suppress=False)
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        logging.critical(f"Startup error: {e}")
        print("💡 Solution: Run the terminal as Administrator and try again.")

if __name__ == "__main__":
    main()
