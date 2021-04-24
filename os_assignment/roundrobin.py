from priority_queue import SimpleQueue

def RoundRobin(time_schedule,quantum):

    time = 0
    index = 0
    quant = quantum
    current_procces = None
    queue = SimpleQueue()


    while True:

        #print('time = ', time ,' quant=',quant)

        if index < len(time_schedule):
            if time >= time_schedule[index].arrival_time :

                new_process = time_schedule[index]

                if current_procces == None:
                    current_procces = new_process
                    current_procces.addMark(time)

                else:
                    queue.put(new_process)

                index = index +1


        if current_procces == None :                     # if the CPU is still empty from the begining
    
            time = round(time + 0.1 ,1)                             # just pass time and skip this iteration in the loop
            continue

        

        if current_procces.time_remaining <= 0:
            
            current_procces.addMark(time)

            
            if queue.isEmpty():
                break

            else:
                current_procces = queue.get()
                current_procces.addMark(time)
                quant = quantum
        


        if quant <= 0:
            current_procces.addMark(time)
            queue.put(current_procces)
            current_procces = queue.get()
            current_procces.addMark(time)
            quant = quantum

        

        current_procces.pass_time()                      
        time = round(time + 0.1 ,1)
        quant = round(quant - 0.1 ,1)


         


        
