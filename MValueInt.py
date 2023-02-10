


from Logger import Logger


class ValueInt():
    """
    Ввод данных из консоли в формате Integer
    """
    log=Logger

    def __init__(self):
        pass

    def checkNumberInt (self,text_in:str = 'Введите число: ', text_breach:str = 'Вы ввели число не правильно, введите его заново'): 
        """
        Получение данных из консоли в формате INT
        и проверка, является ли введённые данные числом. 
        Если нет то повторяется запрос заново.
        text_in - текст запроса в консоли
        text_breach - текст вторичного запроса, при неправильном вводе числа
        """
        
        while True:
            
            try:
                num = str(input(text_in))
                number = int(num)
                self.log.log_data(f"{text_in} {num}")
                return number
        
            except ValueError:
                self.log.log_data(f"Число введено не верно {num}")
                print(text_breach)
    
    def checkNumberMinMax (self, min_number:int = 0, max_number: int =100, text_in:str = 'Введите число: ', text_breach:str = 'Вы ввели число не правильно, введите его заново:', text_min:str ='Вы ввели число меньше минимального, введите его заново: ', text_max:str ='Вы ввели число больше максимального, введите его заново: '): 
        '''
        Проверка, являются ли введённые данные числом, и лежит ли это число в диапазоне 
        от минимума до максимума. 
        Если нет то повторяется запрос заново.
        text_in - текст запроса в консоли
        text_breach - текст вторичного запроса, при неправильном вводе числа
        text_min - текст запроса, если число меньше минимума
        text_max - текст запроса, если число больше максимума
        min_number - минимальное число
        max_number - максимальное число
        '''
       
        while True:
            try:
                num = str(input(text_in))
                number = int(num)
                self.log.log_data(f"{text_in} {num}")
                if number<min_number:
                    self.log.log_data(f"Пользователь ввёл число {number} меньше минерального{min_number}")
                    print(text_min)
                    continue
                if number>max_number:
                    self.log.log_data(f"Пользователь ввёл число {number} больше максимального {max_number}")
                    print(text_max)
                    continue
                return number
        
            except ValueError:
                self.log.log_data(f"Число введено не верно {num}")
                print(text_breach)