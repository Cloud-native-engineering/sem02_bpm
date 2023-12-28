---
layout: default
title: 4.2 Datenaustausch mit AWS SQS
parent: 4. Business Prozess
nav_order: 2
---

# 4.2 Datenaustausch mit AWS SQS

| Thema der Besprechung | Harmonisierung Datenaustausch zwischen Camunda & AWS SQS      |
| :-------------------- | :------------------------------------------------------------ |
| Datum                 | 22.11.2023                                                    |
| Anwesende             | - Yves Wetter, Project Camunda <br> - Fabio Beti, Projekt AWS |

## Agenda

1. Begrüssung und Eröffnung
2. Besprechung des Aufbaus des JSON für den Datenaustausch
3. Offene Diskussion
4. Festlegung von Richtlinien für den JSON-Aufbau
5. Nächste Schritte und Abschluss

---

## 1. Begrüssung und Eröffnung

Die Sitzung wurde am Mittwoch in der TBZ eröffnet. Ziel und Zweck dieses Meeting ist das Format des JSON zu definieren, damit beide Projekte miteinander Daten austauschen können.

## 2. Besprechung des Aufbaus des JSON für den Datenaustausch

### 2.2 Aktueller Stand

Es wurde ein Vorschlag von Yves Wetter vorgestellt und ergänzt aus Informationen aus der Diskussion.

### 2.3 Anforderungen an den JSON-Aufbau

- Struktur
  - Einheitlich
  - Übersichtlich
- Offenheit für Erweiterungen/Ergänzungen
  - Delete VM
  - Restart VM
  - etc.
- Bezeichnung der Attribute sind selbsterklärend

## 3. Offene Diskussion

Es folgte eine offene Diskussion, in der alle Teilnehmer ihre Meinungen und Vorschläge zum JSON-Aufbau äussern konnten. Es wurden verschiedene Ansätze vorgestellt und Vor- sowie Nachteile diskutiert.

## 4. Festlegung von Richtlinien für den JSON-Aufbau

Folgend ist ein Beispiel von einem JSON für den Austausch:

```json
{
  "orderID": "gb393Twie2944345",
  "surname": "Toni",
  "lastname": "Mahoni",
  "department": "it_webshop_development",
  "email": "toni@testcorp.com",
  "orderDescription": "New vm for webshop migration",
  "instanceName": "webshop01",
  "ami": "ubuntu",
  "instanceType": "t2.micro",
  "environment": "dev",
  "networkSubnet": "eu-central-1a-01",
  "firewallProfiles": ["ssh_internal", "https_public", "http_internal"],
  "publicIP": true,
  "state": "present",
  "userData": "sudo apt-get install apache2",
  "costCenter": "2493_it_ops"
}
```

| Number | Attribute        | Type   | Description                                      |
| ------ | ---------------- | ------ | ------------------------------------------------ |
| 1      | orderID          | string | ID der Bestellung                                |
| 2      | surname          | string | Vorname                                          |
| 3      | lastname         | string | Nachname                                         |
| 4      | department       | string | Abteilung                                        |
| 5      | email            | string | E-Mail Adresse                                   |
| 6      | orderDescription | string | Beschreibung der Bestellung                      |
| 7      | instanceName     | string | VM Hostname                                      |
| 8      | ami              | string | Amazon Machine Image, Operating System           |
| 9      | instanceType     | string | Amazon EC2 Instance size, Grösse der VM          |
| 10     | environment      | string | Umgebung, { dev, test, int, prod }               |
| 11     | networkSubnet    | string | Netzwerkzone                                     |
| 12     | firewallProfiles | list   | Enabled Firewall Policies                        |
| 13     | publicIP         | bool   | Hat eine Public-IP                               |
| 14     | state            | string | Status, { present, stopped, deleted, restarted } |
| 15     | userData         | string | Cloud-init                                       |
| 16     | costCenter       | string | Kostenstelle                                     |

## 5. Nächste Schritte und Abschluss

- Test integration
- Erkenntnisse Dokumentieren
- Umsetzung SQS integration
