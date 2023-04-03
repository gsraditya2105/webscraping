import webbrowser
import httplib2
from pprint import pprint

bin_url = 'https://httpbin.org/'
#webbrowser.open(bin_url)

http = httplib2.Http()
# to know what kind of options http web server supports add method='OPTIONS'
# From Response : 'access-control-allow-methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
resp,data = http.request(bin_url, method='OPTIONS')
html = data.decode("utf-8")
pprint(resp)
#pprint(html)

#- POST
post_data = '{"name":"Aditya", "college":"kiet"}'
resp,data = http.request('https://httpbin.org/post', method='POST', body=post_data,
                        headers={'Content-type': 'application/json'})
print("Post Response header = ", resp)
print("Post response body = ", data.decode("utf-8"))

#- PUT
resp,data = http.request('https://httpbin.org/put', method='PUT', body=post_data,
                        headers={'Content-type': 'application/json'})
print("Put Response header = ", resp)
print("Put response body = ", data.decode("utf-8"))

