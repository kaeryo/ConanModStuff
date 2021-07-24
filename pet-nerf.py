import re

tableInput = open("ThrallDataTable.txt", "r")
tableOutput = open("petout.txt", "w")

tableOutput.write("---,ThrallActor,ThrallComponent,BehaviorTree,NPCBehaviorParameters,Diet\n")

for line in tableInput:
    if re.search("Blueprints", line):
        newLine = re.sub("\/Game\/Characters\/NPCs\/.*\/Blueprints\/","/Game/Mods/gt3/nerfs/pet-ai/gt3_",line) #Edit this to suit mod file structure
        newerLine = re.sub("\.BP_NPC_",".gt3_BP_NPC_",newLine)
        tableOutput.write(newerLine)

tableInput.close()
tableOutput.close()