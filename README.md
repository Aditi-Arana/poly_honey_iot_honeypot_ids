# Poly-Honey

Poly-Honey is a decentralized IoT honeypot-driven intrusion detection system designed to detect malicious activity at the network edge.

## Features
- Polymorphic IoT honeypot deception
- Honeytoken-based intent detection
- Edge-based rule IDS
- SIEM integration using Wazuh
- MITRE ATT&CK mapping

## Architecture
Attacker → Honeypot Services → Edge IDS → JSON Logs → Wazuh SIEM → Dashboard

## Tech Stack
Python
Docker
Wazuh SIEM
Async networking
