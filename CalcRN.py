

from View import View
from MSumRN import SumRN
from MSubRN import SubRN
from MMulRN import MulRN
from MDivRN import DivRN

class CalcRN():
    """
    Метод математических операций сложения,
    разности, произведения, деления над рациональными числами
    """

    def getSum(self,mX,nX,mY,nY):
        """
        Метод математической операции сложения натуральных чисел mX/nX+mY/nY
        """
        sum = SumRN()
        sum.setX(mX,nX)
        sum.setY(mY,nY)

        return sum.getSumRN()
    
    def getSub(self,mX,nX,mY,nY):
        """
        Метод математической операции разности натуральных чисел mX/nX-mY/nY
        """
        sub = SubRN()
        sub.setX(mX,nX)
        sub.setY(mY,nY)

        return sub.getSubRN()

    def getMul(self,mX,nX,mY,nY):
        """
        Метод математической операции произведения натуральных чисел mX/nX*mY/nY
        """
        mul = MulRN()
        mul.setX(mX,nX)
        mul.setY(mY,nY)

        return mul.getMulRN()
    
    def getDiv(self,mX,nX,mY,nY):
        """
        Метод математической операции деления натуральных чисел mX/nX / mY/nY
        """
        div = DivRN()
        div.setX(mX,nX)
        div.setY(mY,nY)

        return div.getDivRN()