# 📤 API Data Exporter

API Data Exporter is a Streamlit-based web application that allows users to fetch data from an API and export it as JSON or CSV. The app includes a secure login system, error handling for API requests, and data export functionality.

## 📑 Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Required Libraries](#required-libraries)
- [Files](#files)
- [Contributing](#contributing)

## 📂 Project Structure

The project is organized as follows:

- data
- app.py
- README.md
- requeriments.txt

## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/api-data-exporter.git
   cd api-data-exporter
2. **Run the app:**
   ```bash
   streamlit run app.py
## 🚀 Usage

1. Access the login page and enter the password.

2. Enter an API URL in the provided text field (e.g., https://jsonplaceholder.typicode.com/users).

3. Click "Fetch Data" to retrieve data from the API.

4. Preview the fetched data on the screen.

5. Download the data as a JSON or CSV file using the export buttons.

## 📦 Required Libraries
Make sure you have the following Python libraries installed:

- streamlit
- requests
- json
- csv

## 📄 Files
- `app.py:` Main application script, which includes:
    - Secure login authentication
    - API request handling with error management

- Data fetching, preview, and export functionality

- `requirements.txt:` List of required Python libraries.

- `README.md:` Documentation for the project.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

