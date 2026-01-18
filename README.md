# Cyber-Shield-SIEM-With-Pi-Cluster
" 22S22456" RASPBERRY PI 5 CYBER-SHIELD: INTELLIGENT THREAT DETECTION \& FORENSICS: Distributed Raspberry Pi SIEM/IDS monitoring stack using Suricata, Kismet, Cowrie, InfluxDB, Grafana, and SMTP alerting




# CyberShield SIEM With Pi Cluster (Cyber-Shield Pi 5)

A Raspberry Pi cluster–based cybersecurity monitoring platform that combines:
- **Suricata IDS (Node 1)** for wired network detection,
- **InfluxDB + Grafana (Node 2)** for SIEM storage, visualization, and alerting,
- **Kismet (Node 2)** for wireless monitoring,
- **Cowrie SSH Honeypot (Node 3)** for attacker interaction telemetry.

This repository contains **configuration artifacts**, **dashboards**, **sanitized logs**, **evidence screenshots**, and a **3D cluster case model**.

---

## High-Level Architecture

- **Node 1 (IDS):** Suricata + automation scripts  
  - Config: `node1-ids/suricata/suricata.yaml`  
  - Script: `node1-ids/scripts/realtime_monitor.py`

- **Node 2 (SIEM/UI):** InfluxDB + Grafana + Kismet  
  - Dashboard export: `node2-ui/grafana/dashboards/siem_dashboard.json`  
  - Alerting (sanitized): `node2-ui/grafana/alerts/alerts_smtp.json`  
  - Kismet configs: `node2-ui/kismet/`

- **Node 3 (Honeypot):** Cowrie  
  - Config (sanitized): `node3-honeypot/cowrie/cowrie.cfg`  
  - Sanitized samples: `node3-honeypot/notes/`

**Important operational note:** Node 3 administrative SSH uses **port 22022**. Other SSH exposure is reserved for the honeypot surface.

---

## Dashboards and Alerts (Grafana)
- Import the SIEM dashboard JSON:
  - `node2-ui/grafana/dashboards/siem_dashboard.json`
- Alert rules/contact points are provided in sanitized form:
  - `node2-ui/grafana/alerts/alerts_smtp.json`

---

## Documentation
- Architecture: `docs/architecture/ARCHITECTURE.md`
- Deployment: `docs/deployment/SETUP.md`
- Testing: `docs/testing/TEST_PLAN.md`
- Secrets policy: `docs/security/SECRETS.md`

---

## Diagrams
See: `docs/architecture/diagrams/`
- Flow chart: `flow_chart.png`
- Logical architecture: `logical_architecture.png`
- Physical architecture: `physical_architecture.png`
- Use case: `use_case.png`

---

## Screenshots (Evidence)
See: `screenshots/`
- Grafana dashboard and alerts: `screenshots/grafana/`
- Suricata working: `screenshots/suricata/`
- Cowrie honeypot evidence: `screenshots/cowrie/`
- Kismet wireless detection: `screenshots/kismet/`
- System health: `screenshots/system/`

---

## Hardware: 3D Cluster Case Model
See: `docs/hardware/`
- Model: `docs/hardware/3d-model/`
- Renders: `docs/hardware/renders/`

---

## License
This project is provided under the license included in `LICENSE`.
