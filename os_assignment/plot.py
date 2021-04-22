import matplotlib.pyplot as plt
import random




def Plot(time_schedule):

    y_axis = []

    


    for process in time_schedule:
        list_of_pairs = []
        for i in range(len(process.marks)):
            if i%2 == 0:
                pair = (process.marks[i],process.marks[i+1]-process.marks[i])
                list_of_pairs.append(pair)
            

        y_axis.append(list_of_pairs)

    
    
    plt.ylim(0,len(time_schedule)*10)

    # Setting X-axis limits
    max_X = 0
    for process in time_schedule:
        if process.marks[-1] > max_X :
            max_X = process.marks[-1]

    plt.xlim(0, max_X)

    # Setting labels for x-axis and y-axis
    plt.xlabel('time (ms)')
    plt.ylabel('Processes')
    # Setting ticks on y-axis
    tick_names = []
    tick_places = []
    for i in range(len(time_schedule)):
        tick_places.append(i*10)
        tick_names.append(str(time_schedule[i].ID))

    plt.yticks(tick_places,tick_names)

    plt.grid(True)


    for i in range(len(time_schedule)):
        #print(y_axis[i])
        plt.broken_barh(y_axis[i], (i*10, 10), facecolors =(random.random(),random.random(),random.random()))




    plt.plot()
    plt.show()

        

        

        


        