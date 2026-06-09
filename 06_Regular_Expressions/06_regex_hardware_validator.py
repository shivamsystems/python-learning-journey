"""
Practice: 06 Regular Expressions
Topic: Pattern matching with the 're' library
Goal: Parse a messy network log to extract valid MAC addresses and Robot Serial Numbers.
"""

import re

def parse_hardware_logs(log_text):
    # Pattern for MAC addresses (e.g., 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E)
    mac_pattern = r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"
    
    # Pattern for custom serial numbers (Format: RBT-YYYY-XXX)
    serial_pattern = r"RBT-\d{4}-[A-Z]{3}"
    
    print("--- Extracting Network Interfaces (MAC Addresses) ---")
    for match in re.finditer(mac_pattern, log_text):
        print(f"Valid MAC found: {match.group(0)}")
        
    print("\n--- Extracting Registered Robot Serials ---")
    for match in re.finditer(serial_pattern, log_text):
        print(f"Valid Serial found: {match.group(0)}")

if __name__ == "__main__":
    messy_log = """
    [INFO] Boot sequence initiated...
    [WARN] Unrecognized device detected at MAC 5E:FF:56:A2:AF:15.
    [INFO] Handshake successful with serial RBT-2025-ABC.
    [ERROR] Failed to ping 192.168.1.50.
    [INFO] Primary controller MAC is 0A-1B-2C-3D-4E-5F (Serial: RBT-2026-XYZ).
    [WARN] RBT-202-XX is not a valid serial format.
    """
    
    parse_hardware_logs(messy_log)
