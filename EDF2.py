import string
class EDF():
    def __init__(self, taskset ):
        self.time = 0
        self.shedule = []
        self.id = taskset.id
        self.ts = taskset.ts
        print(taskset.id)
        print(self.ts)
        self.a_list , self.c_list = taskset.create_lists()
        print(self.a_list , self.c_list )


    
    def get_time(self):
        return self.time
    
    def update_time(self):
        self.time += 1

    
    def get_activated_tasks(self):
        ready = []
        current_time = self.get_time()
        for i in range(len(self.a_list)):
            if(current_time >= self.a_list[i] and self.c_list[i] != 0): #alle die bereit sind und die die nicht fertig gerechnet wurden
                ready.append(i)
        return ready
    
    def get_newly_activated(self):
        ready = False
        current_time = self.get_time()
        for i in range(len(self.a_list)):
            if(current_time == self.a_list[i]): # gibt zurück ob gerade eine neue aktiviert wurde
                ready = True
                print("*********************NEW TASK JUST CAME IN******************\n\n")

        return ready
    
    def task_to_run(self):
        activated_tasks = self.get_activated_tasks()
        min_deadline = min(self.ts[i][2] for i in activated_tasks) 
        for i in activated_tasks:
            if(self.ts[i][2] == min_deadline):
                return self.ts[i] , i
        

    def run_task(self):
        ttr ,i  = self.task_to_run()
        while(ttr[1] > 0):#solang keine neue tasks und noch laufzeit
            for key in self.id.keys():
                    if self.id[key] == ttr:
                        self.shedule.append(key)
                        break
            print(self.shedule)
            ttr[1] -= 1

            self.c_list[i] -= 1
            self.update_time()   
            
            if(ttr[2] == 0 and ttr[1] > 0):
                print("deadline verpasst" , ttr)
            
            if(ttr[1] == 0):
                print("TASK Fertig (((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))")
                del self.ts[i]
                del self.a_list[i]
                del self.c_list[i]
            
            if(self.get_newly_activated()):
                break

class Task():
    def __init__(self, activation, run_time, deadline):
        self.activation = activation
        self.run_time = run_time
        self.deadline = deadline
        self.task = [self.activation, self.run_time, self.deadline]
        print(self.task)
      


class Taskset():
    def __init__(self, tasks : list):
        self.id = {}
        self.ts = tasks
        for i , task in enumerate(tasks):
            self.id[string.ascii_uppercase[i]] = task
        

    def create_lists(self):
        self.a = []
        self.c = []
        
        for key in self.id.keys():
            self.a.append(self.id[key][0])#alle activations
            self.c.append(self.id[key][1])#alle laufzeiten  .append(key)
        return (self.a, self.c)
    

  

t1 = Task(0,2,7)
t2 = Task(2,1,8)
t3 = Task(3,2,5)
t4 = Task(2,2,20)

t = Taskset([t1.task,t2.task,t3.task,t4.task])


edf_1 = EDF(t)
while (len(t.ts) > 0):
    edf_1.run_task()

    
