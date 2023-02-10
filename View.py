
from Logger import Logger
from MValueInt import ValueInt
from MValueStr import ValueStr
from MValueShow import ValueShow
from MInputRN import InputRN
from MOtputRN import OutputRN


class View:
    
    def __init__(self):
        pass
    
    log=Logger

#-------------------------- Ввод данных ----------------
    
    def getValueInt(self,text):
        """
        Ввод чисел в формате int  с проверкой на правильность ввода
        """
        integ=ValueInt()
        return integ.checkNumberInt(text)

    def getValueIntMinMax(self,text):
        """
        Ввод чисел в формате int  с проверкой на правильность ввода
        и в диапазоне от MIN до МАЧ
        """
        integ=ValueInt()
        return integ.checkNumberMinMax(text)

    
    def getValueStr(self,text):
        """
        Ввод данных в формате String
        """
        string = ValueStr()
        return string.inputString(text)
    
    def getValueRN(text):
        """
        Ввод рациональных чисел в формате a m/n, m/n, a
        где a - целое число, m - числитель, n- знаменатель.
        Вывод int m, int n
        """
        
        string = ValueStr()
        rn = InputRN()
        rn.setRN(string.inputString(text))
        m,n = rn.getRN()
        return m,n 

#------------- Вывод данных --------------------

    def showNumber(self,text,number):
        """
        Ввод данных в формате String
        """
        show = ValueShow()
        show.showNumber(text,number)
        self.log.log_data(f"{text} {number}")

    
    

    def showRN( text, mNR:int, nNR:int):
        """
        Вывод рациональных чисел в формате a m/n
        где a - целое число, m - числитель, n- знаменатель.
        """
        
        showRN = OutputRN()
        showRN.setRN(mNR,nNR)
        tempRN = showRN.getRN()

        print(f"{text} {tempRN}")
        log=Logger
        log.log_data(f"{text} {tempRN}")

#---------------------- Работа с интерфейсом консоли в программе -------

    def getMenu():
        """
        Вывод текста меню
        """

        print("\n \t\t\t=====================================")
        print("\t\t\tМатематические операции с натуральными числами")
        print("\t\t\t1 - Сложение 2-х чисел")
        print("\t\t\t2 - Разность 2-х чисел")
        print("\t\t\t3 - Произведение 2-х чисел")
        print("\t\t\t4 - Деление первого числа на второе чисел")
        print("\t\t\t0 - exit")
        
        integ=ValueInt()
                
        text = "Выберите математическую операцию путём ввода числа от 0 до 4: "
        return integ.checkNumberInt(text)

