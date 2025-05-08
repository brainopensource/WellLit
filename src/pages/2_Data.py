import streamlit as st
import pandas as pd
from src.components.header import render_header
from src.components.footer import render_footer
from src.components.sidebar import render_sidebar_user_block
from src.utils.connectors.app_response import MOCKED_RESPONSE
from datetime import datetime
import os

render_header()
render_sidebar_user_block()

st.title("Monthly Field Production")
st.write("Explore field-level oil, gas, and water production data from ANP via WoodMac.")

# --- SECTION 1: Fetch / Refresh Data ---
st.subheader("1. Fetch Production Data")

def load_data():
    # Simulate fetching from external source
    df = pd.DataFrame(MOCKED_RESPONSE)
    if "production_period" in df.columns:
        df["production_period"] = pd.to_datetime(df["production_period"])
    return df

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()  # Default empty

if st.button("Fetch or Refresh Data"):
    with st.spinner("Fetching data from source..."):
        try:
            st.session_state.df = load_data()
            st.success(f"Fetched {len(st.session_state.df)} records at {datetime.now().strftime('%H:%M:%S')}")
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

        result = (
            filtered_df.groupby("production_period")[
                ["oil_production_kbd", "gas_production_mmcfd", "liquids_production_kbd", "water_production_kbd"]
            ]
            .sum()
            .reset_index()
            .sort_values("production_period")
        )

        st.dataframe(result, use_container_width=True)

        csv = result.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", data=csv, file_name=f"{selected_field}_production.csv", mime="text/csv")

render_footer()
