
# AI-Enhanced Personalized Learning System

## Overview

The AI-Enhanced Personalized Learning System aims to revolutionize the educational experience by providing personalized learning paths, adaptive content, and real-time feedback using advanced AI and machine learning technologies. The system is designed to enhance student engagement and improve learning outcomes in educational institutions and online learning platforms.

## Features

- **Personalized Learning Paths**: Tailors educational content to individual student needs.
- **Adaptive Content**: Adjusts learning materials based on student performance and learning style.
- **Improved Engagement**: Increases student engagement through customized and interactive learning experiences.
- **Real-Time Feedback**: Provides immediate feedback to students, helping them understand their progress.
- **Enhanced Learning Outcomes**: Improves student performance by addressing individual strengths and weaknesses.
- **Data-Driven Insights**: Offers educators detailed analytics on student performance and areas for improvement.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Development Environment**: Windows/Linux
- **Server**: Apache (XAMPP) (Optional)

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- Flask
- MySQL Connector for Python

### Setting Up the Environment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ai-personalized-learning.git
   cd ai-personalized-learning
------------------------------------------------------------------------------------------------------

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`



-------------------------------------------------------------------------------------------------------
pip install flask mysql-connector-python

------------------------------------------
Configure the Database

Set up the MySQL database and tables as described in database_setup.sql.
Configure the Application

Update the config.py file with your database credentials:
class Config:
    SECRET_KEY = 'your-secret-key'
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'your-db-password'
    DB_NAME = 'learning_system'
-----------------------------------------------
Usage
Run the Flask Application
python app.py

-----------------------------------------------
Access the Application

Open your web browser and go to http://127.0.0.1:5000.
Navigate Through the Application

Home: The landing page of the application.
Profile: Submit and view student profiles.
Learning Module: View personalized learning content.
Development
Branching Strategy: Follow GitFlow for branching and merging.
Testing: Write unit tests and integration tests as needed.
Contributing
Fork the Repository
Create a New Branch
Commit Your Changes
Push to Your Fork
Submit a Pull Request


