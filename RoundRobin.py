import copy
print("RoundRobin SCHEDULLING")
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

treshHold = int(input("Enter Treshhold time:  "))
processes = sorted(processes.items(), key=lambda item: item[1][0])


presentTime = 0
processesRR = []
newArrival = 0

for x in range(len(processes)):
    processes[x] = list(processes[x])
    processes[x][1][0] = int(processes[x][1][0])
    processes[x][1][1] = int(processes[x][1][1])

while len(processes) > 0:
    if processes[0][1][0] <= presentTime:       
        presentTime += processes[0][1][1]
        processesRR.append(copy.deepcopy(processes[0]))
        if processes[0][1][1] - treshHold > 0:
            
            newArrival = 0
            for x in range(len(processesRR)):
                newArrival += min(treshHold, processesRR[x][1][1])  
            
            processes[0][1][0] = newArrival
            processes[0][1][1] = processes[0][1][1] - treshHold 


            processes.append(processes[0])     
            processes.pop(0)
        else:
            processes.pop(0)       
    else :    
        presentTime += 1         
 

exitTime = []
for i in range(len(processesRR)):
    # first process
    if (i == 0):
        exitTime.append(min(treshHold, processesRR[i][1][1]) + processesRR[i][1][0])

    # get prevExitTime + newBurstTime
    else:
        exitTime.append(max(exitTime[i - 1], processesRR[i][1][0]) + min(treshHold, processesRR[i][1][1]))

turnAroundTime = []
for i in range(len(processesRR)):
    turnAroundTime.append(exitTime[i] - processesRR[i][1][0])

waitingTime = []
for i in range(len(processesRR)):
    waitingTime.append(turnAroundTime[i] -  min(treshHold,  processesRR[i][1][1]))

startTime = []
for i in range(len(processesRR)):
    startTime.append(exitTime[i] -  min(treshHold,  processesRR[i][1][1]))    

avgWaitingTime = 0
for item in waitingTime:
    avgWaitingTime += item
avgWaitingTime = avgWaitingTime / len(processesRR)

avgTurnAroundTime = 0
for item in turnAroundTime:
    avgTurnAroundTime += item
avgTurnAroundTime = avgTurnAroundTime / len(processesRR)    

print("Process | Arrival | BurstTimeRemain | Start | Exit | Turn Around | Wait   |")
for i in range(len(processesRR)):
    print(" ", processesRR[i][0], "   |  ", processesRR[i][1][0], "    |     ", max(processesRR[i][1][1] - treshHold, 0), "         |  " , startTime[i], "  |  ", exitTime[i], " |  ", turnAroundTime[i], "        |  ",
          waitingTime[i], "   |  ")

print("Average Waiting Time: ", avgWaitingTime)
print("Average Turn Around Time: ", avgTurnAroundTime)