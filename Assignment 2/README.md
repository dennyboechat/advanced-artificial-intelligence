# QR Code Generator

A simple Python app that generates a QR code image from a user-provided URL.

## Requirements

- Python 3

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install "qrcode[pil]"
```

## Usage

```bash
source venv/bin/activate
python3 main.py
```

You will be prompted to enter a URL. The generated QR code will be saved as `qrcode.png` in the current directory.
