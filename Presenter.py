from os import system

from CalcRN import CalcRN
from View import View
#from Presenter import Presenter
from Logger import Logger


class Presenter():

    mX = 0 # Числитель Х
    nX = 0 # Знаменатель Х

    mY = 0 # Числитель Y
    nY = 0 # Знаменатель Y
    calc = CalcRN()
    
    log = Logger

    def __init__(self,c:CalcRN,v:View):
        self.c=c
        self.v=v
        

    def buttonClic(self):
        textO = " ----------- "
        self.log.log_data(textO+"Старт программы калькулятор"+textO)
        while(True):
            selCalc= self.v.getMenu()
            if(selCalc==1):
                system ('cls')
                text = "Выбрана операция сложения рациональных чисел\n"
                self.log.log_data(text)
                print(text)
                print("Рациональные числа вводятся в формате a m/n, m/n, a.")
                print("Где a - целое число, m - числитель, n- знаменатель.")
                mX,nX =self.v.getValueRN("Введите 1-е число: ")
                mY,nY =self.v.getValueRN("Введите 2-е число: ")
                m,n = self.calc.getSum(mX,nX,mY,nY)
                system ('cls')
                self.v.showRN("Ответ = ", m,n)
            elif(selCalc==2):
                system ('cls')
                text = "Выбрана операция разности рациональных чисел\n"
                self.log.log_data(text)
                print(text)
                print("Рациональные числа вводятся в формате a m/n, m/n, a.")
                print("Где a - целое число, m - числитель, n- знаменатель.")
                mX,nX =self.v.getValueRN("Введите 1-е число: ")
                mY,nY =self.v.getValueRN("Введите 2-е число: ")
                m,n = self.calc.getSub(mX,nX,mY,nY)
                system ('cls')
                self.v.showRN("Ответ = ", m,n)
            elif(selCalc==3):
                system ('cls')
                text = "Выбрана операция произведения рациональных чисел\n"
                self.log.log_data(text)
                print(text)
                print("Рациональные числа вводятся в формате a m/n, m/n, a.")
                print("Где a - целое число, m - числитель, n- знаменатель.")
                mX,nX =self.v.getValueRN("Введите 1-е число: ")
                mY,nY =self.v.getValueRN("Введите 2-е число: ")
                m,n = self.calc.getMul(mX,nX,mY,nY)
                system ('cls')
                self.v.showRN("Ответ = ", m,n)
            elif(selCalc==4):
                system ('cls')
                text = "Выбрана операция деления рациональных чисел"
                self.log.log_data(text)
                print(text)
                print("Рациональные числа вводятся в формате a m/n, m/n, a.")
                print("Где a - целое число, m - числитель, n- знаменатель.")
                mX,nX =self.v.getValueRN("Введите 1-е число: ")
                mY,nY =self.v.getValueRN("Введите 2-е число: ")
                m,n = self.calc.getDiv(mX,nX,mY,nY)
                system ('cls')
                self.v.showRN("Ответ = ", m,n)
            elif(selCalc==0):
                system ('cls')
                text = "Выход из программы калькулятор"
                self.log.log_data(textO+text+textO+"\n\n")
                print(text)
                return
            else:
                system ('cls')
                text = "Введена цифра, которой не присвоена операция"
                self.log.log_data(text)
                continue