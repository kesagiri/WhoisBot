import urllib.request
import json



response = urllib.request.urlopen('http://188.225.28.105:4055/execpluginmethod')
j = json.loads(response.read())
print(str(j))

