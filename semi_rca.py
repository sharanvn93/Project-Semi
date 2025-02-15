import streamlit as st

def main():
    # Set full screen layout
    st.set_page_config(layout="wide")
    
    # App title on the top left
    st.markdown("# Semi-RCA", unsafe_allow_html=True)
    
    # Using a bottom-positioned tab bar
    tab_selection = st.radio("", ["Root Cause Analysis", "Parts History", "Process Run Signals"], horizontal=True)
    
    if tab_selection == "Root Cause Analysis":
        pass  # Content to be added later
    
    elif tab_selection == "Parts History":
        # Create two columns for layout
        col1, spacer, col2 = st.columns([1, 0.005, 1])
        
        with col1:
            st.markdown("<h3 style='text-align: center; padding-bottom: 10px;'>Critical Parts RFH</h3>", unsafe_allow_html=True)
            # Upper part content to be added
            st.markdown("---")  # Horizontal line for division
            st.markdown("<h3 style='text-align: center; padding-bottom: 10px;'>Parts Install</h3>", unsafe_allow_html=True)
            col_lower = st.columns([1, 1, 1, 1])
            with col_lower[0]:
                st.button("Mini PM")
            with col_lower[1]:
                st.button("Major PM")
            with col_lower[2]:
                st.button("Upgrade")
            with col_lower[3]:
                if st.button("New Chamber"):
                    uploaded_file = st.file_uploader("Upload Reference BOM File", type=["xlsx", "csv"])
                    if 'uploaded_file' in locals() and uploaded_file is not None:
                    
                                    if 'bom_df' in locals():
                        import pandas as pd
                        import datetime
                        
                        # Read the uploaded file
                        if uploaded_file.name.endswith(".xlsx"):
                            bom_df = pd.read_excel(uploaded_file)
                        else:
                            bom_df = pd.read_csv(uploaded_file)
                        
                        # Add Date and RFH columns
                        bom_df["Date"] = datetime.datetime.now().strftime("%Y-%m-%d")
                        bom_df["RFH"] = 0
                        
                        # Save the modified file
                        bom_df.to_excel("updated_BOM.xlsx", index=False)
                        
                        st.success("BOM file updated with Date and RFH columns.")
                        st.download_button("Download Updated BOM", data=open("updated_BOM.xlsx", "rb"), file_name="updated_BOM.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        
        with spacer:
            st.markdown("<div style='border-left: 2px solid black; height: 100vh;'></div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h3 style='text-align: center;'>Current Config</h3>", unsafe_allow_html=True)
            if 'uploaded_file' in locals() and uploaded_file is not None:
                if 'bom_df' in locals():
                                    st.dataframe(bom_df)
            # Right column content to be added
    
    elif tab_selection == "Process Run Signals":
        pass  # Content to be added later

if __name__ == "__main__":
    main()
