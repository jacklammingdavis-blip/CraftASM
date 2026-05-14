import os

OPCODES = {
    "ADD": "0000", "SUB": "0001", "XOR": "0010", "XNOR": "0011",
    "OR":  "0100", "AND": "0101", "NOR": "0110", "NAND": "0111",
    "LDI": "1000", "HLT":  "1001"
}

REGISTERS = {f"R{i}": format(i, "04b") for i in range(1, 16)}

def assemble():
    print("=" * 60)
    print(" Reading code from file: 'ASM.txt'")
    print("=" * 60)
    try:
        with open("ASM.txt", "r") as f:
            lines = f.readlines()
        
        output = []
        for line in lines:
            tokens = line.strip().upper().split()
            if not tokens: continue
            
            if tokens[0] == "LDI" and len(tokens) == 3:
                cmd, reg, num = tokens[0], tokens[1], tokens[2]
                if reg in REGISTERS:
                    output.append(f"{OPCODES[cmd]} {REGISTERS[reg]} {format(int(num), '08b')}")
            elif tokens[0] in OPCODES and len(tokens) == 3:
                cmd, r1, r2 = tokens[0], tokens[1], tokens[2]
                if r1 in REGISTERS and r2 in REGISTERS:
                    output.append(f"{OPCODES[cmd]} {REGISTERS[r1]} {REGISTERS[r2]}0000")
            elif tokens[0] in OPCODES and len(tokens) == 2:
                cmd, r1 = tokens[0], tokens[1]
                if r1 in REGISTERS:
                    output.append(f"{OPCODES[cmd]} {REGISTERS[r1]} 00000000")
                    
        print("\n" + "=" * 60)
        print("[Output] Success! Your binary code is ready:")
        print("=" * 60)
        for line in output:
            print(line)
        print("=" * 60)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    assemble()
