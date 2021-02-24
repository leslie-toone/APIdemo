"""
https://www.dataquest.io/blog/python-api-tutorial/
An API, or Application Programming Interface, is a server that you can use to retrieve and send data to using code.
 APIs are most commonly used to retrieve data, and that will be the focus of this beginner tutorial."""
# make sure you've already installed requests using: pip install requests
# make sure you've already installed requests using: pip install requests
import requests
import json
from datetime import datetime

# example of get request that gives a code that it doesn't exist '404'
# Status codes are returned with every request that is made to a web server.
# Status codes indicate information about what happened with a request.
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)

# In order to ensure we make a successful request, when we work with APIs it’s important to consult the documentation.

"""We’ll be working with the Open Notify API, which gives access to data about the international space station. 
It’s a great API for learning because it has a very simple design, and doesn't require authentication.
Often there will be multiple APIs available on a particular server. Each of these APIs are commonly called 
endpoints. """

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
# find out when the international space station will pass over a New York City. We can also do the same thing
# directly by adding the parameters directly to the URL. like this:
# http://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74. It’s almost always preferable to setup the parameters
# as a dictionary, because requests takes care of some things that come up, like properly formatting the query
# parameters, and we don’t need to worry about inserting the values into the URL string.
# NOTE TO RUN SELECTION IN PYCHARM PRESS ALT+SHIFT+E
parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())
"""Understanding the Pass Times
The JSON response matches what the documentation specified:

-A dictionary with three keys
-The third key, response, contains a list of pass times
-Each pass time is a dictionary with risetime (pass start time) and duration keys.
Let’s extract the pass times from our JSON object: """

# Next we’ll use a loop to extract just the five risetime values:
pass_times = response.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)
"""These times are difficult to understand – they are in a format known as timestamp or epoch. Essentially the time 
is measured in the number of seconds since January 1st 1970. We can use the Python datetime.fromtimestamp() method to 
convert these into easier to understand times: """


times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
