![Python](https://img.shields.io/badge/Python-3.x-blue) 
![MIT License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This Python script is an advanced SSH brute force attack tool designed to crack the password of a given SSH target by attempting multiple passwords in parallel. It utilizes multi-threading for faster attacks, supports custom SSH ports, and includes robust error handling and logging features.

---
## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Example Output](#example-output)
5. [Notes](#notes)
6. [Example Password File Format](#example-password-file-format)
7. [Contributing](#contributing)
8. [License](#license)
9. [Disclaimer](#disclaimer)

---

## Features

- Multi-threading for faster brute force attempts.
- Customizable SSH port and number of threads.
- Logging of all attempts (successful and failed) to a log file.
- Timeout handling for slow server responses.
- Enhanced error handling for network or connection issues.
- Simple and efficient password file queue management.

---

## Requirements

- **Python 3.x**
- **Paramiko Library**

You can install the required library by running:

```bash
pip install paramiko
```
## Usage

1. Clone this repository or download the script directly.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:

```bash
python ssh_bruteforce.py
```
You will be prompted to input the following:

- **Target IP Address**: The IP address of the SSH server you're attacking.
- **Username**: The username you want to brute force.
- **Password File**: Path to the file containing a list of passwords to try.
- **SSH Port (Optional)**: The port number where SSH is running (default is 22).
- **Number of Threads (Optional)**: The number of threads for concurrent password attempts (default is 5).
```bash
Please enter target IP address: 192.168.1.100
Please enter username to bruteforce: admin
Please enter location of the password file: /path/to/passwords.txt
Please enter SSH port (default is 22): 22
Please enter number of threads (default is 5): 10
```
## Example Output

If the script finds the correct password, it will output:

```yaml
Password found: your_password
```
If no password is found, or all attempts fail, it will print:
```c
Brute force attack completed. Check ssh_bruteforce.log for details.
```
The ssh_bruteforce.log file will contain all attempts, errors, and successes.
## Notes

- **Legal Warning**: This script is intended for educational purposes only and should only be used to test the security of systems you have permission to access. Unauthorized access to computer systems is illegal and unethical.
- The timeout for each connection attempt is set to 5 seconds. You can adjust this inside the code if needed.

## Example Password File Format

Ensure your password file is structured with one password per line:

```plaintext
password1
password2
password3
...
```
## Contributing

If you want to contribute or suggest improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer

This tool is provided as-is and for educational purposes only. The author is not responsible for any misuse or damage caused by this tool.

