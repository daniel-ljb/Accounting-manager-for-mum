from datetime import datetime

class Transaction():
    def __init__(self, init: str):
        init = init.split()
        # 123545112 12.17 Session
        # {ms since 1.1.1970} {amount} {description}
        if "." in init[0]:
            self.__time = int(init[0].split(".")[0])
            self.__date = init[0].split(".")[1]
        elif "/" in init[0]:
            self.__date = init[0]
            date_obj = datetime.strptime(init[0], '%d/%m/%Y')
            self.__time = int(date_obj.timestamp())
        else:
            self.__time = int(init[0])
            date_obj = datetime.fromtimestamp(self.__time)
            self.__date = date_obj.strftime('%d/%m/%Y')
        self.__amount = float(init[1])
        if len(init) >= 2: self.__description = " ".join(init[2:])
        
    def __eq__(self, other):
        return self.__time == other.__time
    
    def __lt__(self, other):
        return self.__time < other.__time
    
    def __le__(self, other):
        return self.__time <= other.time
    
    def __str__(self):
        return f"{self.__time}.{self.__date} {self.__amount} {self.__description}"