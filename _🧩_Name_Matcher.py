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
st.set_page_config(page_title="Name Matcher", layout="centered", page_icon="🧩")

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
st.markdown('<h1 class="centered-title">👶 שם לפי העדפה 👧</h1>', unsafe_allow_html=True)


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
             'syllabels_score',
             'short_name',
             'med_name',
             'long_name',
             'is_summer_name',
             'is_spring_name',
             'is_winter_name',
             'is_autumn_name']]


IRRELEVANT_ANSWER = 'לא שיקול חשוב עבורי'
if "selections" not in st.session_state:
    st.session_state.selections = [IRRELEVANT_ANSWER] * 12  # Default all to 'None'

#################################### trendy name ####################################
st.markdown(f'<div class="rtl-text"><h4>מגמת פופלריות</h4></div>', unsafe_allow_html=True)
st.session_state.selections[0] = st.radio(
        f'מה עמדתך לגבי שמות טרנדיים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם אופנתי',
        'רוצה שם לא-אופנתי'],
        index=0,
        key=f"radio_0",
        help = 'שמות שהשכיחות שלהם נמצאת במגמת עלייה בעשור האחרון, כמו ריף לבנים וליבי לבנות')


#################################### timeliess name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם על זמני</h4></div>', unsafe_allow_html=True)
st.session_state.selections[1] = st.radio(
        f'מה עמדתך לגבי שמות על-זמניים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם על-זמני',
        'רוצה שם שאינו על-זמני'],
        index=0,
        key=f"radio_1",
        help = 'שמות שהשכיחות שלהם קבועה יחסית לאורך השנים, כמו דן לבנים ויעל לבנות')


#################################### arabic name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם דו-לשוני</h4></div>', unsafe_allow_html=True)
st.session_state.selections[2] = st.radio(
        f'מה עמדתך לגבי שמות משותפים ליהודים ומוסלמים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם דו-לשוני',
        'רוצה שם שאינו דו-לשוני'],
        index=0,
        key=f"radio_2",
        help = 'שמות שהשכיחות שלהם דומה בקרב יהודים ומוסלמים, כמו עומרי לבנים ונור לבנות')


#################################### boys-girls name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם דו-מגדרי</h4></div>', unsafe_allow_html=True)
st.session_state.selections[3] = st.radio(
        f'מה עמדתך לגבי שמות משותפים לבני ובנות?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם לשני המגדרים',
        'רוצה שם שאינו לשני המגדרים'],
        index=0,
        key=f"radio_3",
        help = 'שמות שהשכיחות שלהם דומה בקרב בנים ובנות, כמו יהל, בר וטל')

#################################### common name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם נפוץ</h4></div>', unsafe_allow_html=True)
st.session_state.selections[4] = st.radio(
        f'מה עמדתך לגבי שמות נפוצים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם נפוץ',
        'רוצה שם שאינו נפוץ'],
        index=0,
        key=f"radio_4",
        help = 'שמות נפוצים בעשור האחרון, כמו דוד לבנים ותמר לבנות')


#################################### international name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם גלובלי</h4></div>', unsafe_allow_html=True)
st.session_state.selections[5] = st.radio(
        f'מה עמדתך לגבי שמות גלובליים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם גלובלי',
        'רוצה שם שאינו גלובלי'],
        index=0,
        key=f"radio_5",
        help = 'שמות חוצי גבולות, כמו אדם לבנים ומאיה לבנות')

#################################### biblical name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם שקשור במוסרת היהודית</h4></div>', unsafe_allow_html=True)
st.session_state.selections[6] = st.radio(
        f'מה עמדתך לגבי שמות מהמקורות היהודיים?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם שקשור במסורת היהודית',
        'רוצה שם שאינו קשור במוסרת היהודית'],
        index=0,
        key=f"radio_6",
        help = 'שמות שמקורם בתנ״ך או במסורת היהודית, כמו גבריאל, דניאל ואריאל')

#################################### nature name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם שקשור בטבע</h4></div>', unsafe_allow_html=True)
st.session_state.selections[7] = st.radio(
        f'מה עמדתך לגבי שמות שקשורים בטבע?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם שקשור לטבע',
        'רוצה שם שאינו קשור לטבע'],
        index=0,
        key=f"radio_7",
        help = 'שמות שמקורם בטבע, כמו נטע, תומר וכרמל')

#################################### art name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם שקשור באומנות</h4></div>', unsafe_allow_html=True)
st.session_state.selections[8] = st.radio(
        f'מה עמדתך לגבי שמות שקשורים באומנות?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם שקשור לאומנות',
        'רוצה שם שאינו קשור לאומנות'],
        index=0,
        key=f"radio_8",
        help = 'שמות שמקורם באומנות, כמו שיר, צליל ובצלאל')


#################################### light name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם שקשור באור</h4></div>', unsafe_allow_html=True)
st.session_state.selections[9] = st.radio(
        f'מה עמדתך לגבי שמות שקשורים באור?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם שקשור באור',
        'רוצה שם שאינו קשור באור'],
        index=0,
        key=f"radio_9",
        help = 'שמות שמקורם באור, כמו יהל, אורי וזיו')

