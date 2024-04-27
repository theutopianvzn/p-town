from threading import Thread, Semaphore

class Philosopher(Thread):
    def __init__(self, index, forks):
        super().__init__()
        self.index = index
        self.left_fork = forks[index]
        self.right_fork = forks[(index + 1) % len(forks)]

    def run(self):
        while True:
            self.think()
            self.pick_up_forks()
            self.eat()
            self.put_down_forks()

    def think(self):
        print(f"Philosopher {self.index} is thinking")
        # Simulate thinking time
        # (replace with your desired thinking duration)
        import time
        time.sleep(2)

    def pick_up_forks(self):
        self.left_fork.acquire()
        print(f"Philosopher {self.index} picked up left fork")
        self.right_fork.acquire()
        print(f"Philosopher {self.index} picked up right fork")

    def eat(self):
        print(f"Philosopher {self.index} is eating")
        # Simulate eating time
        # (replace with your desired eating duration)
        import time
        time.sleep(3)

    def put_down_forks(self):
        self.left_fork.release()
        print(f"Philosopher {self.index} put down left fork")
        self.right_fork.release()
        print(f"Philosopher {self.index} put down right fork")

if __name__ == "__main__":
    num_philosophers = 5
    forks = [Semaphore(1) for _ in range(num_philosophers)]  # One semaphore per fork

    philosophers = [Philosopher(i, forks) for i in range(num_philosophers)]
    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()
