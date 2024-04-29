import threading
import time
import random

NUM_PHILOSOPHERS = 5
NUM_CHOPSTICKS = 5

philosopher_threads = []
chopsticks = [threading.Lock() for _ in range(NUM_CHOPSTICKS)]

def dine(n):
    print(f"Philosopher {n} is thinking.")

    # Philosopher picks up the left chopstick (wait)
    chopsticks[n].acquire()

    # Philosopher picks up the right chopstick (wait)
    chopsticks[(n + 1) % NUM_CHOPSTICKS].acquire()

    # After picking up both the chopsticks, philosopher starts eating
    print(f"Philosopher {n} is eating.")
    time.sleep(3)

    # Philosopher places down the left chopstick (signal)
    chopsticks[n].release()

    # Philosopher places down the right chopstick (signal)
    chopsticks[(n + 1) % NUM_CHOPSTICKS].release()

    # Philosopher finishes eating
    print(f"Philosopher {n} finished eating.")

def main():
    for i in range(NUM_PHILOSOPHERS):
        philosopher_thread = threading.Thread(target=dine, args=(i,))
        philosopher_threads.append(philosopher_thread)
        philosopher_thread.start()

    for philosopher_thread in philosopher_threads:
        philosopher_thread.join()

if __name__ == "__main__":
    main()
