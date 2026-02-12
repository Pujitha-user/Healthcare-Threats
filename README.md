# Healthcare Threats - Modeling, Detecting, and Mitigating

A Django-based web application for modeling, detecting, and mitigating threats against healthcare systems using machine learning and data analysis.

## 🚀 Quick Start

### Method 1: Easiest - Double Click Batch File

1. Simply double-click on: `START_PROJECT.bat`
2. Server will start automatically at: http://127.0.0.1:8000/
3. Press `Ctrl+C` to stop the server when done

### Method 2: Using Command Prompt (CMD)

```bash
cd C:\Modeling
env\Scripts\activate.bat
cd "Modeling, Detecting, and Mitigating Threats Against\Modeling_Detecting_and_Mitigating_Threats\modeling_detecting_and_mitigating_threats"
python run_server_new.py
```

### Method 3: Using PowerShell

```powershell
cd C:\Modeling
.\env\Scripts\Activate.ps1
cd "Modeling, Detecting, and Mitigating Threats Against\Modeling_Detecting_and_Mitigating_Threats\modeling_detecting_and_mitigating_threats"
& "C:\Modeling\env\Scripts\python.exe" run_server_new.py
```

## 📋 Prerequisites

- Python 3.10
- MySQL Server
- Virtual Environment (included in `env/` folder)

##  Login Credentials

### Database Credentials
- **Host:** 127.0.0.1
- **Port:** 3306
- **Database:** modeling_detecting_and_mitigating_threats
- **Username:** your user name
- **Password:** your password

### Service Provider Login
- **URL:** http://127.0.0.1:8000/serviceproviderlogin/
- **Username:** ****
- **Password:** ****

### Remote User Accounts (Pre-registered)
1. **Username:** Rajesh | **Password:** Rajesh | **Email:** Rajesh123@gmail.com
2. **Username:** Manjunath | **Password:** Manjunath | **Email:** tmksmanju13@gmail.com
3. **Username:** tmksmanju | **Password:** tmksmanju | **Email:** tmksmanju13@gmail.com

##  Dependencies

The project uses the following main packages:
- Django 3.2.25
- pandas 2.3.3
- numpy 2.2.6
- scikit-learn 1.7.2
- scipy 1.15.3
- mysqlclient 2.2.7
- joblib 1.5.3

##  Project Structure

```
C:\Modeling\
├── env/                                    # Virtual environment
├── START_PROJECT.bat                       # Quick start batch file
├── QUICK_START_GUIDE.txt                   # Detailed setup guide
└── Modeling, Detecting, and Mitigating Threats Against/
    └── Modeling_Detecting_and_Mitigating_Threats/
        └── modeling_detecting_and_mitigating_threats/
            ├── manage.py                   # Django management script
            ├── requirements.txt            # Python dependencies
            ├── Healthcare_Datasets.csv     # Healthcare data
            ├── labeled_data.csv           # Training data
            ├── modeling_detecting_and_mitigating_threats/  # Main app
            ├── Remote_User/               # Remote user module
            ├── Service_Provider/          # Service provider module
            └── Template/                  # HTML templates
```

##  Important Notes

1. **MySQL must be running** before starting the Django server
2. The virtual environment is located at: `C:\Modeling\env\`
3. Always activate the virtual environment before running Django commands
4. Press `Ctrl+C` in the terminal to stop the server
5. Registration issue has been fixed - new users will now register successfully

##  Troubleshooting

### Server doesn't start
- Check if MySQL is running
- Verify database credentials in settings.py
- Ensure virtual environment is activated
- Check for any error messages in the terminal

### "Python not found" error
- Always activate virtual environment first
- Use full path: `C:\Modeling\env\Scripts\python.exe`

##  Features

- Healthcare threat detection using machine learning
- User authentication and authorization
- Service provider dashboard
- Remote user interface
- Data analysis and visualization
- Threat modeling and mitigation strategies

##  License

This project is for educational and research purposes.

##  Contributors

Vangala Pujitha

---

**Server URL:** http://127.0.0.1:8000/

**Note:** Make sure to configure your database settings before the first run.
