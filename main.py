import keyboard
import time
from datetime import datetime

x = datetime.now()

rok = str(x.year)
miesiac = str(x.month)
dzien = str(x.day)

result = 0

def file():
    global result
    global x
    try:
        with open(f'C:/Users/wixax/Desktop/thehunter_KILLKI/grind.txt','a') as f:
            f.write('\n'+rok+" "+miesiac+" "+dzien+" "+f' {result}' + '\n')
    except FileNotFoundError:
        print("niedziala")
    f.close()

def on_key_event(e):
    global result

    if e.name == "-":
        result -= 0.5
    if e.name == "=":
        result += 0.5

    print(f'Result: {result}')

def main():
    # Ustawienie funkcji, która będzie wywoływana przy zdarzeniach klawiatury

    keyboard.hook(on_key_event)

    try:

        # Pętla nieskończona, aby program działał w tle
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Przerwanie programu po naciśnięciu Ctrl+C
        pass
    finally:
        # Zakończenie programu
        keyboard.unhook_all()

if __name__ == "__main__":
    main()
    file()