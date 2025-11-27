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
# Auto-refresh
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
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # --------------------------
    # Summary Metrics
    # --------------------------
    st.subheader("Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Events", len(df))
    col2.metric("Unique Users", df['user_id'].nunique())
    col3.metric("Unique Movies", df['movie_id'].nunique())

    # --------------------------
    # Events Over Time
    # --------------------------
    st.subheader("Events Over Time")
    events_per_minute = (
        df.groupby(pd.Grouper(key='timestamp', freq='1Min'))
        .size()
        .reset_index(name='count')
    )
    fig_time = px.line(events_per_minute, x='timestamp', y='count', title="Events per Minute")
    st.plotly_chart(fig_time, use_container_width=True)

    # --------------------------
    # Top Users
    # --------------------------
    st.subheader("🏆 Top 5 Active Users")

    top_users = (
        df['user_id']
        .value_counts()
        .head(5)
        .reset_index()
    )

    top_users.columns = ['user_id', 'events']
    top_users['rank'] = range(1, len(top_users) + 1)
    top_users['label'] = top_users['rank'].astype(str) + " | " + top_users['user_id'].astype(str)

    fig_users = px.bar(
        top_users,
        x='events',
        y='label',
        orientation='h',
        title="Top 5 Active Users",
    )

    fig_users.update_layout(
        yaxis=dict(title="User", autorange="reversed", tickfont=dict(size=14)),
        xaxis=dict(title="Events", tickfont=dict(size=14)),
        title=dict(x=0.5, font=dict(size=20)),
        margin=dict(l=120, r=20, t=50, b=20),
    )

    st.plotly_chart(fig_users, use_container_width=True)

    # --------------------------
    # Action Distribution
    # --------------------------
    st.subheader("Action Distribution")
    action_counts = df['action'].value_counts().reset_index()
    action_counts.columns = ['action', 'count']
    fig_actions = px.pie(action_counts, names='action', values='count', title="Action Breakdown")
    st.plotly_chart(fig_actions, use_container_width=True)
