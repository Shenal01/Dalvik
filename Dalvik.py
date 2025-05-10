import struct

def high16_to_float(hex16):
    """Convert a 16-bit high16 to float."""
    full_hex = hex16 << 16
    float_val = struct.unpack('>f', full_hex.to_bytes(4, byteorder='big'))[0]
    return f"""
[HIGH16 → FLOAT]
High16:   0x{hex16:04X}
Full Hex: 0x{full_hex:08X}
Float:    {float_val}f
"""

def float_to_hex_and_high16(value):
    """Convert float to 32-bit hex and show const/high16 if compatible."""
    packed = struct.pack('>f', value)
    int_val = struct.unpack('>I', packed)[0]

    result = f"""
[FLOAT → HEX]
Float:    {value}f
Hex:      0x{int_val:08X}
"""

    if int_val & 0xFFFF == 0:
        high16 = int_val >> 16
        result += f"Dalvik:   const/high16 vX, 0x{high16:04X} ✅"
    else:
        result += "Note:     Cannot use const/high16 ❌ (low 16 bits not zero)"
    
    return result

def hex32_to_float(hex32):
    """Convert a full 32-bit float hex to decimal float."""
    float_val = struct.unpack('>f', hex32.to_bytes(4, byteorder='big'))[0]
    return f"""
[HEX32 → FLOAT]
Full Hex: 0x{hex32:08X}
Float:    {float_val}f
"""

def auto_detect_hex(hex_str):
    """Auto-detect if it's high16 or full 32-bit float hex."""
    try:
        hex_val = int(hex_str, 16)
        if hex_val <= 0xFFFF:
            return high16_to_float(hex_val)
        elif hex_val <= 0xFFFFFFFF:
            return hex32_to_float(hex_val)
        else:
            return "[ERROR] Value exceeds 32-bit range."
    except ValueError:
        return "[ERROR] Invalid hex input. Must be valid hexadecimal."

def main():
    print("=== Dalvik Float ↔ Hex ↔ const/high16 Converter ===")
    print("Choose operation:")
    print("1 - Convert Float to Hex + const/high16")
    print("2 - Convert Hex (auto-detect 16/32 bit) to Float")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        val = input("Enter float value (e.g., 30.0, 999999.9, 250.0f, 1.25F): ").strip().lower().rstrip('f')
        try:
            f = float(val)
            print(float_to_hex_and_high16(f))
        except ValueError:
            print("[ERROR] Invalid float input.")

    elif choice == "2":
        val = input("Enter hex value (e.g., 0x4120, 41F00000): ").strip().lower()
        val = val[2:] if val.startswith("0x") else val
        print(auto_detect_hex(val))

    else:
        print("[ERROR] Invalid option. Choose 1 or 2.")

if __name__ == "__main__":
    main()
