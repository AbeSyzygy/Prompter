import sys
import random
import time
import select
import platform

if platform.system() == 'Windows':
    import msvcrt
else:
    import select
    import termios
    import tty

from text_parser import parseText

print(f"Configuring for {platform.system()}\n")

file_path = "prompts.txt"
prompts_weighted = parseText(file_path)

interval = int(input("Enter the interval time in seconds: "))
next_run = time.monotonic()

if platform.system() != 'Windows':
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
# Puts the terminal into "cbreak" mode:
# input characters are delivered as soon as they're entered,
# rather than being buffered and delivered in batches.

last_choice = None
running = True
while running:
    if platform.system() == 'Windows':
        if msvcrt.kbhit():
            input_char = msvcrt.getch().decode('utf-8')
            if input_char == 'q':
                running = False
                print("Exiting program...")

    else:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            input_char = sys.stdin.read(1)
            if input_char == 'q':
                running = False
                print("Exiting program...")

    if time.monotonic() >= next_run:
        this_choice = random.choice(prompts_weighted)

        # Retry randomisation if a consecutive repeat occurs 
        while (this_choice == last_choice):
            this_choice = random.choice(prompts_weighted)

        last_choice = this_choice

        print(this_choice)

        next_run = time.monotonic() + interval

    time.sleep(0.01)

if platform.system() != 'Windows':
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)