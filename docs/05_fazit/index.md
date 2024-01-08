---
layout: default
title: 5. Fazit und Zusammenfassung
nav_order: 5
---

# 5. Fazit und Zusammenfassung

Im Rahmen meiner Semesterarbeit habe ich mich auf die Entwicklung und Implementierung eines Business-Prozesses gemäss des BPMN-Standards in der Camunda Process Engine konzentriert. Ziel war es, einen Prozess zur Erstellung von EC2-Instanzen in der Amazon Cloud zu entwickeln. Die Intention dieses Prozesses war es, Instanzen zu deployen, welche anschliessend nutzbar sind. Besonderen Wert habe ich auf die Realitätsnähe des Prozesses gelegt.

Für die Planung meiner Arbeit nutzte ich die Jira Software von Atlassian als SaaS-Lösung aus der Atlassian Cloud. Das Projekt wurde agil in drei Sprints geplant. Der erste Sprint diente als Startphase mit intensiver Recherche und Grundlagenarbeit. Im zweiten Sprint lag der Fokus auf der Entwicklung des Prozesses, einschliesslich der Erstellung des Prozessdiagramms und der Integration in Camunda 8. Der letzte Sprint wurde für Feinabstimmungen wie auch für umfassende Tests des Prozesses genutzt. Aufgrund begrenzter zeitlicher Ressourcen musste ein Teil der Integration in diesen Sprint verschoben werden.

Das Business Process Model konnte ich erfolgreich entwerfen und dokumentieren. Der Prozess umfasst ein Online-Bestellformular, einen Genehmigungsprozess, Benachrichtigungen sowie als auch Erinnerungen, finanzielle Entscheidungen mittels DMN und einen Datenaustausch via JSON zur Instanz Erstellung. Dieser Datenaustausch stellt ein zentraler Aspekt meiner Arbeit dar. Informationen im JSON-Format werden an eine Amazon Simple Queue gesendet, woraufhin Fabio Beti in seiner Arbeit diese Daten verarbeitet und anschliessend Rückmeldungen über deren Bereitstellungsstatus geben konnte.

Rückblickend erkenne ich, dass ich die Komplexität der Integration in die Camunda Process Engine deutlich unterschätzt hatte. Diese Erkenntnis kam besonders bei der Notwendigkeit der Interaktion mit einer Vielzahl von Services und Systemen zum Tragen. Insbesondere die Einbindung des E-Mail-Gateways, AWS SQS (Simple Queue Service) und AWS DynamoDB stellte sich als weitaus herausfordernder heraus als zunächst angenommen. Jedes dieser Systeme hat seine eigenen Besonderheiten und Anforderungen, was eine sorgfältige Abstimmung und Anpassung des Prozesses erforderte. Darüber hinaus erforderte das Design der Benutzeroberfläche und der Formulare sowie die Definition des Prozess-Flows eine erhebliche Zeitinvestition.

Auch wenn der zeitliche Rahmen der Semesterarbeit überstritten wurde, blicke ich auf die vielen Erkenntnisse und Erfahrungen, welche ich gewonnen habe, zurück. Die Praxiserfahrung, die ich während der Arbeit gesammelt habe, sind von unschätzbarem Wert und ich hatte die Gelegenheit meine IT-Fähigkeiten zu erweitern. Diese Erfahrungen reichen von technischem Know-how in der Arbeit mit Cloud-Diensten und BPMN bis hin zu einem verbesserten Projektmanagement und einer adaptiven Problemlösungskompetenz.
