import time

start = time.perf_counter()

file = open("input.txt")

end = time.perf_counter()

print(f"--- process took {end - start:0.4f} seconds ---")
