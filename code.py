# importing various libraries that we will need to solve the problem statement
from random import randint  #randint() returns an integer between specified range
    
# from givem problem statement defined goodness of a schedule as follows:
#Sum(similarities of all pairs within a single time slot in the same market) + C.Sum(distances of all pairs within a single time slot in the parallel market).

def schedule_goodness(input_array,m,T,k,similarity_between_two_types,distace_between_two_types,C):
    similarity=0
    distance =0
    for i in range(m*T):
        for j in range(k-1):
            for x in range(j+1,k):
                similarity+=similarity_between_two_types[input_array[j+k*i]][input_array[x+k*i]]
    
    for a in range(T):
        for j in range(m):
            for i in range(a*m*k+k*j,a*m*k+k*(j+1)):
                for x in range(a*m*k+k*(j+1),(a+1)*m*k):
                    distance+=distace_between_two_types[input_array[i]][input_array[x]]    
    return round(similarity+(C*distance),4)
    


# random swap function to compute the random states and swapping the random states    
def random_swap_calculator(input_array,n):

    resultant_array=input_array[:]

    random_number_1 = randint(0,n-1) #randomly choosing a no. between 0 to n-1 where n is the types of shops
    random_number_2 = randint(0,n-1) #randomly choosing a no. between 0 to n-1 where n is the types of shops

    swap_condition_1 = random_number_2 - random_number_1
    swap_condition_2 =  random_number_2 - n +1
    temp_variable_for_swapping = resultant_array[random_number_1]

    if (swap_condition_1!=0):
        
        resultant_array[random_number_1]= resultant_array[random_number_2]
        resultant_array[random_number_2]= temp_variable_for_swapping

    elif (swap_condition_2!=0):
        resultant_array[random_number_1]= resultant_array[random_number_2+1]
        resultant_array[random_number_2+1]  = temp_variable_for_swapping

    else:
        resultant_array[random_number_1]  = resultant_array[random_number_2 - 1] 
        resultant_array[random_number_2 - 1] = temp_variable_for_swapping

    return resultant_array


    
def optimization(input_array,iteration,breaker,goodness_arr,n,m,T,k,similarity_between_two_types,distace_between_two_types,C):
    while(iteration<=(pow(n,2)-n)):
        breaker=breaker + 1
        iteration= iteration+1
        
        for i in range(0,n):
            output_new_array = random_swap_calculator(input_array,n)
            
        schedule_goodness_new=schedule_goodness(output_new_array,m,T,k,similarity_between_two_types,distace_between_two_types,C)
        if schedule_goodness_new>goodness_arr:
            input_array=output_new_array
            goodness_arr = schedule_goodness_new
            iteration=0
        if breaker==1000:
            break
    return input_array



def main():

    # taking inputs
    k = int(input())   #taking the input for k total types of shops opening in one time slot in one market
    m = int(input())   #taking the input for number of parallel markets
    T = int(input())   #taking the input for number of time slots
    C = float(input()) #taking the input for trade-off constant

    n = k*m*T #calculating types of shops in city i.e n

    i1=0
    distace_between_two_types = []  ##taking the input for distance between two  two types/categories: d(t1, t2), such that d is between 0 and 1.
    while(i1<n):
        i1=i1+1
        st = input()
        a1 = [] #creating an empty array
        j=0
        while(j<n):
            a1.append(float(st.split(' ')[j]))
            j = j+1         
        distace_between_two_types.append(a1)

    i2=0 
    similarity_between_two_types = [] ##taking the input for distance between two  two types/categories: s(t1, t2) = 1-d(t1, t2)
    while(i2<n):
        a2 = [] #creating an empty array
        j=0
        while(j<n):
            a2.append(1 - distace_between_two_types[i2][j])
            j = j+1
        i2=i2+1
        similarity_between_two_types.append(a2)

    #initializing an array from value 0 to n for initial state
    initial_array = list(range(0, n))
    i0_=0
    b0_=0
    initial_goodness_arr=schedule_goodness(initial_array,m,T,k,similarity_between_two_types,distace_between_two_types,C)
    output_state=optimization(initial_array,i0_,b0_,initial_goodness_arr,n,m,T,k,similarity_between_two_types,distace_between_two_types,C)

    # printing the final output in required format
    for i in range(m):
        for j in range(T):
            for x in range(k):
                print((output_state[x+i*k+m*k*j] + 1), end = " ")
            if j!= T-1:
                print("|", end = " ")
        print(" ")

if __name__ == "__main__":
    main()