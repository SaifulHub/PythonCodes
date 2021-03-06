def findWT(process,n,bt,wt,quantum):
    rem_bt = [0]*n
    for i in range(n):
        rem_bt[i]=bt[i]
    t =0

    while(1):
        done = True
        for i in range(n):
            if(rem_bt[i]> 0):
                done = False
                if (rem_bt[i]>quantum):
                    t = t+quantum
                    rem_bt[i] = rem_bt[i]-quantum
                else:
                    t = t+rem_bt[i]
                    wt[i] = t- bt[i]
                    rem_bt[i]=0
        if (done ==True):
            break
def findTAT(process,n,bt,wt,tat):
    for i in range(n):
        tat[i]= bt[i]+wt[i]

def findAvgTime(process, n, burst_time, quantum):
    wt=[0]*n
    tat = [0]*n
    findWT(process, n,burst_time, wt, quantum)
    findTAT(process,n,burst_time,wt,tat)
    print("Process\tBurst_Time\tWaiting_Time\tTurnAround Time")
    total_wt = 0
    total_tat = 0
    for i in range (n):
        total_wt= total_wt+wt[i]
        total_tat = total_tat +tat[i]
        print("  ",i+1,"\t\t",burst_time[i],"\t\t\t",wt[i],"\t\t",tat[i]," ")

    print("Total Turn around Time is: ",(total_tat/n))
    print("Total waiting Time is: ",(total_wt/n))


if __name__ == '__main__':
    process = [1, 2, 3]
    n = len(process)
    burst_time = [10, 5, 8]
    quantum = 2
    findAvgTime(process, n, burst_time, quantum)