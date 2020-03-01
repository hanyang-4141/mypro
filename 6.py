from lxml import etree



parser=etree.HTMLParser(encoding='utf-8')
html_element=etree.parse('dianjiaban.html',parser=parser)

tt=html_element.xpath("//tr")
print(len(tt))
quexiantongji=[]
for t in tt[2:len(tt)]:    
    tt1=t.xpath('.//td')
    index=0
    info={}
    
    for i in tt1:
        # print('*'*100)
        # print(index)
        # print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
        # str=etree.tostring(i,encoding='utf-8').decode('utf-8')
        # print(str.strip(""))
        # print(i)
        str1=i.xpath('normalize-space(./text())')         #normalize-space:去除/r/t/n
        if index == 0:
            info['序号']=str1   
        elif index == 1:
            info['检修班组']=str1   
        elif index==2:
            info['缺陷单号']=str1   
        elif index==3:
            info['缺陷描述']=str1   
        elif index==4:
            info['措施说明']=str1
        elif index==5:
            info['状态']=str1   
        elif index==6:
            info['状态描述']=str1   
        elif index==7:
            info['登记时间']=str1   
        elif index==8:
            info['完成时间']=str1   
        elif index==9:
            info['登记人']=str1   
        elif index==10:
            info['机组']=str1   
        elif index==11:
            info['缺陷类型']=str1   
        elif index==12:
            info['运行班组']=str1   
        elif index==13:
            pass
        index+=1
    # print(info)
    quexiantongji.append(info)
print(quexiantongji)