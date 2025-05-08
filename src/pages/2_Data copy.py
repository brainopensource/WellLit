import streamlit as st
import pandas as pd
from src.components.header import render_header
from src.components.footer import render_footer
from src.utils.connectors.data import fetch_production_data
from src.components.sidebar import render_sidebar_user_block
from src.utils.connectors.app_response import MOCKED_RESPONSE


import json
import os


render_header()
render_sidebar_user_block()

st.title("Monthly Field Production")
st.write("Explore field-level oil, gas, and water production data from ANP via WoodMac.")

# Check user is logged in
#if not st.session_state.get("logged_in"):
if 1+1==3:
    st.warning("You must be logged in to view this data.")
else:
    if st.button("Fetch Production Data"):
        with st.spinner("Fetching data from WoodMac..."):
            try:
                #data = fetch_production_data(
                #    st.session_state.username,
                #    st.session_state.password
                #)
                data = MOCKED_RESPONSE

                if not data:
                    st.info("No production data was returned.")
                else:
                    #st.write(data)
                    # Save raw response to a JSON file for auditing
                    #output_path = os.path.join(os.getcwd(), "raw_production_data.txt")
                    #with open(output_path, "w", encoding="utf-8") as f:
                    #    json.dump(data, f, ensure_ascii=False, indent=2)
                    #st.success(f"Raw response saved to {output_path}")

                    df = pd.DataFrame(data)

                    if "production_period" in df.columns:
                        df["production_period"] = pd.to_datetime(df["production_period"])

                    if "_field_name" not in df.columns:
                        st.warning("Missing '_field_name' column in data.")
                    else:
                        unique_fields = df["_field_name"].dropna().unique()
                        selected_field = st.selectbox("Select a Field", sorted(unique_fields))

                        filtered_df = df[df["_field_name"] == selected_field]

                        st.write(f"Showing data for field: `{selected_field}`")
                        st.write(f"Total records: {len(filtered_df)}")

                        # Example of basic aggregation (edit to your needs)
                        aggregated = (
                            filtered_df.groupby("production_period")[
                                ["oil_production_kbd", "gas_production_mmcfd", "liquids_production_kbd", "water_production_kbd"]
                            ]
                            .sum()
                            .reset_index()
                            .sort_values("production_period")
                        )
                        st.dataframe(aggregated, use_container_width=True)

                        # Optional: Let user download or copy the result
                        csv = aggregated.to_csv(index=False).encode("utf-8")
                        st.download_button("Download CSV", data=csv, file_name=f"{selected_field}_production.csv", mime="text/csv")

            except Exception as e:
                st.error(f"Failed to retrieve production data: {e}")

render_footer()
