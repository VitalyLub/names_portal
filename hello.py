import streamlit as st
import pandas as pd
import numpy as np
import math



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

df_boys['syllabels_score'] = np.where(df_boys['syllabels_score'].isin([1, 2]), 1, 0)

df_boys['light_score'] = np.where(df_boys['light_score'] == 'error', 0, df_boys['light_score'])
df_boys['light_score'] = pd.to_numeric(df_boys['light_score'])
df_boys['light_score'] = np.where(df_boys['light_score'] >= 0.8, 1, 0)


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

df_girls['syllabels_score'] = np.where(df_girls['syllabels_score'].isin([1, 2]), 1, 0)

df_girls['light_score'] = np.where(df_girls['light_score'] == 'error', 0, df_girls['light_score'])
df_girls['light_score'] = pd.to_numeric(df_girls['light_score'])
df_girls['light_score'] = np.where(df_girls['light_score'] >= 0.8, 1, 0)

df_boys = df_boys.rename(columns={'if_jew_boys_muslim_boys_common': 'is_common_muslim', 'if_jew_boys_jew_girls': 'is_shared_boys_girls', 'syllabels_score': 'is_short_name', '1948-2023':'population'})
df_girls = df_girls.rename(columns={'if_jew_girls_muslim_girls_common': 'is_common_muslim', 'if_jew_boys_jew_girls': 'is_shared_boys_girls', 'syllabels_score': 'is_short_name', '1948-2023':'population'})

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





data = df_boys

# Page Configuration
st.set_page_config(page_title="פורטל שמות", layout="centered")

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

# App Title
st.markdown('<h1 class="centered-title">👶 פורטל שמות 👧</h1>', unsafe_allow_html=True)


BOY_MSG = "👶 בן"
GIRL_MSG = "👧 בת"

# Initialize session state to track selected option
if "selected_option" not in st.session_state:
    st.session_state.selected_option = BOY_MSG  # Start with no selection

left, right = st.columns(2)
if left.button("בן", icon="👶", use_container_width=True):
    st.session_state.selected_option = BOY_MSG
if right.button("בת", icon="👧", use_container_width=True):
    st.session_state.selected_option = GIRL_MSG

# Display the selected option
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
              'is_short_name']]






# Generate 11 radio buttons and corresponding inputs
questions = ['שם במגמת עלייה',
             'שם על זמני',
             'שם בשימוש המגזר המוסלמי',
             'שם לשני המגדרים',
             'שם נפוץ',
             'שם בינלאומי',
             'שם תנ״כי',
             'שם שקשור בטבע',
             'שם שקשור באומנות',
             'שם שקשור באור',
             'שם קצר'
             ]

IRRELEVANT_ANSWER = "לא רלוונטי"
YES_ANSWER = "כן"
NO_ANSWER = "לא"

if "selections" not in st.session_state:
    st.session_state.selections = [IRRELEVANT_ANSWER] * 11  # Default all to 'None'

for i in range(11):
    #st.write(f"#### {questions[i]}")
    st.markdown(f'<div class="rtl-text"><h4>{questions[i]}</h4></div>', unsafe_allow_html=True)
    st.session_state.selections[i] = st.radio(
            f'מה עמדתך לגבי הקריטריון הזה?',
            [IRRELEVANT_ANSWER, YES_ANSWER, NO_ANSWER],
            index=0,
            key=f"radio_{i}",
            help = str(i)
        )

data['score'] = 0
columns_to_compare = ['is_increasing_name', #1
                      'is_timeless_name', #2
                      'is_common_muslim', #3
                      'is_shared_boys_girls', #4
                      'is_common_name', #5
                      'is_international_name', #6
                      'is_bible_name', #7
                      'is_nature_name', #8
                      'is_art_name', #9
                      'is_light_name', #10
                      'is_short_name'] #11
counter = 0
for i in range(len(columns_to_compare)):
    if st.session_state.selections[i] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[i] == YES_ANSWER:
        data['score'] += 1 - data[columns_to_compare[i]]
        counter += 1
    elif st.session_state.selections[i] == NO_ANSWER:
        data['score'] += abs(0 - data[columns_to_compare[i]])
        counter += 1
data['score'] = (counter - data['score']) / counter

st.write(data.sort_values(by=['score', 'population'], ascending=[False, False]))
