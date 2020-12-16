import random

from tqdm import tqdm

import start

from time import sleep


def gen():
    loop_cnt = int(input("How many times should this loop?\n> "))
    lower_range = int(input("Lowest random number?\n> "))
    upper_range = int(input("Highest random number?\n> "))
    file = open(start.dir_path, "w")
    for _ in tqdm(range(1, loop_cnt + 1), desc="Progress", leave=True, unit="lines"):
        file.write(str(random.randint(lower_range, upper_range)) + "\n")
        sleep(0.0000001)
