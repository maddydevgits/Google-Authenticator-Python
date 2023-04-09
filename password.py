import time
import pyotp
import qrcode

key="MadhuforGeeksIsBestForEverything"

totp = pyotp.TOTP(key)

# verifying the code
while True:
    print(totp.verify(input(("Enter the Code : "))))
