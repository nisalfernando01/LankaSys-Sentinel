import psutil
import os

def check_background_processes():
    print("=== LankaSys Sentinel - Security Scanner ===\n")
    print("[*] Scanning background processes...\n")
    
    system_procs = 0
    normal_apps = 0
    suspicious_procs = []
    
    # Process okkoma check karanawa (pid, name, saha run wena path eka)
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            exe_path = proc.info['exe']
            name = proc.info['name']
            pid = proc.info['pid']
            
            if exe_path:
                exe_path_lower = exe_path.lower()
                
                # 1. System Files (Safe)
                if "windows\\system32" in exe_path_lower or "windows\\syswow64" in exe_path_lower:
                    system_procs += 1
                    
                # 2. Installed Applications (Safe)
                elif "program files" in exe_path_lower:
                    normal_apps += 1
                    
                # 3. Suspicious Locations (Red Flags!)
                elif "appdata" in exe_path_lower or "temp" in exe_path_lower or "downloads" in exe_path_lower:
                    suspicious_procs.append({'pid': pid, 'name': name, 'path': exe_path})
                    
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Admin permission nathi system processes amathaka karanawa
            pass
            
    # Result eka print karanawa
    print(f"[+] Safe System Processes Found: {system_procs}")
    print(f"[+] Normal Applications Found: {normal_apps}\n")
    
    if suspicious_procs:
        print("[!] WARNING: Suspicious Background Processes Detected!")
        print("    (Malware godak welawata AppData hari Temp folders wala hangila run wenawa)\n")
        
        for p in suspicious_procs:
            print(f"    [!] Name: {p['name']} | PID: {p['pid']}")
            print(f"        Path: {p['path']}\n")
    else:
        print("[+] No suspicious background processes found. System looks clean!")

if __name__ == "__main__":
    check_background_processes()