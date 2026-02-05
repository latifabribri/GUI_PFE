import tkinter as tk
from tkinter import ttk

#main window
window = tk.Tk()
window.title("Protocol Configurator")
window.geometry("500x400")

#Label
label = tk.Label(window, text="Protocol Configuration Tool", font=("Arial", 14))
label.pack(pady=10)

# Protocol selection
protocol_var = tk.StringVar()
protocols = ["I2C", "UART", "SPI"]

protocol_label = tk.Label(window, text="Select Protocol:", font=("Arial", 12))
protocol_label.pack(pady=5)

protocol_dropdown = ttk.Combobox(window, textvariable=protocol_var, values=protocols, state="readonly")
protocol_dropdown.pack(pady=5)

# Configuration frame (initially empty)
config_frame = tk.Frame(window)
config_frame.pack(pady=20, fill="both", expand=True)

# Function to update configuration fields
def update_config_fields(*args):
    # Clear previous widgets
    for widget in config_frame.winfo_children():
        widget.destroy()

    protocol = protocol_var.get()

    if protocol == "I2C":
        tk.Label(config_frame, text="I2C Configuration", font=("Arial", 12)).pack(pady=5)
        tk.Label(config_frame, text="Clock Speed (kHz):").pack()
        tk.Entry(config_frame).pack()
        tk.Label(config_frame, text="Slave Address:").pack()
        tk.Entry(config_frame).pack()

    elif protocol == "UART":
        tk.Label(config_frame, text="UART Configuration", font=("Arial", 12)).pack(pady=5)
        tk.Label(config_frame, text="Baud Rate:").pack()
        tk.Entry(config_frame).pack()
        tk.Label(config_frame, text="Data Bits:").pack()
        tk.Entry(config_frame).pack()
        tk.Label(config_frame, text="Parity:").pack()
        tk.Entry(config_frame).pack()

    elif protocol == "SPI":
        tk.Label(config_frame, text="SPI Configuration", font=("Arial", 12)).pack(pady=5)
        tk.Label(config_frame, text="Clock Speed (MHz):").pack()
        tk.Entry(config_frame).pack()
        tk.Label(config_frame, text="Mode (0-3):").pack()
        tk.Entry(config_frame).pack()

# Bind the dropdown selection to update the config fields
protocol_var.trace_add("write", update_config_fields)

# Configure Protocol Button
configure_button = tk.Button(window, text="Save Configuration", width=20)
configure_button.pack(pady=10)

# Run the application
window.mainloop()
