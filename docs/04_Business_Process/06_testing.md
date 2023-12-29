---
layout: default
title: 4.6 Testing
parent: 4. Business Prozess
nav_order: 6
---

# 4.6 Testing

Um die Effizienz und Wirksamkeit des in Camunda integrierten Geschäftsprozesses zu verdeutlichen, wurde eine umfangreiche Reihe von Tests durchgeführt. Ziel dieser Tests war es, die technische Funktionsfähigkeit des Geschäftsprozesses zu bestätigen und zu demonstrieren, dass die festgelegten Ziele erreicht wurden. Im Rahmen dieser Tests wurden folgende Funktionalitäten überprüft:

- Formulare in Camunda:
  - Online-Bestellvorgang
  - Genehmigungsworkflow
- Verwendung von XOR-Gateways
- DMN-basierte Entscheidungsfindung
- Versand von E-Mails
- Integration von Datenbanken
- Integration des Simple Queue Service (SQS)
- Intermediate Message Catch zur Verarbeitung von Antworten von AWS (Amazon Web Services)

In dieser Testreihe werden die grundlegenden Funktionalitäten von Services, die als Software-as-a-Service (SaaS) bezogen werden, nicht berücksichtigt. Dazu gehören insbesondere die Camunda Cloud und Amazon Web Services (AWS). Ausserdem sind grundlegende Komponenten wie die Internetverbindung von den Tests ausgenommen.

## Test-001 - Online Bestellformular

| Testfall-001 | Online Bestellformular |
|:--| :-- |
| Ziel: | Es kann erfolgreich eine Bestellung für ein EC2-Instanz mit dem Webformular aufgegeben werden. |
| Beschreibung: | Mit einem Web Browser soll auf die Formularseite zugegriffen werden und eine Bestellung aufgegeben werden. |
| Soll-Wert: | Bestellung kan erfasst werden |
| Ist-Wert: | Die Bestellung konnte aufgegeben werden. Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Test-002 - Genehmigungsprozess

| Testfall-002 | Genehmigungsprozess |
|:--| :-- |
| Ziel: | Nach dem die Bestellung aufgegeben wurde erscheint ein User-Task bei welcher der Line Manager die Bestellung genehmigen muss|
| Beschreibung: | Login auf Camunda Tasklist mit einem Manager-Account. Es soll ein User-Task ersichtlich sein. Dieser soll geöffnet werden. Danach soll die Genehmigung auf True gesetzt werden. |
| Soll-Wert: | Die Bestellung kann genehmigt werden. |
| Ist-Wert: | Der Manager konnte die Bestellung genehmigen. Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Test-003 - Add Costcenter

| Testfall-003 | Add Costcenter |
|:--| :-- |
| Ziel: | Nachdem der Manager die Bestellung genehmigt hat. Wird ein User-Task für die Finanzabteilung erstellt, bei welchem sie eine Kostenstelle hinzufügen müssen. |
| Beschreibung: | Login auf Camunda Tasklist mit einem Finanzmitarbeiter-Account. Es sollte ein User-Task ersichtlich sein. Danach soll die Kostenstelle IT-Main ausgewählt werden. |
| Soll-Wert: | Die Kostenstelle IT-Main kann ausgewählt werden und der User-Task wurde geschlossen. |
| Ist-Wert: | Mit dem Account der Finanzabteilung konnte die Kostenstelle hinzugefügt werden. Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Test-004 - XOR-Gateway

| Testfall-004 | XOR-Gateway |
|:--| :-- |
| Ziel: | In dem Gesamten Business Prouzess existieren mehrere XOR-Gateways. Diese ermöglichen einen einfachen Entscheid für den weiteren Verlauf einer Bestellung. Es soll überprüft werden, dass die XOR-Gateways funktionieren. |
| Beschreibung: | Es sollen zwei Bestellungen ausgelöst werden. Danach soll der Line-Manager eine Bestellung ablehnen und die andere annehmen. |
| Soll-Wert: | Der Manager kann eine Bestellung an- beziehungsweise ab-lehnen. |
| Ist-Wert: | Der XOR-Gateway funktioniert, wie ausgedacht.<br> Es konnte eine Bestellung abgelehnt und eine angenommen werden: <br> **annehmen**: Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) <br> **ablehnen**: Order-ID = 1396598722. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/2251799834305576) |

