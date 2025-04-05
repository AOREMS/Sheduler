# EDF in Python – Aperiodisches, Preemptives Scheduling

Dieses Modul implementiert das Earliest Deadline First (EDF)  
- **Aperiodisch:** Tasks werden unregelmäßig aktiviert.  
- **Preemptiv:** Bei neu eintreffenden Tasks kann die aktuelle Ausführung unterbrochen werden.  

## Nutzung
### Ändern des Shedulers:
-wenn preemtiv dann die get_newly_activated() beibehalten

-wenn algorithmus jedes mal neu rechnet get_newly_activated() löschen und task_to_run in die while Schleife von run_task()

-wenn nicht aperiodisch einfach get_activated_tasks() und get_newly_activated löschen,#alle activation lists löschen und 
  in task_to_run() einfach über alle tasks iterieren und Algorithmus implementieren

## Grund
Implementierung eines in Echtzeitsysteme gelernten Scheduling-Verfahrens
