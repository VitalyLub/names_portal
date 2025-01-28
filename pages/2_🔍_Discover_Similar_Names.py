import streamlit as st
import pandas as pd
import numpy as np
import math
from random import shuffle
import time

df_boys = pd.read_csv("boys.csv")
df_girls = pd.read_csv("girls.csv")

df_boys['is_increasing_name'] = pd.to_numeric(df_boys['is_increasing_name'])
df_boys['is_timeless_name'] = pd.to_numeric(df_boys['is_timeless_name'])
df_boys['if_jew_boys_muslim_boys_common'] = pd.to_numeric(df_boys['if_jew_boys_muslim_boys_common'])
df_boys['if_jew_boys_jew_girls'] = pd.to_numeric(df_boys['if_jew_boys_jew_girls'])
df_boys['is_common_name'] = pd.to_numeric(df_boys['is_common_name'])

df_boys['international_score'] = pd.to_numeric(df_boys['international_score'])
df_boys['international_score'] = np.where(df_boys['international_score'] >= 0.8, 1, 0)

df_boys['bible_score'] = np.where(df_boys['bible_score'] == 'error', 0, df_boys['bible_score'])
df_boys['bible_score'] = pd.to_numeric(df_boys['bible_score'])
df_boys['bible_score'] = np.where(df_boys['bible_score'] >= 0.8, 1, 0)

df_boys['nature_score'] = np.where(df_boys['nature_score'] == 'error', 0, df_boys['nature_score'])
df_boys['nature_score'] = pd.to_numeric(df_boys['nature_score'])
df_boys['nature_score'] = np.where(df_boys['nature_score'] >= 0.8, 1, 0)

df_boys['art_score'] = np.where(df_boys['art_score'] == 'error', 0, df_boys['art_score'])
df_boys['art_score'] = pd.to_numeric(df_boys['art_score'])
df_boys['art_score'] = np.where(df_boys['art_score'] >= 0.8, 1, 0)

df_boys['syllabels_score'] = pd.to_numeric(df_boys['syllabels_score'])
df_boys['short_name'] = np.where(df_boys['syllabels_score'] == 1, 1, 0)
df_boys['med_name'] = np.where((df_boys['syllabels_score'] == 2) | (df_boys['syllabels_score'] == 3), 1, 0)
df_boys['long_name'] = np.where((df_boys['syllabels_score'] < 1) | (df_boys['syllabels_score'] > 3), 1, 0)


df_boys['light_score'] = np.where(df_boys['light_score'] == 'error', 0, df_boys['light_score'])
df_boys['light_score'] = pd.to_numeric(df_boys['light_score'])
df_boys['light_score'] = np.where(df_boys['light_score'] >= 0.8, 1, 0)

df_boys['summer_score'] = np.where(df_boys['summer_score'] == 'error', 0, df_boys['summer_score'])
df_boys['summer_score'] = pd.to_numeric(df_boys['summer_score'])
df_boys['summer_score'] = np.where(df_boys['summer_score'] >= 0.8, 1, 0)

df_boys['winter_score'] = np.where(df_boys['winter_score'] == 'error', 0, df_boys['winter_score'])
df_boys['winter_score'] = pd.to_numeric(df_boys['winter_score'])
df_boys['winter_score'] = np.where(df_boys['winter_score'] >= 0.8, 1, 0)

df_boys['spring_score'] = np.where(df_boys['spring_score'] == 'error', 0, df_boys['spring_score'])
df_boys['spring_score'] = pd.to_numeric(df_boys['spring_score'])
df_boys['spring_score'] = np.where(df_boys['spring_score'] >= 0.8, 1, 0)

df_boys['autumn_score'] = np.where(df_boys['autumn_score'] == 'autumn_score', 0, df_boys['autumn_score'])
df_boys['autumn_score'] = pd.to_numeric(df_boys['autumn_score'])
df_boys['autumn_score'] = np.where(df_boys['autumn_score'] >= 0.8, 1, 0)
            


df_girls['is_increasing_name'] = pd.to_numeric(df_girls['is_increasing_name'])
df_girls['is_timeless_name'] = pd.to_numeric(df_girls['is_timeless_name'])
df_girls['if_jew_girls_muslim_girls_common'] = pd.to_numeric(df_girls['if_jew_girls_muslim_girls_common'])
df_girls['if_jew_boys_jew_girls'] = pd.to_numeric(df_girls['if_jew_boys_jew_girls'])
df_girls['is_common_name'] = pd.to_numeric(df_girls['is_common_name'])

df_girls['international_score'] = pd.to_numeric(df_girls['international_score'])
df_girls['international_score'] = np.where(df_girls['international_score'] >= 0.8, 1, 0)

df_girls['bible_score'] = np.where(df_girls['bible_score'] == 'error', 0, df_girls['bible_score'])
df_girls['bible_score'] = pd.to_numeric(df_girls['bible_score'])
df_girls['bible_score'] = np.where(df_girls['bible_score'] >= 0.8, 1, 0)

