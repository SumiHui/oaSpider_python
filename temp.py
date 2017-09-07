'''
获取前两页的所有代理IP地址
'''
from bs4 import BeautifulSoup
import requests
import urllib.request
import re

headers={'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

def getOAInfo():
    primary = []    #每一行数据临时存储
    oaInfo=[]       #整理汇总所有行文本
    for i in range(1,429):
        try:
            url='http://oa.dlmu.edu.cn/echoWall/listEchoWall.do?page=%d'%i
            print(url)
            req = urllib.request.Request(url, headers=headers)
            res = urllib.request.urlopen(req)
            content = res.read().decode('utf-8')
            pattern = re.compile('<a href="javascript:detail\((\d+)\)">', re.S)
            # detail_ids=re.findall(pattern, content)
            # print(detail_ids)

            soup=BeautifulSoup(content,'lxml')
            trs=soup.select('tr')       #获取当前页所有行数据
            for tr in trs:
                if  len(tr.select('td'))>5:
                    primary.append(tr.select('td')[1].text.strip())     #question time
                    primary.append(tr.select('td')[2].text.strip())     #question title
                    primary.append(tr.select('td')[3].text.strip())     #addr
                    primary.append(tr.select('td')[4].text.strip())     #responser
                    primary.append(tr.select('td')[5].text.strip())     #respons time

                    tag_a = tr.select('a')
                    pkId = ''.join(re.findall(pattern, str(tag_a)))     #detailLetter id
                    url_details = 'http://oa.dlmu.edu.cn/echoWall/detailLetter.do?pkId=%s' % pkId
                    data_details = requests.get(url_details, headers=headers)
                    data_details.encoding = 'utf-8'
                    soup_details = BeautifulSoup(data_details.text, 'lxml')
                    soup_details_trs=soup_details.select('tr')
                    *_ignore,advice,reply=soup_details_trs
                    primary.append(re.sub('[\n\t\s]\s+', '', advice.select('td')[0].text.strip()))     # advice
                    primary.append(pkId)
                    primary.append(re.sub('[\n\t\s]\s+', '', reply.select('td')[0].text.strip()))      # reply

                    oaInfo.append('\t'.join(primary))
                    primary.clear()                                     #用完清空，以备下一次使用
        except:
            continue
    with open('dmuoawithDetails.txt','w',encoding='utf-8',errors='ignore') as fip:
        fip.write(str('\n'.join(oaInfo)))
    return oaInfo


if __name__=='__main__':
    getOAInfo()