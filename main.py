# cd python
# cd Streamlit
# --> C:\Users\Alex\Desktop\python\Streamlit>
# conda activate
# 
# streamlit run main.py


import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
# import numpy as np
import pandas as pd
import numpy as np

from pytrends.request import TrendReq
pytrend = TrendReq()
pd.set_option('display.max_columns', 100)
import time

# from google.colab import auth
# auth.authenticate_user()

# import gspread
# from oauth2client.client import GoogleCredentials

# from gspread_dataframe import set_with_dataframe




df = pd.DataFrame({'first column': [1, 2, 3, 4],
                   'second column': [10, 20, 30, 40]})




startTime = time.time()
pytrend = TrendReq(hl='en-CA', tz=360)



competitive_set_recomended = pd.DataFrame({
        'Nintendo': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega'],
        'Canada': ['Canada', 'United States', 'Mexico','Australia','New Zealand','United Kingdom'],
        'Alberta': ['Alberta', 'Destination Canada','Travel Ontario','New Zealand','France','Germany'],
        'RBC': ['RBC', 'CIBC','BMO','TD','Scotia Bank','Bank of America'],
        'CBC': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega'],
        'Keurig': ['Keurig','Coffeemate','Nesspresso','Xbox','Stadia','Sega'],
        'Amazon Prime Video': ['Amazon Prime Video', 'Crave','Hulu','Disney Plus','Rogers','Netflix'],
        'Ministry of Finance': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega']
    })

#df = pd.DataFrame(competitive_set)

st.sidebar.header("Select your Criteria")  
option = st.sidebar.selectbox(
    'Search from a curated Competititve Set',
     list(competitive_set_recomended.columns))

start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')
date_range = str(start_date) + ' ' + str(end_date)

st.image("https://www.amire.com.au/wp-content/uploads/2020/11/1_Fi6masemXJT3Q8YWekQCDQ.png", width=135,)
# st.header('Google Trends: Interest Overtime')
st.header(option + ': Interest Overtime')

# if option == 'Nintendo':
#   st.subheader(option)

competitive_set = list(competitive_set_recomended.loc[:,option])



dataset = []

for x in range(0,len(competitive_set)):
    keywords = [competitive_set[x]]
    pytrend.build_payload(
    kw_list=keywords,
    #Select Category
    #https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
    cat=41,
    timeframe=date_range,
    geo='CA')
    data = pytrend.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'],axis='columns')
        dataset.append(data)


result = pd.concat(dataset, axis=1)


executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))


print(competitive_set)


import os
import base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

result_csv = result.to_excel('search_trends.xlsx')
# result2 = result.loc[:, option]
# st.line_chart(result2)
st.line_chart(result)
st.markdown(get_binary_file_downloader_html('search_trends.xlsx', 'Data to Excel'), unsafe_allow_html=True)
if st.checkbox('Show me the Data'):
    
    st.write(result)

import altair as alt


np.random.seed(42)
source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                    columns=['A', 'B', 'C'], index=pd.RangeIndex(100, name='x'))
source = source.reset_index().melt('x', var_name='category', value_name='y')

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['x'], empty='none')

# The basic line
line = alt.Chart(source).mark_line(interpolate='basis').encode(
    x='x:Q',
    y='y:Q',
    color='category:N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart(source).mark_point().encode(
    x='x:Q',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'y:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x='x:Q',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
alt.layer(
    line, selectors, points, rules, text
).properties(
    width=1500, height=500
)


st.altair_chart(line)


# linedata = pd.DataFrame([
#     recept_list[1000:cycles],,
#     toneset[1000:cycles],
#     horizontal,
# ]).T.rename(columns={0:'a', 1:'b', 2:'c'})

# series = pd.DataFrame({
#   'year': ['2010', '2011', '2012', '2013','2010', '2011', '2012', '2013'],
#   'animal': ['antelope', 'antelope', 'antelope', 'antelope', 'velociraptor', 'velociraptor', 'velociraptor', 'velociraptor',],
#   'count': [8, 6, 3, 1, 2, 4, 5, 5]
# })

# # Basic Altair line chart where it picks automatically the colors for the lines
# basic_chart = alt.Chart(series).mark_line().encode(
#     x='year',
#     y='count',
#     color='animal',
#     # legend=alt.Legend(title='Animals by year')
# )

# # Custom Altair line chart where you set color and specify dimensions
# custom_chart = alt.Chart(series).mark_line().encode(
#     x='year',
#     y='count',
#     color=alt.Color('animal',
#             scale=alt.Scale(
#                 domain=['antelope', 'velociraptor'],
#                 range=['blue', 'red'])
#                 )
# ).properties(
#     width=900,
#     height=500
# )

# st.altair_chart(basic_chart)
# st.altair_chart(custom_chart)





















# import plotly.graph_objects as go

# import matplotlib.pyplot as plt

 
# z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
# z = z_data.values
# sh_0, sh_1 = z.shape
# x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
# fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
# fig.update_layout(title='IRR', autosize=False,
#                   width=800, height=800,
#                   margin=dict(l=40, r=40, b=40, t=40))
# st.plotly_chart(fig)

# Initialize the figure style
##df = result

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
 
# # Make a data frame
# df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })
 
# # Initialize the figure style
# plt.style.use('seaborn-darkgrid')
 
# # create a color palette
# palette = plt.get_cmap('Set1')
 
# # multiple line plot
# num=0
# for column in df.drop('x', axis=1):
#     num+=1
 
#     # Find the right spot on the plot
#     plt.subplot(3,3, num)
 
#     # plot every group, but discrete
#     for v in df.drop('x', axis=1):
#         plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
 
#     # Plot the lineplot
#     plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)
 
#     # Same limits for every chart
#     plt.xlim(0,10)
#     plt.ylim(-2,22)
 
#     # Not ticks everywhere
#     if num in range(7) :
#         plt.tick_params(labelbottom='off')
#     if num not in [1,4,7] :
#         plt.tick_params(labelleft='off')
 
#     # Add title
#     plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )

# # general title
# plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)
 
# # Axis titles
# plt.text(0.5, 0.02, 'Time', ha='center', va='center')
# plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

# # Show the graph
# st.plotly_chart(plt)


