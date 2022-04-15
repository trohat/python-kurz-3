

import time

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        time.sleep(1)
    except KeyboardInterrupt:
        print("Haha, máš smůlu, tenhle program nejde zastavit...")
    
