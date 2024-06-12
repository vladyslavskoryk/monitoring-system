import tkinter as tk
from time import strftime
from tkinter import ttk
import psutil
from app_table_wiget import tableFrame
from componentUsaged import componentUsaged
from main import runningProcesses, showNetwork, FreeSpace

# Set up the root window
root = tk.Tk()
root.geometry('1000x700')  # Provide more space for better layout
root.title('Системний Моніторинг')

# Define a custom theme
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#2b2b2b')
style.configure('TNotebook', background='#2b2b2b', borderwidth=0)
style.configure('TNotebook.Tab', padding=[20, 10], font=('Arial', 12, 'bold'), background='#3c3f41', foreground='white')
style.configure('TLabel', background='#2b2b2b', foreground='white', font=('Arial', 10))
style.configure('TButton', padding=[10, 5], font=('Arial', 10, 'bold'), background='#4b6eaf', foreground='white')

# Create a notebook with expanded padding for a cleaner layout
notebook = ttk.Notebook(root)
notebook.pack(pady=30, padx=20, expand=True)

# Create frames for tabs
frame1 = ttk.Frame(notebook, width=800, height=650)
frame2 = ttk.Frame(notebook, width=800, height=650)
frame3 = ttk.Frame(notebook, width=800, height=650)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# Add frames to notebook
notebook.add(frame1, text='Ресурси')
notebook.add(frame2, text='Процеси')
notebook.add(frame3, text='Мережа')

# Configure tables
tableFrame(root=root, frame=frame3, dataGener=showNetwork, columns=["Опис", "MAC-адреса", "IP-адреса"])
tableFrame(root=root, frame=frame2, dataGener=runningProcesses, columns=["ід", "ім'я", "Віртуальний розмір (VirtualSize)"])

# Dynamic updates
def update_time():
    time_label.config(text='ЧАС: ' + strftime('%H:%M:%S %p'))
    time_label.after(1000, update_time)

def update_ram():
    ram_label.config(text='ОЗУ: ' + str(psutil.virtual_memory().percent) + '%')
    ram_label.after(1000, update_ram)

def update_cpu():
    cpu_label.config(text='ПРОЦЕСОР: ' + str(psutil.cpu_percent(interval=None)) + '%')
    cpu_label.after(1000, update_cpu)

time_label = ttk.Label(frame1, font=('Arial', 12))
time_label.pack(anchor='w', pady=5)
ram_label = ttk.Label(frame1, font=('Arial', 12))
ram_label.pack(anchor='w', pady=5)
cpu_label = ttk.Label(frame1, font=('Arial', 12))
cpu_label.pack(anchor='w', pady=5)

update_time()
update_ram()
update_cpu()

# Display free space information
for info in FreeSpace():
    lbl = ttk.Label(frame1, text=info, font=('Arial', 10))
    lbl.pack(anchor="w", pady=2)

# Run the main loop
root.mainloop()