df_girls['nature_score'] = np.where(df_girls['nature_score'] == 'error', 0, df_girls['nature_score'])
df_girls['nature_score'] = pd.to_numeric(df_girls['nature_score'])
df_girls['nature_score'] = np.where(df_girls['nature_score'] >= 0.8, 1, 0)

df_girls['art_score'] = np.where(df_girls['art_score'] == 'error', 0, df_girls['art_score'])
df_girls['art_score'] = pd.to_numeric(df_girls['art_score'])
df_girls['art_score'] = np.where(df_girls['art_score'] >= 0.8, 1, 0)

df_girls['syllabels_score'] = pd.to_numeric(df_girls['syllabels_score'])
df_girls['short_name'] = np.where(df_girls['syllabels_score'] == 1, 1, 0)
df_girls['med_name'] = np.where((df_girls['syllabels_score'] == 2) | (df_girls['syllabels_score'] == 3), 1, 0)
df_girls['long_name'] = np.where((df_girls['syllabels_score'] < 1) | (df_girls['syllabels_score'] > 3), 1, 0)

df_girls['light_score'] = np.where(df_girls['light_score'] == 'error', 0, df_girls['light_score'])
df_girls['light_score'] = pd.to_numeric(df_girls['light_score'])
df_girls['light_score'] = np.where(df_girls['light_score'] >= 0.8, 1, 0)

df_girls['summer_score'] = np.where(df_girls['summer_score'] == 'error', 0, df_girls['summer_score'])
df_girls['summer_score'] = pd.to_numeric(df_girls['summer_score'])
df_girls['summer_score'] = np.where(df_girls['summer_score'] >= 0.8, 1, 0)

df_girls['winter_score'] = np.where(df_girls['winter_score'] == 'error', 0, df_girls['winter_score'])
df_girls['winter_score'] = pd.to_numeric(df_girls['winter_score'])
df_girls['winter_score'] = np.where(df_girls['winter_score'] >= 0.8, 1, 0)

df_girls['spring_score'] = np.where(df_girls['spring_score'] == 'error', 0, df_girls['spring_score'])
df_girls['spring_score'] = pd.to_numeric(df_girls['spring_score'])
df_girls['spring_score'] = np.where(df_girls['spring_score'] >= 0.8, 1, 0)

df_girls['autumn_score'] = np.where(df_girls['autumn_score'] == 'autumn_score', 0, df_girls['autumn_score'])
df_girls['autumn_score'] = pd.to_numeric(df_girls['autumn_score'])
df_girls['autumn_score'] = np.where(df_girls['autumn_score'] >= 0.8, 1, 0)

df_boys = df_boys.rename(columns={'if_jew_boys_muslim_boys_common': 'is_common_muslim', 'if_jew_boys_jew_girls': 'is_shared_boys_girls', '1948-2023':'population'})
df_girls = df_girls.rename(columns={'if_jew_girls_muslim_girls_common': 'is_common_muslim', 'if_jew_boys_jew_girls': 'is_shared_boys_girls', '1948-2023':'population'})

df_boys = df_boys.rename(columns={'international_score': 'is_international_name'})
df_girls = df_girls.rename(columns={'international_score': 'is_international_name'})

df_boys = df_boys.rename(columns={'bible_score': 'is_bible_name'})
df_girls = df_girls.rename(columns={'bible_score': 'is_bible_name'})

df_boys = df_boys.rename(columns={'nature_score': 'is_nature_name'})
df_girls = df_girls.rename(columns={'nature_score': 'is_nature_name'})

df_boys = df_boys.rename(columns={'art_score': 'is_art_name'})
df_girls = df_girls.rename(columns={'art_score': 'is_art_name'})

df_boys = df_boys.rename(columns={'light_score': 'is_light_name'})
df_girls = df_girls.rename(columns={'light_score': 'is_light_name'})
       
df_boys = df_boys.rename(columns={'summer_score': 'is_summer_name'})
df_girls = df_girls.rename(columns={'summer_score': 'is_summer_name'})

df_boys = df_boys.rename(columns={'winter_score': 'is_winter_name'})
df_girls = df_girls.rename(columns={'winter_score': 'is_winter_name'})

df_boys = df_boys.rename(columns={'spring_score': 'is_spring_name'})
df_girls = df_girls.rename(columns={'spring_score': 'is_spring_name'})

df_boys = df_boys.rename(columns={'autumn_score': 'is_autumn_name'})
df_girls = df_girls.rename(columns={'autumn_score': 'is_autumn_name'})


data = df_boys

# Page Configuration
st.set_page_config(page_title="פורטל שמות", layout="centered", page_icon="📈")