## Test-005 - DMN-basierte Entscheidungsfindung

| Testfall-005 | DMN-basierte Entscheidungsfindung |
|:--| :-- |
| Ziel: | Das DMN-Diagramm kann einen Entscheid fällen, ob eine Kostenstelle genügend Budget hat um eine Bestellung auszuführen. E |
| Beschreibung: | Es sollen zwei Bestellungen erstellt werden. Eine soll genügend Budget haben und eine weitere soll zu teuer sein. Die erste Kostenstelle sollte IT-Main und die andere Project-webshop-2.0 sein. |
| Soll-Wert: | Die IT-Main Kostenstelle hat genügend finanzielle Mittel, das Project Webshop 2.0 nicht. |
| Ist-Wert: | Das DMN funktioniert wie designed.<br> Es konnten beide Szenarien getestet werden: <br> **genügend Budget**: Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) <br> **ungenügend Budget**: Order-ID = 6477712117. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/2251799834306406)|

## Test-006 - Versand von E-Mails

| Testfall-006 | Versand von E-Mails |
|:--| :-- |
| Ziel: | Bei verschiedenen Status werden E-Mails versandt. |
| Beschreibung: | Es soll die Mailbox aufgerufen werden. Es sollten bereits diverse E-Mails existieren über ein Status einer Bestellung, welche abgelehnt, oder umgesetzt wurde. |
| Soll-Wert: | Es wurden E-Mails im Zeitrahmen dieser Testserie verschickt. |
| Ist-Wert: | Es wurden E-Mails erhalten über ungenügend-Budget und weitere. |

## Test-007 - Integration von Datenbanken

| Testfall-007 | Integration von Datenbanken |
|:--| :-- |
| Ziel: | Es wurden Abfragen zur DynamoDB gemacht. Read & Write |
| Beschreibung: | Es soll eine Bestellung ausgelöst werden. Diese soll vom Manager genehmigt werden und von der Finanzabteilung soll die Kostenstelle IT-Main ausgewählt werden. |
| Soll-Wert: | Der DMN-Prozess ist durchgelaufen, auch konnte erfolgreich der Preis der Instanz der Kostenstelle abgezogen werden. |
| Ist-Wert: | Die DMN-Entscheidung funktionierte tadellos. Auch wurde der Preis der Instanz der Kostenstelle abgezogen. <br> Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Test-008 - Integration des Simple Queue Service (SQS)

| Testfall-008 | Integration des Simple Queue Service (SQS) |
|:--| :-- |
| Ziel: | Es können Nachrichten an die SQS-Queue verschickt werden. |
| Beschreibung: | Es soll eine Bestellung ausgelöst werden. Die Bestellung soll vom Manager akzeptiert werden und von der Finanzabteilung wurde IT-Main ausgewählt. |
| Soll-Wert: | Es wurde eine Message an die SQS-Queue versandt. Die Nachricht ist in der SQS-Queue ersichtlich. |
| Ist-Wert: | Ein JSON wurde an die SQS-Queue verschickt. <br> Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Test-009 - Intermediate Message Catch

| Testfall-009 | Intermediate Message Catch |
|:--| :-- |
| Ziel: | Es wird eine Nachricht empfangen, welche informiert, dass die Message von AWS verarbeitet wurde. |
| Beschreibung: | Es soll mit der gleichen Bestellung von vorhin weiter gefahren werden. Es soll im Operate Portal die dazugehörige Bestellung geöffnet werden. Danach soll 20 Minuten gewartet werden. Während dieser Zeit sollte AWS eine Rückmeldung zum Deployment geschickt haben. |
| Soll-Wert: | Es wurde eine Rückmeldung innerhalb von 20 Minuten erhalten. |
| Ist-Wert: | Es wurde eine Rückmeldung nach 2 Minuten nach Versand der Bestellung erhalten. <br> Order-ID = 4735644383. [Camunda Operate](https://bru-2.operate.camunda.io/a21c5657-a334-441e-85f8-4d680f16d26f/processes/4503599647984790) |

## Fazit

Die Testergebnisse bestätigen eindrucksvoll die Funktionsfähigkeit aller in dieser Arbeit implementierten Funktionalitäten. Sie zeigen, dass der Geschäftsprozess vollständig einsatzbereit und effektiv ist.
