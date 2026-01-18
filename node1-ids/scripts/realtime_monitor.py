#!/usr/bin/env python3
"""
Raspberry Pi 5 Cyber-Shield - Real-Time Alert Monitor
Displays alerts as they happen in real-time

Author: Abdul Hakim Hussam Shalabieh
Date: November 2025
"""

import json
import time
import os
from datetime import datetime
from collections import deque

# ============================================
# CONFIGURATION
# ============================================
EVE_LOG_PATH = "/var/log/suricata/eve.json"
REFRESH_INTERVAL = 2  # seconds
MAX_DISPLAY_ALERTS = 10  # Show last 10 alerts

# Colors for terminal output
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def get_severity_color(severity):
    """Get color based on severity level"""
    if severity == 1:
        return Colors.RED
    elif severity == 2:
        return Colors.YELLOW
    elif severity == 3:
        return Colors.CYAN
    else:
        return Colors.WHITE

def get_severity_label(severity):
    """Get label for severity"""
    labels = {
        1: "🚨 CRITICAL",
        2: "⚠️  WARNING",
        3: "ℹ️  INFO"
    }
    return labels.get(severity, "❓ UNKNOWN")

def format_timestamp(timestamp):
    """Format timestamp for display"""
    try:
        dt = datetime.fromisoformat(timestamp.replace('+0400', ''))
        return dt.strftime("%H:%M:%S")
    except:
        return timestamp

def get_device_name(ip):
    """Get friendly name for known devices"""
    devices = {
        '192.168.100.182': 'Your Computer',
        '192.168.100.40': 'Samsung Smart TV',
        '192.168.100.1': 'Router',
        '192.168.100.115': 'Node 1 (IDS)',
    }
    return devices.get(ip, ip)

def print_header(stats):
    """Print the header with statistics"""
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}  🛡️  RASPBERRY PI 5 CYBER-SHIELD - REAL-TIME MONITOR{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}  Node 1: Wired IDS (Suricata){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print()
    
    # Statistics bar
    print(f"{Colors.BOLD}System Status:{Colors.RESET}")
    print(f"  Time: {Colors.GREEN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"  Monitoring: {Colors.GREEN}eth0 (192.168.100.115){Colors.RESET}")
    print(f"  Total Alerts Today: {Colors.YELLOW}{stats['total']}{Colors.RESET}")
    print(f"  Critical: {Colors.RED}{stats['critical']}{Colors.RESET} | " +
          f"Warning: {Colors.YELLOW}{stats['warning']}{Colors.RESET} | " +
          f"Info: {Colors.CYAN}{stats['info']}{Colors.RESET}")
    print()
    print(f"{Colors.BOLD}Recent Alerts (Last {MAX_DISPLAY_ALERTS}):{Colors.RESET}")
    print("-" * 80)

def display_alert(alert, is_new=False):
    """Display a single alert"""
    severity = alert.get('alert', {}).get('severity', 3)
    color = get_severity_color(severity)
    severity_label = get_severity_label(severity)
    
    timestamp = format_timestamp(alert.get('timestamp', ''))
    signature = alert.get('alert', {}).get('signature', 'Unknown')
    src_ip = get_device_name(alert.get('src_ip', 'Unknown'))
    dst_ip = get_device_name(alert.get('dest_ip', 'Unknown'))
    proto = alert.get('proto', 'Unknown')
    
    # Truncate signature if too long
    if len(signature) > 50:
        signature = signature[:47] + "..."
    
    # New alert indicator
    new_indicator = "🆕 " if is_new else "   "
    
    print(f"{new_indicator}{color}{severity_label}{Colors.RESET} " +
          f"[{Colors.BOLD}{timestamp}{Colors.RESET}] " +
          f"{signature}")
    print(f"     {Colors.MAGENTA}{src_ip}{Colors.RESET} → " +
          f"{Colors.MAGENTA}{dst_ip}{Colors.RESET} " +
          f"({proto})")
    print()

def tail_log(file_path, num_lines=MAX_DISPLAY_ALERTS):
    """Get last N lines from log file"""
    try:
        with open(file_path, 'r') as f:
            # Seek to end
            f.seek(0, 2)
            file_size = f.tell()
            
            # Read backwards to get last lines
            lines = deque(maxlen=num_lines)
            buffer_size = 8192
            buffer = ''
            
            position = file_size
            while position > 0 and len(lines) < num_lines:
                read_size = min(buffer_size, position)
                position -= read_size
                f.seek(position)
                chunk = f.read(read_size)
                buffer = chunk + buffer
                
                # Split into lines
                temp_lines = buffer.split('\n')
                buffer = temp_lines[0]
                
                for line in reversed(temp_lines[1:]):
                    if line.strip():
                        lines.appendleft(line)
                        if len(lines) >= num_lines:
                            break
            
            return list(lines)
    except Exception as e:
        return []

def parse_alerts(lines):
    """Parse alert lines from log"""
    alerts = []
    for line in lines:
        try:
            event = json.loads(line.strip())
            if event.get('event_type') == 'alert':
                alerts.append(event)
        except:
            continue
    return alerts

def calculate_stats(alerts):
    """Calculate alert statistics"""
    stats = {
        'total': len(alerts),
        'critical': 0,
        'warning': 0,
        'info': 0
    }
    
    for alert in alerts:
        severity = alert.get('alert', {}).get('severity', 3)
        if severity == 1:
            stats['critical'] += 1
        elif severity == 2:
            stats['warning'] += 1
        elif severity == 3:
            stats['info'] += 1
    
    return stats

def main():
    """Main monitoring loop"""
    print(f"{Colors.GREEN}Starting Real-Time Monitor...{Colors.RESET}")
    print(f"{Colors.YELLOW}Press Ctrl+C to stop{Colors.RESET}")
    time.sleep(2)
    
    previous_alerts = []
    
    try:
        while True:
            # Get latest alerts
            lines = tail_log(EVE_LOG_PATH, num_lines=100)
            current_alerts = parse_alerts(lines)
            
            # Calculate stats
            stats = calculate_stats(current_alerts)
            
            # Find new alerts
            new_alert_sigs = []
            if previous_alerts:
                prev_timestamps = [a.get('timestamp') for a in previous_alerts]
                for alert in current_alerts:
                    if alert.get('timestamp') not in prev_timestamps:
                        new_alert_sigs.append(alert.get('timestamp'))
            
            # Display
            clear_screen()
            print_header(stats)
            
            # Show last MAX_DISPLAY_ALERTS alerts
            display_alerts = current_alerts[-MAX_DISPLAY_ALERTS:] if len(current_alerts) > MAX_DISPLAY_ALERTS else current_alerts
            
            for alert in reversed(display_alerts):
                is_new = alert.get('timestamp') in new_alert_sigs
                display_alert(alert, is_new)
            
            if not display_alerts:
                print(f"  {Colors.GREEN}✓ No alerts yet. Monitoring...{Colors.RESET}")
                print()
            
            # Footer
            print("-" * 80)
            print(f"{Colors.CYAN}Refreshing every {REFRESH_INTERVAL} seconds... (Ctrl+C to stop){Colors.RESET}")
            
            # Store for next iteration
            previous_alerts = current_alerts.copy()
            
            # Wait before refresh
            time.sleep(REFRESH_INTERVAL)
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Monitoring stopped by user{Colors.RESET}")
        print(f"{Colors.GREEN}Thank you for using Cyber-Shield!{Colors.RESET}")

if __name__ == "__main__":
    main()
