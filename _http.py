import requests

url = "http://www.ibm.com/"
r = requests.get(url) # making get request
print(r)
print(r.status_code) # status code
print(r.request.headers) # status headers
print(r.request.body) # request body

header = r.headers # view response header
print(header)
print(header['date']) # date request was sent
print(header['Content-Type']) # type of data
print(r.encoding) # check the encoding
print(r.text[0:100]) # since content type is text, we can view the content by specifying index

# Get Request

url_get = "http://httpbin.org/get"
payload = {"name":"Joseph", "ID":"123"}
r=requests.get(url_get, params=payload)
print(r.url)
print(r.request.body) # request body
print(r.status_code) # status code
print(r.text)
print(r.headers["Content-Type"])
print(r.json())
print(r.json()["args"]) # The key 'args' has the name and values for the  query string

# Post Request
url_post = "http://httpbin.org/post"
payload = {"name":"Joseph", "ID":"123"}
r_post = requests.post(url_post, data=payload)

print("POST request URL: ", r_post.url)
print("GET request URL: ", r.url)

print("POST request body: ", r_post.request.body)
print("GET request body: ", r.request.body)