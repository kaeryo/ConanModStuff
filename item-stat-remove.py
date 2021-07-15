import re

tableInput = open("ItemStatModificationTable.txt", "r")
tableOutput = open("itemstatnerf.txt", "w")

tableOutput.write("---,Modifications\n")

for line in tableInput:
    if re.search("\(OperatorID=Add,StatID=(14|15|16|17|18|19|20|21)", line):
        newLine = re.sub("(,|)\(OperatorID=Add,StatID=(14|15|16|17|18|19|20|21),ModificationValue=(-|)([0-9]|[0-9][0-9]|[0-9][0-9][0-9]).000000\)(,|)","(OperatorID=Add,StatID=14,ModificationValue=0.000000)",line)
        tableOutput.write(newLine)

tableInput.close()
tableOutput.close()