from Logger import Logger

class ValueShow():
    """
    Вывод данных в консоль
    """

    log=Logger
    
    def showNumber(self, text, number):
        """
        Вывод данных в консоль в формате  text+number
        """
        
        print(f"{text} {number}")
    