import requests
from collections import namedtuple

class dictToObj(object):
    def __init__(self, initial_data, **kwargs):
        self.initial_data = initial_data
        if type(initial_data) is list:
            for dictionary in initial_data:
                for key in dictionary:
                    setattr(self, key, dictionary[key])
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            for a, b in initial_data.items():
                if isinstance(b, (list, tuple)):
                   setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
                else:
                   setattr(self, a, obj(b) if isinstance(b, dict) else b)

    def getDict(self):
        return vars(self)

    def __repr__(self):
       return str(self.initial_data)

class clientLoot():
    def __init__(self, token):
        self.token = token

    def getItems(self):
        items = requests.get(f'http://fenixweb.net:3300/api/v2/{self.token}/items').json()["res"]

        listItems = []
        for item in items:
            listItems.append(dictToObj(item))    

        return listItems

    def getItemsDict(self):
        items = requests.get(f'http://fenixweb.net:3300/api/v2/{self.token}/items').json()["res"]  
        return items

    def getItem(self,item):
        item = requests.get(f'http://fenixweb.net:3300/api/v2/{self.token}/items/{item}').json()["res"]
        return dictToObj(item)

    def getNeeded(self,item):
        needed = requests.get(f'http://fenixweb.net:3300/api/v2/{self.token}/crafts/{item}/needed').json()["res"]
        listItems = []
        for item in needed:
            listItems.append(dictToObj(item))    

        return listItems

    def getUsed(self,item):
        used = requests.get(f"http://fenixweb.net:3300/api/v2/{self.token}/crafts/{item}/used").json()["res"]
        listItems = []
        for item in used:
            listItems.append(dictToObj(item))    

        return listItems

    def getCrafts(self):
        crafts = requests.get(f"http://fenixweb.net:3300/api/v2/{self.token}/crafts/id").json()["res"]
        listItems = []
        for item in crafts:
            listItems.append(dictToObj(item))    
        return listItems

    def getPlayers(self):
        players = requests.get(f"http://fenixweb.net:3300/api/v2/{self.token}/players").json()["res"]
        listItems = []
        for item in players:
            listItems.append(dictToObj(item))    
        return listItems

    def getPlayer(self,player):
        player = requests.get(f"http://fenixweb.net:3300/api/v2/{self.token}/players/{player}").json()["res"]
        return dictToObj(player)




    