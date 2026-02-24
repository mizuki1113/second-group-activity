import time
from multiprocessing import Pool, cpu_count

def screen_passenger(passenger_id):
    time.sleep(0.01)
    time.sleep(0.01)
    time.sleep(0.01)
    return passenger_id

if __name__ == "__main__":
    passengers = list(range(1000))

    start = time.time()

    with Pool(cpu_count()) as pool:
        pool.map(screen_passenger, passengers)

    end = time.time()

    parallel_time = end - start
    print("Parallel Time:", parallel_time)
    print("CPU Cores Used:", cpu_count())