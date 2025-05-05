# Mix and Match

## Project Overview

**Mix and Match** is an app designed for first-year students, with a focus on international students who often arrive on campus alone, without existing friendships or family support. The main purpose of the app is to bring these students together and facilitate new friendships by generating groups from registered Students and assigning them collective tasks and on-campus activities.

The app is split into two sub-apps (Mix&Match Admin and Mix&Match Android App) and features 3 user types: Students, Mentors (Senior student volunteers) and Admins. Admins are meant to solely use the Mix&Match Admin, while Students and Mentors only use the Mix&Match Android App. The only exception is: Students must use the Mix&Match Admin Backend for initial registration (only once).

The Mix&Match Admin allows admins to perform Student/Mentor group formation, view students' details, view groups' details and generate tasks for the groups.

The Mix&Match Android App allows Students and Mentors to view other Students within their group and tasks assigned to their group. Additionally, a task completion and confirmation system is in place within group where Mentors can validate activities completed by the group's Students. The original version of the app envisioned messaging and task rewards functionality within each group, however, it was cut from the prototype due to time limitations.

---

## How to Run the Project

**Requirements:**  
- Python 3.12
- pip (Python package manager)

**Steps:**  
1. Open a terminal and navigate to the downloaded project directory.  
2. (Optional but recommended) Create and activate a virtual environment.  
3. Install the dependencies using pip and the `requirements.txt` file.  
4. Run the application using the `run.py` entry point.  
5. Access the application in your browser at [127.0.0.1:5000](http://127.0.0.1:5000).

---

## Languages and Frameworks Used

- **Programming Languages:** Python, HTML, CSS
- **Frameworks:** Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, SQLAlchemy, Jinja2, Bootstrap 5.0
- **Development Tools:** PyCharm, Visual Studio Cod 
- **Target Platforms:** Windows, macOS
- **Database:** SQLite

---

## Core functionalities
    
- ***Note:**
- **Student Registration:** Allows unregistered Students to validate their identity and register in the system by comparing a combination of username and student_id to the 1-st year student database (mock database used for prototype).
- **Group formation:** Gives admin users a button that assigns all non-grouped students into groups of 4 along with a 1 mentor (total 5), given enough students and mentors are available.
- **Mentor Tasks:** Mentors can create and validate tasks, as well as assign and approve rewards.  


## Secondary/Supporting functionalities
- **User Authentication/Login:** Users can log in with university credentials, which also define their role (administrator, mentor, or student). 
- **Student Tasks:** Students can view tasks and submit evidence of completion to potentially earn rewards. 
- **Home Page:** Serves as a portal to access group and task features.
---

## Contributors

- Arseniy Vasilko (2072309)  
- Charlotte Ashmore (2897025)  
- Gurjeevan Pannu (2897368)  
- Logesh Sharma Kalimuthan (2845496)  
- Mashrur Hossain Chowdhury Ritom (2867717)

*Each member contributed equally (20%).*