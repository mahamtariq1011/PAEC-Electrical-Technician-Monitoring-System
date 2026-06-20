# =====================================================
# ATOMIC ENERGY ELECTRICAL TECHNICIAN MONITORING SYSTEM
# Developed By: Maham Tariq
# Degree: BS Artificial Intelligence
# Description:
# This project provides information about nuclear power
# plants, electrical technician duties, maintenance,
# safety procedures, emergency systems, equipment
# monitoring, and power calculations.
# =====================================================

import tkinter as tk
from tkinter import scrolledtext
import random
# =====================================================
# FUNCTION: update_text()
# Purpose:
# Updates the information display area whenever the
# user clicks a button.
# =====================================================

# ---------------- UPDATE TEXT ----------------

def update_text(message):
    detail_box.config(state=tk.NORMAL)
    detail_box.delete("1.0", tk.END)
    detail_box.insert(tk.END, message)
    detail_box.config(state=tk.DISABLED)

 # =====================================================
# DASHBOARD SECTION
# Displays general information about Pakistan's
# nuclear power generation system.
# =====================================================
# ---------------- INFORMATION FUNCTIONS ----------------

def show_dashboard():
    update_text(
        "PAEC MONITORING DASHBOARD\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🟢 System Status        : ONLINE\n"
        "🟢 Safety Status        : NORMAL\n"
        "🟢 Equipment Monitoring : ACTIVE\n\n"
        "Operational Plants : 6\n"
        "Installed Capacity : 3530 MWe\n"
        "Contribution        : 18.3%\n\n"
        "Available Modules:\n"
        "• Job Overview\n"
        "• Plant Maintenance\n"
        "• Emergency Systems\n"
        "• Safety Protocols\n"
        "• Equipment Status\n"
        "• Nuclear Plants\n"
        "• Statistics 2024\n"
        "• Future Expansion\n"
    )
    
# =====================================================
# JOB OVERVIEW SECTION
# Displays responsibilities of an Electrical Technician
# working in a nuclear power plant.
# =====================================================
def show_overview():
    update_text(
        "=== ELECTRICAL TECHNICIAN ROLE ===\n\n"
        "Electrical Technicians are responsible for:\n\n"
        "• Operating electrical systems safely.\n"
        "• Maintaining transformers and motors.\n"
        "• Troubleshooting faults.\n"
        "• Monitoring power systems.\n"
        "• Supporting nuclear plant operations.\n"
        "• Ensuring plant reliability and safety."
    )
# =====================================================
# MAINTENANCE SECTION
# Shows preventive and corrective maintenance tasks.
# =====================================================
def show_maintenance():
    update_text(
        "=== PREVENTIVE & CORRECTIVE MAINTENANCE ===\n\n"
        "• Inspect transformers, motors, switchgear and breakers.\n"
        "• Diagnose faults using Multimeters.\n"
        "• Perform routine maintenance.\n"
        "• Repair damaged equipment.\n"
        "• Calibrate electrical instruments.\n"
        "• Maintain control panels and protection systems."
    )
# =====================================================
# EMERGENCY SYSTEMS SECTION
# Displays information about backup power and
# emergency response systems.
# =====================================================
def show_emergency():
    update_text(
        "=== EMERGENCY & BACKUP SYSTEMS ===\n\n"
        "• UPS provides instant backup power.\n"
        "• Diesel Generators start automatically.\n"
        "• Cooling systems remain operational.\n"
        "• Emergency alarms notify operators.\n"
        "• Reactor safety systems remain active."
    )
# =====================================================
# SAFETY PROTOCOLS SECTION
# Shows radiation safety and electrical safety
# procedures used in nuclear facilities.
# =====================================================
def show_safety():
    update_text(
        "=== SAFETY & RADIATION PROTOCOLS ===\n\n"
        "• Follow Lockout/Tagout procedures.\n"
        "• Wear protective equipment.\n"
        "• Use radiation monitoring devices.\n"
        "• Follow plant safety regulations.\n"
        "• Observe quality assurance standards.\n"
        "• Report hazards immediately."
    )

# =====================================================
# NUCLEAR POWER PLANTS SECTION
# Displays information about Pakistan's nuclear power plants.
# nuclear power plants in Pakistan.
# =====================================================
def show_nuclear_plants():
    update_text(
        "=== NUCLEAR POWER PLANTS ===\n\n"
        "C-1 : 325 MWe\n"
        "C-2 : 325 MWe\n"
        "C-3 : 340 MWe\n"
        "C-4 : 340 MWe\n"
        "K-2 : 1100 MWe\n"
        "K-3 : 1100 MWe\n\n"
        "Total Installed Capacity = 3530 MWe"
    )
