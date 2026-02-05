import tkinter as tk

window = tk.Tk()
window.title("Protocol Configurator")
window.geometry("400x250")


label = tk.Label(window, text="Protocol Configuration Tool", font=("Arial", 14))
label.pack(pady=20)


button = tk.Button(window, text="Configure Protocol", width=20)
button.pack(pady=10)

window.mainloop()
