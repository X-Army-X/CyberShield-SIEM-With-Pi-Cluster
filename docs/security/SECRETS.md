# Secrets Handling (Cyber-Shield)

This repository intentionally excludes credentials and tokens.

## Items NOT committed
- InfluxDB API tokens (Grafana data source + ingestion scripts)
- Grafana SMTP credentials / alert contact points
- Any real usernames/passwords used for administration
- Webhook URLs (Discord/Slack/email relay)

## How to configure locally
1. Create a local file (not committed) named: .env
2. Store values such as:
   - INFLUX_URL
   - INFLUX_TOKEN
   - SMTP_HOST / SMTP_USER / SMTP_PASS
3. Ensure .env is listed in .gitignore.

## Why this is required
Publishing tokens or passwords to GitHub can compromise the system and violates secure engineering practice.
