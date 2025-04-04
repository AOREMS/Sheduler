######################--------------EDF Shedule-----------------#####################
"""Variablen die ich verwenden werde
ts = Taskset
t = task
a = activation time
c = Laufzeit
d = absolute deadline
"""

time = 0

#t = [a,c,d]
t1 = [0,1,2]
t2 = [0,2,5]
t3 = [2,2,4]

id = {"A" : t1,
      "B":  t2,
      "C" : t3}

shedule = []

ts = [t1,t2,t3]

n_tasks = len(ts)

a_list = [t1[0],t2[0],t3[0]]
c_list = [t1[1], t2[1], t3[1]]
d_list = [t1[2], t2[2], t3[2]]


def get_activated_tasks():
    global time
    print("                                                                                                                                            1. ZEIT ZEIT ZEIT   " , time)

    ready = []
    for i in range(len(a_list)):
        if(time >= a_list[i] and c_list[i] != 0): #alle die bereit sind und die die nicht fertig gerechnet wurden
            print("the activation of task" , list(id)[i] , "is ", a_list[i])
            print("the runtime of    task" , list(id)[i] , "is ", c_list[i])

            ready.append(i)
    return ready

def get_newly_activated():
    global time
    
    print("                                                                                                                                           2.  ZEIT ZEIT ZEIT   " , time)

    ready = False
    for i in range(len(a_list)):
        if(time == a_list[i]): # gibt zurück ob gerade eine neue aktiviert wurde
            ready = True
            print("*********************NEW TASK JUST CAME IN******************\n\n")
            print("                                                                                                                                          3.   ZEIT ZEIT ZEIT   " , time)

    return ready

#or len(activated_tasks) == 1
def task_to_run():
    global time
    print("                                                                                                                                           4.  ZEIT ZEIT ZEIT   " , time)
    activated_tasks = get_activated_tasks()
    print("es gibt " , len(activated_tasks) , " aktivierte Tasks    zum Zeitpunkt" , time , "\n\n")
    print("activated task ist " , activated_tasks)
    for i in activated_tasks:
        print("Die Task " , i , "wird untersucht", ts[i])
        print("Dies task hat" , ts[i][2] , " als deadline")
        print(" Die task sollte " , min(d_list), " als deadline haben")
        if((ts[i][2]) == min(d_list) or len(activated_tasks) == 1): #die mit der kleinsten deadline wird gewählt außer nur eine Aktiv 
            print("|||||||||||||||||||||||||||||||| Die Tasks sind|||||||||||||||||||||||" , ts)
            
            print("Task sollte " , min(d_list) , "als deadline haben")
            print("die gewählte task " , ts[i] , "wird gewählt" , "\n\n")
            return ts[i] , i

def run_task():
    global time
    ttr  , i = task_to_run()
    print("||||||||||||||||||             TASK              TO          RUN          "           , ttr)
    print ( "                      #################                    Laufzeit ist:               " , ttr[1], "                       ####################" , "\n\n")
    print("Die task to run ist" , ttr)
    #newly_ac = get_newly_activated(time+1) #check if newly updated tasks 
    while(ttr[1] > 0):#solang keine neue tasks und noch laufzeit
        """for x in range(len(ts)): 
            print("ok ok also die Task die wir suchen sollte " , ts[x] , "sein...  die die wir gerade überprüfen ist" ,  id[list(id)[x]])
            if(id[list(id)[x]] in ts): shedule.append(list(id)[x])
            x += 1
            """
        for key in id.keys():
            if id[key] == ttr:
                shedule.append(key)
                break
        ttr[1] -= 1
        c_list[i] -= 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>> run time to go " , ttr[1] , ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time +=1   
        print("                                                                                                                                            5. ZEIT ZEIT ZEIT   " , time)
        if(ttr[2] == 0 and ttr[1] > 0):
            print("deadline verpasst" , ttr)
        if(ttr[1] == 0):
            print("TASK Fertig (((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))" ,)
            print(" deadline wird gelöscht weil task fertig" , d_list[i])
            del d_list[i]
            print(" task wird gelöscht weil task fertig" , ts[ts.index(ttr)])
            del ts[i]
            print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO DIE TASK DIE GELoeSCHT WIRD " , list(id)[i])

            #del list(id)[i]
            #print("//////////////////TASK FINISHED/////////////////\n\n")
            #print("//////////////////TASK WILL GET DELETED//////////////\n\n")
            #print("//////////////////INDEX OF DELETING TASKS/IS/////////////\n\n" , index)
            del a_list[i]
            #print("//////////////////NEW ACTIVATION LIST/////////////\n\n" , a_list)
            del c_list[i]
            #print("/////////////////deadlines ar//////////////////////////\n\n", d_list)
            #del ts[index]
            #print("&&&&&&&&&&&&&&&&&&&&&&& TASK SET IS&&&&&&&&&&&&&&&&&&&&&\n\n", ts)
        if(get_newly_activated()):
            break

    
            
while(len(ts) != 0):
    run_task()
    

print(shedule)
"""
for i in range(run_time):
        print("----------task wird ausgeführt-----\n")
        run_time= run_time - 1                         #task wird durgeführt
        t.sleep(1)
        print("laufzeit neu:-------- " , run_time , "--------\n")
        t.sleep(1)
        
        time += 1                           #time wird aktualisiert
        print(time)
        t.sleep(1)
        newly_ac = get_newly_activated(time)    #check ob neuberechnung nötig
        print("Wurde gerade eine neue Task aktiviert?" , newly_ac)
        t.sleep(1)
"""