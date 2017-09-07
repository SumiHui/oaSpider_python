import re

keyNameList=['校领导','纪委','组织部','宣传部','学生处','保卫处','人事处','教务处','科技处','研究生','质管处','学生就业指导中心','规划与资产','国际合作处','财务处','信息处','基建处','离退休','校友处','工会','团委','体工部','图书馆','档案馆','教学设施','后勤集团','综合校务']
keyFullNameList=['校领导信箱','纪委信箱','组织部信箱','宣传部信箱','学生处信箱','保卫处信箱','人事处信箱','教务处信箱','科技处信箱','研究生信箱','质管处信箱','学生就业指导中心','规划与资产','国际合作处','财务处信箱','信息处信箱','基建处信箱','离退休信箱','校友处','工会信箱','团委信箱','体工部信箱','图书馆信箱','档案馆信箱','教学设施','后勤集团','综合校务系统']
print(len(keyFullNameList))
list1=[0,0,0,0,0,0,0,0,0]
listOA=[[0 for col in range(9)] for row in range(27)]       #初始化一个27*9的矩阵

pattern = re.compile('2017-0(\d)-\d+',re.S)

listtotal=[]
with open('dmuoaShortInfo.txt', 'r', encoding='utf-8', errors='ignore') as f:
    listtotal=f.readlines()
for row in listtotal:
    list_row=row.strip().split('\t')
    post_time,title,letterbox,responser,reply_time,_ignore2=list_row
    if reply_time.startswith('2016'):
        break
    try:
        partId=keyFullNameList.index(letterbox)
        orderId=re.findall(pattern,reply_time)
        listOA[partId][int(orderId[0])-1]+=1
    except:
        print(letterbox)
        continue



#
# from pyecharts import Polar
# radius =['一月', '二月', '三月', '四月', '五月', '六月', '七月','八月','九月']
# polar =Polar("2017年各部门处理信件数对比", "数据截止2017-09-06 14:25",title_pos='center',width=1200, height=800)
# polar.add(keyNameList[0], listOA[0], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[1], listOA[1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[2], listOA[2], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[3], listOA[3], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[4], listOA[4], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[5], listOA[5], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[6], listOA[6], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[7], listOA[7], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[8], listOA[8], radius_data=radius, type='barRadius', is_stack=True)
#
# polar.add(keyNameList[9], listOA[9], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[10], listOA[10], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[11], listOA[11], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[12], listOA[12], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[13], listOA[13], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[14], listOA[14], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[15], listOA[15], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[16], listOA[16], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[17], listOA[17], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[18], listOA[18], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[19], listOA[19], radius_data=radius, type='barRadius', is_stack=True)
#
# polar.add(keyNameList[20], listOA[20], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[21], listOA[21], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[22], listOA[22], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[23], listOA[23], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[24], listOA[24], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[25], listOA[25], radius_data=radius, type='barRadius', is_stack=True)
# polar.add(keyNameList[26], listOA[26], radius_data=radius, type='barRadius', is_stack=True,legend_orient='vertical', legend_pos='left')
#
# polar.show_config()
# polar.render('各部门处理信件数量对比图.html')


#
# from pyecharts import Radar
# schema =[ ("January", 168), ("February", 43), ("March", 363), ("April", 288), ("May", 385), ("June", 462), ("July", 507), ("August", 332), ("September", 104)]
# v1 =[[168, 43,363, 288, 385, 462, 507,  332, 104]]
# v2=[listOA[0]]
# radar =Radar()
# radar.config(schema)
# radar.add("全体信件总处理量", v1, is_splitline=True, is_axisline_show=True)
# radar.add("校领导信箱处理量", v2, label_color=["#4e79a7"], is_area_show=False,is_label_show=True)
# radar.show_config()
# radar.render('radar.html')



from pyecharts import Funnel
attr=keyNameList
value=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(27):
    for j in range(9):
        value[i]+=listOA[i][j]

funnel=Funnel('各部门截止目前2017年处理总量金字塔',title_pos='center',width=1200, height=800)
funnel.add('infomation',attr,value,is_label_show=True,label_pos="inside",label_text_color='#999',legend_orient='vertical',legend_pos='left')
funnel.render('funnel.html')