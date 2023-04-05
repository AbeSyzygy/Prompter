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

print(f"Configuring for {platform.system()}\n")

# ////////////////////////////
# To Do : Refactor the .txt file-parsing code into a singer parse function.
# ////////////////////////////

file_path = "prompts.txt"

with open(file_path, "r") as f:
    sentences = f.readlines()

sentences = [s.strip() for s in sentences]

weight_idx = []
i = 0
for s in sentences:
    if ":" in s:
        num_pos = (sentences[i]).index(":") + 1
        weight_idx.append(int(s[num_pos]))
        s = s[:num_pos-1]
        sentences[i] = s
    else:
        weight_idx.append(1)
    i = i + 1

sentences_weighted = []
for i, s in enumerate(sentences):
    for chance in range(weight_idx[i]):
        sentences_weighted.append(s)

interval = int(input("Enter the interval time in seconds: "))
next_run = time.monotonic()

if platform.system() != 'Windows':
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
# Puts the terminal into "cbreak" mode:
# input characters are delivered to the program as soon as they're entered,
# rather than being buffered and delivered in batches.
# This ensures that the program can detect keyboard input as soon as it's entered,
# rather than waiting for a newline character or other input event.

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
        this_choice = random.choice(sentences_weighted)

        # Retry randomisation if a consecutive repeat occurs 
        while (this_choice == last_choice):
            this_choice = random.choice(sentences_weighted)

        last_choice = this_choice

        print(this_choice)

        next_run = time.monotonic() + interval

    time.sleep(0.01)

if platform.system() == 'Windows':
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)