print("PRIORITY SCHEDULLING")
n = int(input("Enter number of processes : "))
processes = dict()

for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process" + str(i + 1) + ": "))
    b = int(input("Enter burst time of process" + str(i + 1) + ": "))
    c = int(input("Enter priority of process" + str(i + 1) + ": "))
    listOfProcesses = []
    listOfProcesses.append(a)
    listOfProcesses.append(b)
    listOfProcesses.append(c)
    processes[key] = listOfProcesses

processes = sorted(processes.items(), key=lambda item: item[1][0])



presentTime = 0
processesPriority = []
temp = []

while len(processesPriority) != n:
    for j in range(len(processes)):
        if processes[j][1][0] <= presentTime:
            temp.append(processes[j])

    if temp != []:
        temp = [min(temp, key=lambda item: item[1][2])]        
        presentTime += temp[0][1][1]
        processesPriority.append(temp[0])
        processes.remove(temp[0])
        temp.clear()
    else :    
        presentTime += 1    
  


exitTime = []
for i in range(len(processesPriority)):
    # first process
    if (i == 0):
        exitTime.append(processesPriority[i][1][1] + processesPriority[i][1][0])

    # get prevExitTime + newBurstTime
    else:
        exitTime.append(max(exitTime[i - 1], processesPriority[i][1][0]) + processesPriority[i][1][1])

turnAroundTime = []
for i in range(len(processesPriority)):
    turnAroundTime.append(exitTime[i] - processesPriority[i][1][0])

waitingTime = []
for i in range(len(processesPriority)):
    waitingTime.append(turnAroundTime[i] - processesPriority[i][1][1])

startTime = []
for i in range(len(processesPriority)):
    startTime.append(exitTime[i] - processesPriority[i][1][1])    

avgWaitingTime = 0
for item in waitingTime:
    avgWaitingTime += item
avgWaitingTime = avgWaitingTime / n

avgTurnAroundTime = 0
for item in turnAroundTime:
    avgTurnAroundTime += item
avgTurnAroundTime = avgTurnAroundTime / n    

print("Process | Arrival | Burst | Priority | Start | Exit | Turn Around | Wait |")
for i in range(n):
    print(" ", processesPriority[i][0], "   |  ", processesPriority[i][1][0], "    |  ", processesPriority[i][1][1], "  |  " , processesPriority[i][1][2] , "     |  " , startTime[i], "  |  ",
     exitTime[i], " |  ", turnAroundTime[i], "        |  ", waitingTime[i], "   |  ")

print("Average Waiting Time: ", avgWaitingTime)
print("Average Turn Around Time: ", avgTurnAroundTime)