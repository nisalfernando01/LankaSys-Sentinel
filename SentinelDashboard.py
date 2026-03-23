import customtkinter as ctk
import psutil
import os
import shutil

# Setting up the Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SentinelApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LankaSys Sentinel - Cyber Security Dashboard")
        self.geometry("800x600")

        # Sidebar for navigation
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        self.label = ctk.CTkLabel(self.sidebar, text="SENTINEL V1.0", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        # Buttons
        self.btn_sys = ctk.CTkButton(self.sidebar, text="System Monitor", command=self.show_system)
        self.btn_sys.pack(pady=10, padx=20)
        
        self.btn_net = ctk.CTkButton(self.sidebar, text="Network Tracker", command=self.show_network)
        self.btn_net.pack(pady=10, padx=20)
        
        self.btn_disk = ctk.CTkButton(self.sidebar, text="Disk Cleaner", command=self.show_disk)
        self.btn_disk.pack(pady=10, padx=20)

        # Main Display Area
        self.display = ctk.CTkTextbox(self, width=550, height=500, font=("Courier New", 12))
        self.display.pack(pady=20, padx=20, fill="both", expand=True)

    def show_system(self):
        self.display.delete("1.0", "end")
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        self.display.insert("end", f"--- SYSTEM RESOURCE MONITOR ---\n\n")
        self.display.insert("end", f"CPU Usage: {cpu}%\n")
        self.display.insert("end", f"RAM Usage: {ram}%\n\n")
        self.display.insert("end", "Top Processes:\n")
        for proc in sorted(psutil.process_iter(['name', 'memory_percent']), key=lambda x: x.info['memory_percent'], reverse=True)[:5]:
            self.display.insert("end", f"- {proc.info['name']}: {proc.info['memory_percent']:.2f}%\n")

    def show_network(self):
        self.display.delete("1.0", "end")
        self.display.insert("end", f"{'Process':<20} | {'Remote IP':<20} | {'Status'}\n")
        self.display.insert("end", "-"*60 + "\n")
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED':
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                try: name = psutil.Process(conn.pid).name()
                except: name = "Unknown"
                self.display.insert("end", f"{name:<20} | {raddr:<20} | {conn.status}\n")

    def show_disk(self):
        self.display.delete("1.0", "end")
        usage = psutil.disk_usage('C:\\')
        self.display.insert("end", f"--- DISK ANALYZER ---\n\n")
        self.display.insert("end", f"C: Free Space: {usage.free / (1024**3):.2f} GB\n")
        self.display.insert("end", f"C: Used Space: {usage.used / (1024**3):.2f} GB\n")
        
    def clean_junk(self):
        # Junk cleaning logic can be added here as a button
        pass

if __name__ == "__main__":
    app = SentinelApp()
    app.mainloop()