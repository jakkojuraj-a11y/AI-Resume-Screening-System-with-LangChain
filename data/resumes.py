# ============================================================
# data/resumes.py
# Sample Resumes – Strong, Average, and Weak Candidates
# ============================================================
# Each resume is a plain-text string simulating real candidate data.
# These are used as inputs to the AI screening pipeline.
# ============================================================

RESUMES = {
    "strong": {
        "name": "Arjun Mehta",
        "label": "Strong Candidate",
        "text": """
ARJUN MEHTA
Senior Data Scientist | Bangalore, India
Email: arjun.mehta@email.com | LinkedIn: linkedin.com/in/arjunmehta

PROFESSIONAL SUMMARY
Accomplished Data Scientist with 6+ years of experience building end-to-end 
machine learning pipelines, deploying production ML models, and driving 
data-driven decision-making at scale. Expertise in deep learning, NLP, 
and cloud-based ML infrastructure.

EXPERIENCE

Senior Data Scientist | Flipkart (2021 – Present)
- Designed and deployed a real-time product recommendation engine using 
  TensorFlow and AWS SageMaker, increasing click-through rate by 18%.
- Built NLP-based customer sentiment analysis pipeline processing 2M+ 
  reviews daily using BERT and spaCy.
- Led a team of 4 data scientists; mentored junior members on MLOps best practices.
- Implemented A/B testing frameworks to validate model performance improvements.

Data Scientist | Infosys (2018 – 2021)
- Developed predictive maintenance models using Random Forest and XGBoost, 
  reducing equipment downtime by 25%.
- Created automated ETL pipelines using Python, SQL, and Apache Airflow.
- Designed interactive dashboards in Tableau for executive stakeholders.
- Collaborated with cross-functional teams to translate business requirements 
  into ML solutions.

EDUCATION
M.Tech in Computer Science – IIT Hyderabad (2018)
B.Tech in Computer Science – NIT Warangal (2016)

SKILLS
- Programming: Python, R, SQL, PySpark
- ML/DL Frameworks: TensorFlow, PyTorch, Scikit-learn, XGBoost, Keras
- NLP: BERT, spaCy, Hugging Face Transformers, NLTK
- Cloud & MLOps: AWS (SageMaker, EC2, S3), Docker, MLflow, Airflow
- Data Visualization: Tableau, Matplotlib, Seaborn, Plotly
- Databases: PostgreSQL, MongoDB, Redis
- Tools: Git, Jupyter, VS Code, Linux

CERTIFICATIONS
- AWS Certified Machine Learning – Specialty (2022)
- TensorFlow Developer Certificate (2021)
- Deep Learning Specialization – Coursera (Andrew Ng)

PUBLICATIONS
- "Scalable Sentiment Analysis for E-Commerce" – IEEE Conference 2023
"""
    },

    "average": {
        "name": "Priya Sharma",
        "label": "Average Candidate",
        "text": """
PRIYA SHARMA
Data Analyst / Aspiring Data Scientist | Pune, India
Email: priya.sharma@email.com | LinkedIn: linkedin.com/in/priyasharma

PROFESSIONAL SUMMARY
Data Analyst with 2 years of experience in data analysis and reporting, 
currently transitioning into data science. Familiar with Python, basic 
machine learning, and statistical analysis.

EXPERIENCE

Data Analyst | Wipro Technologies (2022 – Present)
- Performed exploratory data analysis on customer datasets using Python 
  and Pandas to identify trends and patterns.
- Built automated reporting dashboards using Power BI for monthly KPI tracking.
- Wrote SQL queries to extract and transform data from MySQL databases.
- Assisted senior data scientists with data preprocessing and feature engineering 
  for churn prediction models.

Intern – Data Analytics | TCS (2021 – 2022)
- Cleaned and preprocessed large datasets using Excel and Python.
- Created basic visualizations using Matplotlib and Seaborn.
- Supported team in building a logistic regression model for lead scoring.

EDUCATION
B.Tech in Information Technology – Pune University (2021)

SKILLS
- Programming: Python, SQL
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- ML Basics: Linear Regression, Logistic Regression, Decision Trees
- Tools: Power BI, Excel, Jupyter Notebook, Git
- Databases: MySQL

CERTIFICATIONS
- Google Data Analytics Professional Certificate (2023)
- Python for Data Science – Coursera (IBM)

PROJECTS
- Customer Churn Prediction – Built a logistic regression model achieving 
  78% accuracy on a telecom dataset.
- Sales Dashboard – Created interactive Power BI dashboard for retail analytics.
"""
    },

    "weak": {
        "name": "Rahul Gupta",
        "label": "Weak Candidate",
        "text": """
RAHUL GUPTA
Recent Graduate | Delhi, India
Email: rahul.gupta@email.com | LinkedIn: linkedin.com/in/rahulgupta

PROFESSIONAL SUMMARY
Recent B.Tech graduate looking for opportunities in the technology field. 
Completed coursework in programming and databases. Eager to learn and grow 
in a professional environment.

EXPERIENCE

Intern – IT Support | Local IT Solutions (2023, 3 months)
- Provided technical support for office hardware and software issues.
- Installed and configured Windows operating systems.
- Maintained inventory spreadsheets using Microsoft Excel.

EDUCATION
B.Tech in Electronics and Communication – MDU Rohtak (2023)

SKILLS
- Programming: Basic C, Basic Python (academic level)
- Tools: Microsoft Office (Word, Excel, PowerPoint)
- Web: Basic HTML, CSS
- Others: Manual Testing basics

PROJECTS (Academic)
- Student Management System – Built a basic CRUD application using C and 
  file handling (college project).
- Personal Portfolio Website – Created a static website using HTML and CSS.

EXTRA-CURRICULAR
- Volunteer at college tech fest (2022)
- Member of college cricket team
"""
    }
}
