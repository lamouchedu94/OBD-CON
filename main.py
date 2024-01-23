import serial
import time

DEVICE = '/dev/rfcomm99'
BAUD_RATE = 38400

try:
    # Connect to the device
    s = serial.Serial(DEVICE, BAUD_RATE)
    print('Connected to', DEVICE)

    # Envoyer la commande ATZ pour réinitialiser l'interface
    s.write(b'ATZ\r')
    time.sleep(2)
    response = s.read_until(b'>', 128)

    for i in range(20) :
        s.write(b'010C\r')
        if i == 0 :
            time.sleep(2)
        else :
            time.sleep(1)
        response = s.read_until(b'>', 128)
        rep = response.decode('utf-8')
        rep1 = rep[11:16].replace(" ", "")
        print(int(rep1, 16)//4 , "rpm")
        #print('Response:', response.decode('utf-8'))

    # Fermer la connexion série
    s.close()

except Exception as e:
    print('Error:', e)