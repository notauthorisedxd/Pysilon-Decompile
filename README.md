# PySilon Token Extractor

A simple tool to extract Discord tokens from `.exe` files packaged with PyInstaller. This tool is primarily for educational purposes and should not be used for malicious activities.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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
