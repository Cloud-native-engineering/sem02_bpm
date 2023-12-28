---
layout: default
title: 3.2 Camunda 7 vs. 8
parent: 3. Camunda-Engine
nav_order: 2
---

# 3.2 Camunda 7 vs. Camunda 8

Mit dem Major-Release von Sieben auf Acht hat Camunda viele neue Features und Funktionen eingeführt. Was sind die Vor- und was sind aber die Nach-teile. Diese werden in diesem Abschnitt verglichen und aufgelistet. Auch wird in diesem Abschnitt einen Entscheid gefällt, welche Camunda Version eingesetzt wird.

## 3.2.1 Camunda 7

Camunda in der Version 7 ist 2010 erschienen und wurde immer kontinuierlich weiter entwickelt. Camunda 7 bietet verschiedene Deployment Optionen an, von lokalen Entwicklungsinstanzen, bis zu Container Fähigen und hochverfügbaren Umgebungen viele Möglichkeiten vorhanden. Für die Integration in andere Systemen kann hauptsächlich die Rest-, SOAP-API und Java-API verwendet werden. Unterstützt werden eine Vielzahl von Datentypen, von normalen Datentypen, wie zum Beispiel Strings, Byte-objekten, Float, Integers, Bool auch wird JSON und serialisierte Java Objekte unterstützt. Integriert werden kann über eigene Scripte, sowie über bereits existierende Erweiterungen.

| Beschreibung  | Datum          |
| :------------ | :------------- |
| First Release | November, 2017 |
| End-of-life   | April, 2027    |

## 3.2.2 Camunda 8

Camunda 8 ist der Nachfolger von der Version 7 dabei wurde viel überarbeitet und verbessert. Neu basiert die Version 8 auf der Zebee-Engine. Die Zebee-Engine ist hoch performant und skalierbar. Die Kommunikation erfolgt über den Zebee-Gateway-API. Somit unterstützt sie nur noch den Remote Engine Modus. Bei den Schnittstellen gab es auch eine Anpassung. Nicht mehr unterstützt wird der SOAP Standart, dazugekommen sind JMS(Java Messaging Service) und AMQP(ActiveMQ). Neu dazugekommen ist die [Camunda Cloud](https://console.cloud.camunda.io) und der [Camunda Marketplace](https://marketplace.camunda.com).

| Beschreibung  | Datum              |
| :------------ | :----------------- |
| First Release | April, 2022        |
| End-of-life   | Noch nicht bekannt |

## 3.2.3 Camunda Cloud

Camunda Cloud ist die Software as a Service Lösung von Camunda. Sie ermöglicht die Camunda Software als Service zu beziehen. Dabei wird diese Camunda Instanz in der Cloud betrieben und Camunda übernimmt den Update Prozess und die Skalierung der Prozess-Engine.

Die Camunda Cloud unterstützt nur die Version 8.

## 3.2.4 Camunda Marketplace

Der Camunda Marketplace bietet eine vielzahl von Camunda 8 Erweiterungen an. Diese Module sind zu diesem Zeitpunkt nur in der Camunda-Cloud verfügbar. Das Camunda Team arbeitet aber daran dass der Marketplace auch mit self-hosted Instanzen verwendet werden kann.

## 3.2.5 Vergleich

Folgend werden die beiden Major Versionen von Camunda verglichen.

| **_Funktion_**             |                                 **Camunda 7**                                 |                                    **Camunda 8**                                     |
| :------------------------- | :---------------------------------------------------------------------------: | :----------------------------------------------------------------------------------: |
| Architektur und Deployment |                 Shared Engine, Embedded Engine, Remote Engine                 |                                    Remote Engine                                     |
| Task Processing            |                              REST API, Java API                               |                                    Zeebe Gateway                                     |
| Datentypen                 |             Primäre Datentypen, JSON, serialisierte Java-Objekte              |           Primäre Datentypen (String, Byte, Float, char, Bool, ...), JSON            |
| Connector-Infrastruktur    |                                  HTTP, SOAP                                   |                                REST, HTTP, JMS, AMQP                                 |
| Skalierbarkeit             |                                  Horizontal                                   |                                  Horizontal, linear                                  |
| Camunda Cloud              |                                     Nein                                      |                                          Ja                                          |
| Camunda Marketplace        |                                     Nein                                      |                                          Ja                                          |
| Integration                | Eigene Scripte/Programme über API, sowie existierende Tools und Erweiterungen | Der Camunda Marketplace bietet eine vielzahl von bereits existierenden Erweiterungen |

## 3.2.6 Entscheid

Der Entscheid wurde lange überlegt. Es wurde entschieden Camunda in der Version 8 zu verwenden und idealerweise die Camunda Instanz in der Camunda Cloud zu betreiben. Die Hauptgründe hierfür liegen darin, dass die Integration in andere Systeme mit Version 7 umständlich ist. Zwar wäre es möglich, Python-Skripte für die Erweiterung zu schreiben, und obwohl mich dieser technische Ansatz interessiert, glaube ich, dass der damit verbundene Zeitaufwand und Mehraufwand nicht gerechtfertigt sind. Der Fokus sollte im Business Prozess und dessen Integration liegen und nicht in der konzeption von Scripten und Erweiterungen. Es ist einfach so, dass die Camunda Cloud zusammen mit dem Camunda Marketplace den grössten mehrwert für diese Arbeit liefert. Die Camunda Cloud in Kombination mit dem Camunda Marketplace bietet zweifellos den grössten Mehrwert für diese Semesterarbeit.
