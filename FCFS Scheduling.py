def find_TAT(process,n,bt,wt,tat):       #turn around time finding
    for i in range (n):
        tat[i] = bt[i] + wt[i]

def find_WT(process,n,bt,wt):        #waiting time finding
    wt[0] = 0
    for i in range (1,n):
        wt[i] = bt[i-1]+ wt[i-1]

##########################################################
process = [1,2,3,4,5]              # process input given by pelob sir.
n = len(process)
burst_time = [4,3,1,2,5]
arrival_time = 0                        #arrival time is 0 for all process.

wt = [0] * n
tat = [0] * n
total_wt = 0
total_tat = 0

find_WT(process,n,burst_time,wt)
find_TAT(process,n,burst_time,wt,tat)

print("Process\t|\t"+"Arrival_T\t|\t"+"B_T\t|\t"+"W_T\t|\t"+"T_A_T")
for i in range (n):
    print("\t" + str(i+1) + "\t\t\t" +str(arrival_time)+ "\t\t\t"
          + str(burst_time[i]) + "\t\t"+ str(wt[i]) + "\t\t"+ str(tat[i]))