# =====================================================
# PLANT PERFORMANCE STATISTICS
# Displays generation and availability data
# for nuclear power plants.
# =====================================================
def show_statistics():
    update_text(
        "=== PERFORMANCE STATISTICS 2024 ===\n\n"
        "C-1 Availability Factor : 92.83%\n"
        "C-2 Availability Factor : 92.98%\n"
        "C-3 Availability Factor : 85.49%\n"
        "C-4 Availability Factor : 93.80%\n"
        "K-2 Availability Factor : 75.00%\n"
        "K-3 Availability Factor : 85.79%\n\n"
        "Electricity Supplied:\n"
        "22,795 Million kWh"
    )
# =====================================================
# FUTURE EXPANSION SECTION
# Displays information about the C-5 Nuclear
# Power Plant project.
# =====================================================
def show_future():
    update_text(
        "=== FUTURE EXPANSION (C-5) ===\n\n"
        "Project Name : Chashma Unit-5\n"
        "Capacity : 1200 MWe\n"
        "Status : Under Construction\n\n"
        "Groundbreaking Ceremony:\n"
        "14 July 2023\n\n"
        "Purpose:\n"
        "Increase Pakistan's nuclear power generation capacity."
    )

# ---------------- EQUIPMENT STATUS ----------------
# =====================================================
# EQUIPMENT STATUS SIMULATOR
# Randomly generates equipment status to simulate
# monitoring of plant electrical equipment.
# =====================================================
def check_equipment():

    equipment = [
        "Transformer",
        "Circuit Breaker",
        "Emergency Generator",
        "UPS System",
        "Control Panel",
        "Electric Motor"
    ]

    status = random.choice([
        "WORKING NORMALLY ✓",
        "MAINTENANCE REQUIRED ⚠",
        "FAULT DETECTED ✖"
    ])

    update_text(
        f"=== EQUIPMENT STATUS ===\n\n"
        f"Equipment : {random.choice(equipment)}\n\n"
        f"Status : {status}"
    )

# ---------------- POWER CALCULATOR ----------------
# =====================================================
# POWER CALCULATOR
# Formula Used:
# Power (W) = Voltage (V) × Current (A)
# =====================================================
def calculate_power():

    try:

        voltage = float(voltage_entry.get())
        current = float(current_entry.get())

        power = voltage * current

        update_text(
            "=== POWER CALCULATION ===\n\n"
            f"Voltage : {voltage} V\n"
            f"Current : {current} A\n\n"
            f"Power : {power:.2f} Watts"
        )

    except:
        update_text("Please enter valid numeric values.")

# ---------------- EMERGENCY TEST ----------------
# =====================================================
# EMERGENCY BACKUP TEST
# Simulates a power failure and activation of
# backup safety systems.
# =====================================================
def emergency_test():

    update_text(
        "=== EMERGENCY BACKUP TEST ===\n\n"
        "MAIN POWER FAILURE DETECTED!\n\n"
        "Checking UPS System... ✓\n"
        "UPS Activated Successfully ✓\n\n"
        "Starting Generator... ✓\n"
        "Generator Online ✓\n\n"
        "Cooling System Active ✓\n"
        "Control Systems Active ✓\n\n"
        "PLANT STATUS : SAFE ✓"
    )

# ---------------- WINDOW ----------------
# =====================================================
# MAIN APPLICATION WINDOW
# Creates the main GUI window.
# =====================================================
root = tk.Tk()
root.title("Atomic Energy Electrical Technician Monitoring System")
root.state("zoomed")
root.configure(bg="light green")

# ---------------- TITLE ----------------
# =====================================================
# APPLICATION TITLE
# =====================================================
title = tk.Label(
    root,
    text="PAEC ELECTRICAL TECHNICIAN MONITORING SYSTEM",
    font=("Segoe UI", 18, "bold"),
    bg=root["bg"],
    fg="#1f2937"
)

title.pack(pady=8)
stats_frame = tk.Frame(root, bg="#0f172a")
stats_frame.pack(fill="x", padx=20, pady=5)

tk.Label(
    stats_frame,
    text="⚡ Operational Plants\n6",
    font=("Segoe UI", 12, "bold"),
    bg="#4a7c59",
    fg="white",
    width=20,
    height=3
).pack(side="left", padx=10)

tk.Label(
    stats_frame,
    text="🏭 Capacity\n3530 MWe",
    font=("Segoe UI", 12, "bold"),
    bg="#4a7c59",
    fg="white",
    width=20,
    height=3
).pack(side="left", padx=10)

