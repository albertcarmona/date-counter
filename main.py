from datetime import datetime
import streamlit as st
import pytz
import time

madrid_tz = pytz.timezone('Europe/Madrid')
final_date = madrid_tz.localize(datetime(2026, 3, 27, 0, 0, 0))

def main():
    now = datetime.now(madrid_tz)
    time_left = final_date - now
    
    st.title("Hans Zimmer Live Counter⏳")
    st.subheader(f"Barcelona Concert Date: {final_date}")
    st.subheader("Minutes left:")

    total_minutes = int(time_left.total_seconds() // 60)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title(f"{total_minutes}")

    time.sleep(10)
    st.rerun()

if __name__ == "__main__":
    main()