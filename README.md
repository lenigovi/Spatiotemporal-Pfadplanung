# Multi Agent Spatiotemporal Pfadplanung




## Systemaufbau

Unser kleines System besteht aus dem Raspberry Pi und drei mobile Roboter. Auf dem Raspberry Pi läuft das Hauptprogram DStarLiteMain.py von D* für die Pfadplanung.

Unser Missionsgebiet ist 10 Felder breit und 7 Felder hoch. Jedes einzelne Feld ist 40cm x 40cm groß. Die Feldgröße orientiert sich an der Größe des Roboters plus einem Spielraum um den Roboter herum.


## Pfadplannung Metode

> Weiterentwicklungen wie A* verwenden für den Start zusätzlich eine erste Abschätzung welche Kanten von Knoten schneller zum Ziel führen könnten. Solche Abschätzungen nennt man auch Heuristiken und man findet sie in vielen Bereichen der Computertechnik. A* hat jedoch die Schwäche des Treffens des Roboters auf ein zuvor unbekanntes Hindernis, also eine Unterbrechung einer Kante, wird eine komplette Neuplanung vom aktuellen Standort bis zum Ziel durchgeführt. Allerdings, der D* Algorithmus verwendet hingegen Teile der vorherigen Planung weiter und ist somit schneller. Diese Algorithmen nennen sich als inkrementelle Planungsalgorithmen.


## Simulation

![/Pfadplanung_Program/Simulation/Multiagent_Simulation.png](https://github.com/lenigovi/Spatiotemporal-Pfadplanung/blob/main/Pfadplanung_Program/Simulation/Multiagent_Simulation.png)


## Tutorial

### Der Aufbau des ersten Roboters 

![IMG_6056](https://github.com/user-attachments/assets/eda2f7bc-4c88-4868-849d-5e58d7d48778)


Kamera, Ultraschallsensor, Raspberry Pi, Leiterplatte (vor dem Anbau der Räder)  |  Raspberry Pi Verbindung und Zwei Motoren | 3D gedruckte Leiterplatte
:-------------------------:|:-------------------------:|:-------------------------:
![Hardware](https://github.com/user-attachments/assets/5e2e6235-ff58-432d-b706-0ce72c0c5e60) |  ![IMG_5937](https://github.com/lenigovi/Spatiotemporal-Pfadplanung/assets/145778326/e8c7a905-1657-4614-b84f-46b776adf872) | ![IMG_5943](https://github.com/lenigovi/Spatiotemporal-Pfadplanung/assets/145778326/741c7065-8dbd-45d2-af04-29ed423433b1) 

&nbsp;
&nbsp;

## Tests

![IMG_6633](https://github.com/user-attachments/assets/ea0312cc-16cd-4902-89b9-8cde275a6210)

### Initial Test
In the initial test, Agent-2 is put in motor motion of 60RPM. It was observed that Agent-1 attempted to adjust its speed based on the probability distribution of displacement, however, did not manage to bridge the distance in time, and collided with Agent-2.

https://github.com/user-attachments/assets/85119169-766d-4c95-9216-9a06cfa29a55

&nbsp;
&nbsp;

### Agent-1 Adjusts Speed Correctly
After algorithm edits, the speed adjustment of Agent-1 was improved and it bridged the distance between start and terminal points, resulting the test positively.

https://github.com/user-attachments/assets/e0f80b09-8e4c-44f1-821a-3d70297d8a7d 

&nbsp;
&nbsp;

### Agent-1 Changes Orientation
In the second test, Agent-2 is put on 175RPM motor motion, and it was observed that Agent-1 moved behind the dynamic constraint, however, the end goal was not reached.

https://github.com/user-attachments/assets/465a7fbd-da9d-4160-9c9d-050ca8907b9c

