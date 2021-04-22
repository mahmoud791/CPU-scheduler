from process import*

def FCFS(time_schedule):

    time = time_schedule[0].arrival_time

    

    for process in time_schedule:

       
        process.addMark(time)
        time = time + process.duration
        process.addMark(time)
        
        
        

