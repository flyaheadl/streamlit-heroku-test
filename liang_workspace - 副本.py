import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
from PIL import Image
import nest_asyncio
nest_asyncio.apply()

import numpy as np
import pandas as pd
from scipy.interpolate import Rbf  
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
def Layouts_plotly():
    
    image = Image.open(r'G:\streamlit\image.png')
    st.image(image,use_column_width=False)
    st.subheader('“放弃”二字15笔，“坚持”二字16笔，放弃和坚持就在一笔之差！差之毫厘，失之千里。无论你睡多晚，总有人比你更晚。无论你起多早，总有人比你更早。无论你多努力，总有人比你更努力。不管你有多辛苦，总有人比你更辛苦。所以要持之以恒，坚持就是胜利！')
    st.sidebar.title('导航栏')
    st.sidebar.button('实时要素分布',on_click=elements)
    st.sidebar.button('自动站分布图',on_click=station)
    st.sidebar.button('临近一小时累计雨量',on_click=Line)
    st.sidebar.button('主站备站及各备份观测对比（翻斗称重）',on_click=Line)
    st.sidebar.button('预警信号快速查询',on_click=alert)
    st.sidebar.button('基本数据表',on_click=Double_coordinates)
     # # 单选复选框
    # add_selectbox = st.sidebar.radio(
    #     "综合气象业务",
    #     ("Bubble", "Scatter", "Line","aggregate_bar","bar_charts","pie","pulled_out")
    # )
    # if add_selectbox=="Bubble":
    #     Bubble()
    # elif add_selectbox=="Scatter": 
    #     Scatter() 
    # elif add_selectbox == "Line":
    #     Line()
    # elif add_selectbox == "aggregate_bar":    
    #     aggregate_bar()
    # elif add_selectbox == "bar_charts":    
    #     bar_charts()
    # elif add_selectbox == "pie":     
    #     pie()
    # elif add_selectbox == "pulled_out":
    #     pulled_out()
   
    

def main():
    Layouts_plotly()
def elements():
    # form1 = st.form(key='my_form1')#key是form的关键字，不同form的key不能相同
    # a1=form1.date_input("起始日期", value=None)
    # a2=form1.time_input("起始时间", value=None)
    # b1=form1.date_input("结束日期", value=None)
    # b2=form1.time_input("结束时间", value=None)
    # submit_button = form1.form_submit_button(label='Submit')
    
    # if submit_button:
    #     st.write('出图中')
    #     d=datetime.combine(a1,a2)
    #     d =datetime.strftime(d,'%Y-%m-%d %H:%M')
    #     e=datetime.combine(b1,b2)
    #     e =datetime.strftime(e,'%Y-%m-%d %H:%M')
    #     st.write(d)
    #     st.write(e)
    #     st.title('# 延庆区气象局风速数据统计分析')
    #     st.subheader('**图表说明：**')
    #     st.write("""
    #         - 实时数据统计
    #         - 联系：81195317
    #             """)
    #     #增加进度条
    #     draw_elements(d,e)
        
    #     ==================================
    with st.form(key='my_form'):
        st.write("Inside the form")
        a1=st.date_input("起始日期", value=None)
        a2=st.time_input("起始时间", value=None)
        b1=st.date_input("结束日期", value=None)
        b2=st.time_input("结束时间", value=None)
    
        # Every form must have a submit button.
        submitted = st.form_submit_button(label='Submit')
    if submitted:
        d=datetime.combine(a1,a2)
        d =datetime.strftime(d,'%Y-%m-%d %H:%M')
        e=datetime.combine(b1,b2)
        e =datetime.strftime(e,'%Y-%m-%d %H:%M')
        st.write('出图中')
        draw_elements(d,e)
    st.write("Outside the form")        
    # with st.form(key='my_form'):
    #     a1=st.date_input("起始日期", value=None)
    #     a2=st.time_input("起始时间", value=None)
    #     b1=st.date_input("结束日期", value=None)
    #     b2=st.time_input("结束时间", value=None)
        
        
    
    #     d=datetime.combine(a1,a2)
    #     d =datetime.strftime(d,'%Y-%m-%d %H:%M')
    #     e=datetime.combine(b1,b2)
    #     e =datetime.strftime(e,'%Y-%m-%d %H:%M')
    #     submit_button = st.form_submit_button(label='Submit')
    #     # e=b1+datetime.strftime(b2,'%H:%M')
    #     # e =datetime.strptime(e,'%Y-%M-%d %H:%M')
    # st.write(d)
    # st.write(e)
    # st.title('# 延庆区气象局风速数据统计分析')
    # st.subheader('**图表说明：**')
    # st.write("""
    #     - 实时数据统计
    #     - 联系：81195317
    #         """)
    # #增加进度条
   

    # draw_elements(d,e)


     
def station():
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    
    # Plot the data
    st.plotly_chart(fig)
       
def Line():
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    st.plotly_chart(fig)
   
def alert():
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    st.plotly_chart(fig)
    
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
# def station():       
#     df = px.data.gapminder()
    
#     fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
#               size="pop", color="continent",
#                      hover_name="country", log_x=True, size_max=60)
#     # Plot the data
#     st.plotly_chart(fig)
     
# def Scatter():
#     fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    
#     # Plot the data
#     st.plotly_chart(fig)
       
# def Line():
#     df = px.data.stocks()
#     fig = px.line(df, x='date', y="GOOG")
#     st.plotly_chart(fig)
   
# def aggregate_bar():
#     df = px.data.tips()
#     fig = px.histogram(df, x="sex", y="total_bill",
#                  color='smoker', barmode='group',
#                  histfunc='avg',
#                  height=400)
    
#     st.plotly_chart(fig)
   
# def bar_charts():
#     data_canada = px.data.gapminder().query("country == 'Canada'")
#     fig = px.bar(data_canada, x='year', y='pop')

#     st.plotly_chart(fig)
   
# def pie():
#     df = px.data.tips()
#     fig = px.pie(df, values='tip', names='day', color='day',
#                  color_discrete_map={'Thur':'lightcyan',
#                                      'Fri':'cyan',
#                                      'Sat':'royalblue',
#                                      'Sun':'darkblue'})
#     st.plotly_chart(fig)
   
# def pulled_out():    
#     labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
#     values = [4500, 2500, 1053, 500]
    
#     # pull is given as a fraction of the pie radius
#     fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.2, 0, 0])])   
#     st.plotly_chart(fig)

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

    
if __name__ == "__main__":
    main()  
