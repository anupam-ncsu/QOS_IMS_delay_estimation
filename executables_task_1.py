import random
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math
import decimal

############################command line
print "You are now executing the IMS simulation on Python2.7(Version: Python Anaconda)"
print "Author: ANUPAM MAHAPATRA"
print "Student ID: 200062145"
print "NORTH CAROLINA STATE UNIERSITY-Batch of 2016"
print "This simulation requires you to enter the location of input.txt and output.txt files"

ask_input_loc = raw_input ("Please enter the file location for input (ie: E:\\input.txt)")
ask_output_loc = raw_input("Please enter the file location for input (ie: E:\\output.txt)")

plotting=[]

####################### READING USER INPUT
file = open(ask_input_loc,"r")
inp=[]
for line in file:
    x=line.split(",")
    inp= inp+ [float(x[1])]
file.close()
####################### DATA INITIALIZATION  

mc=0
in_time = 0.05
p_time = 999999999
s_time = 999999999
a_time = 999999999
pp_time = 999999999
ss_time = 999999999
aa_time = 999999999

##################### DECLARATION
p_queue_time=[]
p_queue_flag=[]
s_queue_time=[]
s_queue_flag=[]
a_queue_time=[]
a_queue_flag=[]
o_queue_time=[]
o_queue_flag=[]

##################### CUSTOMER_BASE
customer_flag=[]
customer_time=[]
incoming_flag = range(50000)
for x in incoming_flag:
    customer_flag.append(False)

random.seed(50)
a=random.random()
lamda=1/inp[0]
miup = inp[1]
mius = inp[2]
miua = inp[3]
tobreak = inp[4]
batc = inp[5]

print "CODE EXECUTION HAS STARTED"

while 1 :
    time_arr=[1000000000,in_time,p_time,s_time,a_time]
    #print time_arr
    #print time_arr
    mc = min(time_arr)

###############################################ARRIVAL TIME OF CUSTOMER AT P    
    if mc == time_arr[1]:
        customer_time = customer_time +[mc]
        time = mc
        flag = False
        if p_time == 999999999:
            p_queue_time= p_queue_time + [time]
            p_queue_flag= p_queue_flag + [flag]
            pp_time = mc + (round((decimal.Decimal(-(miup)*(math.log(random.random())))),2))
            p_time = (round((decimal.Decimal(pp_time)),2))
            
            #print p_time
        else:
            p_queue_time= p_queue_time + [time]
            p_queue_flag= p_queue_flag + [flag]
                              
        inn_time = in_time + (round((decimal.Decimal(-(lamda)*(math.log(random.random())))),2))
        in_time = (round((decimal.Decimal(inn_time)),2))
        
        #print in_time
        
############################################### DEPARTURE TIME OF CUSTOMER FROM P        
    elif mc == time_arr[2]:
        time_2 = p_queue_time.pop(0)
        flag_2 = p_queue_flag.pop(0)
        #print flag_2
        if flag_2 == False:
            if s_time == 999999999:
                s_queue_time = s_queue_time + [time_2]
                s_queue_flag = s_queue_flag + [flag_2]
                ss_time = mc + (round((decimal.Decimal(-(mius)*(math.log(random.random())))),2))
                s_time = (round((decimal.Decimal(ss_time)),2))
                
                #print s_time
            else:
                s_queue_time = s_queue_time + [time_2]
                s_queue_flag = s_queue_flag + [flag_2]   
        else:
            o_queue_time = o_queue_time + [mc]
            o_queue_flag = o_queue_flag + [flag_2]
            
        if not p_queue_flag:
            p_time = 999999999
        else:
            pp_time = mc + (round((decimal.Decimal(-(miup)*(math.log(random.random())))),2))
            p_time = (round((decimal.Decimal(pp_time)),2))
            
            
############################################### DEPARTURE TIME OF CUSTOMER FROM S        
    elif mc == time_arr[3]:
        time_3 = s_queue_time.pop(0)
        flag_3 = s_queue_flag.pop(0)
        if flag_3==False:
            if a_time == 999999999:
                a_queue_time = a_queue_time + [time_3]
                a_queue_flag = a_queue_flag + [flag_3]
                aa_time= mc + (round((decimal.Decimal(-(miua)*(math.log(random.random())))),2))
                a_time= (round((decimal.Decimal(aa_time)),2))
                
            else:
                a_queue_time = a_queue_time + [time_3]
                a_queue_flag = a_queue_flag + [flag_3]   
        else:
            if p_time == 999999999:
                p_queue_time = p_queue_time + [time_3]
                p_queue_flag = p_queue_flag + [flag_3]
                pp_time = mc + (round((decimal.Decimal(-(miup)*(math.log(random.random())))),2))
                p_time = (round((decimal.Decimal(ss_time)),2))
                
            else:
                p_queue_time = p_queue_time + [time_3]
                p_queue_flag = p_queue_flag + [flag_3]
                
        if not s_queue_flag:
            s_time = 999999999
        else:
            ss_time = mc + (round((decimal.Decimal(-(mius)*(math.log(random.random())))),2))
            s_time = (round((decimal.Decimal(ss_time)),2))
             
             
        del time_3,flag_3
