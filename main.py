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
#import datetime as dt
import datetime as dt
from pytrends.request import TrendReq
pytrend = TrendReq()
pd.set_option('display.max_columns', 100)
import time
import plotly.graph_objects as go

import os
import base64


categories = pd.read_csv(r'C:\Users\Alex\Desktop\python\Streamlit\pytrends_categories.csv') 


startTime = time.time()
pytrend = TrendReq(hl='en-CA', tz=360)

geo_code =  [
['Canada', 'CA'],
['Andorra', 'AN'],
['United Arab Emirates', 'AE'],
['Afghanistan', 'AF'],
['Antigua and Barbuda', 'AC'],
['Anguilla', 'AV'],
['Albania', 'AL'],
['Armenia', 'AM'],
['Angola', 'AO'],
['Antarctica', 'AY'],
['Argentina', 'AR'],
['American Samoa', 'AQ'],
['Austria', 'AU'],
['Australia', 'AS'],
['Aruba', 'AA'],
['Azerbaijan', 'AJ'],
['Bosnia and Herzegovina', 'BK'],
['Barbados', 'BB'],
['Bangladesh', 'BG'],
['Belgium', 'BE'],
['Burkina Faso', 'UV'],
['Bulgaria', 'BU'],
['Bahrain', 'BA'],
['Burundi', 'BY'],
['Benin', 'BN'],
['Saint Barthalemy', 'TB'],
['Bermuda', 'BD'],
['Brunei', 'BX'],
['Bolivia', 'BL'],
['Brazil', 'BR'],
['Bahamas', 'BF'],
['Bhutan', 'BT'],
['Bouvet Island', 'BV'],
['Botswana', 'BC'],
['Belarus', 'BO'],
['Belize', 'BH'],
['Cocos Islands', 'CK'],
['Democratic Republic of the Congo', 'CG'],
['Central African Republic', 'CT'],
['Republic of the Congo', 'CF'],
['Switzerland', 'SZ'],
['Ivory Coast', 'IV'],
['Cook Islands', 'CW'],
['Chile', 'CI'],
['Cameroon', 'CM'],
['China', 'CH'],
['Colombia', 'CO'],
['Costa Rica', 'CS'],
['Cuba', 'CU'],
['Cape Verde', 'CV'],
['Curacao', 'UC'],
['Christmas Island', 'KT'],
['Cyprus', 'CY'],
['Czech Republic', 'EZ'],
['Germany', 'GM'],
['Djibouti', 'DJ'],
['Denmark', 'DA'],
['Dominica', 'DO'],
['Dominican Republic', 'DR'],
['Algeria', 'AG'],
['Ecuador', 'EC'],
['Estonia', 'EN'],
['Egypt', 'EG'],
['Western Sahara', 'WI'],
['Eritrea', 'ER'],
['Spain', 'SP'],
['Ethiopia', 'ET'],
['Finland', 'FI'],
['Fiji', 'FJ'],
['Falkland Islands', 'FK'],
['Micronesia', 'FM'],
['Faroe Islands', 'FO'],
['France', 'FR'],
['Gabon', 'GB'],
['United Kingdom', 'UK'],
['Grenada', 'GJ'],
['Georgia', 'GG'],
['French Guiana', 'FG'],
['Guernsey', 'GK'],
['Ghana', 'GH'],
['Gibraltar', 'GI'],
['Greenland', 'GL'],
['Gambia', 'GA'],
['Guinea', 'GV'],
['Guadeloupe', 'GP'],
['Equatorial Guinea', 'EK'],
['Greece', 'GR'],
['South Georgia and the South Sandwich Islands', 'SX'],
['Guatemala', 'GT'],
['Guam', 'GQ'],
['Guinea-Bissau', 'PU'],
['Guyana', 'GY'],
['Hong Kong', 'HK'],
['Heard Island and McDonald Islands', 'HM'],
['Honduras', 'HO'],
['Croatia', 'HR'],
['Haiti', 'HA'],
['Hungary', 'HU'],
['Indonesia', 'ID'],
['Ireland', 'EI'],
['Israel', 'IS'],
['Isle of Man', 'IM'],
['India', 'IN'],
['British Indian Ocean Territory', 'IO'],
['Iraq', 'IZ'],
['Iran', 'IR'],
['Iceland', 'IC'],
['Italy', 'IT'],
['Jersey', 'JE'],
['Jamaica', 'JM'],
['Jordan', 'JO'],
['Japan', 'JA'],
['Kenya', 'KE'],
['Kyrgyzstan', 'KG'],
['Cambodia', 'CB'],
['Kiribati', 'KR'],
['Comoros', 'CN'],
['Saint Kitts and Nevis', 'SC'],
['North Korea', 'KN'],
['South Korea', 'KS'],
['Kosovo', 'KV'],
['Kuwait', 'KU'],
['Cayman Islands', 'CJ'],
['Kazakhstan', 'KZ'],
['Laos', 'LA'],
['Lebanon', 'LE'],
['Saint Lucia', 'ST'],
['Liechtenstein', 'LS'],
['Sri Lanka', 'CE'],
['Liberia', 'LI'],
['Lesotho', 'LT'],
['Lithuania', 'LH'],
['Luxembourg', 'LU'],
['Latvia', 'LG'],
['Libya', 'LY'],
['Morocco', 'MO'],
['Monaco', 'MN'],
['Moldova', 'MD'],
['Montenegro', 'MJ'],
['Saint Martin', 'RN'],
['Madagascar', 'MA'],
['Marshall Islands', 'RM'],
['Macedonia', 'MK'],
['Mali', 'ML'],
['Myanmar', 'BM'],
['Mongolia', 'MG'],
['Macao', 'MC'],
['Northern Mariana Islands', 'CQ'],
['Martinique', 'MB'],
['Mauritania', 'MR'],
['Montserrat', 'MH'],
['Malta', 'MT'],
['Mauritius', 'MP'],
['Maldives', 'MV'],
['Malawi', 'MI'],
['Mexico', 'MX'],
['Malaysia', 'MY'],
['Mozambique', 'MZ'],
['Namibia', 'WA'],
['New Caledonia', 'NC'],
['Niger', 'NG'],
['Norfolk Island', 'NF'],
['Nigeria', 'NI'],
['Nicaragua', 'NU'],
['Netherlands', 'NL'],
['Norway', 'NO'],
['Nepal', 'NP'],
['Nauru', 'NR'],
['Niue', 'NE'],
['New Zealand', 'NZ'],
['Oman', 'MU'],
['Panama', 'PM'],
['Peru', 'PE'],
['French Polynesia', 'FP'],
['Papua New Guinea', 'PP'],
['Philippines', 'RP'],
['Pakistan', 'PK'],
['Poland', 'PL'],
['Saint Pierre and Miquelon', 'SB'],
['Pitcairn', 'PC'],
['Puerto Rico', 'RQ'],
['Palestinian Territory', 'WE'],
['Portugal', 'PO'],
['Palau', 'PS'],
['Paraguay', 'PA'],
['Qatar', 'QA'],
['Reunion', 'RE'],
['Romania', 'RO'],
['Serbia', 'RI'],
['Russia', 'RS'],
['Rwanda', 'RW'],
['Saudi Arabia', 'SA'],
['Solomon Islands', 'BP'],
['Seychelles', 'SE'],
['Sudan', 'SU'],
['South Sudan', 'OD'],
['Sweden', 'SW'],
['Singapore', 'SN'],
['Saint Helena', 'SH'],
['Slovenia', 'SI'],
['Svalbard and Jan Mayen', 'SV'],
['Slovakia', 'LO'],
['Sierra Leone', 'SL'],
['San Marino', 'SM'],
['Senegal', 'SG'],
['Somalia', 'SO'],
['Suriname', 'NS'],
['Sao Tome and Principe', 'TP'],
['El Salvador', 'ES'],
['Sint Maarten', 'NN'],
['Syria', 'SY'],
['Swaziland', 'WZ'],
['Turks and Caicos Islands', 'TK'],
['Chad', 'CD'],
['French Southern Territories', 'FS'],
['Togo', 'TO'],
['Thailand', 'TH'],
['Tajikistan', 'TI'],
['Tokelau', 'TL'],
['East Timor', 'TT'],
['Turkmenistan', 'TX'],
['Tunisia', 'TS'],
['Tonga', 'TN'],
['Turkey', 'TU'],
['Trinidad and Tobago', 'TD'],
['Tuvalu', 'TV'],
['Taiwan', 'TW'],
['Tanzania', 'TZ'],
['Ukraine', 'UP'],
['Uganda', 'UG'],
['United States', 'US'],
['Uruguay', 'UY'],
['Uzbekistan', 'UZ'],
['Vatican', 'VT'],
['Saint Vincent and the Grenadines', 'VC'],
['Venezuela', 'VE'],
['British Virgin Islands', 'VI'],
['U.S. Virgin Islands', 'VQ'],
['Vietnam', 'VM'],
['Vanuatu', 'NH'],
['Wallis and Futuna', 'WF'],
['Samoa', 'WS'],
['Yemen', 'YM'],
['Mayotte', 'MF'],
['South Africa', 'SF'],
['Zambia', 'ZA'],
['Zimbabwe', 'ZI'],
['Serbia and Montenegro', 'YI'],
['Netherlands Antilles', 'NT']
]
geo_code = pd.DataFrame(geo_code)
geo_code.columns = ['Long', 'Short']

