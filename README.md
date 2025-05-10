# Dalvik Converter 
This is a Python converter for Dalvik Float Equations

###### Supports All of the Following:
1. Float to Hex + const/high16 (if valid)
2. Accepts inputs like 250.0, 999999.9, 30.0f, 1.25F, etc.
3. Hex (auto-detect 16-bit high16 or 32-bit full IEEE float) to Float (Accepts inputs like 0x4120, 41F00000, or even just 4120)
4. Clean Output, Auto Formatting, and Error Handling

#### Example Inputs and Outputs

```
[FLOAT → HEX]
Float:    250.0f
Hex:      0x43780000
Dalvik:   const/high16 vX, 0x4378 ✅

[FLOAT → HEX]
Float:    999999.9f
Hex:      0x497424CC
Note:     Cannot use const/high16 ❌ (low 16 bits not zero)

[HIGH16 → FLOAT]
High16:   0x41F0
Full Hex: 0x41F00000
Float:    30.0f

[HEX32 → FLOAT]
Full Hex: 0x497424CC
Float:    999999.875f

```
