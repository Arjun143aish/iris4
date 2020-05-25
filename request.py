import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepal_length':6.3, 'sepal_width':2.5, 'petal_length':4.9,
                            'petal_width':1.5})

print(r.json())


#Local Environment IP address
