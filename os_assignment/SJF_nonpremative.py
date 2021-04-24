from process import*



def SJF_nonpremative(time_schedule):



    for e in range(len(time_schedule)):

                if time_schedule[0].arrival_time == time_schedule[e].arrival_time:

                    if time_schedule[0].duration > time_schedule[e].duration:

                        temp = time_schedule[e]

                        #print(temp.duration)

                        time_schedule[e] = time_schedule[0]

                        time_schedule[0] = temp

                        #print(time_schedule[e].duration)



    time = time_schedule[0].arrival_time



    



    for i in range(len(time_schedule)):



        time_schedule[i].addMark(time)

        time = time + time_schedule[i].duration

        time_schedule[i].addMark(time)

        if i < len(time_schedule)-1:

            #print("awl if")

            min = time_schedule[i+1].duration

            c=i+1

            for j in range(c,len(time_schedule)):

                if time > time_schedule[j].arrival_time:

                    #print('tany if')

                    if min > time_schedule[j].duration:

                        #print('talt if')

                        min = time_schedule[j].duration

                        temp = time_schedule[c]

                        #print(temp.duration)

                        time_schedule[c] = time_schedule[j]

                        time_schedule[j] = temp

                        #print(time_schedule[c].duration)
        
        






                
             