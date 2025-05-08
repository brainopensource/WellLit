import streamlit as st
import pandas as pd
from src.components.header import render_header
from src.components.footer import render_footer
from src.components.sidebar import render_sidebar_user_block
#from src.utils.connectors.app_response import MOCKED_RESPONSE
from src.utils.connectors.mocked_prod_data import MOCKED_RESPONSE
from src.utils.connectors.data import fetch_all_data
from datetime import datetime
import os
import matplotlib.pyplot as plt


# --- PAGE CONFIG ---
render_header()
render_sidebar_user_block()

st.title("Monthly Field Production")
st.write("Explore field-level oil, gas, and water production data from ANP via WoodMac.")

# --- SECTION 1: Fetch / Refresh Data ---
st.subheader("1. Fetch Production Data")

def load_data():
    # Simulate fetching from external source
    df = pd.DataFrame(MOCKED_RESPONSE)
    # df = fetch_all_data(st.session_state.username, st.session_state.password)
    if "production_period" in df.columns:
        df["production_period"] = pd.to_datetime(df["production_period"])
    return df

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()  # Default empty

if st.button("Fetch or Refresh Data"):
    with st.spinner("Fetching data from source..."):
        try:
            st.session_state.df = load_data()
            st.success(f"Fetched records at {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            st.error(f"Error fetching data: {e}")

# --- SECTION 2: Filter & Analyze ---
st.subheader("2. Analyze Field Production")

df = st.session_state.df

if df.empty:
    st.info("No data loaded. Please fetch the data above.")
else:
    if "_field_name" not in df.columns:
        st.warning("Missing '_field_name' column in data.")
    else:
        fields = sorted(df["_field_name"].dropna().unique())
        selected_field = st.selectbox("Select Field", fields)

        filtered_df = df[df["_field_name"] == selected_field]

        st.write(f"Showing data for: **{selected_field}**")
        st.write(f"Total records: {len(filtered_df)}")

        filtered_df = filtered_df[['_field_name', 'production_period', 'oil_production_kbd', 'gas_production_mmcfd']].reset_index(drop=True)

        st.dataframe(filtered_df, use_container_width=True)

        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", data=csv, file_name=f"{selected_field}_production.csv", mime="text/csv")

# --- SECTION 3: Further Analysis ---
st.subheader("3. Analyze Field Production Trends")

import pandas as pd
import streamlit as st
from datetime import datetime
import calendar

df = st.session_state.df

if df.empty:
    st.info("No data loaded. Please fetch the data above.")
else:
    # Calculate total production per month (multiply by days in the month)
    filtered_df['month_days'] = filtered_df['production_period'].dt.days_in_month
    filtered_df['monthly_oil_production_kb'] = filtered_df['oil_production_kbd'] * filtered_df['month_days']
    filtered_df['monthly_gas_production_mmcf'] = filtered_df['gas_production_mmcfd'] * filtered_df['month_days']

    # Extract the year from the production_period
    filtered_df['year'] = filtered_df['production_period'].dt.year

    # Aggregate by year
    yearly_production = (
        filtered_df.groupby('year')
        .agg({
            'monthly_oil_production_kb': 'sum',
            'monthly_gas_production_mmcf': 'sum'
        })
        .reset_index()
    )

    # Compute the KBD average per year by dividing by 365
    yearly_production['oil_production_kbd_avg'] = yearly_production['monthly_oil_production_kb'] / 365
    yearly_production['gas_production_mmcfd_avg'] = yearly_production['monthly_gas_production_mmcf'] / 365

    yearly_production = yearly_production[['year', 'oil_production_kbd_avg', 'gas_production_mmcfd_avg']]

    st.write("Yearly Production (KBD average per year):")
    st.dataframe(yearly_production, use_container_width=True)

    # Option to download the aggregated yearly data as CSV
    csv = yearly_production.to_csv(index=False).encode('utf-8')
    st.download_button("Download Yearly CSV", data=csv, file_name=f"{selected_field}_yearly_production.csv", mime="text/csv")

# --- SECTION 4: Plotting Production vs Year ---
st.subheader("4. Plot Field Production by Year")

# Assuming `yearly_production` is already defined and contains the data
df = yearly_production

if df.empty:
    st.info("No data available for plotting. Please fetch the data above.")
else:
    import plotly.graph_objects as go

    fig = go.Figure()

    # Oil Production
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['oil_production_kbd_avg'],
        mode='lines+markers',
        name='Oil Production (KBD)',
        line=dict(color='royalblue')
    ))

    # Gas Production
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['gas_production_mmcfd_avg'],
        mode='lines+markers',
        name='Gas Production (MMCFD)',
        line=dict(color='darkorange')
    ))

    # Layout settings
    fig.update_layout(
        title=f"Field Production Trends: {selected_field}",
        xaxis_title='Year',
        yaxis_title='Average Production (per day)',
        template='simple_white',
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=20, r=20, t=40, b=20)
    )

    # Render in Streamlit
    st.plotly_chart(fig, use_container_width=True)

# --- SECTION 5: Plot Monthly Production ---
st.subheader("5. Plot Field Production by Month")

# Assuming `filtered_df` is the original DataFrame filtered by selected_field
df = filtered_df.copy()
df = df.sort_values("production_period")

if df.empty:
    st.info("No data available for plotting. Please fetch the data above.")
else:
    import plotly.graph_objects as go

    fig = go.Figure()

    # Oil Production
    fig.add_trace(go.Scatter(
        x=df['production_period'],
        y=df['oil_production_kbd'],
        mode='lines+markers',
        name='Oil Production (KBD)',
        line=dict(color='royalblue')
    ))

    # Gas Production
    fig.add_trace(go.Scatter(
        x=df['production_period'],
        y=df['gas_production_mmcfd'],
        mode='lines+markers',
        name='Gas Production (MMCFD)',
        line=dict(color='darkorange')
    ))

    fig.update_layout(
        title=f"Monthly Production Trends: {selected_field}",
        xaxis_title='Month',
        yaxis_title='Production (per day)',
        template='simple_white',
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)



render_footer()
