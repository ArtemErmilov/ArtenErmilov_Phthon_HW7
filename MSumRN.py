

class SumRN:
    """
    Метод сложения рациональных чисел
    """
    mX = 0 # Числитель Х
    nX = 0 # Знаменатель Х

    mY = 0 # Числитель Y
    nY = 0 # Знаменатель Y

    outM = 0 # Числитель рационального числа, после совершения математической операции 
    outN = 0 # Знаменатель рационального числа, после совершения математической операции

    def setX(self, mX,nX):
        """
        Ввод первого рационального числа.
        """
        self.mX=mX
        self.nX=nX
    
    def setY(self, mY,nY):
        """
        Ввод второго  рационального числа.
        """
        self.mY=mY
        self.nY=nY
    
    def getSumRN(self):
        """
        Сложение рациональных чисел m1/n1 + m2/n2
        m - числитель, n- знаменатель.
        Возвращения математической операции в формате Integer[m3,n3].
        """
        if( self.nX==self.nY):
            self.outM=self.mX+self.mY
            self.outN=self.nX
        else:
            self.outM=self.mX*self.nY+self.mY*self.nX
            self.outN=self.nX*self.nY
        
        return self.outM, self.outN

