## StudyBuddy
by eric talbot

# 1. Overview:
### i. Basics
The goal of StudyBuddy is to create both a directory and interface for users to instantly locate and connect safely with qualified private tutors in their area at any time, and at an affordable cost.

### ii. Features, Frameworks, Fun
#### a. Features
Below is a list of the main features I plan to implement throughout the development process:

**General**
- desktop & mobile functionality
- geo-location
- desktop/ push notifications
- calendar for both tutors & students
- & more

**Users**
- user registration/ login & authentication
- user profile & information (account)
- user payment methods & information
- search bar for tutors, subjects, areas, etc
- save personal lists of preferred & less preferred tutors & areas of study that can be referenced at any time
- compare/ contrast feature for tutors
- & more

**Tutors**
- tutor registration/ login & authentication
- tutor profile & information (account)
- tutor compensation methods & information
- search bar for students, areas, etc
- save list of students worked with & currently working with
- keep track of lessons taught, frequency, duration
- draft, send, & save student evaluations
- & more

#### b. Frameworks & Fun
Frameworks, Languages, Libraries, APIs, etc to be used are as follows:

- python
- html5
- css
- javascript
- django
- jQuery
- vue.js
- wyzant app API
- facebook API for login w facebook?
- google maps geo-locator
- others TBD

*^items subject to change without notice*

# 2. Functionality
The following section in its current form is meant to theorize and outline the functionality of this project from both student and tutor perspectives.

### i. Students
#### a. Registration & Login
1. User will be brought to landing page, which will have a registration/ login field and will be able to login using their email address or facebook.
2. User will then be asked for some basic but pertinent information (i.e. areas of study, location, age, name, online or in person lessons, reasons for seeking tutoring in subject etc.) data will be saved to user profile which may be edited later.
3. Once user info is entered and saved, they can continue filling in other info on their profile (i.e. hobbies, interests, bio, etc). This data will also be saved.
4. User will be brought to their 'Dashboard,' which will display only the users most relevant information: Profile, Lessons, Subjects, Tutors, Calendar, Messages. User will navigate from here.

#### b. Dashboard
So far, the dashboard will consist of 6 fields: Profile, Lessons, Subjects, Tutors, Calendar, and Messages.
- **Profile:** When clicked, will bring the user to their profile, where they can add/ update/ delete information.
- **Lessons:** Record of the users recent lessons organized chronologically, with date/ time, subject, tutor, and duration of the lesson.
- **Subjects:** Subjects that the user has already expressed interest in will be saved here for future reference. User can also search and add more subjects to their list from here. Each subject tab will redirect to the Tutor selector for that particular subject.
- **Tutors:** Will display a list of tutors & bios that the user has worked with by date/time, frequency & duration. User will be able to search tutors by subject, price, distance, availability, etc. and add to a list of prospectives to compare.
- **Calendar:** Standard calendar for the user that will sync with the tutors calendar upon confirmation, update, or deletion of an appointment or scheduled lesson.
- **Messages:** Messenger for student and teacher to correspond.

### ii. Tutors
#### a. Registration & Login
This part (assuming I get to it) will be similar to the student-side R & L but a bit different in a few ways. For one, tutors wont need a tutor tab on their end, but a student one. Secondly, The registration information being requested will have to authenticate their employment and/ or teaching experience & credentials. Tutors without formal credentials will have to formally request that an exception be made. The subjects tab will also work a bit differently as well, and wil be used to track what subjects a particular tutor is interested and/ or available to teach. They will be asked to present the necessary credentials and upon verification, the subject will be added to their list of available ones to tutor.

#### b. Dashboard
The Dashboard for Tutors will consist of the following fields: Profile, Lessons, Subjects, Students, Calendar, and Messages.
- **Profile:** When clicked, will bring the user to their profile, where they can add/ update/ delete information.
- **Lessons:** Record of the tutors recent lessons organized chronologically, with date/ time, subject, student, and duration of the lesson.
- **Subjects:** List of subjects that the tutor is qualified to and interested in teaching. Can be changed with verification & approval. 
- **Students:** List of students under ones tutelage & bios, sorted by name/ subject/ frequency etc.
- **Calendar:** Standard calendar for the tutor that will sync with the users calendar upon confirmation, update, or deletion of an appointment or scheduled lesson.
- **Messages:** Same as student.

### iii. General Notes
Ideally, I'd like to try to make this an SPA, but if that cant work out, I want to try and emphasize very minimalist design for this project, both aesthetically and functionally for user-friendliness and ease of interpretation. I want to present all relevant and desired information to the user as simply and as clearly as possible without overwhelming them, but I also want them to get the most out of the application with minimal usage- because as always, time is of the essence.

# 3. Data Model
Below is a list of all of the data fields that will need to be stored and used for students and tutors in their experience of the application:

**Students & Tutors**

- User
- User Status (Student/ Tutor)
- DOB (mm/dd/yyyy)
- Phone Number
- E- Mail Address
- Address
- City
- State
- Country
- Zip
- Bio
- Sex
- Gender
- Race/ Ethnicity
- Profile Photo
- Current/ Highest Level of Education
- Employment Status
- Subject/s of Study/ Interest
- Availability
- Payment Information
- Lessons Scheduled: Date/ Time, Tutor/ Student, Price, Duration, etc
- Lessons Taken (completed):  Date/ Time, Tutor/ Student, Price, Duration, etc
- Message History??
- Online/ Live Tutor Preference
- Private/ Public Live Tutor Meeting Preference
- Student Max Budget/ Tutor Min Compensation Price
- *other relevant information im probably missing*

# 4. Schedule
The tentative schedule for this seemingly over-ambitious project of mine:

**1. Week One:**
- Research
- Build back-end in Django and construct database, data relations, and server communications for a student user to register/ log in. Make sure all fields are accessible and can store data as intended
- Once user is able to log in and all database tables are constructed, build out the back end of the Dashboard.

**2. Week Two:**
- Finish & finalize dashboard operations, forms, & data exchanges. Fix errors & work out kinks.
- Work on javascript operations & functionality & presentation
- Start working on CSS/ HTML

**3. Week Three:**
- Finish & polish everything from top to bottom. Add additional features if time allows.
- Test & Fix Errors.
- Test & Fix Errors again.
