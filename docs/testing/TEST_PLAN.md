\# Test Plan (Cyber-Shield Pi 5)



\## Objective

Validate that the IDS, SIEM dashboard, and honeypot pipeline functions end-to-end:

\- Suricata detects events and produces logs.

\- Node 2 stores/visualizes metrics in Grafana dashboards.

\- Cowrie captures attacker sessions and presents evidence in Grafana.



\## Test Cases



\### TC-01: Suricata Service Health

\*\*Steps\*\*

1\. On Node 1: `sudo systemctl status suricata`

2\. Confirm Suricata version: `suricata -V`



\*\*Expected\*\*

\- Service is active/running.

\- Version is displayed.



\### TC-02: Suricata Alert Generation

\*\*Steps\*\*

1\. Generate benign traffic or known test signature.

2\. Confirm Suricata logs update (eve.json/fast.log depending on configuration).

3\. Confirm the dashboard updates on Grafana.



\*\*Expected\*\*

\- Alerts appear in Suricata output.

\- Grafana dashboard reflects new events.



\### TC-03: InfluxDB + Grafana Availability

\*\*Steps\*\*

1\. On Node 2: check service status for InfluxDB and Grafana.

2\. Open Grafana UI in browser and load the SIEM dashboard.



\*\*Expected\*\*

\- Services running.

\- Dashboard renders panels successfully.



\### TC-04: Cowrie Honeypot Capture

\*\*Steps\*\*

1\. Connect to honeypot SSH surface (not port 22022).

2\. Attempt failed login and basic commands.

3\. Confirm Cowrie logs record the attempt and sessions appear in Grafana panels.



\*\*Expected\*\*

\- Cowrie logs contain login attempts/session metadata.

\- Grafana panels show honeypot activity.



\## Evidence Files (Repository)

\- Node 1 evidence: `node1-ids/\*\_status.txt`, `node1-ids/\*\_version.txt`

\- Node 2 evidence: `node2-ui/\*\_service\_status.txt`, `node2-ui/influx\_version.txt`

\- Node 3 evidence: `node3-honeypot/notes/\*`



