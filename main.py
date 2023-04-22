result = []
work_n = []
class Calculus:

    def simple_addition_derivatives(self):
        
        pre_derivative = input("write your function here   ")
        pre_derivative = pre_derivative.split(" + ")

        

        for i in range(len(pre_derivative)):
            s = pre_derivative[i]
            s = s.split("^")
            # print(s)
            work_n.append(s)
            
            # print("/n/n/n/n/n/\n\n\n\n\n\n\n\n\n\n")
            # print(work_n)

        

        for n in range(len(work_n)):
            work_n[n]
            
            y = f"{int(work_n[n][1])}{work_n[n][0]}^{int(work_n[n][1])-1}"
            
            
            
            result.append(y)

        # print(result)
            
            
        '''
        code is working

        '''
        print("\n\n\n\n\n\n\n\n\n\n")
        print(*result, sep = ' + ') 


c = Calculus()
c.simple_addition_derivatives()


# code runs :)