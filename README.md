# KeeLawg - Simple Keylogger in Python

KeeLawg is a simple keylogger written in Python that captures and logs keystrokes. This tool can be used for educational purposes, cybersecurity research, or as a component in larger projects where monitoring of keystrokes is required. The script also includes functionality to email the log file when the keylogger is stopped.

## Legal Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool is illegal and unethical. The author does not take any responsibility for any misuse of this tool. Always obtain explicit permission before using this keylogger on any device that does not belong to you.

**Use responsibly and ethically.**

## Features

- **Keystroke Logging**: Captures all keypresses and logs them to a file.
- **Special Key Handling**: Logs special keys (like `Esc`, `Shift`, etc.) with appropriate labels.
- **Email Log File**: Automatically sends the log file via email when the keylogger is stopped.
- **Verbose Output**: Provides real-time updates in the console about what the keylogger is doing.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/un1xr00t/KeeLawg.git
    cd KeeLawg
    ```

2. **Install the Required Dependencies**:
    This project relies on the `pynput` package to capture keyboard input. Install it using pip:

    ```bash
    pip install pynput
    ```

3. **Run the Keylogger**:
    ```bash
    python keylogger.py
    ```

4. **Stopping the Keylogger**:
    - Press the `Esc` key to stop the keylogger. The log file will be sent to the configured email address, and the script will terminate.

## Integration into Other Programs

You can integrate KeeLawg into any Python-based project that requires keystroke logging. Simply import the relevant functions and modify the script to fit your needs.

**Example**:
- Import the `on_press` and `on_release` functions into your existing script.
- Customize the logging and email functionality as per your requirements.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

