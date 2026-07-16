import qrcode
import os


def generate_qr(data):

    folder = "qr_codes"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = f"{folder}/{data}.png"

    qr = qrcode.make(data)

    qr.save(file_path)

    return file_path