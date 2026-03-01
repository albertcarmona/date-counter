
from datetime import datetime
import streamlit as st
import time

now = datetime.now()
final_date = datetime(2026, 3, 27, 0, 0, 0)

time_left = final_date - now


def main():
    st.title("Hans Zimmer Live Counter")
    st.subheader(f"Barcelona\t\tConcert Date: {final_date}")
    st.subheader("Minutes left:")
    st.title(time_left.seconds // 60)
    time.sleep(10)
    st.rerun()


if __name__ == "__main__":
    main()
