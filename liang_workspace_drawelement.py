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

def draw_elements(starttime,endtime,element):       
    dic_ele={'阵风':['http://10.224.97.125/ldad/tcsj/listNewAWSFTJData.action','延庆风力分布图'],
             '降水':['http://10.224.97.125/ldad/tcsj/listNewAWSRAINTJData.action','延庆降水分布图'],
             '气温':['http://10.224.97.125/ldad/tcsj/listNewAWSWDTJData.action','延庆气温分布图']
    }
    
    url = dic_ele[element][0]
    req_dict = {'siteTypeCode': '',
    'areaCode': 'yq',
    'province': 'bjs',
    'startTime': starttime,
    'endTime':  endtime,
    'country': '',
    'showDataType': 'tongjibiao'}
    import requests
    rep = requests.post(url,data=req_dict)
    import json
    rep_dict = json.loads(rep.text)[ 'data']['resultJson']
    
    wind_df = pd.DataFrame(json.loads(rep_dict)).set_index([ 'stationName'])
    st_df= pd.read_excel(r'E:\工作\Python程序\Python Study亮\11、获取网站数据生成延庆区实况图\延庆\自动站数据.xls',index_col='stationName')
    wind_df['Ex_WD']=pd.to_numeric(wind_df['Ex_WD'])#将A列数据类型转换为数字
    wind_df['Ex_WS']=pd.to_numeric(wind_df['Ex_WS'])#将A列数据类型转换为数字
    #print(wind_df.dtypes)
    new_df = pd.concat([wind_df[['Ex_WD','Ex_WS']],st_df],axis=1)[['Ex_WD','Ex_WS','经度','纬度']].dropna(axis=0,how='any')
    def shp2clip(originfig, ax, shpfile):
        sf = shapefile.Reader(shpfile, encoding='utf-8')#ansi
        shape_rec = sf.shapeRecords()[0]
        vertices = []
        codes = []
        pts = shape_rec.shape.points
        prt = list(shape_rec.shape.parts) + [len(pts)]
        for i in range(len(prt) - 1):
            for j in range(prt[i], prt[i + 1]):
                vertices.append((pts[j][0], pts[j][1]))
            codes += [Path.MOVETO]
            codes += [Path.LINETO] * (prt[i + 1] - prt[i] - 2)
            codes += [Path.CLOSEPOLY]
        clip = Path(vertices, codes)
        clip = PathPatch(clip, transform=ax.transData)
        for contour in originfig.collections:
            contour.set_clip_path(clip)
        return clip
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''数据源会变，因为爬出来的数据不一样'''
    
    new_df['Ex_WD'] = pd.to_numeric(new_df['Ex_WD'], downcast = 'integer')
    new_df['Ex_WS'] = pd.to_numeric(new_df['Ex_WS'], downcast = 'integer')
    new_df['u']=list(map(lambda x,y: -x*math.sin(y), new_df['Ex_WS'], new_df['Ex_WD']))
    new_df['v']=list(map(lambda x,y: -x*math.cos(y), new_df['Ex_WS'], new_df['Ex_WD']))
    
    wind = new_df['Ex_WS']
    
    olon = np.linspace(115.7, 116.65, 52)
    olat = np.linspace(40.25, 40.8, 40)
    olon, olat = np.meshgrid(olon, olat)
    
    lon = new_df['经度']
    lat = new_df['纬度']
    
    func = Rbf(lon, lat, wind, function='linear')#径向基函数
    wind_data_new = func(olon, olat)#格点数据
    
    # 画布及绘图声明
    fig = plt.figure(figsize=(16, 9.6), dpi=300, facecolor='#666666', edgecolor='Blue', frameon=False)  # 画布
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())  # 绘图区
    
    '''自定义的颜色列表和色阶会变,可用字典解决'''
    
    clevs = [0.3,1.6,3.4,5.5,8.0,10.8,13.9,17.2,20.8,24.5,28.5]  # 自定义颜色列表
    
    cdict = ['#b9f6fd', '#a9dcf9', '#71b0fd', '#91fbd7', '#8ffeb6',
              '#f4fd8f', '#feac4b', '#ff0000', '#d80000', '#a80000', '#860000']  # 自定义颜色列表 '#A9F090','#40B73F','#63B7FF','#0000FE','#FF00FC','#850042'
    my_cmap = colors.ListedColormap(cdict)  # 自定义颜色映射 color-map
    norm = mpl.colors.BoundaryNorm(clevs, my_cmap.N)  # 基于离散区间生成颜色映射索引
    #  绘制等值线、等值线填色
    
    cf = ax.contourf(olon, olat, wind_data_new, clevs, transform=ccrs.PlateCarree(), cmap=my_cmap, norm=norm,extend='both')
    
    '''标题会变，可用字典解决'''
    ax.set_title('延庆区极大风分布图\n时间：'+starttime+'-'+endtime, fontsize=25, color='r')
    
    position = fig.add_axes([0.82, 0.13, 0.05, 0.4])  # 位置【左，下，宽。高】
    cb = plt.colorbar(cf, cax=position)  # 颜色参照表
    
    '''显示的图例标注会变，可用字典解决'''
    
    cb.set_ticks([0.95,2.5,4.45,6.75,9.4,12.35,15.55,19,22.65,26.5])
    cb.set_ticklabels(['2级','3级','4级','5级','6级','7级','8级','9级','10级','11级'])
    
    ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=True))
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.set_xticks(np.arange(115.7, 116.7, 0.1), crs=ccrs.PlateCarree())  # x轴
    ax.set_yticks(np.arange(40.3, 40.9, 0.1), crs=ccrs.PlateCarree())  # y轴
    ax.gridlines()  # 显示背景线
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    '''制作延庆区的乡镇shp'''
    clip = shp2clip(cf, ax, r'E:\工作\Python程序\Python Study亮\G-地图\延庆\延庆.shp')
    #clip = shp2clip(cf, ax, r'E:\工作\Python程序\Python Study亮\G-SHP文件、GIS文件\各种shp文件\4.china_shp_country-李梓铭\shp\北京市.shp')
    #添加行政边界！！！！
    proj= ccrs.PlateCarree()  # 简写投影
    shp_path = r'E:\工作\Python程序\Python Study亮\G-地图\延庆\延庆.shp'
    reader = Reader(shp_path)
    enshicity = cfeat.ShapelyFeature(reader.geometries(), proj, edgecolor='k', facecolor='none')
    ax.add_feature(enshicity, linewidth=0.7)#添加市界细节
    
    new_df['Ex_WS'] = new_df['Ex_WS'].apply(lambda x: str(round(float(x), 1)))
    
    '''填图中的风向杆会变'''
    for i in new_df.index:
        ax.scatter(new_df.loc[i, '经度'], new_df.loc[i, '纬度'], marker='.', s=5, color="k", zorder=3)
        ax.barbs(new_df.loc[i, '经度'], new_df.loc[i, '纬度'],new_df.loc[i, 'u'],new_df.loc[i,'v'],barb_increments={'half':2,'full':4,'flag':20},zorder=5)
        ax.text(new_df.loc[i, '经度'], new_df.loc[i, '纬度'], i, fontsize=10, color="k")
        ax.text(new_df.loc[i, '经度'], new_df.loc[i, '纬度'] - 0.01, new_df.loc[i, 'Ex_WS'], fontsize=10, color="k")
    #加LOGO
    img1=plt.imread(r'E:\工作\Python程序\Python Study亮\11、获取网站数据生成延庆区实况图\延庆气象局logo.jpg')#图片地址
    ax2=fig.add_axes([0.75,0.855,0.15,0.15])#添加存放图片的子图
    ax2.imshow(img1)#显示图片
    ax2.axis('off')#去除框线
    # plt.savefig('1.png')
    # img =Image.open(r'G:\streamlit\1.png')
    # st.image(img)
    # return img
    st.pyplot(fig)
#draw_elements('2022-03-10 08:00','2022-03-11 09:00','阵风')