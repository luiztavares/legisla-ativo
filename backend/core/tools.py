import requests

class Request:

    def get_params(self):
        params = dict()
        for field in self._meta.get_fields():
            key = field.name
            value = getattr(self, field.name)
            if( key != 'id' and value):
                params[key] = value
        return params

    def get(self):
        
        headers = {'Accept': 'application/json'}
        params = self.get_params()
        req = requests.get(url=self.url,headers=headers,params=params)
        
        return req.json()