competitive_set_recomended = pd.DataFrame({
        'Nintendo': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega'],
        'Destination Canada': ['Canada', 'United States', 'Mexico','Australia','New Zealand','United Kingdom'],
        'Travel Alberta': ['Alberta', 'Destination Canada','Travel Ontario','New Zealand','France','Germany'],
        'RBC': ['RBC', 'CIBC','BMO','TD','Scotia Bank','Bank of America'],
        'CBC': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega'],
        'Keurig': ['Keurig','Coffeemate','Nesspresso','Xbox','Stadia','Sega'],
        'Amazon Prime Video': ['Amazon Prime Video', 'Crave','Hulu','Disney Plus','Rogers','Netflix'],
        'Ministry of Finance': ['Nintendo', 'Blizzard Activision','Sony PlayStation','Xbox','Stadia','Sega']
    })


st.set_page_config(layout="wide")
col1, col2 = st.beta_columns(2)



st.sidebar.header("Select your Criteria")  
option = st.sidebar.selectbox(
    'Search from a curated Competititve Set',
     list(competitive_set_recomended.columns))


placeholder_startdate = dt.date.today() - dt.timedelta(30)
placeholder_end_date = dt.date.today() - dt.timedelta(1)

sidebar_col1, sidebar_col2 = st.sidebar.beta_columns(2)
#start_date = st.sidebar.date_input('Start Date')
#end_date = st.sidebar.date_input('End Date')
start_date = sidebar_col1.date_input('Start Date',
                                     placeholder_startdate)
