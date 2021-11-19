import requests

#GET

r = requests.get('https://jsonplaceholder.typicode.com/posts/20')
print(r)
print(r.status_code)
#respuesta
print(r.text)
#print(r.json)

my_query = r.json()
#print(my_query)
print(my_query['title'])

#POST

r = requests.post('https://jsonplaceholder.typicode.com/posts/', data={'title':'Hola mundo', 'body': 'aaa+'})
print(r.status_code)
print(r.text)
