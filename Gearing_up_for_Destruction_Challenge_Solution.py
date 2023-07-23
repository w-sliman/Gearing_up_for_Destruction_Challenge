def solution(pegs):
    number_of_pegs=len(pegs)
    #double checking that the number of pigs is valid
    if (number_of_pegs<=1): return [-1,-1]

    #Building our equation to find the radius of the first gear
    b=3 if (number_of_pegs%2==0) else 1
    
    x=0
    for i in range(1,number_of_pegs-1):
        sign= -1 if (i%2==0) else +1
        x= x+pegs[i]*sign
    
    sign= +1 if (number_of_pegs%2==0) else -1
    a= 2*(-pegs[0]+2*x+pegs[number_of_pegs-1]*sign) 

    #here we have are as a fraction (not necessarily in the simplist form)
    r=a/b

    #Excluding the case that would make the radius of last gear less than 1,
    #Which is when the radius of the first gear is less than 2
    if(r<2): return [-1,-1]

    #Checking other gears' radius to make sure non is less than 1
    for i in range (1,number_of_pegs-1):
        r_i=pegs[i]-pegs[i-1]-r

        if r_i<1:
            return [-1,-1]
        else:
            r=r_i

    #Simplifying the fraction r=a/b to it's simplist form (when b=3)
    if b==3 and a%3==0:
        a=int(a/3)
        b=1

    return [a,b]


test=solution([1,14,24,27])
print(test)