end_date = sidebar_col2.date_input('End Date',
                                     placeholder_end_date)
date_range = str(start_date) + ' ' + str(end_date)

option2 = st.sidebar.selectbox('Select a category', categories['Categories'])

#st_categories = int(str(categories.loc[categories['Categories'] == st_categories,'ID'].unique))
option2 = categories.loc[categories['Categories'] == option2,'ID'].iloc[0]




option3 = st.sidebar.selectbox('Select a Geography', geo_code['Long'])

#st_categories = int(str(categories.loc[categories['Categories'] == st_categories,'ID'].unique))
option3 = geo_code.loc[geo_code['Long'] == option3,'Short'].iloc[0]








#https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable
# Defining my own encoder to sovle JSON serialization issue when for selecting categories
import json
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

option2 = json.dumps(option2, cls=NpEncoder)






competitive_set = list(competitive_set_recomended.loc[:,option])

result_cols = list(competitive_set_recomended.columns)


multiselect_option = st.multiselect('Select Competitors', 
                                            competitive_set,
                                            competitive_set)





dataset = []

for x in range(0,len(multiselect_option)):
    keywords = [multiselect_option[x]]
    pytrend.build_payload(
    kw_list=keywords,
    #Select Category
    #https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
    cat=option2,
    timeframe=date_range, 
    geo=option3)
    data = pytrend.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'],axis='columns')
        dataset.append(data)


result = pd.concat(dataset, axis=1)


executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))


print(competitive_set)



result_csv = result.to_excel('search_trends.xlsx')



col1.header(f"{option}: Interest Overtime prices for {result.index[0].strftime('%B %Y')} - " \
          +                f"{result.index[-1].strftime('%B %Y')}")

col2.image("https://www.amire.com.au/wp-content/uploads/2020/11/1_Fi6masemXJT3Q8YWekQCDQ.png", width=135,)




#import plotly.graph_objects as go

# instantiate the figure object
fig = go.Figure(
    layout=go.Layout(
        height=1000,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
)



fig.update_xaxes(showline=True, linewidth=2, linecolor='LightGrey')
fig.update_yaxes(showline=True, linewidth=2, linecolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

# add a scatter trace for every column
for col in result.columns:
    fig.add_scatter(x=result.index, y=result[col], name=col)

# change the scale to logarithmic and add title
fig.update_layout(
    uniformtext_minsize=20
    #yaxis=dict(type="log"),
)



st.plotly_chart(fig, use_container_width=True)
#st.altair_chart(line, use_container_width=True)


# import os
# import base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


st.markdown(get_binary_file_downloader_html('search_trends.xlsx', 'Data to Excel'), unsafe_allow_html=True)
if st.checkbox('Show me the Data'):
    st.write(result)







