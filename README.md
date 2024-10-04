# Lab: Environment injection

Ceci est un petit lab local dans lequel deux machines sont setup dans un réseau docker. L'une expose un service très simple sur un port TCP en écoute, qui propose une interface permettant de modifier des variables d'environnement et de lancer un binaire (e.g.: python perl). L'objectif est, à partir de l'injection d'environnement, d'obtenir une RCE.

## Setup

```bash
# À la racine
docker compose up --build

# # Dans le terminal victime / serveur, si vous souhaitez avoir les logs
# docker attach victim

# Dans le terminal attaquant
docker attach attacker
```

## Objectif

Votre mission, si vous l'acceptez: créer un fichier dans /tmp/pwned

Votre mission 2, si vous l'acceptez aussi: obtenir un reverse shell sur la machine

## Lecture

<https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-python-applications-injection>

<https://0xn3va.gitbook.io/cheat-sheets/web-application/command-injection#pythonwarnings>
