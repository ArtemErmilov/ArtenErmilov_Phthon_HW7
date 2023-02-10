from Logger import Logger

class ValueStr ():
    """
    Ввод данных из консоли в формате String
    """

    log=Logger

    def inputString(self,text_in:str = 'Введите данные: '):
        """
        Ввод данных в формате String
        """
        data = str(input( text_in))
        self.log.log_data(f"{text_in} {data}")
        return  data