#################################### season name ####################################
st.markdown(f'<div class="rtl-text"><h4>שם שקשור בעונות השנה</h4></div>', unsafe_allow_html=True)
st.session_state.selections[10] = st.radio(
        f'מה עמדתך לגבי שמות שקשורים בעונות השנה?',
        ['לא שיקול חשוב עבורי',
        'רוצה שם שקשור בסתיו',
        'רוצה שם שקשור בחורף',
        'רוצה שם שקשור באביב',
        'רוצה שם שקשור בקיץ',],
        index=0,
        key=f"radio_10",
        help = 'שמות שקשורים בעונות השנה כמו אדר, כרם ומטר')

#################################### length of name ####################################
st.markdown(f'<div class="rtl-text"><h4>אורך שם</h4></div>', unsafe_allow_html=True)
st.session_state.selections[11] = st.radio(
        f'אורך שם מועדף',
        ['לא שיקול חשוב עבורי',
        'רוצה שם קצר',
        'רוצה שם באורך בינוני',
        'רוצה שם ארוך'],
        index=0,
        key=f"radio_11",
        help = 'הברה אחת=שם קצר, 2-3 הברות=שם באורך בינוני, 4 הברות ומעלה=שם ארוך')


_, center, _ = st.columns((2, 1, 2))

