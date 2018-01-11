import urllib
import urllib2
import re
import thread
import time
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
url = 'http://www.chinahr.com/wuxi/jobs/21625/'
headers = {'User-Agent':user_agent}
result = urllib2.Request( url, headers=headers)
response = urllib2.urlopen( result )
pageCode = response.read().decode('utf-8')
pattern = re.compile(r'<a href="http://www.chinahr.com/job/.*?>(.*?)</a>.*?<span class="e2">(.*?)</span>.*?<span class="e2">(.*?)</span>.*?<em>(.*?)</em>',re.S )
items = re.findall(pattern,pageCode)
for i in items:
    input = raw_input()
    for g in i:
        
        print g
        


        
