from Logger import Logger

class InputRN:
    """
    Ввод рациональных чисел в формате: a m/n, m/n, a.
    a - целое число, m - числитель, n- знаменатель
    """
    log=Logger
       
    inputStRN = "" # Введённое рациональное в формате стринг
    outIntRNm = -1 # Выведенный числитель
    outIntRNn = -1 # Выведены знаменатель

    def setRN(self, inputStRN):
        """
        Метод ввода рациональных чисел в формате a m/n, m/n, a.
        a - целое число, m - числитель, n- знаменатель
        """
        self.inputStRN = inputStRN
    
    def getRN(self):
        """
        Метод преобразование рациональных чисел из String (формат ввода a, a m/n, m/n) 
        в  int m и int n. Где a - целое число, m - числитель, n- знаменатель.
        """
                
        try:
                
            if ((self.inputStRN.count(" ")==1) and self.inputStRN.count("/")==1):

                newData = self.inputStRN.replace(" ","/")
                self.inputStRN = newData
                tempArr = self.inputStRN.split("/")
                self.outIntRNm = int(tempArr[0])*int(tempArr[2])+int(tempArr[1])
                self.outIntRNn = int(tempArr[2])
                        
            elif ((self.inputStRN.count(" ")!=1) and self.inputStRN.count("/")==1):
                tempArr = self.inputStRN.split("/")
                self.outIntRNm = int(tempArr[0])
                self.outIntRNn = int(tempArr[1])
            else:
                self.outIntRNm = int(self.inputStRN)
                self.outIntRNn = 1               

            return self.outIntRNm, self.outIntRNn
        except ValueError:
            self.log.log_data(f"Рациональное число введено не правильно {self.inputStRN}")
            print("Рациональное число введено не правильно")
            return self.outIntRNm, self.outIntRNn
       