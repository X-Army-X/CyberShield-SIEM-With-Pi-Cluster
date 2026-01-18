\# Planned Advanced Analytics (Beyond Project Scope)



\## CyberShield ML Anomaly Detection (Planned – Future Work)

\*\*Status:\*\* Not implemented in this prototype. This document describes the intended ML layer and integration points.



\## Purpose

Identify anomalous security behaviour by learning a baseline from normal telemetry and flagging deviations.



\## Intended data sources (already integrated into the SIEM pipeline)

\- \*\*Suricata:\*\* alert counts over time, signatures, source/destination distribution, severity

\- \*\*Cowrie:\*\* login failures, session events, username patterns, source IP behaviour

\- \*\*Kismet:\*\* device/AP detection rates, emergence of new devices, (optionally) cloaked SSIDs



\## Feature engineering (examples)

\*\*Sliding-window features (e.g., 1m / 5m / 15m):\*\*

\- counts per source IP / destination IP

\- entropy of signature distribution

\- severity-weighted alert score

\- rate of Cowrie authentication failures

\- rate of new wireless devices / APs



\*\*Optional correlation features:\*\*

\- Suricata spikes aligned with Cowrie events

\- wireless spikes aligned with IDS spikes (multi-layer signal)



\## Candidate models (unsupervised by default)

\- Isolation Forest

\- One-Class SVM

\- Autoencoder reconstruction error

\- Statistical baselines (EWMA / z-score) as a strong non-ML benchmark



\## Output (future)

\- `anomaly\_score` time series (0–1 or unbounded score)

\- `anomaly\_flag` boolean (thresholded)

\- top contributing features (explainability summary)



\## Evaluation plan

Offline validation using:

\- injected test scenarios (documented attacks)

\- precision/recall where labels exist

\- time-to-detect and false positive rate



Operational considerations:

\- concept drift monitoring and periodic retraining

\- threshold tuning per environment



\## Next integration step

Publish computed `anomaly\_score` and `anomaly\_flag` into InfluxDB as measurement `ml\_anomalies`, then visualize in Grafana.



