import json
class TranslateData:
    txtdata : str
    dest: str
    
    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__)
