from tkinter import*
from process import*
from FCFS import*
from SJF_nonpremative import*
from SJF_premative import*
from roundrobin import*
from priority_nonpremative import*
from priority_premative import*
from plot import*
from avgWaitingTime import get_avg_WaitingTime
import os
import sys




root = Tk()

time_schedule = []

processes_arrivals = []
processes_durations = []
processes_priorities = []


label_1 = Label(root,text='enter number of processes :')
label_1.grid(row=1,column=1)
entry = Entry(root)
entry.grid(row=1,column=2)

chosen_algorithm = StringVar()
chosen_algorithm.set('FCFS')

drop = OptionMenu(root,chosen_algorithm,'FCFS','SJF_nonpremative','SJF_premative','priority_nonpremative','priority_premative','round_robin')
drop.grid(row=1,column=3)


button = Button(root,text='submit',command= lambda : manager(chosen_algorithm.get()))
button.grid(row=1,column=4)



def manager(algorithm):
    
    if algorithm == 'FCFS' or algorithm == 'SJF_nonpremative' or algorithm == 'SJF_premative' :
    	enter_processes_1(algorithm=algorithm)

		
    elif algorithm == 'round_robin':
        enter_processes_2(algorithm=algorithm)

    elif algorithm == 'priority_premative' or algorithm == 'priority_nonpremative':
    	enter_processes_3(algorithm=algorithm)
    	
    		
    		
		
    	
	
    
    			
    			


def build_schedule_1(algorithm):
	
    #build time_schedule for FCFS , SJF



	for i in range(len(processes_arrivals)):
		new_process = process(float(processes_arrivals[i].get()),float(processes_durations[i].get()),"P"+str(i),0)
		time_schedule.append(new_process)		

	time_schedule.sort(key=lambda x:x.arrival_time)

	#print(algorithm)

	if algorithm =='FCFS':
    		FCFS(time_schedule=time_schedule)

	elif algorithm == 'SJF_nonpremative':
    		SJF_nonpremative(time_schedule=time_schedule)
	
	
	elif algorithm == 'SJF_premative':
    		SJF_premative(time_schedule=time_schedule)

	
	


	label = Label(root,text = 'avg waiting time = ' + str(get_avg_WaitingTime(time_schedule))).grid(row=5,column=3)
	


	Plot(time_schedule=time_schedule)


	os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def build_schedule_2(algorithm,quantum_entry):
    #build time_schedule for round robin

    quantum = int(quantum_entry.get())

    for i in range(len(processes_arrivals)):
    	new_process = process(float(processes_arrivals[i].get()),float(processes_durations[i].get()),"P"+str(i),0)
    	time_schedule.append(new_process)			
    time_schedule.sort(key=lambda x:x.arrival_time)

    RoundRobin(time_schedule=time_schedule,quantum=quantum)



	
    label = Label(root,text = 'avg waiting time = ' + str(get_avg_WaitingTime(time_schedule))).grid(row=5,column=3)
	


    Plot(time_schedule=time_schedule)


    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def build_schedule_3(algorithm):
    	
    #build time_schedule for priority



	for i in range(len(processes_arrivals)):
		new_process = process(float(processes_arrivals[i].get()),float(processes_durations[i].get()),"P"+str(i),int(processes_priorities[i].get()))
		time_schedule.append(new_process)		

	time_schedule.sort(key=lambda x:x.arrival_time)

	
	#print(algorithm)

	if algorithm =='priority_nonpremative':
    		priority_nonpremative(time_schedule=time_schedule)

	elif algorithm == 'priority_premative':
    		priority_premative(time_schedule=time_schedule)
    		
    		



	
	


	label = Label(root,text = 'avg waiting time = ' + str(get_avg_WaitingTime(time_schedule))).grid(row=5,column=4)
	


	Plot(time_schedule=time_schedule)


	os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 





def enter_processes_1(algorithm): 

	NumberOfProcesses=int(entry.get())
	label_II = Label(root,text = "Enter arrival times").grid(row = 2,column=1)
	label_III = Label(root,text = "enter Processes Durations").grid(row = 2,column=2)

	for i in range(NumberOfProcesses):
		label_I = Label(root,text = "P"+str(i)).grid(row = i+3,column=0)
		process_arrival = Entry(root)
		process_arrival.grid(row=i+3,column=1)
		processes_duration = Entry(root)
		processes_duration.grid(row=i+3,column=2)
		processes_arrivals.append(process_arrival)
		processes_durations.append(processes_duration)
	
	button_2 = Button(root,text="submit",command =lambda: build_schedule_1(algorithm)).grid(row=3,column=3)

def enter_processes_2(algorithm): 

	NumberOfProcesses=int(entry.get())

	label_II = Label(root,text = "Enter arrival times").grid(row = 2,column=1)
	label_III = Label(root,text = "enter Processes Durations").grid(row = 2,column=2)
	label_V = Label(root,text = 'quantum = ').grid(row = 4 ,column = 3)
	quantum_entry = Entry(root)
	quantum_entry.grid(row = 4 , column =4)


	for i in range(NumberOfProcesses):
		label_I = Label(root,text = "P"+str(i)).grid(row = i+3,column=0)
		process_arrival = Entry(root)
		process_arrival.grid(row=i+3,column=1)
		processes_duration = Entry(root)
		processes_duration.grid(row=i+3,column=2)
		processes_arrivals.append(process_arrival)
		processes_durations.append(processes_duration)
	
	button_2 = Button(root,text="submit",command =lambda: build_schedule_2(algorithm,quantum_entry)).grid(row=3,column=3)


def enter_processes_3(algorithm): 

	NumberOfProcesses=int(entry.get())
	label_II = Label(root,text = "Enter arrival times").grid(row = 2,column=1)
	label_III = Label(root,text = "enter Processes Durations").grid(row = 2,column=2)
	label_V = Label(root,text = "enter Priorities").grid(row = 2,column=3)

	for i in range(NumberOfProcesses):
		label_I = Label(root,text = "P"+str(i)).grid(row = i+3,column=0)
		process_arrival = Entry(root)
		process_arrival.grid(row=i+3,column=1)
		processes_duration = Entry(root)
		processes_duration.grid(row=i+3,column=2)
		processes_priority = Entry(root)
		processes_priority.grid(row=i+3,column=3)
		processes_arrivals.append(process_arrival)
		processes_durations.append(processes_duration)
		processes_priorities.append(processes_priority)
	
	button_2 = Button(root,text="submit",command =lambda: build_schedule_3(algorithm)).grid(row=3,column=4)    	
	    
	    	





    	

root.mainloop()





    
    	
    




    	

	

