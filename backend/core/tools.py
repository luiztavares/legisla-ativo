from email.quoprimime import body_check
import requests

class Request():
    def __init__(self):
        self.body = None
        self.code = None

    @property
    def func(self,body):
        if(self.body):
            return self.body
        
    def __get_params(self):
        params = dict()
        for field in self._meta.get_fields():
            key = field.name
            value = getattr(self, field.name)
            if( key != 'id' and value and not field.help_text == 'path' ):
                params[key] = value
        return params

    def get(self):
        if(self.code):
            return

        headers = {'Accept': 'application/json'}
        params = self.__get_params()
        req = requests.get(url=self.url,headers=headers,params=params)
        try:
            self.code = req.status_code
            self.body = req.json()
        except:
            self.code = req.status_code