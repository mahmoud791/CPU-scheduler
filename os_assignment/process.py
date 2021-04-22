class process(object):

    


    def __init__(self, arrival_time,Duration,ID,priority):
        self.priority = priority
        self.ID = ID
        self.time_remaining = Duration
        self.duration = Duration
        self.arrival_time = arrival_time
        self.marks = []


    def pass_time(self):
        self.time_remaining=self.time_remaining-1

    def addMark(self,time):
        self.marks.append(time)

    def get_waiting_time(self):

        
        waiting_time = ( self.marks[0] - self.arrival_time)+ (self.marks[-1] - self.marks[0] - self.duration)
        return waiting_time

        
        
        