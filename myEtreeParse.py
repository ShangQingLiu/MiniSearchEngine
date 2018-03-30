#This file is the function to parse the file come from spider
#author: sql
#date:2018/03/29
#test
from lxml import etree
for i in range(41,836):#this is our document id number
    temp = i-39 #set it as the number I want
    myhtml = etree.parse('./htmldata/'+str(i)+'.txt',etree.HTMLParser())
    title = myhtml.xpath('//title/text()')#parse the title
    print title
    newtitle = [i.replace('\n',' ')for i in title]
    print newtitle
    #capture the following tag text
    result = myhtml.xpath('//td/text()|//p/text()|//h1/text()|//h2/text()|//h3/text()|//blockquote/i/text()|//blockquote/a/text()|//a/b/text()|//p/i/text()|//address/text()|//td/a/text()|//body/blockquote/text()')#parse the content
    print result
    f = open('data//'+str(temp)+'.txt','w')# write the pure content in to data folder and save it
    for t in newtitle:
        f.write(t+'\n')
    for line in result:
        f.write(line)
    f.close()

