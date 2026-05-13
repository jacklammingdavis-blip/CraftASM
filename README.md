# CraftASM
A lightweight assembler that compiles custom assembly language into Minecraft-compatible binary structures and Redstone ROM formats.

CraftASM User ManualCraftASM is a lightweight, scriptable assembler designed specifically for computational Redstone engineers. It maps human-readable assembly instructions onto custom instruction set architectures (ISAs) for in-game Minecraft CPUs.Quick Start GuideStep 1: Initialize the ScriptSave the Python compiler source code into a file named Assemble.py.Step 2: Create the Source FileIn the exact same directory, create a raw text file named ASM.txt.Step 3: Write Your Code Open ASM.txt in a text editor and enter your assembly logic.Example

LID R1 1
LID R2 2
ADD R1 R2 R3

Use code with caution.Step 4: Run the CompilationOpen your system terminal or command prompt, navigate to your project directory, and execute:bashpython Assemble.py
Use code with caution.Customizing Your Hardware DefinitionYou can adapt CraftASM to fit any custom hardware project by editing the structural dictionaries directly inside Assemble.py:python# Change these values to match your custom ALU or control unit layout

OPCODES = {
    "ADD": "0000", "SUB": "0001", "XOR": "0010", "XNOR": "0011",
    "OR":  "0100", "AND": "0101", "NOR": "0110", "NAND": "0111",
    "LDI": "1000"
}

Use code with caution.Architectural Layout and Syntax RulesCraftASM targets a 16-bit instruction format supporting 15 unique registers (R1 through R15). The assembler parses instructions based on three strict structural layouts:1. Data Initialization Format (LDI)Loads an 8-bit immediate integer directly into a specified destination register.Syntax: LDI [Register] [ImmediateValue]Example: LDI R1 5Binary Structure: [4-bit Opcode] [4-bit Register] [8-bit Immediate Value]2. Dual Register Format (ALU Operations)Executes math or logic functions using data from two separate registers. The result updates the destination register.Syntax: [OPCODE] [DestinationRegister] [SourceRegister]Example: ADD R3 R2Binary Structure: [4-bit Opcode] [4-bit Dest Register] [4-bit Src Register] [4-bit Zero Padding]3. Single Register FormatRuns instructions that require only a target register. The remaining instruction space is padded out with zeros.Syntax: [OPCODE] [TargetRegister]Example: SUB R1Binary Structure: [4-bit Opcode] [4-bit Target Register] [8-bit Zero Padding]
