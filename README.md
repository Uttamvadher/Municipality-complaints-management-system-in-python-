# 🏩 Municipal Complaint System (MCS)  
### A Python Project for Dharmsinh Desai University (BCA - Semester 4)  

## 📌 Project Overview  
The **Municipal Complaint System (MCS)** is a Python-based application designed to streamline the process of lodging and managing municipal complaints. This project provides an efficient platform for residents to report issues related to infrastructure, sanitation, water supply, and other public services. The system ensures that complaints are tracked, managed, and resolved efficiently by the municipal authorities.  

## 🚀 Features  
✅ **User Registration & Authentication** – Secure login system for users and administrators.  
✅ **Complaint Submission** – Users can file complaints with category selection and descriptions.  
✅ **Status Tracking** – Users can check the status of their complaints in real-time.  
✅ **Admin Dashboard** – Authorities can view, assign, and update complaint statuses.  
✅ **Search & Filter** – Users and admins can search complaints by ID, category, or status.  
✅ **Feedback System** – Users can provide feedback after complaint resolution.  

## 🛠 Technologies Used  
- **Python** – Core programming language  
- **Django / Flask** – Web framework (if applicable)  
- **SQLite / MySQL** – Database for storing complaints and user data  
- **HTML, CSS, JavaScript** – Frontend for user interface  
- **Bootstrap** – Responsive design (if applicable)  

## 📂 Project Structure  
Django Project Root
│   manage.py                     # Django management script
│   structure.txt                  # Project structure file
│
├── mcs/                           # Main project settings directory
│   ├── asgi.py                    # ASGI configuration
│   ├── settings.py                # Project settings
│   ├── urls.py                     # URL configurations
│   ├── wsgi.py                    # WSGI configuration
│   ├── __init__.py                 # Init file for module recognition
│   ├── __pycache__/                 # Compiled Python files
│
├── mcsapp/                         # Main application
│   ├── apps.py                     # Application configuration
│   ├── models.py                   # Database models
│   ├── urls.py                     # Application-specific URL patterns
│   ├── views.py                    # Business logic and views
│   ├── __init__.py                  # Module recognition file
│   ├── __pycache__/                  # Compiled Python files
│   │
│   ├── migrations/                  # Database migration files
│   │   ├── 0001_initial.py           # Initial migration
│   │   ├── 0002_alter_complaint_department.py 
│   │   ├── 0003_admintoken_user_admin_user_is_resolved.py
│   │   ├── 0004_user_token.py
│   │   ├── 0005_alter_user_token.py
│   │   ├── __init__.py
│   │   ├── __pycache__/              # Compiled migration files
│   │
│   ├── static/                        # Static files (CSS, JS, Images)
│   │   ├── css/
│   │   │   ├── styles.css             # Stylesheet
│   │
│   ├── templates/                      # HTML templates
│   │   ├── app/                         # Templates for complaints module
│   │   │   ├── analysis.html
│   │   │   ├── complaint_form.html
│   │   │   ├── home.html
│   │   │   ├── password_protect.html
│   │   │   ├── view_complaints.html
│   │   │
│   │   ├── reg/                         # Templates for user registration & auth
│   │   │   ├── login.html
│   │   │   ├── usr_reg.html
│
└── __pycache__/                        # Compiled Python files


## 🎯 Objectives  
- Improve municipal governance by providing a digital complaint management system.  
- Reduce delays in addressing public complaints.  
- Provide transparency in complaint resolution.  

## 📌 Installation & Setup  
1⃣ Clone the repository:  
   ```bash
   git clone https://github.com/your-username/municipal-complaint-system.git
   cd municipal-complaint-system
   ```  
2⃣ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3⃣ Run the application:  
   ```bash
   python manage.py runserver
   ```  

## 📢 Contributing  
Feel free to contribute by submitting issues or feature requests!  

## 🏆 Acknowledgments  
This project was developed as part of **BCA Semester 4 Python Project** at **Dharmsinh Desai University**.  

