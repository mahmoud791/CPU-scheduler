
from priority_queue import PriorityQueue

def priority_nonpremative(time_schedule):

    all_at_sametime = True

    for process in time_schedule:
        if process.arrival_time != time_schedule[0].arrival_time:
            all_at_sametime = False
            break

    if all_at_sametime:
        time_schedule.sort(key=lambda x:x.priority)

    time = 0
    index = 0
    current_procces = None
    queue = PriorityQueue()

    while True:

        if index < len(time_schedule):
            if time >= time_schedule[index].arrival_time :    


                new_process = time_schedule[index]

                if current_procces == None:
                    current_procces = new_process
                    current_procces.addMark(time)
                else:
                    queue.put(new_process)
                    
                    
                
                index = index + 1 

        
        if current_procces == None :                     # if the CPU is still empty from the begining
    
            time = time + 1                              # just pass time and skip this iteration in the loop
            continue


        if current_procces.time_remaining <= 0:
            
            current_procces.addMark(time)

            if queue.isEmpty():
                break
            else:
                current_procces = queue.get()
                current_procces.addMark(time)
            

        current_procces.pass_time()                      
        time = time + 1
    
