import streamlit as st
import requests
import json
import csv
from io import StringIO

# Hardcoded password (for simplicity; not secure for production!)
CORRECT_PASSWORD = "password123"

# -----------------------------------------------
# Password Check Page
# -----------------------------------------------
def login_page():
    st.title("🔒 Login")
    password = st.text_input("Enter Password:", type="password")

    if st.button("Login"):
        if password == CORRECT_PASSWORD:
            st.session_state.logged_in = True  # Update session state
            st.success("Login successful! Redirecting...")
        else:
            st.error("Incorrect password!")

# -----------------------------------------------
# Main App (API + Export) with Enhanced Error Handling
# -----------------------------------------------
def main_app():
    st.title("📤 API Data Exporter")
    
    # Input for API URL
    api_url = st.text_input("Enter API URL:", "https://jsonplaceholder.typicode.com/users")
    
    # Fetch data from API
    if st.button("Fetch Data"):
        try:
            # Attempt API connection with timeout
            response = requests.get(api_url, timeout=10)
            
            # Raise HTTPError for 4xx/5xx status codes
            response.raise_for_status()  
            
            # Attempt to parse JSON
            data = response.json()
            
            # Check if data is empty or not a list/dict
            if not data:
                st.warning("API returned no data.")
                return
            
            st.session_state.data = data
            st.success("Data fetched successfully!")
            st.write(data[:2])  # Preview
            
        except requests.exceptions.HTTPError as http_err:
            # Handle 4xx/5xx errors
            status_code = response.status_code
            if 400 <= status_code < 500:
                st.error(f"Client Error ({status_code}): Check the URL or parameters.")
            else:
                st.error(f"Server Error ({status_code}): Try again later.")
        
        except requests.exceptions.ConnectionError:
            st.error("Connection Failed: Invalid URL or no internet connection.")
        
        except requests.exceptions.Timeout:
            st.error("Request Timed Out: Took longer than 10 seconds.")
        
        except requests.exceptions.RequestException as err:
            st.error(f"Request Failed: {str(err)}")
        
        except ValueError:
            st.error("Invalid JSON: API did not return valid JSON data.")
        
        except Exception as e:
            st.error(f"Unexpected Error: {str(e)}")

    # Export buttons (only if data exists)
    if "data" in st.session_state:
        st.markdown("---")
        st.subheader("Export Data")
        
        # Export as JSON
        json_data = json.dumps(st.session_state.data, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="data.json",
            mime="application/json"
        )
        
        # Export as CSV
        if st.button("Download CSV"):
            try:
                # Convert JSON to CSV
                csv_data = StringIO()
                writer = csv.writer(csv_data)
                
                # Write header (assumes data is a list of dictionaries)
                writer.writerow(st.session_state.data[0].keys())
                
                # Write rows
                for item in st.session_state.data:
                    writer.writerow(item.values())
                
                # Create download link
                st.download_button(
                    label="Click to Save CSV",
                    data=csv_data.getvalue(),
                    file_name="data.csv",
                    mime="text/csv"
                )
            except Exception as e:
                st.error(f"CSV Conversion Failed: {str(e)}")

# -----------------------------------------------
# Run the App
# -----------------------------------------------
def main():
    # Initialize session state for login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # Show login page if not logged in
    if not st.session_state.logged_in:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()