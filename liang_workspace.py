import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#import plotly.graph_objects as go
from PIL import Image
#from pyecharts.charts import Bar
#from pyecharts import options as opts
import pandas as pd
from PIL import Image
#import nest_asyncio
#nest_asyncio.apply()

import numpy as np
import pandas as pd
#from scipy.interpolate import Rbf  
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib as mpl
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter
import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math
#from mpl_toolkits.basemap import Basemap 
from matplotlib.patches import Polygon 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
import cartopy.feature as cfeat
from cartopy.io.shapereader import Reader
from datetime import datetime
from liang_workspace_drawelement import draw_elements



def elements():
    
    st.header('请填写表单')

     
def station():
    # col1,col2 =st.columns(2)
    # with col1:
    #     st.header('站点分布图')
    #     image1 = Image.open(r'G:\streamlit\延庆自动站分布图2021.10.26.png')
    #     st.image(image1,use_column_width=False)
    # with col2:
    #     st.header('高程分布图')
    #     image2 = Image.open(r'G:\streamlit\topography-yq.png')
    #     st.image(image2,use_column_width=False)
    
    st.header('站点分布图')
    image1 = Image.open(r'G:\streamlit\延庆自动站分布图2021.10.26.png')
    st.image(image1,use_column_width=True)

    st.header('高程分布图')
    image2 = Image.open(r'G:\streamlit\topography-yq.png')
    st.image(image2,use_column_width=True)
       
def Line():
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    st.plotly_chart(fig)
   
def alert():
     st.header('请填写表单')

    
def aggregate_bar():
    df = px.data.tips()
    fig = px.histogram(df, x="sex", y="total_bill",
                  color='smoker', barmode='group',
                  histfunc='avg',
                  height=400)
    
    st.plotly_chart(fig)
   
def bar_charts():
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    st.plotly_chart(fig)
   
def pie():
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', color='day',
                  color_discrete_map={'Thur':'lightcyan',
                                      'Fri':'cyan',
                                      'Sat':'royalblue',
                                      'Sun':'darkblue'})
    st.plotly_chart(fig)
   
def pulled_out():    
    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    
    # pull is given as a fraction of the pie radius
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.2, 0, 0])])   
    st.plotly_chart(fig)

@st.cache
def load_data():
    df = pd.read_csv(r'G:\streamlit\STAT202112.csv', encoding='UTF-8')
    df['年月'] = df['年月'].astype("str")    
    
    return df

def Double_coordinates():  
    df = load_data()

    st.markdown('#### 数据表展示')
    st.table(df)    

    st.markdown('#### 双坐标图')
    x = df["年月"]
    y1_1 = df['流失客户']
    y1_2=df['新客户']
    
    y2 = df["余额"]
    
    trace0_1 = go.Bar(x=x,y=y1_1,
                    marker=dict(color="red"),
                    opacity=0.5,
                   name="流失客户")

    trace0_2 = go.Bar(x=x,y=y1_2,
                    marker=dict(color="blue"),
                    opacity=0.5,
                   name="新客户")
    
    trace1 = go.Scatter(x=x,y=y2,
                        mode="lines",
                        name="余额",
                        # 【步骤一】：使用这个参数yaxis="y2"，就是绘制双y轴图
                        yaxis="y2")
    
    data = [trace0_1,trace0_2,trace1]
    
    layout = go.Layout(title="客户发展趋势",
                       xaxis=dict(title="年月"),
                       yaxis=dict(title="客户数量"),
                       # 【步骤二】：给第二个y轴，添加标题，指定第二个y轴，在右侧。
                       yaxis2=dict(title="金额",overlaying="y",side="right"),
                       legend=dict(x=0.78,y=0.98,font=dict(size=12,color="black")))
    
    fig = go.Figure(data=data,layout=layout)
    
    st.plotly_chart(fig)


#--------------------------------------------------------------主体内容    
# image = Image.open(r'G:\streamlit\image.png')
# st.image(image,use_column_width=False)
# st.subheader('“放弃”二字15笔，“坚持”二字16笔，放弃和坚持就在一笔之差！差之毫厘，失之千里。无论你睡多晚，总有人比你更晚。无论你起多早，总有人比你更早。无论你多努力，总有人比你更努力。不管你有多辛苦，总有人比你更辛苦。所以要持之以恒，坚持就是胜利！')
st.sidebar.title('导航栏')
st.balloons()
st.sidebar.button('1、实时要素分布',on_click=elements)
with st.sidebar.expander("请在这里填写表单"):
    
    #st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    form =  st.form(key='my_form')
    a1=form.date_input("起始日期", value=None)
    a2=form.time_input("起始时间", value=None)
    b1=form.date_input("结束日期", value=None)
    b2=form.time_input("结束时间", value=None)
    sle_elem = form.radio("选择要素类型",
     ('阵风', '降水', '气温'))
        # Every form must have a submit button.
    submitted = form.form_submit_button(label='Submit')
    #with st.container():
        #st.write("This is inside the container")
    
        # You can call any Streamlit command, including custom components:
        #st.bar_chart(np.random.randn(50, 3))
    
