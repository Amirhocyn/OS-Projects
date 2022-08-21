print("FCFS SCHEDULLING")
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


exitTime = []
for i in range(len(processes)):
    # first process
    if (i == 0):
        exitTime.append(processes[i][1][1] + processes[i][1][0])

    # get prevExitTime + newBurstTime
    else:
        exitTime.append(max(exitTime[i - 1], processes[i][1][0]) + processes[i][1][1])

turnAroundTime = []
for i in range(len(processes)):
    turnAroundTime.append(exitTime[i] - processes[i][1][0])

waitingTime = []
for i in range(len(processes)):
    waitingTime.append(turnAroundTime[i] - processes[i][1][1])

startTime = []
for i in range(len(processes)):
    startTime.append(exitTime[i] - processes[i][1][1])    

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
    print(" ", processes[i][0], "   |  ", processes[i][1][0], "    |  ", processes[i][1][1], "  |  " , startTime[i], "  |  ", exitTime[i], " |  ", turnAroundTime[i], "        |  ",
          waitingTime[i], "   |  ")

print("Average Waiting Time: ", avgWaitingTime)
print("Average Turn Around Time: ", avgTurnAroundTime)