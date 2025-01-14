
---

# Assista AI Chatbot  

**Assista** is an AI-powered chatbot designed to assist with various tasks. This guide provides a step-by-step approach to set up and run the chatbot locally.

## Prerequisites  
Before you begin, ensure you have the following installed on your system:  
- Python (version 3.7 or above)  
- pip (Python package installer)  
- Git  

## Installation and Setup  

Follow these steps to set up and run the chatbot:

1. **Clone the Repository**  
   Download the project files from the Git repository:  
   ```bash  
   git clone <repository-url>  
   ```  

2. **Extract the Files**  
   If you downloaded a ZIP file, extract its contents to your desired location.  

3. **Navigate to the Project Directory**  
   Open your terminal or command prompt and navigate to the extracted project directory:  
   ```bash  
   cd <project-directory>  
   ```  

4. **Create a Virtual Environment**  
   Set up a virtual environment to isolate project dependencies:  
   ```bash  
   python -m venv venv  
   ```  

5. **Activate the Virtual Environment**  
   - On **Windows**:  
     ```bash  
     .\venv\Scripts\activate  
     ```  
   - On **macOS/Linux**:  
     ```bash  
     source venv/bin/activate  
     ```  

6. **Install Dependencies**  
   Install all the required Python packages using:  
   ```bash  
   pip install -r requirements.txt  
   ```  

7. **Run the Streamlit Application**  
   Launch the chatbot application with the following command:  
   ```bash  
   streamlit run app.py  
   ```  

## Usage  
Once the application is running, it will open in your default web browser. Interact with the chatbot as per your needs.


