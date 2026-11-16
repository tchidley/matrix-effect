import random
import shutil
import time

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
GREEN = "\033[92m"
RESET = "\033[0m"

columns = shutil.get_terminal_size().columns
drops = [0] * columns

try:
    while True:
        line = ""
        for i in range(columns):
            if drops[i] > 0:
                line += GREEN + random.choice(chars) + RESET
                drops[i] -= 1
            else:
                line += " "
                if random.random() > 0.985:
                    drops[i] = random.randint(5, 20)
        print(line)
        time.sleep(0.05)
except KeyboardInterrupt:
    print(RESET + "\nStopped.")
