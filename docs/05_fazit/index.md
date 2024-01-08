---
layout: default
title: 5. Fazit und Zusammenfassung
nav_order: 5
---

# 5. Fazit und Zusammenfassung

In meiner Semesterarbeit konzentrierte ich mich auf die Entwicklung und Implementierung eines Business-Prozesses gemäss des BPMN-Standards in der Camunda Process Engine. Ziel war es, einen Prozess zur Erstellung von EC2-Instanzen in der Amazon Cloud zu entwickeln. Dieser Prozess sollte in der Lage sein, Instanzen zu deployen, die anschliessend nutzbar sind. Besonderen Wert legte ich auf die Realitätsnähe des Prozesses.

Für die Planung meiner Arbeit nutzte ich die Jira Software von Atlassian als SaaS-Lösung aus der Atlassian Cloud. Das Projekt wurde agil in drei Sprints geplant. Der erste Sprint diente als Startphase mit intensiver Recherche und Grundlagenarbeit. Im zweiten Sprint lag der Fokus auf der Entwicklung des Prozesses, einschliesslich der Erstellung des Prozessdiagramms und der Integration in Camunda 8. Der letzte Sprint wurde für Feinabstimmungen und umfassende Tests des Prozesses genutzt auch mussten leider auf Grund zeitlichem Mangel ein Teil der Integration in diesen Sprint verschoben werden.

Das Business Process Model konnte ich erfolgreich entwerfen und dokumentieren. Der Prozess umfasst ein Online-Bestellformular, einen Genehmigungsprozess, Benachrichtigungen/Erinnerungen, finanzielle Entscheidungen mittels DMN und einen Datenaustausch via JSON zur Instanzerstellung. Dieser Datenaustausch ist ein zentraler Aspekt meiner Arbeit. Informationen im JSON-Format werden an eine Amazon Simple Queue gesendet, woraufhin Fabio Beti in seiner Arbeit diese Daten verarbeitet und Rückmeldungen über den Bereitstellungsstatus gibt.

Rückblickend erkenne ich, dass ich die Komplexität der Integration in die Camunda Process Engine deutlich unterschätzt hatte. Diese Erkenntnis kam besonders bei der Notwendigkeit der Interaktion mit einer Vielzahl von Services und Systemen zum Tragen. Insbesondere die Einbindung des E-Mail-Gateways, AWS SQS (Simple Queue Service) und AWS DynamoDB stellte sich als weitaus herausfordernder heraus als zunächst angenommen. Jedes dieser Systeme hatte seine eigenen Besonderheiten und Anforderungen, was eine sorgfältige Abstimmung und Anpassung des Prozesses erforderlich machte. Darüber hinaus erforderte das Design der Benutzeroberfläche und der Formulare sowie die Definition des Prozess-Flows eine erhebliche Zeitinvestition.

Beim Zurückblicken auf die gesamte Arbeit, fällt auf, wie umfangreich und komplex mein Projekt tatsächlich ist. Angefangen bei der ersten Idee bis hin zur endgültigen Umsetzung, jede Phase war gefüllt mit tiefer Recherche, wiederholten Verbesserungszyklen und ständigem Wissenszuwachs. Auch wenn der Zeitliche Rahmen der Semesterarbeit überstritten wurde, blicke ich zurück auf die vielen Erkenntnisse und Erfahrungen, welche ich gewonnen habe zurück. Die Praxiserfahrung, die ich während der Arbeit gesammelt habe, sind von unschätzbarem Wert und haben meine Fähigkeiten in der IT erweitert. Diese Erfahrungen reichen von technischem Know-how in der Arbeit mit Cloud-Diensten und BPMN bis hin zu einem verbesserten Projektmanagement und einer adaptiven Problemlösungskompetenz.
