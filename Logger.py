from datetime import datetime

class Logger:
    """
    Логирование данных 
    """

    def log_data(text_log):
        """
        Логирование данных в файл
        LogCalc.txt
        """
        

        folder = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\PYTHON_HW13_OOP\LogCalc.txt'
        #folder =r'LogCalc.txt'

        with open( folder, 'a+', encoding='UTF-8') as file:
            file.write(f'{datetime.now()}:  {text_log}\n')
        