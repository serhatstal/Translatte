# 🌍 Translatte — In-Game Quick Translator

**Translatte** is a lightweight Python tool designed to streamline in-game communication. With a single hotkey (`Ctrl + B`), it automatically selects, translates, and pastes your chat messages—making multilingual gameplay faster and smoother.

---

## ✨ Features

* ⚡ One-key instant translation (`Ctrl + B`)
* 🌐 Supports multiple languages via `deep-translator`
* 🎮 Works with PC games like Valorant
* 🧩 Minimal, fast, and easy to configure

---

## ⚠️ Important Notice (Anti-Cheat & Security)

> 🛡️ **Translatte does NOT modify game files, memory, or input pipelines.**
> It only uses system-level hotkeys and clipboard access.

However:

* 🔸 Simulating `Ctrl + A` and `Ctrl + V` may be flagged as **macro behavior** by some anti-cheat systems (e.g., Riot Vanguard).
* 🔸 For **maximum safety**, disable automation:

  * Set `SIMULATE_SELECT_ALL = False`
  * Set `SIMULATE_PASTE = False`
  * Use manually: `Ctrl + C → Ctrl + B → Ctrl + V`
* 🔸 Use at your **own risk**. This is not an official tool.

---

## 🚀 Installation

### 1. Requirements

* Python **3.8+**
* Windows **10/11** (required for global hotkeys)

---

### 2. Clone & Install Dependencies

```bash
git clone https://github.com/your-username/translatte.git
cd translatte
pip install -r requirements.txt
```

#### 📦 `requirements.txt`

```
keyboard==0.13.5
pyperclip==1.9.0
deep-translator==1.11.4
```

---

### 3. Run the Application

> ⚠️ Must be run as **Administrator** (required for global keyboard hooks)

```bash
python translatte.py
```

💡 Tip: Make sure your main file is named `translatte.py`.

---

## 🎮 Usage

1. Type your message in-game (or anywhere).
2. Press **Ctrl + B**
3. Done — your message is translated and pasted instantly.

📝 **Recommended:** Test in Notepad first to fine-tune delays and translation accuracy.

---

## ⚙️ Configuration

Edit the `SETTINGS` section inside `translatte.py`:

```python
HOTKEY = "ctrl+b"              # Trigger hotkey
SIMULATE_SELECT_ALL = True     # Auto Ctrl+A
SIMULATE_PASTE = True          # Auto Ctrl+V

DELAY_SELECT = 0.15            # After Ctrl+A
DELAY_COPY = 0.25              # Clipboard sync delay
DELAY_PASTE = 0.15             # Before paste

SOURCE_LANG = "tr"             # Source language
TARGET_LANG = "en"             # Target language
```

💡 Adjust delays depending on system performance and game responsiveness.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your branch

   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes

   ```bash
   git commit -m "feat: add new feature"
   ```
4. Push and open a Pull Request

💬 Feedback, bug reports, and new language support are highly appreciated.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---

Developed with care to make in-game communication faster and easier. 🎮💬
