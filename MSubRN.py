
from MSumRN import SumRN

class SubRN(SumRN):
    """
    Разность рациональных чисел m1/n1 - m2/n2
    m - числитель, n- знаменатель
    Возвращения математической операции в формате Integer[m3,n3]
    """
    


    def setX(self, mX, nX):
        """
        Первое рациональное число
        """
        super().setX(mX, nX)
   
    def setY(self, mY, nY):
        """
        Второе рациональное число
        """                
        super().setY(mY, nY)
       
    

    def getSubRN(self):
        """
        Разность рациональных чисел m1/n1 - m2/n2
        m - числитель, n- знаменатель.
        Возвращения математической операции в формате Integer[m3,n3].
        """

        if (self.nX==self.nY):
            self.outM = self.mX-self.mY
            self.outN = self.nX
        else:
            self.outM = self.mX*self.nY-self.mY*self.nX
            self.outN = self.nX*self.nY
        return self.outM, self.outN
       