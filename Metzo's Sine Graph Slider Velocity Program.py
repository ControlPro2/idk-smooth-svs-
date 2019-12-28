#ive never made a program before so this is probs riddled with mistakes
#THIS IS ONLY FOR MAKING A SLOW TO FAST SLOWDOWN OR SLOW TO FAST UPRISE

import math
StartSV = float(input("what's the starting sv: "))
EndSV = float(input("what's the ending sv: "))
NoteAmount = float(input("how many notes are there: "))
NoteAmount = NoteAmount - 1
SVRange = StartSV - EndSV
SV = 1000
x = 1
print(x, StartSV)
while x != NoteAmount + 1:
    SV = SVRange * math.sin(0.5 * math.pi * (x / NoteAmount) + math.pi / 2) + EndSV
    x = x + 1
    print(x, SV)