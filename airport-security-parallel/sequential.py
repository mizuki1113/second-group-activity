import time

def screen_passenger(passenger_id):
    time.sleep(0.01)
    time.sleep(0.01)
    time.sleep(0.01)
    return passenger_id

def sequential_screening(passengers):
    results = []
    for p in passengers:
        results.append(screen_passenger(p))
    return results

if __name__ == "__main__":
    passengers = list(range(1000))

    start = time.time()
    sequential_screening(passengers)
    end = time.time()

    sequential_time = end - start
    print("Sequential Time:", sequential_time)