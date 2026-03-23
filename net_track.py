import psutil
import socket

def track_network():
    print("=== LankaSys Sentinel - Network Connection Tracker ===\n")
    print(f"{'Process Name':<20} | {'PID':<8} | {'Local Address':<20} | {'Remote (Internet) IP':<20} | {'Status'}")
    print("-" * 85)

    # Active network connections check karanawa
    connections = psutil.net_connections(kind='inet')
    
    for conn in connections:
        # Connect wela thiyana ewa (ESTABLISHED) witharak balamu
        if conn.status == 'ESTABLISHED':
            pid = conn.pid
            try:
                proc = psutil.Process(pid)
                name = proc.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                name = "Unknown"

            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            
            print(f"{name:<20} | {pid:<8} | {laddr:<20} | {raddr:<20} | {conn.status}")

if __name__ == "__main__":
    track_network()