if submitted:
    d=datetime.combine(a1,a2)
    d =datetime.strftime(d,'%Y-%m-%d %H:%M')
    e=datetime.combine(b1,b2)
    e =datetime.strftime(e,'%Y-%m-%d %H:%M')
    #elements()
    st.write('出图中')
    draw_elements(d,e,sle_elem)
#st.write("Outside the form")        


st.sidebar.button('2、自动站分布图,3D?',on_click=station)
st.sidebar.button('3、临近一小时累计雨量（5分钟自动刷新）',on_click=Line)
st.sidebar.button('4、主站备站及各备份观测对比（翻斗称重）',on_click=Line)
st.sidebar.button('5、预警信号快速查询',on_click=alert)
with st.sidebar.expander("请在这里填写表单"):
    
    #st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
     
    form_al =  st.form(key='my_form2')
    add_selectbox=form_al.radio(
        "预警类型",
        ("大风", "雷电", "暴雨","冰雹","大雾","沙尘暴","暴雪","霜冻","寒潮","高温","道路结冰","持续低温")
    )
    add_selectbox2 = form_al.radio(
        "预警级别",
        ("蓝", "黄", "橙","红")
    )
    
        # Every form must have a submit button.
    submitted2 = form_al.form_submit_button(label='Submit')
    #with st.container():
        #st.write("This is inside the container")
    
        # You can call any Streamlit command, including custom components:
        #st.bar_chart(np.random.randn(50, 3))
    
