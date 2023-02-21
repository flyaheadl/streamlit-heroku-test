# from pyecharts.charts import Bar
# from pyecharts.faker import Faker
# import streamlit_echarts
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType
# import streamlit as st

# st.title('股票查询系统')
# bar = Bar()
# bar.add_xaxis(Faker.choose())
# bar.add_yaxis('',Faker.values())

# streamlit_echarts.st_pyecharts(
#     bar,
#     theme=ThemeType.DARK
# )

import streamlit as st
import numpy as np
import pandas as pd
import time
st.title('我的第一个MLweb')

st.write("尝试运用dataframe弄一个表格")
df = pd.DataFrame({
    '第一列':[1,2,3,4],
    '第二列':['a','b','c','d']})
st.table(df)
st.write("尝试运用dataframe弄一个表格---write函数")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
 
st.line_chart(chart_data)