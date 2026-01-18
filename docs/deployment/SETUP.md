\# Deployment / Setup Guide (Cyber-Shield Pi 5)



\## Preconditions

\- 3 Raspberry Pi nodes reachable on the same LAN.

\- SSH enabled on all nodes.

\- Node 3 administrative SSH is on \*\*port 22022\*\* (port 22 is reserved for honeypot interaction).



\## Node 1 (IDS) — Suricata

1\. Install Suricata and confirm service is active:

&nbsp;  - `sudo systemctl status suricata`

2\. Configure Suricata:

&nbsp;  - Update `suricata.yaml` as required for the interface and logging.

3\. Run automation scripts:

&nbsp;  - Use the provided Python scripts under `node1-ids/scripts/` (project-specific).



\## Node 2 (SIEM/UI) — InfluxDB + Grafana + Kismet

1\. Install and start InfluxDB:

&nbsp;  - `sudo systemctl status influxdb`

2\. Install and start Grafana:

&nbsp;  - `sudo systemctl status grafana-server`

3\. Configure Grafana data source (InfluxDB):

&nbsp;  - Influx token is required locally and is not stored in GitHub.

&nbsp;  - See `docs/security/SECRETS.md`

4\. Import dashboards:

&nbsp;  - Import `node2-ui/grafana/dashboards/siem\_dashboard.json`

5\. Configure alerting:

&nbsp;  - Import/replicate alert rules from `node2-ui/grafana/alerts/alerts\_smtp.json` (sanitized).

&nbsp;  - Re-enter SMTP credentials locally (not committed).

6\. Kismet:

&nbsp;  - Use `node2-ui/kismet/kismet\_site.conf` and scripts as needed.



\## Node 3 (Honeypot) — Cowrie

1\. Ensure Cowrie is installed and running.

2\. Administrative SSH:

&nbsp;  - `ssh -p 22022 npc@<node3-ip>`

3\. Honeypot SSH:

&nbsp;  - Any other SSH port exposed for attacker simulation should be treated as the honeypot surface.

4\. Logs:

&nbsp;  - Cowrie logs exist as text and JSON (samples provided in repo).



