listtotal=[]
list_countbymonth=dict(January=0,February=0,March=0,April=0,May=0,June=0,July=0,August=0,September=0)

list_countbyJan_bypart=dict(校领导=0,纪委=0,组织部=0,宣传部=0,学生处=0,保卫处=0,人事处=0,教务处=0,科技处=0,研究生=0,质管处=0,学生就业指导中心=0,规划与资产=0,国际合作处=0,财务处=0,信息处=0,基建处=0,离退休=0,校友处=0,工会=0,团委=0,体工部=0,图书馆=0,档案馆=0,教学设施=0,后勤集团=0,综合校务=0)
list_countbySept_bypart=list_countbyAug_bypart=list_countbyJuly_bypart=list_countbyJune_bypart=list_countbyMay_bypart=list_countbyApr_bypart=list_countbyMar_bypart=list_countbyFeb_bypart=list_countbyJan_bypart
keyNameList=list(list_countbySept_bypart.keys())
# print(keyNameList)

with open('dmuoaShortInfo.txt', 'r', encoding='utf-8', errors='ignore') as f:
    listtotal=f.readlines()
for row in listtotal:
    list_row=row.strip().split('\t')
    post_time,_ignore,letterbox,responser,reply_time,_ignore2=list_row
    if reply_time.startswith('2017-09'):
        list_countbymonth['September']+=1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbySept_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-08'):
        list_countbymonth['August'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyAug_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-07'):
        list_countbymonth['July'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyJuly_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-06'):
        list_countbymonth['June'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyJune_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-05'):
        list_countbymonth['May'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyMay_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-04'):
        list_countbymonth['April'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyApr_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-03'):
        list_countbymonth['March'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyMar_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-02'):
        list_countbymonth['February'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyFeb_bypart[keyname]+=1
                break
            else:
                continue
    elif reply_time.startswith('2017-01'):
        list_countbymonth['January'] += 1
        for keyname in keyNameList:
            if letterbox.startswith(keyname):
                list_countbyJan_bypart[keyname]+=1
                break
            else:
                continue
    else:
        break

print(list_countbymonth)
# print(list_countbySept_bypart)

from pyecharts import Bar
bar=Bar("前9个月每月反馈数",width=1024,height=768)
attr=['January','February','March','April','May','June','July','August','September']
val=[list_countbymonth['January'],list_countbymonth['February'],list_countbymonth['March'],list_countbymonth['April'], list_countbymonth['May'],list_countbymonth['June'],list_countbymonth['July'],list_countbymonth['August'],list_countbymonth['September']]
bar.add('月反馈数',attr,val)
bar.render('barbymonth.html')




#
# bar=Bar("各部门前9个月每月处理数",width=1024,height=1980)
# val_aug=[]
# for keyname in keyNameList:
#     val_aug.append(list_countbyAug_bypart[keyname])
#
# val_july=[]
# for keyname in keyNameList:
#     val_july.append(list_countbyJuly_bypart[keyname])
#
# val_june = []
# for keyname in keyNameList:
#     val_june.append(list_countbyJune_bypart[keyname])
#
# val_may = []
# for keyname in keyNameList:
#     val_may.append(list_countbyMay_bypart[keyname])
#
# bar.add('8',keyNameList,val_aug)
# bar.add('7',keyNameList,val_july)
# bar.add('6',keyNameList,val_june)
# bar.add('5',keyNameList,val_may,is_convert=True)
# bar.render('bar_month_part.html')

#
# from pyecharts import Polar
# radius =['一月', '二月', '三月', '四月', '五月', '六月', '七月','八月','九月']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("A", [1, 2, 3, 4, 3, 5, 1, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("B", [2, 4, 6, 1, 2, 3, 1, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("C", [1, 2, 3, 4, 1, 2, 5, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("d", [1, 2, 3, 4, 3, 5, 1, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("e", [2, 4, 6, 1, 2, 3, 1, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("f", [1, 2, 3, 4, 1, 2, 5, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("g", [1, 2, 3, 4, 3, 5, 1, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("h", [2, 4, 6, 1, 2, 3, 1, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("i", [1, 2, 3, 4, 1, 2, 5, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.show_config()
# polar.render('polar.html')

# from pyecharts import Pie
# pie =Pie('各类电影中"好片"所占的比例', "数据来自dmu", title_pos='center',width=1280,height=768)
# pie.add("", ["剧情", "A"], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, )
# pie.add("", ["奇幻", "B"], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
# pie.add("", ["爱情", "C"], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["惊悚", "D"], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["冒险", "E"], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["动作", "F"], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["喜剧", "G"], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["科幻", "H"], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["悬疑", "I"], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["犯罪", "J"], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
# pie.show_config()
# pie.render('pie_sort.html')

# from pyecharts import Pie
# pie =Pie("各部门处理信件数", title_pos='center', width=1600, height=800)
# # pie.add("", keyNameList, val_aug, radius=[70, 75],is_label_show=True)
# pie.add("", keyNameList, val_july, radius=[0,75], legend_orient='vertical', legend_pos='left',is_label_show=True)
# pie.show_config()
# pie.render('pie_enbed.html')


# from pyecharts import Pie
# pie = Pie("",width=1280,height=768)
# # pie.add("", keyNameList, val_aug, is_label_show=True)
# pie.add("", keyNameList, val_july, is_label_show=True)
# pie.show_config()
# pie.render('pie.html')

# from pyecharts import Radar
# schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
# v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
# v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
# radar =Radar()
# radar.config(schema)
# radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
# radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
# radar.show_config()
# radar.render('radar.html')

# from pyecharts import Parallel
# c_schema =[ {"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"},
#             {"dim": 2, "name": "PM2.5"}, {"dim": 3, "name": "PM10"},
#             {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"},
#             {"dim": 6, "name": "CO2"},
#             {"dim": 7, "name": "等级", "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
# data =[ [1, 91, 45, 125, 0.82, 34, 23, "良"], [2, 65, 27, 78, 0.86, 45, 29, "良"],
#         [3, 83, 60, 84, 1.09, 73, 27, "良"], [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
#         [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"], [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
#         [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"], [8, 89, 65, 78, 0.86, 51, 26, "良"],
#         [9, 53, 33, 47, 0.64, 50, 17, "良"], [10, 80, 55, 80, 1.01, 75, 24, "良"],
#         [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"], [12, 99, 71, 142, 1.1, 62, 42, "良"],
#         [13, 95, 69, 130, 1.28, 74, 50, "良"], [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
# parallel =Parallel("平行坐标系-用户自定义指示器")
# parallel.config(c_schema=c_schema)
# parallel.add("parallel", data)
# parallel.show_config()
# parallel.render('paralle.html')


# from pyecharts import Gauge
# gauge=Gauge('Sample')
# gauge.add('回复率','完成率',66.66)
# gauge.show_config()
# gauge.render('gauge.html')

# from pyecharts import Bar
# bar=Bar("sample",width=1024,height=768)
# attr=['a','b','c','c']
# val=[23,45,34,41]
# bar.add('A',attr,val)
# bar.render('bar.html')


# from pyecharts import EffectScatter
# v1=[10,20,30,40,50,60]
# v2=[25,20,15,10,60,33]
# es=EffectScatter('动态散点图实例')
# es.add('effectScatter',v1,v2)
# es.render('effectScatter.html')

# from pyecharts import Funnel
# attr=[1,2,3,4,5,6,7]
# value=[20,40,60,80,100,120,140]
# funnel=Funnel('漏斗实例')
# funnel.add('infomation',attr,value,is_label_show=True,label_pos="inside",label_text_color='#fff')
# funnel.render('funnel.html')


# from pyecharts import Polar
# radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.show_config()
# polar.render('polar.html')