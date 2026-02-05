import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Protocol Configurator")
window.geometry("800x600")

# Sidebar frame for protocol selection
sidebar = tk.Frame(window, width=200, bg="#f0f0f0", relief="sunken", borderwidth=2)
sidebar.pack(side="left", fill="y", padx=5, pady=5)

# Label for the sidebar
sidebar_label = tk.Label(sidebar, text="Protocols", font=("Arial", 12, "bold"), bg="#f0f0f0")
sidebar_label.pack(pady=10)

# List of protocols
protocols = ["I2C", "UART", "SPI"]

# Variable to store the selected protocol
selected_protocol = tk.StringVar()

# Function to handle protocol selection
def on_protocol_select(protocol):
    selected_protocol.set(protocol)
    update_config_area()

# Create protocol selection buttons
for protocol in protocols:
    btn = tk.Button(
        sidebar,
        text=protocol,
        command=lambda p=protocol: on_protocol_select(p),
        width=15,
        anchor="w"
    )
    btn.pack(fill="x", pady=2)

# Main configuration frame
config_area = tk.Frame(window)
config_area.pack(side="right", fill="both", expand=True, padx=5, pady=5)

# Label for the configuration area
config_label = tk.Label(config_area, text="Configuration", font=("Arial", 12, "bold"))
config_label.pack(pady=10)

# Frame to hold dynamic configuration fields
config_fields = tk.Frame(config_area)
config_fields.pack(fill="both", expand=True)

# Function to update configuration fields
def update_config_area():
    for widget in config_fields.winfo_children():
        widget.destroy()

    protocol = selected_protocol.get()

    if protocol == "I2C":
        tk.Label(config_fields, text="I2C Configuration", font=("Arial", 11, "bold")).pack(pady=5)
        tk.Label(config_fields, text="Clock Speed (kHz):").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)
        tk.Label(config_fields, text="Slave Address:").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)

    elif protocol == "UART":
        tk.Label(config_fields, text="UART Configuration", font=("Arial", 11, "bold")).pack(pady=5)
        tk.Label(config_fields, text="Baud Rate:").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)
        tk.Label(config_fields, text="Data Bits:").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)
        tk.Label(config_fields, text="Parity:").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)

    elif protocol == "SPI":
        tk.Label(config_fields, text="SPI Configuration", font=("Arial", 11, "bold")).pack(pady=5)
        tk.Label(config_fields, text="Clock Speed (MHz):").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)
        tk.Label(config_fields, text="Mode (0-3):").pack(anchor="w")
        tk.Entry(config_fields).pack(fill="x", pady=2)

# Run the application
window.mainloop()
