import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- Page configuration (must be the first Streamlit command) ----
st.set_page_config(page_title="EDA Interface", layout="wide")

st.title("Exploratory Data Analysis Interface")

# ================= Sidebar: Dataset Controls =================
st.sidebar.header("Dataset Controls")
uploaded_file = st.sidebar.file_uploader("Upload CSV File for Analysis", type=["csv"])

if uploaded_file is not None:
    # Validate the uploaded file is a correctly formatted CSV
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.sidebar.error(f"Invalid CSV file: {e}")
        st.stop()

    # ================= Sidebar: Attribute Selection =================
    st.sidebar.header("Attribute Selection")
    selected_column = st.sidebar.selectbox("Select Attribute for Visualization", df.columns)

    # ================= Main Area - Top Section: Preview & Metadata =================
    st.subheader("Dataset Preview & Metadata")

    st.write("First 5 Rows:")
    st.dataframe(df.head())

    st.write("Shape:", df.shape)  # (rows, columns)

    st.write("Column Data Types:")
    st.dataframe(df.dtypes.astype(str).rename("Data Type"))

    st.write("Missing Values per Column:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    st.dataframe(pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct}))

    st.write("Statistical Summary (Numerical Columns):")
    st.dataframe(df.describe())  # mean, std, min, 25/50(median)/75%, max

    # ================= Main Area - Bottom Section: Conditional Visualization =================
    st.subheader("Visualization")

    # Automated attribute typing: numerical vs categorical
    if pd.api.types.is_numeric_dtype(df[selected_column]):
        # ---- Numerical attribute -> Histogram ----
        fig, ax = plt.subplots()
        ax.hist(df[selected_column].dropna(), bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"Histogram of {selected_column}")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        # ---- Categorical attribute -> Bar chart with frequency + percentage ----
        counts = df[selected_column].value_counts()
        percentages = (counts / counts.sum() * 100).round(1)

        fig, ax = plt.subplots()
        bars = ax.bar(counts.index.astype(str), counts.values, color="lightgreen", edgecolor="black")
        ax.set_title(f"Bar Chart of {selected_column}")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        plt.xticks(rotation=45, ha="right")

        # Display percentage label above each bar
        for bar, pct in zip(bars, percentages):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     f"{pct}%", ha="center", va="bottom", fontsize=8)

        st.pyplot(fig)

else:
    st.info("Please upload a CSV file from the sidebar to begin analysis (use Titanic-Dataset.csv).")
