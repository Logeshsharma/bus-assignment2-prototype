# Mix and Match

## Project Overview

**Mix and Match** is an app designed primarily for first-year students, whether undergraduate or postgraduate, with a particular focus on international students who often arrive on campus alone, without existing friendships or family support.

The app groups students together, each group supervised by an assigned mentor. These groups receive designated tasks that help students integrate into the university community. Mentors assign and monitor tasks, and students who complete them receive rewards. Task completion is verified by the evidence students upload within the app.

Additionally, the app promotes social events, such as those organized by university student societies, with the goal of further helping students settle in and build new friendships.

The app also offers an in-app messaging service to foster connections within each group, ensuring every member builds at least a few friendships to help them acclimate to university life.

---

## How to Run the Project

**Requirements:**  
- Python 3.7+  
- pip (Python package manager)

**Steps:**  
1. Open a terminal and navigate to the downloaded project directory.  
2. (Optional but recommended) Create and activate a virtual environment.  
3. Install the dependencies using pip and the `requirements.txt` file.  
4. Run the application using the `run.py` entry point.  
5. Access the application in your browser at [127.0.0.1:5000](http://127.0.0.1:5000).

---

## Languages and Frameworks Used

- **Programming Languages:** HTML, Python  
- **Frameworks:** Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, SQLAlchemy, Gunicorn  
- **Development Tools:** PyCharm, Visual Studio Code  
- **Target Platforms:** Windows, macOS

---

## Added Functionalities

- **User Authentication:** Users can log in with university credentials, which also define their role (administrator, mentor, or student).  
- **Grouping of Students:** Randomly assigns students to groups along with a mentor.  
- **Student Tasks:** Students can view tasks and submit evidence of completion to potentially earn rewards.  
- **Mentor Tasks:** Mentors can create and validate tasks, as well as assign and approve rewards.  
- **Home Page:** Serves as a portal to access group and task features.

---

## Contributors

- Arseniy Vasilko (2072309)  
- Charlotte Ashmore (2897025)  
- Gurjeevan Pannu (2897368)  
- Logesh Sharma Kalimuthan (2845496)  
- Mashrur Hossain Chowdhury Ritom (2867717)

*Each member contributed equally (20%).*
---

## TEST CASES FOR ADDED FUNCTIONALITIES

### User Authentication

| Test Type  | Inputs                                                            | Expected Output                                                       |
|------------|------------------------------------------------------------------|----------------------------------------------------------------------|
| Positive   | Valid university email `student@university.ac.uk`, correct password | User is successfully logged in and directed to appropriate dashboard (student, mentor, or admin) |
| Negative   | Invalid email `notarealuser@gmail.com`, wrong password            | Authentication fails, user sees error message “Invalid credentials”    |

### Grouping of Students

| Test Type  | Inputs                                    | Expected Output                                                          |
|------------|------------------------------------------|--------------------------------------------------------------------------|
| Positive   | 10 newly registered students without assigned groups | Students are randomly grouped into 2 groups of 5 with one mentor each      |
| Negative   | 0 students available for grouping        | System shows message “No students available to group”                     |

### Task – Student

| Test Type  | Inputs                                         | Expected Output                                              |
|------------|-----------------------------------------------|--------------------------------------------------------------|
| Positive   | Student uploads a photo as evidence for a “Join a club” task | Evidence is saved, task status updates to “Pending approval”  |
| Negative   | Student tries to submit evidence without uploading a file   | Error message “Please upload evidence to submit”             |

### Tasks – Mentor

| Test Type  | Inputs                                                           | Expected Output                                            |
|------------|-----------------------------------------------------------------|------------------------------------------------------------|
| Positive   | Mentor creates task “Attend a campus tour” with deadline and reward points | Task appears in all assigned student dashboards             |
| Negative   | Mentor attempts to approve a task with no evidence submitted     | Error message “Cannot approve task without evidence”        |

### Home Page

| Test Type  | Inputs                                  | Expected Output                                                      |
|------------|----------------------------------------|----------------------------------------------------------------------|
| Positive   | User logs in and clicks “Home”         | User sees dashboard with group members, task list, and messages       |
| Negative   | Server is down, user tries to load Home page | Error message “Unable to load homepage. Please try again later.”      |
