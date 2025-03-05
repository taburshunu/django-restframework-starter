# 🚀 Django REST Framework Starter  

## 📥 Getting the Files  

Download the zip file **or** use Git (requires Git to be installed):  

```sh
git clone https://github.com/taburshunu/django-restframework-starter/.git . && rm -rf .git

<br>
⚙️ Setup
🔹 1️⃣ Create a Virtual Environment
Linux & Mac

python3 -m venv venv  
source venv/bin/activate  

Windows

python3 -m venv venv  
.\venv\Scripts\activate.bat  

<br>
🔹 2️⃣ Install Dependencies

pip install --upgrade pip  
pip install -r requirements.txt  

<br>
🔹 3️⃣ Set Up PostgreSQL
🛠️ Install PostgreSQL (Skip if already installed)

    Arch Linux:

sudo pacman -S postgresql

Ubuntu/Debian:

    sudo apt update && sudo apt install postgresql postgresql-contrib

    Windows: Download from the official PostgreSQL site.

Start PostgreSQL:

sudo systemctl enable --now postgresql

<br>
📌 Create Database & User

Run:

sudo -u postgres psql

Inside psql, execute:

CREATE DATABASE mydatabase;  
CREATE USER myuser WITH PASSWORD 'mypassword';  
ALTER USER myuser WITH CREATEROLE CREATEDB;  
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;  
GRANT ALL ON SCHEMA public TO myuser;  
ALTER DATABASE mydatabase OWNER TO myuser;

Exit psql:

\q

<br>
🔧 Update Django Settings

Modify settings.py:

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'mydatabase',  
        'USER': 'myuser',  
        'PASSWORD': 'mypassword',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }  
}

<br>
🔹 4️⃣ Migrate Database

python manage.py migrate  
python manage.py createsuperuser  

<br>
🔹 5️⃣ Run Application

python manage.py runserver  

<br>
🔹 6️⃣ Generate Secret Key (For Deployment)

python manage.py shell
from django.core.management.utils import get_random_secret_key  
print(get_random_secret_key())  
exit()

Add this key to your .env or settings.py.
<br>
🛠 Troubleshooting
❌ "Permission denied for schema public"

Run inside psql:

GRANT ALL ON SCHEMA public TO myuser;

❌ PostgreSQL Service Not Running

Check the status:

sudo systemctl status postgresql

If it's inactive, start it:

sudo systemctl restart postgresql

💡 Need Help?

Open an issue in the repository! 🚀


Let me know if you need any modifications! 🚀