st.markdown(
    """
    <style>
    .rtl {
        direction: rtl; /* Right-to-Left text direction */
        text-align: right; /* Align text to the right */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .rtl-text {
        direction: rtl; /* Right-to-Left text direction */
        text-align: right; /* Align text to the right */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    div[data-testid="stRadio"] {
        direction: rtl; /* Change text direction to Right-to-Left */
        text-align: right; /* Align labels to the right */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center; /* Center-align text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .center-button {
        display: flex;
        justify-content: center; /* Center horizontally */
        margin-top: 20px; /* Add space above */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown('<h1 class="centered-title">👶 שם לפי שם 👧</h1>', unsafe_allow_html=True)


BOY_MSG = "👶 בן"
GIRL_MSG = "👧 בת"

# # Initialize session state to track selected option
# st.session_state.selected_option = GIRL_MSG

# left, right = st.columns(2)
# if left.button("בן", icon="👶", use_container_width=True):
#     st.session_state.selected_option = BOY_MSG
# if right.button("בת", icon="👧", use_container_width=True):
#     st.session_state.selected_option = GIRL_MSG

if 'selected_option' not in st.session_state:
    st.session_state.selected_option = "👧 בת"  # Default to 'GIRL_MSG'

# Button for selecting 'Boy' or 'Girl'
BOY_MSG = "👶 בן"
GIRL_MSG = "👧 בת"

left, right = st.columns(2)
if left.button("בן", icon="👶", use_container_width=True):
    st.session_state.selected_option = BOY_MSG
if right.button("בת", icon="👧", use_container_width=True):
    st.session_state.selected_option = GIRL_MSG

# Displa

if st.session_state.selected_option:
    st.markdown(f'<div class="rtl-text"><h5>מציג תוצאות עבור: {st.session_state.selected_option}🎉</h5></div>', unsafe_allow_html=True)
    if st.session_state.selected_option == GIRL_MSG:
        data = df_girls
    elif st.session_state.selected_option == BOY_MSG:
        data = df_boys
else:
    st.write("Please select an option.")

data = data[['name',
             'population',
             'is_increasing_name',
             'is_timeless_name',
             'is_common_muslim',
             'is_shared_boys_girls',
             'is_common_name',
             'is_international_name',
             'is_bible_name',
             'is_nature_name',
             'is_art_name',
             'is_light_name',
             'syllabels_score',
             'short_name',
             'med_name',
             'long_name',
             'is_summer_name',
             'is_spring_name',
             'is_winter_name',
             'is_autumn_name']]



all_names = data['name'].unique().tolist()


st.markdown(
    """
    <style>
    /* Make the selectbox dropdown content RTL */
    div[data-baseweb="select"] {
        direction: rtl; /* Makes the dropdown text RTL */
        text-align: right; /* Aligns dropdown text to the right */
    }

    /* Center and make the selectbox label RTL */
    .stSelectbox > label {
        text-align: center; /* Center the label text */
        direction: rtl; /* Make the label text RTL */
        display: block; /* Ensures proper layout for centering */
        font-weight: bold; /* Optional: Make it bold */
        font-size: 16px; /* Optional: Adjust font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# The selectbox with its label
selected_name = st.selectbox('בחרו שם:', options=all_names, index=all_names.index('יובל'))


name_the_user_wanted = data[data['name'] == selected_name]

data['score'] = 0
data['score'] += abs(name_the_user_wanted['is_increasing_name'].tolist()[0] - data['is_increasing_name'])
data['score'] += abs(name_the_user_wanted['is_timeless_name'].tolist()[0] - data['is_timeless_name'])
data['score'] += abs(name_the_user_wanted['is_common_muslim'].tolist()[0] - data['is_common_muslim'])
data['score'] += abs(name_the_user_wanted['is_shared_boys_girls'].tolist()[0] - data['is_shared_boys_girls'])
data['score'] += abs(name_the_user_wanted['is_common_name'].tolist()[0] - data['is_common_name'])
data['score'] += abs(name_the_user_wanted['is_international_name'].tolist()[0] - data['is_international_name'])
data['score'] += abs(name_the_user_wanted['is_bible_name'].tolist()[0] - data['is_bible_name'])
data['score'] += abs(name_the_user_wanted['is_nature_name'].tolist()[0] - data['is_nature_name'])
data['score'] += abs(name_the_user_wanted['is_art_name'].tolist()[0] - data['is_art_name'])
data['score'] += abs(name_the_user_wanted['is_light_name'].tolist()[0] - data['is_light_name'])
data['score'] += abs(name_the_user_wanted['is_summer_name'].tolist()[0] - data['is_summer_name'])
data['score'] += abs(name_the_user_wanted['is_autumn_name'].tolist()[0] - data['is_autumn_name'])
data['score'] += abs(name_the_user_wanted['is_spring_name'].tolist()[0] - data['is_spring_name'])
data['score'] += abs(name_the_user_wanted['is_winter_name'].tolist()[0] - data['is_winter_name'])
data['score'] += abs(name_the_user_wanted['syllabels_score'].tolist()[0] - data['syllabels_score'])


data['pop_delta'] = abs(name_the_user_wanted['population'].tolist()[0] - data['population'])

sorted_data = data.sort_values(by=['score', 'pop_delta'], ascending=[True, True])
sorted_data = sorted_data[sorted_data['name'] != selected_name]
sorted_data = sorted_data[sorted_data['population'] >= 100]
sorted_data = sorted_data[:20]

names_to_show = sorted_data['name'].tolist()

for name in names_to_show:
    st.markdown('<div class="rtl-text">' + "- " + name + '</div>', unsafe_allow_html=True)
    time.sleep(0.01)

#st.dataframe(sorted_data, hide_index=True)
