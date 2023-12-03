file = open("ex1-file.txt","r")
endoutput = 0
Lines = file.readlines()
for line in Lines:
    try:
        endResult = ""
        start = 0
        end = len(line) - 1
        i = 0
        while i < end:
            if(line[i].isnumeric()):
                endResult += line[i]
                break
            i += 1
        i = end
        while i >= 0:
            if(line[i].isnumeric()):
                endResult += line[i]
                break
            i -= 1
        endoutput += int(endResult)
    except Exception as e:
        pass
print(endoutput)