if submitted2:
    
    add_selectbox = add_selectbox
    add_selectbox2 = add_selectbox2
    dic_sentence={"大风":[{'蓝':['（受冷空气影响，）预计*日白天，延庆区将有4、5级偏北风，阵风可达7级左右，请注意防范。','（受冷空气影响，）预计*日傍晚到*日白天，延庆区将有5级左右偏北风，阵风可达7到8级，局地伴有扬沙。请注意防范。','（受冷空气影响，）预计*日凌晨至午后，延庆区将出现5、6级偏北风，阵风可达8级左右。请注意防范大风可能造成的衍生灾害。','（受强降雨云团影响，）预计当前至*日白天，延庆区将出现7级左右短时大风 ，请注意防范。'],
	                       "黄":['预计，当前至*日前半夜延庆区有5级左右偏北风，阵风9级、局地10级以上，伴有扬沙，请注意防范。'],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "雷电":[{'蓝':['预计当前至**时，延庆区将出现雷阵雨天气，有雷电活动，并伴有短时大风，请注意防范。','预计当前至*日*时，延庆区有分散性雷阵雨天气，并伴有雷电活动和短时大风，请注意防范。',' 预计当前至*日*时，延庆区将出现雷阵雨天气，有雷电活动，局地短时雨强较大，请注意防范。'],
	                       "黄":['预计当前至**日**时，延庆区将出现雷阵雨，有雷电活动，短时雨强较大，局地有短时大风和冰雹，请注意防范。',' 预计当前至**时，延庆区将出现雷阵雨天气，有雷电活动，局地短时雨强较大，并伴有6级以上短时大风，部分地区可能出现冰雹，请注意防范。',' 预计当前至**时，延庆**地区将出现雷阵雨天气，有雷电活动，局地短时雨强较大，并伴有短时大风，部分地区可能出现冰雹，请注意防范。','','',''],
		                   "橙":['','','','','',''],
		                   "红":['','','','','','']}],
              "暴雨":[{'蓝':['预计当前至**日**时，延庆区大部分地区将出现短时强降水，小时雨量可达30毫米以上，伴有6级以上短时大风，山区及浅山区可能出现强降水诱发的中小河流洪水、山洪、地质灾害等次生灾害，城市低洼地区可能出现积水，请注意防范。','预计当前至**日**时，延庆区大部分地区将出现短时强降水，小时雨量可达30毫米以上，伴有冰雹，山区及浅山区可能出现强降水诱发的中小河流洪水、山洪、地质灾害等次生灾害，城市低洼地区可能出现积水，请注意防范。','预计当前至**日**时，延庆区大部分地区将出现短时强降水，小时雨量可达30毫米以上，并伴有6级以上短时大风或冰雹，山区及浅山区可能出现强降水诱发的中小河流洪水、山洪、地质灾害等次生灾害，城市低洼地区可能出现积水，请注意防范。','目前延庆区大部分地区已经出现中雨，局地大雨，预计**日傍晚到夜间降水仍将持续，部分地区累计雨量可达50毫米，山区及浅山区可能出现强降水诱发的中小河流洪水、山洪、地质灾害等次生灾害，城市低洼地区可能出现积水，请注意防范。'],
		                   "黄":['目前延庆区**站降水量已达40毫米，预计当前至**时降水持续，局地将会出现6小时降水量达70毫米的强降水，并伴有短时大风。强降水易诱发中小河流洪水、山洪、地质灾害等次生灾害，低洼地区可能出现积水，请注意防范。','','','','',''],
		                   "橙":['','','','','',''],
		                   "红":['','','','','','']}],
              "冰雹":[{'蓝':['无此级别'],
	                       "黄":['预计当前至*日*时，延庆区有分散性冰雹天气，可能造成一定的损失，请注意防范。','预计未来两小时内，延庆区可能出现冰雹，请注意防范。','预计当前至*时，延庆区（西部地区）将出现冰雹天气，可能造成一定的损失，请注意防范。','','',''],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "大雾":[{'蓝':['无此级别'],
	                       "黄":['预计**日后半夜到**日上午，延庆将出现大雾天气，能见度小于1千米，部分地区小于500米，请注意防范。','预计**月**日傍晚到**月**日中午，延庆区将出现大雾天气，大部分地区能见度低于500米，局地能见度低于200米，请注意防范。','','','',''],
	                       "橙":['预计今天下午到夜间，延庆大部分地区将出现浓雾，部分地区能见度小于200米，请注意防范。','','','','',''],
	                       "红":['','','','','','']}],
              "沙尘暴":[{'蓝':['受上游沙尘天气影响，预计**日下午到前半夜，延庆地区将出现浮尘或扬沙天气，请注意防范。','受上游强沙尘暴影响，预计**日傍晚到夜间，延庆区将出现沙尘暴天气，能见度小于1000米，请注意防范。',''],
	                         "黄":['受上游强沙尘暴影响，预计**日傍晚到夜间，延庆区将出现沙尘暴天气，能见度小于1000米，请注意防范。','','','','',''],
	                         "橙":['','','','','',''],
	                         "红":['','','','','','']}],
              "暴雪":[{'蓝':['目前延庆区大部分地区已出现降雪，预计*日白天，本区大部分地区将有大雪，部分地区有暴雪，请注意防范。',''],
	                       "黄":['截止到*时*分延庆区本站降雪量已达*mm，降雪将持续到今天夜间，全区大部分地区将出现暴雪。请注意防范雪灾和冻害，交通、电力、通信、市政等部门及时进行道路、铁路、线路巡查维护，及时清扫道路和融化积雪。','截止到09时40分降雪量（毫米），延庆站**，佛爷顶**，农场**。预计降雪将持续到今天夜间，全区大部分地区将出现暴雪。请注意防范雪灾和冻害。','','','',''],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "霜冻":[{'蓝':[' 预计**夜间，延庆区大部分地区地面最低温度将下降到0℃以下 ，对农业将产生影响，请注意防范。','',''],
	                       "黄":['预计**日夜间，延庆大部分地区地面最低温度将下降到-3℃以下， 对农业将产生影响，请注意防范。','','','','',''],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "寒潮":[{'蓝':['受强冷空气影响，预计*日至*日，延庆区最低气温将下降10℃左右，*日夜间最低气温达-11℃，并伴有5、6级偏北风，阵风可达8级左右，请注意防范。','',''],
	                       "黄":['','','','','',''],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "高温":[{'蓝':['预计**至**日，延庆区日最高气温将达35-37℃，请注意防暑降温。','预计**至**日，延庆区大部分地区日最高气温将达35℃以上，请注意防暑降温。',''],
	                       "黄":['','','','','',''],
	                       "橙":['','','','','',''],
	                       "红":['','','','','','']}],
              "道路结冰":[{'蓝':['无此级别'],
	                           "黄":['受强冷空气影响，预计延庆区**日夜间有小到中雪，局地大雪，会出现道路结冰现象，请注意交通安全。','（目前，延庆区已出现降雪天气，）预计至**日早晨，延庆区地表温度低于0℃ ，易于形成道路结冰，请注意交通安全。','目前，延庆城区已出现雨夹雪，预计后半夜将出现降雪天气，易形成道路结冰，对交通有影响，请注意防范。','','',''],
	                           "橙":['','','','','',''],
	                           "红":['','','','','','']}],
              "持续低温":[{'蓝':['受持续补充冷空气影响，预计**至**日，延庆区将出现持续低温天气，平原地区日最低气温将低于零下10℃，请注意防寒保暖。','预计**日夜间至**日，延庆区日平均气温较常年同期偏低5～6℃，最高气温-5～-3℃，最低气温**、**日可低至-13℃左右。请注意防寒保暖，室内取暖注意通风，预防一氧化碳中毒。',''],
	                           "黄":['受持续补充冷空气影响，预计**至**日，延庆区将出现持续低温天气，平原地区日最低气温将低于零下12℃，请注意防寒保暖。','','','','',''],
	                           "橙":['','','','','',''],
	                           "红":['','','','','','']}]
    }
    st.write(dic_sentence[add_selectbox][0][add_selectbox2])
st.sidebar.button('基本数据表',on_click=Double_coordinates)
    
  
