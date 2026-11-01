
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Urban Traffic Intelligence",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Urban Traffic Intelligence")
st.caption("Data-driven traffic analysis and predictive analytics")

DATA_PATH = Path("data/final_cleaned_dataset.csv")

if not DATA_PATH.exists():
    st.warning(
        "Dataset not found. Create a 'data' folder "
        "and place final_cleaned_dataset.csv inside it."
    )
    st.stop()

df = pd.read_csv(DATA_PATH)
df["DateTime"] = pd.to_datetime(df["DateTime"])

st.sidebar.header("Dashboard Filters")

junctions = sorted(df["Junction"].unique())
selected = st.sidebar.multiselect(
    "Select Junction",
    junctions,
    default=junctions
)

filtered = df[df["Junction"].isin(selected)].copy()

if filtered.empty:
    st.warning("Select at least one junction.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Records", f"{len(filtered):,}")
c2.metric("Average Vehicles", f"{filtered['Vehicles'].mean():.2f}")
c3.metric("Maximum Vehicles", int(filtered["Vehicles"].max()))
c4.metric("Junctions", filtered["Junction"].nunique())

st.divider()

st.subheader("Traffic Volume Over Time")

trend = (
    filtered.groupby("DateTime", as_index=False)["Vehicles"]
    .mean()
)

fig = px.line(
    trend,
    x="DateTime",
    y="Vehicles",
    title="Average Vehicle Count Over Time",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Junction Comparison")

junction_data = (
    filtered.groupby("Junction", as_index=False)["Vehicles"]
    .mean()
)

fig2 = px.bar(
    junction_data,
    x="Junction",
    y="Vehicles",
    color="Vehicles",
    title="Average Vehicles by Junction",
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

st.success("Urban Traffic Intelligence dashboard loaded successfully!")
