import psutil
import os

def get_size_format(b, factor=1024, suffix="B"):
    # Bytes walin thiyana ewa lassanata GB/MB walata harawana function eka
    for unit in ["", "K", "M", "G", "T"]:
        if b < factor:
            return f"{b:.2f} {unit}{suffix}"
        b /= factor
    return f"{b:.2f} Y{suffix}"

def get_directory_size(path):
    # Folder ekaka thiyana okkoma files wala size eka ekathu karanawa
    total_size = 0
    if os.path.exists(path):
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    # Permission errors amathaka karala access thiyana files wala size gannawa
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
                except (PermissionError, FileNotFoundError):
                    pass
    return total_size

def analyze_disk():
    print("=== LankaSys Sentinel - Disk Storage Analyzer ===\n")
    
    # 1. C: Drive eke general usage eka
    usage = psutil.disk_usage('C:\\')
    print(f"[*] C: Drive Total Space: {get_size_format(usage.total)}")
    print(f"[*] C: Drive Used Space:  {get_size_format(usage.used)} ({usage.percent}%)")
    print(f"[*] C: Drive Free Space:  {get_size_format(usage.free)}\n")

    # 2. Temporary Files (Junk) scan kireema
    print("[*] Scanning for Temporary (Junk) Files...\n")
    
    # Temp folders thiyana locations
    temp_folders = {
        "User Temp (App Cache)": os.environ.get('TEMP'),
        "Windows Temp (System Cache)": r"C:\Windows\Temp",
        "SoftwareDistribution (Update Cache)": r"C:\Windows\SoftwareDistribution\Download"
    }
    
    total_junk = 0
    for name, path in temp_folders.items():
        if path:
            print(f"    Scanning: {name}...")
            size = get_directory_size(path)
            total_junk += size
            print(f"    -> Found: {get_size_format(size)}\n")
            
    print("-" * 40)
    print(f"[!] Total Junk Files that can be deleted: {get_size_format(total_junk)}")
    print("-" * 40)

if __name__ == "__main__":
    analyze_disk()