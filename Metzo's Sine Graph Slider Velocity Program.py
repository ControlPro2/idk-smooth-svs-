#ive never made a program before so this is probs riddled with mistakes
#make sure to not be stupid when inputting values - make sure it makes sense and isnt impossible

input = input("Press 1 for Slow to Fast Slowdown/Uprise. Press 2 for Fast to Slow Slowdown/Uprise.")
if input == "1":
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

if input =="2":
    StartSV = float(input("what's the starting sv: "))
    EndSV = float(input("what's the ending sv: "))
    NoteAmount = float(input("how many notes are there: "))
    NoteAmount = NoteAmount - 1
    SVRange = EndSV - StartSV
    SV = 1000
    x = 1
    print(x, StartSV)
    while x != NoteAmount + 1:
        SV = SVRange * math.sin(0.5 * math.pi * (x / NoteAmount) + math.pi / 2) + EndSV
        x = x + 1
        print(x, SV)
