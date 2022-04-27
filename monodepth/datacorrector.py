import os


listLines = []
with open('utils/filenames/csDataSetFinal1.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        sentences = l.split()
        if sentences[0].find("left")!=-1:
            listLines.append([sentences[0],sentences[1]])
            # listLines.append(sentences[0])
        else:
            listLines.append([sentences[1],sentences[0]])
            # listLines.append(sentences[1])

print(len(listLines))
with open('utils/filenames/csDataSetFinal4.txt','w') as f1:
    for i in range(0, 5000):
        f1.write(listLines[i][0] + " " + listLines[i][1])
        f1.write("\n")