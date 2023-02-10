

class OutputRN():
    """
    Вывод рациональных чисел в консоль
    """
    @staticmethod
    def PrimeNumbers(numberM):
        """
        Нахождение простых чисел решетом Эратосфена
        numberM - число, до которого будут находиться простые числа
        """
        
        arrayList = []

        for n in range(2,numberM+1): # Заполнение массива цифрами от 2 до number
            arrayList.append(n)
        
        for  data in arrayList: # Нахождение простых чисел решетом Эратосфена
            i=arrayList.index(data)
            if(data!=0):
                for  data1 in arrayList[i+1:]:
                    i1 = arrayList.index(data1)
                    
                    if(data1!=0 and data1%data==0):
                        arrayList[i1]=0
        newArrayList =[]

        for data in arrayList:
            if(arrayList[arrayList.index(data)]!=0):
                newArrayList.append(arrayList[arrayList.index(data)])
                    
        return newArrayList
        
    @staticmethod
    def Reduction(mRN,nRN):
        """
        Метод  сокращение числителя и знаменателя дроби
        mRN - числитель
        nRN - знаменатель
        """
        ot = OutputRN()
        arrList = ot.PrimeNumbers(nRN)

        for data in arrList:
            if(nRN>=data):
                if(mRN%data==0 and nRN%data==0):
                    while(True):
                        d1= mRN
                        mRN=d1/data
                        d2 = nRN
                        nRN=d2/data
                        if(mRN%data!=0 or nRN%data!=0):
                            break
                      
            else: break

        return int(mRN), int (nRN)
    
    m = 0
    n = 0

    
    def setRN(self, m:int,n:int):
        """
        Метод ввода рациональных чисел в формате int m, int n
        m - числитель, n- знаменатель.
        """
        self.m=m
        self.n=n

    def getRN(self):
        """
        Метод вывода рационального числа
        Вывод осуществляется в формате String: a m/n, m/n, a.
        Где a - целое число, m - числитель, n- знаменатель
        """
        outRn =""
        a = 0
        mNew = self.m
        nNew = self.n
        ot = OutputRN()

        if (mNew==0 or  nNew==0):
            outRn= "0"
        elif ( nNew==1): outRn = str(mNew)
        elif (mNew%nNew==0): outRn = str(int(mNew/nNew))
        else:
            a = int((mNew-mNew%nNew)/nNew)
            mNew = int(mNew%nNew)
            mNew,nNew = ot.Reduction(mNew,nNew)
            if (a!=0):
                outRn = str(a)+" "+str(mNew)+"/"+str(nNew)
            else: outRn = str(mNew)+"/"+str(nNew)
        return outRn

