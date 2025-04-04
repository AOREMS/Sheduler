import string
class EDF():
    def __init__(self, taskset ):
        self.time = 0
        self.shedule = []
        self.ts = taskset.ts
        print(taskset.ts)
        self.a_list , self.c_list , self.d_list = taskset.create_lists()
        print(self.a_list , self.c_list , self.d_list )


    
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
        for i in activated_tasks:
            if((self.ts[string.ascii_uppercase[i]][2]) == min(self.d_list) or len(activated_tasks) == 1): #die mit der kleinsten deadline wird gewählt außer nur eine Aktiv 
                return self.ts[string.ascii_uppercase[i]] , i

    def run_task(self):
        ttr  , i = self.task_to_run()
        
        while(ttr[1] > 0):#solang keine neue tasks und noch laufzeit
            for key in self.ts.keys():
                    if self.ts[key] == ttr:
                        self.shedule.append(key)
                        break
            ttr[1] -= 1
            self.c_list[i] -= 1
            self.update_time()   
            
            if(ttr[2] == 0 and ttr[1] > 0):
                print("deadline verpasst" , ttr)
            
            if(ttr[1] == 0):
                print("TASK Fertig (((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))" )
                del self.d_list[i]
                del self.ts[string.ascii_uppercase[i]]
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
        self.ts = {}
        for i , task in enumerate(tasks):
            self.ts[string.ascii_uppercase[i]] = task
        

    def create_lists(self):
        self.a = []
        self.c = []
        self.d = []
        
        for key in self.ts.keys():
            self.a.append(self.ts[key][0])#alle activations
            self.c.append(self.ts[key][1])#alle laufzeiten  .append(key)
            self.d.append(self.ts[key][2])#alle deadlines
        return (self.a, self.c, self.d)
    

  

t1 = Task(0,2,7)
t2 = Task(2,1,8)
t3 = Task(3,2,5)
t4 = Task(2,2,20)

t = Taskset([t1.task,t2.task,t3.task,t4.task])


edf_1 = EDF(t)
while (len(t.ts) > 0):
    edf_1.run_task()
    
