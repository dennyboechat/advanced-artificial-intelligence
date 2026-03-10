#!/usr/bin/env python3
"""Generates a QR code image from a user-provided URL. The QR code is saved as a PNG file."""

import qrcode


def main():
    # Prompt the user for a URL
    url = input("Enter a URL: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    # Generate the QR code and save it as a PNG
    img = qrcode.make(url)
    filename = "qrcode.png"
    img.save(filename)
    print(f"QR code saved to {filename}")


if __name__ == "__main__":
    main()
