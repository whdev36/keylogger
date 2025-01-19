# Keylogger 🔐

[![GitHub repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/whdev36/keylogger.git) [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

## Overview 🔧
A basic keylogger implementation for educational and testing purposes. This project logs keystrokes using Python and provides a Flask-based interface for monitoring.

**Warning:** Use this tool responsibly and only with proper authorization. Unauthorized use may violate local, state, or federal laws.

## Features ✨
- **Keystroke logging**: Captures keypresses from the user's keyboard.
- **Flask integration**: Provides a web-based interface for monitoring logs.
- **Executable version**: A compiled Windows executable for easy deployment.

## Installation 📬

1. Clone the repository:
   ```bash
   git clone https://github.com/whdev36/keylogger.git
   cd keylogger
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Build an executable (optional):
   ```bash
   pyinstaller --onefile basic_logger.py
   ```

## File Structure 🗁
- **basic_logger.py**: Core keylogger logic.
- **app.py**: Flask application for monitoring logs.
- **dist/basic_logger.exe**: Compiled executable for Windows.

## Dependencies 📚
This project uses the following Python libraries:
- `altgraph==0.17.4`
- `blinker==1.9.0`
- `certifi==2024.12.14`
- `charset-normalizer==3.4.1`
- `click==8.1.8`
- `colorama==0.4.6`
- `Flask==3.1.0`
- `Flask-SQLAlchemy==3.1.1`
- `greenlet==3.1.1`
- `idna==3.10`
- `itsdangerous==2.2.0`
- `Jinja2==3.1.5`
- `MarkupSafe==3.0.2`
- `packaging==24.2`
- `pefile==2023.2.7`
- `pyinstaller==6.11.1`
- `pyinstaller-hooks-contrib==2025.0`
- `pynput==1.7.7`
- `pywin32-ctypes==0.2.3`
- `requests==2.32.3`
- `setuptools==75.8.0`
- `six==1.17.0`
- `SQLAlchemy==2.0.37`
- `typing_extensions==4.12.2`
- `urllib3==2.3.0`
- `Werkzeug==3.1.3`

## Usage ⚙️
1. Run the keylogger using `basic_logger.py`.
2. Access the Flask monitoring interface by navigating to the provided URL (default: `http://127.0.0.1:5000`).
3. View captured logs and manage data via the interface.

## License 📚
This project is licensed under the [MIT License](./LICENSE).

## Disclaimer ⚠️
This project is intended for educational purposes only. The author is not responsible for any misuse or damages caused by this tool.

