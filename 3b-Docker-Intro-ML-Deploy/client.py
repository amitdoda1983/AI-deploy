import requests
#url = 'http://127.0.0.1:5000/api'
#url = 'http://flask-demo-python-client-dev.ap-south-1.elasticbeanstalk.com'
url = 'http://flask-demo-python-client-dev.ap-south-1.elasticbeanstalk.com.'
r = requests.post(url,json={'exp':1.8,})
print ('hello')
print(r.json())