if center.button("מצאו את השמות המתאימים ביותר עבורי", type="primary"):
    if st.session_state.selected_option == GIRL_MSG:
        data = df_girls
    elif st.session_state.selected_option == BOY_MSG:
        data = df_boys

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
             'is_summer_name',
             'is_spring_name',
             'is_winter_name',
             'is_autumn_name',
             'syllabels_score',
             'short_name',
             'med_name',
             'long_name']]

    data['score'] = 0
    counter = 0
    gpt_counter = 0
    
    
    #################################### trendy name ####################################
    if st.session_state.selections[0] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[0] == 'רוצה שם אופנתי':
        data['score'] += 1 - data['is_increasing_name']
        counter += 1
    elif st.session_state.selections[0] == 'רוצה שם לא-אופנתי':
        data['score'] += abs(0 - data['is_increasing_name'])
        counter += 1

    #################################### timeliess name ####################################
    if st.session_state.selections[1] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[1] == 'רוצה שם על-זמני':
        data['score'] += 1 - data['is_timeless_name']
        counter += 1
    elif st.session_state.selections[1] == 'רוצה שם שאינו על-זמני':
        data['score'] += abs(0 - data['is_timeless_name'])
        counter += 1

    #################################### arabic name ####################################
    if st.session_state.selections[2] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[2] == 'רוצה שם דו-לשוני' :
        data['score'] += 1 - data['is_common_muslim']
        counter += 1
    elif st.session_state.selections[2] == 'רוצה שם שאינו דו-לשוני':
        data['score'] += abs(0 - data['is_common_muslim'])
        counter += 1

    #################################### boys-girls name ####################################
    if st.session_state.selections[3] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[3] == 'רוצה שם לשני המגדרים':
        data['score'] += 1 - data['is_shared_boys_girls']
        counter += 1
    elif st.session_state.selections[3] == 'רוצה שם שאינו לשני המגדרים':
        data['score'] += abs(0 - data['is_shared_boys_girls'])
        counter += 1

    #################################### common name ####################################
    if st.session_state.selections[4] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[4] == 'רוצה שם נפוץ':
        data['score'] += 1 - data['is_common_name']
        counter += 1
    elif st.session_state.selections[4] == 'רוצה שם שאינו נפוץ':
        data['score'] += abs(0 - data['is_common_name'])
        counter += 1

    #################################### international name ####################################
    if st.session_state.selections[5] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[5] == 'רוצה שם גלובלי':
        data['score'] += 1 - data['is_international_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[5] == 'רוצה שם שאינו גלובלי':
        data['score'] += abs(0 - data['is_international_name'])
        counter += 1
        gpt_counter += 1

    #################################### bible name ####################################
    if st.session_state.selections[6] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[6] == 'רוצה שם שקשור במסורת היהודית':
        data['score'] += 1 - data['is_bible_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[6] == 'רוצה שם שאינו קשור במוסרת היהודית':
        data['score'] += abs(0 - data['is_bible_name'])
        counter += 1
        gpt_counter += 1

    #################################### nature name ####################################
    if st.session_state.selections[7] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[7] == 'רוצה שם שקשור לטבע':
        data['score'] += 1 - data['is_nature_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[7] == 'רוצה שם שאינו קשור לטבע':
        data['score'] += abs(0 - data['is_nature_name'])
        counter += 1
        gpt_counter += 1

    #################################### art name ####################################
    if st.session_state.selections[8] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[8] == 'רוצה שם שקשור לאומנות':
        data['score'] += 1 - data['is_art_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[8] == 'רוצה שם שאינו קשור לאומנות':
        data['score'] += abs(0 - data['is_art_name'])
        counter += 1
        gpt_counter += 1

    #################################### light name ####################################
    if st.session_state.selections[9] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[9] == 'רוצה שם שקשור באור':
        data['score'] += 1 - data['is_light_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[9] == 'רוצה שם שאינו קשור באור':
        data['score'] += abs(0 - data['is_light_name'])
        counter += 1
        gpt_counter += 1

    #################################### season name ####################################
    if st.session_state.selections[10] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[10] == 'רוצה שם שקשור בסתיו':
        data['score'] += 1 - data['is_autumn_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[10] == 'רוצה שם שקשור בחורף':
        data['score'] += 1 - data['is_winter_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[10] == 'רוצה שם שקשור באביב':
        data['score'] += 1 - data['is_spring_name']
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[10] == 'רוצה שם שקשור בקיץ':
        data['score'] += 1 - data['is_summer_name']
        counter += 1
        gpt_counter += 1

    #################################### length of name ####################################
    if st.session_state.selections[11] == IRRELEVANT_ANSWER:
        pass
    elif st.session_state.selections[11] == 'רוצה שם קצר':
        data['score'] += 1 - data["short_name"]
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[11] == 'רוצה שם באורך בינוני':
        data['score'] += 1 - data["med_name"]
        counter += 1
        gpt_counter += 1
    elif st.session_state.selections[11] == 'רוצה שם ארוך':
        data['score'] += 1 - data["long_name"]
        counter += 1
        gpt_counter += 1
     
    if counter > 0:           
        data['score'] = (counter - data['score']) / counter

    sorted_data = data[['name', 'score', 'population','is_increasing_name','is_timeless_name','is_common_muslim','is_shared_boys_girls','is_common_name','is_international_name','is_bible_name','is_nature_name','is_art_name','is_light_name','syllabels_score','short_name', 'med_name', 'long_name', 'is_summer_name', 'is_winter_name', 'is_spring_name', 'is_autumn_name']].sort_values(by=['score', 'population'], ascending=[False, False])

    if st.session_state.selections[4] == 'רוצה שם שאינו נפוץ':
        pass
    else:
        sorted_data = sorted_data[sorted_data['population'] >= 50]

    max_score = sorted_data['score'].max()
    second_max_score = sorted_data[sorted_data['score'] != max_score]['score'].max()
    
    if gpt_counter > 0:
        st.markdown('<div class="rtl-text"><h6 style="color: blue;">התוצאות מסתמכות על בינה מלאכותית, מומלץ להיות ביקורתיים להזיות 😵‍💫</h5></div>', unsafe_allow_html=True)

    #st.markdown('<div class="rtl-text">' + str(max_score) + '</div>', unsafe_allow_html=True)
    #st.markdown('<div class="rtl-text">' + str(second_max_score) + '</div>', unsafe_allow_html=True)
    #st.dataframe(sorted_data, hide_index=True)

    how_many_show_to_show = 50
    if counter == 0:
        st.markdown(f'<div class="rtl-text"><h5>לא ביקשתם כלום, מדפיסים רשימה אקראית של שמות</h5></div>', unsafe_allow_html=True)
        lst = sorted_data['name'].tolist()
        shuffle(lst)
        lst = lst[0:how_many_show_to_show]
        lst.sort()
        for i in lst[0:how_many_show_to_show]:
            st.markdown('<div class="rtl-text">' + "- " + i + '</div>', unsafe_allow_html=True)
            time.sleep(0.01)

    elif sorted_data[sorted_data['score'] == max_score].shape[0] > 50:
        if str(int(max_score)) == '1':
            st.markdown(f'<div class="rtl-text"><h5>התאמה מושלמת</h5></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="rtl-text"><h5>לא מושלם, אבל הכי טוב שמצאנו</h5></div>', unsafe_allow_html=True)
        
        lst = sorted_data['name'].tolist()[0:how_many_show_to_show]
        lst.sort()
        for i in lst:
            st.markdown('<div class="rtl-text">' + "- " + i + '</div>', unsafe_allow_html=True)
            time.sleep(0.01)
    else:
        if str(int(max_score)) == '1':
            st.markdown(f'<div class="rtl-text"><h5>התאמה מושלמת</h5></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="rtl-text"><h5>לא מושלם, אבל הכי טוב שמצאנו</h5></div>', unsafe_allow_html=True)
        
        lst = sorted_data[sorted_data['score'] == max_score]['name'].tolist()
        length_of_best = len(lst)
        lst.sort()
        for i in lst:
            st.markdown('<div class="rtl-text">' + "- " + i + '</div>', unsafe_allow_html=True)
            time.sleep(0.01)

        if second_max_score > 0:
            st.markdown(f'<br>', unsafe_allow_html=True)
            time.sleep(0.05)
            st.markdown(f'<div class="rtl-text"><h5>התאמה שעונה על חלק מהתנאים</h5></div>', unsafe_allow_html=True)
            lst = sorted_data[sorted_data['score'] != max_score]['name'].tolist()[0:50-length_of_best+1]
            lst.sort()
            for i in lst:
                st.markdown('<div class="rtl-text">' + "- " + i + '</div>', unsafe_allow_html=True)
                time.sleep(0.01)

else:
    pass
