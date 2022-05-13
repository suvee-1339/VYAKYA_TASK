import sys
def list_sum(li):
    di={}
    end=0
    for i in range(len(li)):
        while(end<len(li)):
            key = tuple(li[i:end+1])
            di[key]=sum(li[i:end+1])
            end+=1
        end=0
    end1 = len(li)-1
    for j in range(len(li)):
        start=j
        while(end1>start+1):
            li1=[]
            li1.append(li[start])
            li1.append(li[end1])
            di[tuple(li1)]=sum(li1)
            end1-=1
        end1=len(li)-1

    return di
    
a=[10,11,12,13,14]
b=[2, 3, 19, 99, 101]

# a=[1,2,3,4,5,6]
# b=[9,10,11,12,13,14]

possible_sum_a=list_sum(a)
possible_sum_b=list_sum(b)
possible_sum_b= dict(sorted(possible_sum_b.items()))
possible_sum_a= dict(sorted(possible_sum_a.items()))

# print(possible_sum_a)
# print()
# print(possible_sum_b)



for (b_key,b_val) in possible_sum_b.items() :
        for(a_key,a_val) in possible_sum_a.items():
            if a_val==b_val and a_val :
                print(list(a_key),list(b_key))
                
                
                
print(0)

            
        
            
            


    


    

