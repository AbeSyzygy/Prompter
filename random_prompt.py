import sys
import random
import time
import keyboard

# Set the file path of the text file containing the list of prompts
file_path = "prompts.txt"

# Read each line from the text file into an array
with open(file_path, "r") as f:
    sentences = f.readlines()

# Remove leading and trailing whitespace characters from the string
sentences = [s.strip() for s in sentences]

# Store an index of chance of appearance in an array mapping to the phrase list
chance_idx = []
i = 0
for s in sentences:
    if ":" in s:
        num_pos = (sentences[i]).index(":") + 1
        chance_idx.append(int(s[num_pos]))
        s = s[:num_pos-1]
        sentences[i] = s
    else:
        chance_idx.append(1)
    # print("sentence: " + sentences[i] + ", chance: " + str(chance_idx[i]) + "\n")
    i = i + 1

sentences_weighted = []
for i, s in enumerate(sentences):
    for chance in range(chance_idx[i]):
        sentences_weighted.append(s)

interval = int(input("Enter the interval time in seconds: "))


last_choice = None
running = True
while running:
    if keyboard.is_pressed('q'):
        running = False
        print('Exiting program...')

    this_choice = random.choice(sentences_weighted)
 
    # print("this_choice (before): " + this_choice)
    # if last_choice:
    #     print("last_choice: " + str(last_choice))

    # Retry randomisation if a consecutive repeat occurs 
    while (this_choice == last_choice):
        # print("this_choice == last_choice")
        this_choice = random.choice(sentences_weighted)

    last_choice = this_choice

    print(this_choice)

    time.sleep(interval)
