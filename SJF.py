print("SJF SCHEDULLING")
n = int(input("Enter number of processes : "))
processes = dict()

for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process" + str(i + 1) + ": "))
    b = int(input("Enter burst time of process" + str(i + 1) + ": "))
    listOfProcesses = []
    listOfProcesses.append(a)
    listOfProcesses.append(b)
    processes[key] = listOfProcesses

processes = sorted(processes.items(), key=lambda item: item[1][0])



presentTime = 0
processesSjf = []
temp = []

while len(processesSjf) != n:
    for j in range(len(processes)):
        if processes[j][1][0] <= presentTime:
            temp.append(processes[j])

    if temp != []:
        temp = [min(temp, key=lambda item: item[1][1])]        
        presentTime += temp[0][1][1]
        processesSjf.append(temp[0])
        processes.remove(temp[0])
        temp.clear()
    else :    
        presentTime += 1    
  


exitTime = []
for i in range(len(processesSjf)):
    # first process
    if (i == 0):
        exitTime.append(processesSjf[i][1][1] + processesSjf[i][1][0])

    # get prevExitTime + newBurstTime
    else:
        exitTime.append(max(exitTime[i - 1], processesSjf[i][1][0]) + processesSjf[i][1][1])

turnAroundTime = []
for i in range(len(processesSjf)):
    turnAroundTime.append(exitTime[i] - processesSjf[i][1][0])

waitingTime = []
for i in range(len(processesSjf)):
    waitingTime.append(turnAroundTime[i] - processesSjf[i][1][1])

startTime = []
for i in range(len(processesSjf)):
    startTime.append(exitTime[i] - processesSjf[i][1][1])    

avgWaitingTime = 0
for item in waitingTime:
    avgWaitingTime += item
avgWaitingTime = avgWaitingTime / n

avgTurnAroundTime = 0
for item in turnAroundTime:
    avgTurnAroundTime += item
avgTurnAroundTime = avgTurnAroundTime / n    

print("Process | Arrival | Burst | Start | Exit | Turn Around | Wait |")
for i in range(n):
    print(" ", processesSjf[i][0], "   |  ", processesSjf[i][1][0], "    |  ", processesSjf[i][1][1], "  |  " , startTime[i], "  |  ", exitTime[i], " |  ", turnAroundTime[i], "        |  ",
          waitingTime[i], "   |  ")

print("Average Waiting Time: ", avgWaitingTime)
print("Average Turn Around Time: ", avgTurnAroundTime)