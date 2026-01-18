\# System Architecture (Cyber-Shield Pi 5)



\## Overview

Cyber-Shield Pi 5 is a 3-node Raspberry Pi cluster implementing a lightweight SIEM pipeline that integrates:

\- \*\*Node 1 (IDS):\*\* Suricata IDS + local automation scripts

\- \*\*Node 2 (UI/SIEM):\*\* InfluxDB (storage) + Grafana (visualization + alerting) + Kismet (wireless monitoring)

\- \*\*Node 3 (Honeypot):\*\* Cowrie SSH honeypot (attacker interaction + telemetry)



\## Node Roles

\### Node 1 — IDS (Suricata)

\- Captures and analyzes network traffic using Suricata rules.

\- Produces structured logs and alerts.

\- Runs automation scripts (e.g., real-time monitoring / parsing / forwarding as implemented).



Artifacts in repo:

\- `node1-ids/suricata/suricata.yaml`

\- `node1-ids/scripts/realtime\_monitor.py`

\- Evidence: `node1-ids/suricata\_service\_status.txt`, `node1-ids/suricata\_version.txt`



\### Node 2 — SIEM / UI (InfluxDB + Grafana + Kismet)

\- Aggregates telemetry into InfluxDB.

\- Visualizes security metrics in Grafana dashboards.

\- Provides alerting (SMTP contact point/rules) with secrets excluded from GitHub.

\- Monitors wireless activity using Kismet.



Artifacts in repo:

\- Grafana: `node2-ui/grafana/dashboards/siem\_dashboard.json`

\- Alerts: `node2-ui/grafana/alerts/alerts\_smtp.json` (sanitized)

\- Kismet configs: `node2-ui/kismet/\*`

\- Evidence: `node2-ui/\*\_service\_status.txt`, `node2-ui/influx\_version.txt`



\### Node 3 — Honeypot (Cowrie)

\- Exposes SSH honeypot on the standard SSH port(s) while \*\*real administration SSH uses port 22022\*\*.

\- Captures attacker behavior (login attempts, sessions, commands) and provides logs in text and JSON.



Artifacts in repo:

\- `node3-honeypot/cowrie/cowrie.cfg` (sanitized)

\- `node3-honeypot/notes/cowrie\_\*\_sample.txt` (sanitized samples)

\- Evidence: `node3-honeypot/notes/cowrie\_service\_status.txt`



\## Data Flow (High-level)

1\. \*\*Suricata (Node 1)\*\* generates IDS events/alerts.

2\. Telemetry is forwarded/ingested into \*\*InfluxDB (Node 2)\*\*.

3\. \*\*Grafana (Node 2)\*\* queries InfluxDB and renders dashboards; alert rules trigger notifications.

4\. \*\*Cowrie (Node 3)\*\* generates honeypot events/logs which are also integrated into Grafana dashboards.



\## Security Notes

\- Tokens/passwords are intentionally excluded from the repository.

\- See: `docs/security/SECRETS.md`

## Architecture Diagrams
The project includes the following diagrams (see `docs/architecture/diagrams/`):
- `flow_chart.png` – overall workflow / process flow
- `logical_architecture.png` – logical layout of services and data movement
- `physical_architecture.png` – physical node layout (Pi cluster and roles)
- `use_case.png` – administrator/system interactions




