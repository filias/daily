import multiprocessing
import sys
import time


def func(num):
    print(f"Sleeping for {num}")
    time.sleep(num)


if __name__ == "__main__":
    breakpoint()
    data = sys.stdin.readlines()
    data = data[0].split()

    processes = [multiprocessing.Process(target=func, args=(int(num),)) for num in data]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
