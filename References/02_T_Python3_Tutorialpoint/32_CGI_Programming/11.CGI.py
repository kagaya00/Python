


"""


Retrieving Cookies
It is very easy to retrieve all the set cookies. Cookies are stored in CGI environment variable HTTP_COOKIE and they will have following form −

key1 = value1;key2 = value2;key3 = value3....
Here is an example of how to retrieve cookies.


"""

#!/usr/bin/python

# Import modules for CGI handling 
from os import environ
import cgi, cgitb

if environ.has_key('HTTP_COOKIE'):
   for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
      (key, value ) = split(cookie, '=');
      if key == "UserID":
         user_id = value

      if key == "Password":
         password = value

print "User ID  = %s" % user_id
print "Password = %s" % password


"""

This produces the following result for the cookies set by above script −

User ID = XYZ
Password = XYZ123
"""

