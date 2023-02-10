
from MSumRN import SumRN

class MulRN(SumRN):
    """
    Класс произведение рациональных чисел m1/n1 * m2/n2
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

    def getMulRN(self):
        """
        Метод произведение рациональных чисел m1/n1 * m2/n2
        m - числитель, n- знаменатель
        Возвращения математической операции в формате Integer[m3,n3]
        """

        self.outM = self.mX*self.mY
        self.outN = self.nX*self.nY

        return self.outM, self.outN