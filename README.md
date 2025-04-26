# Netflix-Intelligence-Insights-and-Recommendations

**Project Overview**

This project explores and enhances the Netflix dataset to deliver both analytical insights and a content-based recommendation system.
The project is divided into two main parts:

- Data Analyst Role:  Discover trends and present insights using Python (Pandas/Plotly) OR Power BI OR Tableau.
- Data Scientist Role: Build a basic content-based recommendation system.

**Roles and Contributions**

- Data Analyst Role - Preprocessed the Netflix dataset, created visualizations (Top genres, Trends, Ratings, Content by country), and built a dashboard.
- Data Scientist Role - Built a content-based recommendation system using TF-IDF vectorization and cosine similarity. Developed a Streamlit web app to interact with the recommendation model.

**How to run**

Step 1: Download the Project Folder
- Download the Streamlit_Interface folder above.
- Open the folder in Visual Studio Code (VS Code).

Step 2: Download the Required Files
- Download the necessary model files using the provided google drive links and save it inside the downloaded folder.
- cosine_similarity.pkl: https://drive.google.com/file/d/1DbJNviw3q2wodKgTzKKmmfBoUhoA6Nxj/view?usp=sharing
- indices.pkl: https://drive.google.com/file/d/1nEUTrS6bEjII0lYOXFxlmXBtYBpZchTq/view?usp=sharing
- netflix_dataset_preprocessed.csv: https://drive.google.com/file/d/1aNp6NM1C9so5W47wB273EQxm1jg6f1qn/view?usp=sharing

Step 3: Install Required Python Libraries
- Open a new terminal inside VS Code.
- Install the required libraries listed in the requirements.txt file by running: pip install -r requirements.txt

Step 4: Run the Streamlit Application
- In the terminal, navigate to the streamlit_interface folder if you're not already there.
- Run the Streamlit app using: streamlit run app.py
- The app will launch in your browser (at http://localhost:8501).

**Folder Structure**

Netflix-Intelligence-Insights-and-Recommendations/

│

├── Streamlit_Interface/   

│    ├── app.py

│    └── requirements.txt

│

├── Notebooks/

│    └── Netflix-Intelligence-Insights-and-Recommendations.ipynb  

│

├── README.md

└── README images/

     ├── screenshot(100).png
     
     └── screenshot(101).png

**Streamlit Interface**

![image_alt](https://github.com/TharinsaMudalige/Netflix-Intelligence-Insights-and-Recommendations/blob/084ee670c025f53c209333548e9e975db260fb40/README%20images/Screenshot%20(100).png)


![image_alt](https://github.com/TharinsaMudalige/Netflix-Intelligence-Insights-and-Recommendations/blob/084ee670c025f53c209333548e9e975db260fb40/README%20images/Screenshot%20(101).png)


