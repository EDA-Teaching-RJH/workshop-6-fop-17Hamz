rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}
print(rover_status["Battery"])

rover_status["Battery"] = 85
rover_status["Heater"] = "On"
print(rover_status)

mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
] 

