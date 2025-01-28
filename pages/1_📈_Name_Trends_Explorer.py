import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

df_boys = pd.read_csv("boys.csv")
df_girls = pd.read_csv("girls.csv")

boys_names = df_boys['name'].unique().tolist()
girls_names = df_girls['name'].unique().tolist()
all_names = list(set(boys_names + girls_names))

#selected_name = st.selectbox('בחרו שם:', options=all_names, index = all_names.index('יובל'))

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


years_columns = [item for item in list(range(1948,2024))]

for year in years_columns:
    df_boys[str(year)] = pd.to_numeric(df_boys[str(year)])
    df_girls[str(year)] = pd.to_numeric(df_girls[str(year)])



st.markdown(
    """
    <div style="text-align: center; direction: rtl; font-size: 24px; font-weight: bold;">
        שכיחות שם לפי שנה
    </div>
    """,
    unsafe_allow_html=True
)


if selected_name in boys_names and selected_name in girls_names:
    last_rows = [
        [
            df_boys[df_boys['name'] == selected_name][str(years_columns[0])].tolist()[0],
            df_girls[df_girls['name'] == selected_name][str(years_columns[0])].tolist()[0],
        ]
    ] 
    columns = ['בנים', 'בנות']  # Names for the two lines
    x_values = [str(years_columns[0])]  # Initialize the index
    chart_data = pd.DataFrame(last_rows, columns=columns, index=x_values)

    # Create the chart
    chart = st.line_chart(chart_data)

    # Initialize the data
    for year in years_columns[1:]:
        new_rows = [
            [
                df_boys[df_boys['name'] == selected_name][str(year)].tolist()[0],
                df_girls[df_girls['name'] == selected_name][str(year)].tolist()[0],
            ]
        ]

        last_rows.extend(new_rows)
        x_values.append(str(year))  # Update the index with the new year
        
        new_data = pd.DataFrame(last_rows, columns=columns, index=x_values)

        chart.add_rows(new_data)

        time.sleep(0.01)
elif selected_name in boys_names:
    last_rows = [
        [
            df_boys[df_boys['name'] == selected_name][str(years_columns[0])].tolist()[0]
        ]
    ] 
    columns = ['בנים']
    x_values = [str(years_columns[0])] 
    chart_data = pd.DataFrame(last_rows, columns=columns, index=x_values)

    chart = st.line_chart(chart_data)

    for year in years_columns[1:]:
        new_rows = [
            [
                df_boys[df_boys['name'] == selected_name][str(year)].tolist()[0]
            ]
        ]

        last_rows.extend(new_rows)
        x_values.append(str(year))  # Update the index with the new year
        new_data = pd.DataFrame(last_rows, columns=columns, index=x_values)
        chart.add_rows(new_data)

        time.sleep(0.01)
elif selected_name in girls_names:
    last_rows = [
        [
            df_girls[df_girls['name'] == selected_name][str(years_columns[0])].tolist()[0]
        ]
    ] 
    columns = ['בנות']
    x_values = [str(years_columns[0])] 
    chart_data = pd.DataFrame(last_rows, columns=columns, index=x_values)

    chart = st.line_chart(chart_data)

    for year in years_columns[1:]:
        new_rows = [
            [
                df_girls[df_girls['name'] == selected_name][str(year)].tolist()[0]
            ]
        ]

        last_rows.extend(new_rows)
        x_values.append(str(year))  # Update the index with the new year
        new_data = pd.DataFrame(last_rows, columns=columns, index=x_values)
        chart.add_rows(new_data)

        time.sleep(0.01)