def findWT(process,n,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i] = process[i - 1][1] + wt[i - 1]
def findTAT(process,n,wt,tat):
    for i in range(n):
        tat[i] = process[i][1] + wt[i]

def AverageTime(process, n):
    wt = [0]*n
    tat = [0]*n
    findWT(process,n,wt)
    findTAT(process,n,wt,tat)
    print("\nProcess\tburstTime\twaitingTime\tTurnAroundTime")
    total_tat = 0
    total_wt = 0
    for i in range (n):
        total_wt = total_wt+wt[i]
        total_tat = total_tat + tat[i]
        print(" ",process[i][0],"\t\t", process[i][1],"\t\t",wt[i],"\t\t",tat[i])
    print("Average waiting Time is : ",total_wt/n)
    print("Average Turn around Time is : ",total_tat/n)


def priorityScheduling(process,n):
    print("Given Processes: ")
    for  i in process:
        print(i[0],end=" ")
    AverageTime(process,n)

if __name__ == '__main__':
    process = [[1,10,1],
               [2,5,0],
               [3,8,1]]
    n = 3
    priorityScheduling(process,n)