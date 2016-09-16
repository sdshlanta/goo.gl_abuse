#!/usr/bin/python
import urllib2
from time import sleep

lists = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
po1 = po2 = po3 = po4 = po5 = po6 =0
uri_end=''
for i in xrange (56800235584):
    if po6 and po5 and po4 and po3 and po2 == 61 and po1 == 62:
        print 'done'
        exit();
    uri_end = str(lists[po6]+lists[po5]+lists[po4]+lists[po3]+lists[po2]+lists[po1])
    full_url = "http://goo.gl/"+uri_end
    try:
        request_url = urllib2.urlopen(full_url).geturl()
        with open('urls.txt', 'a') as f:
            f.write("Requested Short URL: "+full_url+" Unshortened version: "+request_url+'\n')
            f.close()
            sleep(5)
    except Exception as e:
        sleep(10)
    if po1==61:
        po2 +=1
        if po2==61:
            po3 +=1
            if po3==61:
                po4 +=1
                if po4==61:
                    po5 +=1
                    if po6 <61:
                        if po5==61:
                            po6 +=1
	
    else:pass;
    po1 +=1	
    if po1==62:po1=0
    if po2==62:po2=0
    if po3==62:po3=0
    if po4==62:po4=0
    if po5==62:po5=0
    if po6==62:po6=0
