---
layout: default
title: 2.5 GIT Branching Konzept
parent: 2. Projektorganisation
nav_order: 5
---

# 2.5 GIT Branching Konzept

Ich habe ein Git-Branching-Konzept erstellt, um sicherzustellen, dass ich unabhängig an verschiedenen Features arbeiten kann. Durch die Verwendung dieses Konzepts kann ich sicherstellen, dass Änderungen dokumentiert und nachverfolgt werden können.

![GIT-Branching-Concept-Image](../../resources/images/2023_git-branching-concept.svg)

## Erläuterung des Konzepts

Falls Änderungen im Git-Repository gemacht werden müssen, muss ein neuer Branch erstellt werden, welcher die Ticket-Nummer beinhaltet. Ein Beispiel könnte (feature/11-Add-Project) sein. Dieser Branch hat die Abstammung vom DEV-Branch. Wurden die Anpassungen in den Branch gepusht und getestet, kann ein Pull Request eröffnet werden. Dieser Pull Request wird geprüft. Beim Erstellen des Pull Requests soll das bestehende Template verwendet werden. Nach dem Review und einer positiven Rückmeldung können die Änderungen in den DEV-Branch gemerged werden.

Nach jedem Sprint wird ein Tag auf dem DEV-Branch erstellt. Somit kann nachverfolgt werden, wie der Stand des Projektes zu diesem Zeitpunkt war.

Nach dem 3. Sprint werden die Inhalte des DEV-Branch mithilfe eines Pull Requests in den MAIN-Branch gemerged. Auf dem MAIN-Branch wird bei diesem Zeitpunkt auch ein Release Tag gesetzt.

## Verlinkung von Branches, Pull Requests & Tickets

Sobald eine Änderung im GIT Repository gemacht werden muss, müssen das Ticket, der Branch und der Pull Request miteinander verlinkt werden. Dies kann in der Projektplanung gemacht werden

Ticket Branches haben folgenden Aufbau:

- feature/{TICKET-NUMMER}-{BESCHREIBUNG}
