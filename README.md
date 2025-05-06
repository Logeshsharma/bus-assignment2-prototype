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

- **Student Registration:** Allows unregistered Students to validate their identity and register in the system by comparing a combination of username and student_id to the 1-st year student database (mock database used for prototype). Once the student is registered, their "registered" field value is changed to True in "users" table, and they become eligible for Group Generation and using the Android App.
- **Group formation:** Gives admin users a button that assigns all non-grouped students into groups of 4 along with a 1 mentor (total 5), given enough students and mentors are available. Group is created in the database "groups" table and stores the names of all Students/Mentors in the group, as well as the group's progression status for every task "groupTaskStatuses".
- **Group task creation:** Admins can create tasks in the Mix&Match Admin through a form on the /create_task page. Tasks are then recorded into the database "tasks" table, and assigned to every existing group with each group's own task status being tracked in "groupTaskStatuses" table by using combination of task and group foreign keys.  
- **Task completion/validation** Students can mark the group task statuses as completed. Mentors can then validate the completion tasks in the app. All changes reflected in database's "groupTaskStatuses" table.
  - **Note:** A significant part of this functionality is implemented in the Android Mix&Match App, as Mentors and Students are meant to primarily use it. For more details about this functionality and implementation please refer to the Mix&Match Android App's documentation or view the source code at: https://github.com/Logeshsharma/bus-assignment2-moibleapp-prototype.git  


## Secondary/Supporting functionalities
- **User Authentication/Login:** Admins can log in to Mix&Match Admin with their credentials. Custom error messages are displayed if a Student/Mentor tries to log into the Mix&Match Admin.
- **User Logout:** Logs the current User out of the app.
- **Home Page:** Serves as a portal to access group and task features.
- **View Tasks:** Displays an overview of existing tasks in the system as a table.
- **Task Details:** Given a task id, displays a particular task's details including Task id, Description, Upload required status, and every group's completion status for that task as a table.
- **View Tasks:** Displays an overview of existing tasks in the system as a table.
- **Admin Account Panel:** Displays an overview of each User's details in the system including User Name, User SID, User Email, User Role, User Registration Status, Group ID as atable. Also the logged in Admin's Name, Account ID, and email address.
- **View All Groups:** Displays and overview of all groups in the system, including Group id, Student names and Mentor names as a table. Total number of groups displayed.
---

## Contributors

- Arseniy Vasilko (2072309)  
- Charlotte Ashmore (2897025)  
- Gurjeevan Pannu (2897368)  
- Logesh Sharma Kalimuthan (2845496)  
- Mashrur Hossain Chowdhury Ritom (2867717)

*Each member contributed equally (20%).*