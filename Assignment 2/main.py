#!/usr/bin/env python3
"""Generates a QR code image from a user-provided URL."""

import qrcode


def main():
    url = input("Enter a URL: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    img = qrcode.make(url)
    filename = "qrcode.png"
    img.save(filename)
    print(f"QR code saved to {filename}")


if __name__ == "__main__":
    main()
