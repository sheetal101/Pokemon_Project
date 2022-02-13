power_list=list(map(int,input("enter the list elements: ").rstrip().split())) # please enter next element in same row after one space
max_power=max(power_list)
a=[]
min_power=0
check_lenght=0
c=0
while True:
    if check_lenght==0:
        a.append(max_power)
        min_power=min(power_list)
        print(min_power, min_power) 
        check_lenght+=1
    else:
        power=max_power-c  
        if power in power_list:
            a.append(power)
            check_lenght+=1
        c+=1
        if check_lenght==len(power_list):
            a.sort()
            i=1
            while i<len(a):
                print(min_power, a[i])
                i+=1
            break










