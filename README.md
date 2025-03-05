# 🚀 Django REST Framework Starter  

## 📥 Getting the Files  

Download the zip file **or** use Git (requires Git to be installed):  

```sh
git clone https://github.com/taburshunu/django-restframework-starter.git . && rm -rf .git
```

---

## ⚙️ Setup  

### 🔹 1️⃣ Create a Virtual Environment  

#### Linux & Mac  
```sh
python3 -m venv venv  
source venv/bin/activate  
```

#### Windows  
```sh
python3 -m venv venv  
.env\Scriptsctivate.bat  
```

---

### 🔹 2️⃣ Install Dependencies  
```sh
pip install --upgrade pip  
pip install -r requirements.txt  
```

---

### 🔹 3️⃣ Set Up PostgreSQL  

#### 🛠️ Install PostgreSQL (Skip if already installed)  

**Arch Linux:**  
```sh
sudo pacman -S postgresql
```

**Ubuntu/Debian:**  
```sh
sudo apt update && sudo apt install postgresql postgresql-contrib
```

**Windows:** Download from the [official PostgreSQL site](https://www.postgresql.org/download/).  

#### Start PostgreSQL:  
```sh
sudo systemctl enable --now postgresql
```

---

### 📌 Create Database & User  

Run:  
```sh
sudo -u postgres psql
```

Inside psql, execute:  
```sql
CREATE DATABASE mydatabase;  
CREATE USER myuser WITH PASSWORD 'mypassword';  
ALTER USER myuser WITH CREATEROLE CREATEDB;  
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;  
GRANT ALL ON SCHEMA public TO myuser;  
ALTER DATABASE mydatabase OWNER TO myuser;
```

Exit psql:  
```sh
\q
```

---

### 🔧 Update Django Settings  

Modify `settings.py`:  

```python
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
```

---

### 🔹 4️⃣ Migrate Database  
```sh
python manage.py migrate  
python manage.py createsuperuser  
```

---

### 🔹 5️⃣ Run Application  
```sh
python manage.py runserver  
```

---

### 🔹 6️⃣ Generate Secret Key (For Deployment)  

```sh
python manage.py shell
```
Then, inside the shell:  
```python
from django.core.management.utils import get_random_secret_key  
print(get_random_secret_key())  
exit()
```

Add this key to your `.env` or `settings.py`.

---

## 🛠 Troubleshooting  

### ❌ "Permission denied for schema public"  
Run inside psql:  
```sql
GRANT ALL ON SCHEMA public TO myuser;
```

### ❌ PostgreSQL Service Not Running  
Check the status:  
```sh
sudo systemctl status postgresql
```
If it's inactive, start it:  
```sh
sudo systemctl restart postgresql
```

---

## 💡 Need Help?  
Open an issue in the repository! 🚀  
