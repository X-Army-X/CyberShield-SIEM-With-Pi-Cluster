\# Cyber-Shield – Release Notes (Final Build)



\## Project Status

This repository represents the final, demonstrable implementation of the

Raspberry Pi 5 Cyber-Shield project.



\## Implemented Components

\- Node 1: Wired IDS (Suricata + ML baseline)

\- Node 2: SIEM (InfluxDB + Grafana) + Wireless IDS (Kismet)

\- Node 3: Honeypot (Cowrie) with dashboard integration



\## Known Limitations

\- Cowrie fake filesystem lists decoy files; some file content read operations

&nbsp; are limited due to Cowrie filesystem emulation constraints.

\- ML component currently provides baseline profiling and anomaly comparison

&nbsp; logic; advanced adaptive learning is future work.



\## Academic Note

All limitations are documented intentionally to preserve system stability and

examiner reproducibility.



