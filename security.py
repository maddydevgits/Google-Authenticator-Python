import time
import pyotp
import qrcode

key="MadhuforGeeksIsBestForEverything"
uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Padmaja_K',
	issuer_name='MakeSkilled')

print(uri)

# Qr code generation step
qrcode.make(uri).save("qr.png")
