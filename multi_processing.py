import time
import random
from multiprocessing import Process


def calculate_prime_factor(n):
    prime_fac = []
    d = 2
    while d**2 <= n:
        while n % d == 0:
            prime_fac.append(d)
            n //= d
        d += 1
    if n > 1:
        prime_fac.append(n)

    return prime_fac


def execute():
    for i in range(1000):
        rand = random.randint(2000, 2000000)
        print(calculate_prime_factor(rand))


def main():
    t0 = time.time()
    procs = []
    # execute()
    for i in range(10):
        proc = Process(target=execute, args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    t1 = time.time()
    print(t1-t0)


if __name__ == "__main__":
    main()