############################################### DEPARTURE TIME OF CUSTOMER FROM A                
    else:
        time_4 = a_queue_time.pop(0)
        flag_4 = a_queue_flag.pop(0)
        if s_time == 999999999:
            s_queue_time = s_queue_time + [time_4]
            s_queue_flag = s_queue_flag + [True]
            ss_time = mc + (round((decimal.Decimal(-(mius)*(math.log(random.random())))),2))
            s_time = (round((decimal.Decimal(ss_time)),2))
            
        else:
            s_queue_time = s_queue_time + [time_4]
            s_queue_flag = s_queue_flag + [True]
            
        if not a_queue_flag:
            a_time = 999999999
        else:
            aa_time = mc + (round((decimal.Decimal(-(miua)*(math.log(random.random())))),2))
            a_time =(round((decimal.Decimal(aa_time)),2))
            
             
        del time_4, flag_4
##########               
    if len(o_queue_time) == tobreak:
        break
########################################### parameters calculation   
 
print "CODE EXECUTION COMPLETE"

out= [x1 - x2 for (x1, x2) in zip(o_queue_time,customer_time )]

endtoend = [j/1.00  for j in out]
#print"end to end arrival time for the required number of customers are:"
#print endtoend

m = np.mean(endtoend) 
print "Mean of end-to-end delay without using batch means:" ,m

per1 =  np.percentile(endtoend,95)
print "95th percentile without using batch means:" ,per1

#DISTRIBUTED CALCULATION
c2=endtoend[100:]
#print "total number of elements for which calculation is done :",len(c2)

endtoend2=[]
leng = int(tobreak-100)
divid = int(math.floor(leng/batc))

for x in range(0,len(c2),divid):
    a= c2[x:x+divid]
    endtoend2 = endtoend2 + [a]
#endtoend2 is the list of 300group elements

q=[]
for x in endtoend2:
    per2 = (np.percentile(x,95))
    q = q + [per2]

r= np.mean(q)
print "Mean of end-to-end delay using batch means" ,r

per2 =  np.percentile(q,95)
print "95th percentile using batch means" ,per2

s= np.std(q)
print "Standard deviation of the percentiles" , s  

n=math.sqrt(divid)
mn=1.96*(s/n)
x1=r-mn
x2=r+mn
x3=[x1,x2]
print "My confidence interval using batch means" ,x3

########################### WRITING TO OUTPUT FILE
with open(ask_output_loc,"w+") as out_file:
    out_file.write("IMS simulation results")
    out_file.write('\n')
    out_file.write("-----------------------------------")
    out_file.write("\n")    
    out_file.write("Mean of end-to-end delay without using batch means :")
    out_file.write(' ')
    out_file.write(str(m))
    out_file.write('\n')
    out_file.write("95th percentile without using batch means :" )
    out_file.write(' ')
    out_file.write(str(per1))
    out_file.write('\n')
    out_file.write("Mean of end-to-end delay using batch means :")
    out_file.write(' ')
    out_file.write(str(r))
    out_file.write('\n')
    out_file.write("95th percentile using batch means :")
    out_file.write(' ')
    out_file.write(str(per2))
    out_file.write('\n')
    out_file.write("Standard deviation of the percentiles")
    out_file.write(' ')
    out_file.write(str(s))
    out_file.write('\n')
    out_file.write("My confidence interval using batch means :")
    out_file.write(' ')
    out_file.write(str(x3))
    
out_file.close()    
#######################################GRAPH PLOT ALGORITHM
"""out.sort()
plt.plot(out)
plt.xlabel("CUSTOMER PROCESSED AT OUTPUT QUEUE")
plt.ylabel('OUT TIME FOR PROCESSED CUSTOMER')
plt.show()"""
#####################
raw_input("press <ENTER> to exit the simulation")
