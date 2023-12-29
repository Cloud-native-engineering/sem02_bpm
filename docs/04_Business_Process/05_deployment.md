---
layout: default
title: 4.5 Deployment
parent: 4. Business Prozess
nav_order: 5
---

# 4.5 Deployment

Die Bereitstellung auf Camunda SaaS (Camunda Cloud) erfolgt mithilfe einer GitHub Actions Pipeline. Dies ermöglicht eine Versionskontrolle der BPMN-Dateien, sodass jederzeit nachvollzogen werden kann, wer welche Änderungen vorgenommen hat. Darüber hinaus können Pull-Requests verwendet werden, um anderen Personen die Möglichkeit zur Überprüfung der Änderungen zu geben.

In dieser Semesterarbeit werden sämtliche Camunda-Dateien, die im Verzeichnis '~sem02_bpm/camunda/*' abgelegt sind, auf die Camunda SaaS-Plattform deployed. Der Prozess der Deployment-Pipeline gestaltet sich wie folgt:

````yml
name: Deploy Camunda Resources

on:
  push:
    branches:
        - dev
        - main
    paths:
      - 'camunda/*'

jobs:
  deploy-resources:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Deploy Updated Resources
        uses: camunda-community-hub/camunda-platform-8-github-action@master
        with:
          clientConfig:  {% raw %}${{ secrets.ZEEBE_CLIENT_CONFIG }}{% endraw %}
          operation: deployResource
          resourceDirectory: camunda
````

Diese Pipeline wird automatisch ausgeführt, sobald ein Push auf die Branches 'dev' oder 'main' erfolgt. Zusätzlich ist es erforderlich, dass sich der Inhalt des Camunda-Ordners ändert. Die für die Pipeline erforderlichen Credentials sind bei GitHub als '[Actions Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)' hinterlegt und sind für Benutzer und Mitwirkende nicht einsehbar. Sie können ausschliesslich von der Pipeline selbst gelesen und verwendet werden. Zusätzlich muss ein zugelassener Admin den RUN bestätigen und es gibt einen Timer von 15 min.

Folgend ein Beispiel eines Pipeline Runs: [GitHub Actions Pipeline Run](https://github.com/Cloud-native-engineering/sem02_bpm/actions/runs/7346844833)
