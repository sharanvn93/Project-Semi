import streamlit as st

def main():
    # Set full screen layout
    st.set_page_config(layout="wide")
    
    # App title on the top left
    st.markdown("# Semi-RCA", unsafe_allow_html=True)
    
    # Using a bottom-positioned tab bar
    tab_selection = st.radio("", ["Root Cause Analysis", "Parts History", "Process Run Signals"], horizontal=True)
    
    if tab_selection == "Root Cause Analysis":
        
        # Content to be added later
    
        elif tab_selection == "Parts History":
        
        
        # Create two columns for layout
            col1, col2 = st.columns([1, 1])
        
            with col1:
                st.markdown("---")  # Horizontal line for division
                st.markdown("<h3 style='text-align: center;'>Critical Parts RFH</h3>", unsafe_allow_html=True)
                # Upper part content to be added
                st.markdown("---")  # Horizontal line for division
                st.markdown("<h3 style='text-align: center;'>Parts Install</h3>", unsafe_allow_html=True)
                # Lower part content to be added
        
            with col2:
                st.markdown("<h3 style='text-align: center;'>Current Config</h3>", unsafe_allow_html=True)
                # Right column content to be added
        
        elif tab_selection == "Process Run Signals":
        
            # Content to be added later

    if __name__ == "__main__":
    main()
