# Multi-Agent Spatiotemporal Pfadplanung


## Systemaufbau

Unser kleines System besteht aus dem Raspberry Pi und einem mobilen Roboter. Auf dem Raspberry Pi läuft das Hauptprogram DStarLiteMain.py von D* für die Pfadplanung.

Unser Missionsgebiet ist 10 Felder breit und 7 Felder hoch. Jedes einzelne Feld ist 40cm x 40cm groß. Die Feldgröße orientiert sich an der Größe des Roboters plus einem Spielraum um den Roboter herum.


## Pfadplannung Metode

> Weiterentwicklungen wie A* verwenden für den Start zusätzlich eine erste Abschätzung welche Kanten von Knoten schneller zum Ziel führen könnten. Solche Abschätzungen nennt man auch Heuristiken und man findet sie in vielen Bereichen der Computertechnik. A* hat jedoch die Schwäche des Treffens des Roboters auf ein zuvor unbekanntes Hindernis, also eine Unterbrechung einer Kante, wird eine komplette Neuplanung vom aktuellen Standort bis zum Ziel durchgeführt. Allerdings, der D* Algorithmus verwendet hingegen Teile der vorherigen Planung weiter und ist somit schneller. Diese Algorithmen nennen sich als inkrementelle Planungsalgorithmen.






