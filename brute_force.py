from itertools import product
from time import perf_counter
import subprocess

def main():
    start_time = perf_counter()
    perm_set = product(range(0,10), repeat=6)
    for permutation in perm_set:
        new_input = " ".join(map(str, permutation))
        curr_input = f"Verbosity leads to unclear, inarticulate things.\n1 2 4 8 16 32\n0 z 208\n10 37\n5 115\n{new_input}\n"
        process = subprocess.Popen(["./bomb"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = process.communicate(input=curr_input.encode())[0]
        if "BOOM!!!" not in output.decode():
            seconds = perf_counter() - start_time
            print(f"{new_input} passed")
            print(f"{seconds:0.4f} seconds")
            return
        print(f"{new_input} failed")

if __name__ == "__main__":
    main()