tk.Label(
    stats_frame,
    text="📊 Contribution\n18.3%",
    font=("Segoe UI", 12, "bold"),
    bg="#4a7c59",
    fg="white",
    width=20,
    height=3
).pack(side="left", padx=10)
# ---------------- MAIN FRAME ----------------
# =====================================================
# MAIN FRAME
# Divides the application into left and right sections.
# =====================================================
main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(fill=tk.BOTH, expand=True)

# ---------------- LEFT PANEL ----------------
# =====================================================
# LEFT PANEL
# Contains all navigation buttons and calculator.
# =====================================================
button_frame = tk.Frame(
    main_frame,
    bg="Dark Green",
    padx=10,
    pady=10
)
button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# ---------------- RIGHT PANEL ----------------
# =====================================================
# RIGHT PANEL
# Contains the information display area.
# =====================================================
text_frame = tk.Frame(
    main_frame,
    bg="#0f172a",
    highlightbackground="#66bb6a",
    highlightthickness=3
)
text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# ---------------- BUTTON STYLE ----------------
# =====================================================
# BUTTON STYLING
# Common design for all buttons.
# =====================================================
btn_style = {
    "font": ("Segoe UI", 11, "bold"),
    "bg": "forest green",
    "fg": "white",
    "width": 22,
    "height": 1,
    "bd": 0,
    "activebackground": "lime green",
    "activeforeground": "white",
    "cursor": "hand2"
}

# ---------------- BUTTONS ----------------
# =====================================================
# NAVIGATION BUTTONS
# Used to access different project modules.
# =====================================================
tk.Button(button_frame, text="1. Dashboard", command=show_dashboard, **btn_style).pack(pady=4)

tk.Button(button_frame, text="2. Job Overview", command=show_overview, **btn_style).pack(pady=4)

tk.Button(button_frame, text="3. Plant Maintenance", command=show_maintenance, **btn_style).pack(pady=4)

tk.Button(button_frame, text="4. Emergency Systems", command=show_emergency, **btn_style).pack(pady=4)

tk.Button(button_frame, text="5. Safety Protocols", command=show_safety, **btn_style).pack(pady=4)

tk.Button(button_frame, text="6. Equipment Status", command=check_equipment, **btn_style).pack(pady=4)

tk.Button(button_frame, text="7. Nuclear Plants", command=show_nuclear_plants, **btn_style).pack(pady=4)

tk.Button(button_frame, text="8. Statistics 2024", command=show_statistics, **btn_style).pack(pady=4)

tk.Button(button_frame, text="9. Future Expansion", command=show_future, **btn_style).pack(pady=4)

# ---------------- CALCULATOR ----------------
# =====================================================
# POWER CALCULATOR INPUT FIELDS
# Accepts voltage and current values from user.
# =====================================================
tk.Label(
    button_frame,
    text="⚡ POWER CALCULATOR",
    bg="dark green",
    fg="white",
    font=("Segoe UI", 13, "bold")
).pack(pady=(15, 5))

tk.Label(button_frame, text="Voltage (V)", bg="#0f172a", fg="white").pack()

voltage_entry = tk.Entry(
    button_frame,
    font=("Segoe UI", 11),
    width=20
)
voltage_entry.pack(pady=2)

tk.Label(button_frame, text="Current (A)", bg="#0f172a", fg="white").pack()

current_entry = tk.Entry(
    button_frame,
    font=("Segoe UI", 11),
    width=20
)
current_entry.pack(pady=2)

tk.Button(
    button_frame,
    text="Calculate Power",
    command=calculate_power,
    **btn_style
).pack(pady=10)

tk.Button(
    button_frame,
    text="Emergency Backup Test",
    command=emergency_test,
    **btn_style
).pack(pady=5)

# ---------------- OUTPUT BOX ----------------
# =====================================================
# INFORMATION DISPLAY AREA
# Displays information selected by the user.
# =====================================================
detail_box = scrolledtext.ScrolledText(
    text_frame,
    font=("Segoe UI", 14),
    bg="#202124",
    fg="#e8eaed",
    insertbackground="white",
    wrap=tk.WORD,
    bd=0
)
detail_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

detail_box.insert(
    tk.END,
    "WELCOME TO PAEC MONITORING SYSTEM\n\n"
    "Select any option from the left panel."
)

detail_box.config(state=tk.DISABLED)

# ---------------- FOOTER ----------------
# =====================================================
# FOOTER SECTION
# Displays developer information.
# =====================================================
footer = tk.Label(
    root,
    text="Developed By Maham Tariq | BS Artificial Intelligence",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 10, "italic")
)

footer.pack(pady=5)

# ---------------- RUN ----------------
# =====================================================
# PROGRAM EXECUTION
# Starts the GUI application.
# =====================================================
show_dashboard()
root.mainloop()