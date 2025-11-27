import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --------------------------
# Configuration
# --------------------------
st.set_page_config(page_title="User Activity Dashboard", layout="wide")
st.title("🎬 Real-Time User Activity Dashboard")

csv_file = 'user_activity.csv'
rolling_window = 1000  # last 1000 events
refresh_interval = 2000  # in milliseconds (2 seconds)

# --------------------------
# Auto-refresh every few seconds
# --------------------------
st_autorefresh(interval=refresh_interval, key="data_refresh")

# --------------------------
# Load data
# --------------------------
try:
    df = pd.read_csv(csv_file).tail(rolling_window)
except FileNotFoundError:
    df = pd.DataFrame(columns=['user_id', 'movie_id', 'action', 'timestamp'])

if df.empty:
    st.info("Waiting for user activity... Start the producer!")
else:
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # --------------------------
    # Sidebar Filters
    # --------------------------
    st.sidebar.header("Filters")
    users = st.sidebar.multiselect(
        "Select Users", options=df['user_id'].unique(), default=df['user_id'].unique()
    )
    actions = st.sidebar.multiselect(
        "Select Actions", options=df['action'].unique(), default=df['action'].unique()
    )

    filtered_df = df[(df['user_id'].isin(users)) & (df['action'].isin(actions))]

    # --------------------------
    # Summary Metrics
    # --------------------------
    st.subheader("Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Events", len(filtered_df))
    col2.metric("Unique Users", filtered_df['user_id'].nunique())
    col3.metric("Unique Movies", filtered_df['movie_id'].nunique())

    # --------------------------
    # Events Over Time
    # --------------------------
    st.subheader("Events Over Time")
    events_per_minute = (
        filtered_df.groupby(pd.Grouper(key='timestamp', freq='1Min'))
        .size()
        .reset_index(name='count')
    )
    fig_time = px.line(events_per_minute, x='timestamp', y='count', title="Events per Minute")
    st.plotly_chart(fig_time, use_container_width=True)

    # --------------------------
    # Top Users
    # --------------------------
    st.subheader("Top Users by Activity")
    top_users = filtered_df['user_id'].value_counts().head(10).reset_index()
    top_users.columns = ['user_id', 'events']
    fig_users = px.bar(top_users, x='user_id', y='events', title="Top 10 Active Users")
    st.plotly_chart(fig_users, use_container_width=True)

    # --------------------------
    # Action Distribution
    # --------------------------
    st.subheader("Action Distribution")
    action_counts = filtered_df['action'].value_counts().reset_index()
    action_counts.columns = ['action', 'count']
    fig_actions = px.pie(action_counts, names='action', values='count', title="Action Breakdown")
    st.plotly_chart(fig_actions, use_container_width=True)
