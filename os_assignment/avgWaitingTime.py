
def get_avg_WaitingTime(time_schedule):

    sum = 0

    for process in time_schedule:
        sum += process.get_waiting_time()

    avg = sum/len(time_schedule)

    return avg
