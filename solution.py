class Plot:
    def __init__(self):
        self.__size=None
        self.__matrix=[]
        
    def set_size(self):
        self.__size=int(input("Enter plot size"))
    
    #matrix user input
    def set_matrix(self):
        for i in range(self.__size):
            self.__matrix.append([])
            for j in range(self.__size):
                self.__matrix[i].append(int(input("Enter row "+str(i)+" column "+str(j)+":")))
    
    def get_size(self):
        return self.__size
    
    def print_matrix(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.__matrix[i][j],end="")
            print()
    
    #find the area of largest rectangle in the histogram.
    def calculate_area(self,temp):
        maxArea = 0
        stacktemp = []
        stackIndex = []
        #use stacks to push the values of histogram 
        for i in range(len(temp)):
            #push if next value is greater than top of stack
            if stacktemp == [] or temp[i] > stacktemp[len(stacktemp)-1]:
                stacktemp.append(temp[i])
                stackIndex.append(i)
            #if next value is lesser, keep popping from stack till lesser value is found or stack is empty
            elif temp[i] < stacktemp[len(stacktemp)-1]:
                lastIndex = 0
                while stacktemp and temp[i] < stacktemp[len(stacktemp)-1]:
                    lastIndex = stackIndex.pop()
                    #find the area of histogram
                    tempArea = stacktemp.pop() * (i-lastIndex)
                    if maxArea < tempArea: maxArea = tempArea
                stacktemp.append(temp[i])
                stackIndex.append(lastIndex)
        while stacktemp:
            tempArea = stacktemp.pop() * (len(temp) - stackIndex.pop())
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea
    
    def find_area(self):
        #copy row 1 of matrix into temp anf flip 0s to 1s and vice versa
        temp=self.__matrix[0]
        for i in range(self.__size):
            if temp[i]==0:
                temp[i]=1
            else:
                temp[i]=0
        area=0
        max_area=self.calculate_area(temp)
        #make histograms for rows in the matrix
        for i in range(1,self.__size):
            for j in range(0,self.__size):
                if self.__matrix[i][j]==0:
                    temp[j]+=1
                else:
                    temp[j]=0
            area=self.calculate_area(temp)
            if area>max_area:
                max_area=area
        print("Largest house that can be built is:"+str(max_area))
                
obj=Plot()
obj.set_size()
obj.set_matrix()
obj.print_matrix()
obj.find_area()