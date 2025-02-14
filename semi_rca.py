import streamlit as st

def main():
    # Set full screen layout
    st.set_page_config(layout="wide")
    
    # App title on the top left
    st.markdown("# Semi-RCA", unsafe_allow_html=True)
    
    # Create Tabs at the bottom of the screen
    tab1, tab2, tab3 = st.tabs(["Root Cause Analysis", "Parts History", "Process Run Signals"])
    
    with tab1:
        st.header("Root Cause Analysis")
        # Content to be added later
    
    with tab2:
        st.header("Parts History")
        
        # Create two columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("---")  # Horizontal line for division
            st.subheader("Critical Parts RFH", divider="red")
            # Upper part content to be added
            st.markdown("---")  # Horizontal line for division
            st.subheader("Parts Install", divider="blue")
            # Lower part content to be added
        
        with col2:
            st.subheader("Current Config")
            # Right column content to be added
    
    with tab3:
        st.header("Process Run Signals")
        # Content to be added later

if __name__ == "__main__":
    main()
