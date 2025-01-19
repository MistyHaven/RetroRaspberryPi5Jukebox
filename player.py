import lgpio
from mfrc522 import SimpleMFRC522

h = lgpio.gpiochip_open(0)
reader = SimpleMFRC522()

try:
    print("Please scan RFID card")
    id = reader.read()
    print("Id for card: ", id)
    
finally:
    lgpio.gpiochip_close(h)
