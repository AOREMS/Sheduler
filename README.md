# EDF in Python – Aperiodisches, Preemptives Scheduling

Dieses Modul implementiert das Earliest Deadline First (EDF)  
- **Aperiodisch:** Tasks werden unregelmäßig aktiviert.  
- **Preemptiv:** Bei neu eintreffenden Tasks kann die aktuelle Ausführung unterbrochen werden.  

## Nutzung
### Ändern des Shedulers:
### wenn preemtiv & aperiodisch
alle Fkt beibehalten

### wenn algorithmus jedes mal neu rechnet: 
get_newly_activated() löschen und ttr , i = task_to_run() in die while Schleife von run_task() packen siehe(Latest Laxity)

### wenn nicht aperiodisch:
get_activated_tasks(), get_newly_activated löschen und activation lists löschen
und in task_to_run() einfach über alle tasks iterieren und AuswahlAlgorithmus implementieren

## Grund
Implementierung eines in Echtzeitsysteme gelernten Scheduling-Verfahrens
