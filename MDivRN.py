from MSumRN import SumRN

class DivRN(SumRN):
    """
    Класс деления рациональных чисел m1/n1 / m2/n2
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
    
    def getDivRN(self):
        """
        Метод деления рациональных чисел m1/n1 / m2/n2
        m - числитель, n- знаменатель
        Возвращения математической операции в формате Integer[m3,n3]
        """

        self.outM = self.mX*self.nY
        self.outN = self.nX*self.mY

        return self.outM, self.outN