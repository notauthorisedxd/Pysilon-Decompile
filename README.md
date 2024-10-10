# PySilon Decompiler and Token Extractor
```


______      _____ _ _               _____     _                _____     _                  _             
| ___ \    /  ___(_) |             |_   _|   | |              |  ___|   | |                | |            
| |_/ /   _\ `--. _| | ___  _ __     | | ___ | | _____ _ __   | |____  _| |_ _ __ __ _  ___| |_ ___  _ __ 
|  __/ | | |`--. \ | |/ _ \| '_ \    | |/ _ \| |/ / _ \ '_ \  |  __\ \/ / __| '__/ _` |/ __| __/ _ \| '__|
| |  | |_| /\__/ / | | (_) | | | |   | | (_) |   <  __/ | | | | |___>  <| |_| | | (_| | (__| || (_) | |   
\_|   \__, \____/|_|_|\___/|_| |_|   \_/\___/|_|\_\___|_| |_| \____/_/\_\\__|_|  \__,_|\___|\__\___/|_|   
       __/ |                                                                                              
      |___/                                                                                               


```


A tool to extract Discord tokens from `.exe` files which are made with the malware Pysilon. Pysilon can be found at this link https://github.com/mategol/PySilon-malware



It turns built .exe versions of pysilon into a .pyc (using utils/pyinstxtractor.py) and then reads the bytecode from the .pyc, decrypts strings and gets the token.

![image](https://github.com/user-attachments/assets/7bf66ecd-ad93-4004-88e3-ddc1e5027968)

                     ↓
                     
![image](https://github.com/user-attachments/assets/83e94d88-4613-4c11-a2ca-d3d1c3cc1a7d)

                     ↓
                     
![image](https://github.com/user-attachments/assets/50e33bdc-ec97-4e4f-a213-b5dacf1528c3)
                     
                     

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)

## Features

- Decompiles PyInstaller executables to extract `.pyc` files.
- Scans for Discord tokens in bytecode.
- Deletes extracted files after processing to keep your workspace clean.

## Requirements

Make sure you have Python 3.6 or higher installed on your machine. You will also need to install the required Python packages.

### Required Packages

- [colorama](https://pypi.org/project/colorama/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/notauthorisedxd/Pysilon-Decompile.git
   cd Pysilon-Decompile
   ```
