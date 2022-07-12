[![Run on Repl.it](https://repl.it/badge/github/GiviToo/Backend)](https://repl.it/github/GiviToo/Backend)
# GiviTo.me
A backend source code of Generasi Gigih 2.0 Capstonian Project

## How to run
1. Install virtualenv
```bash
pip install virtualenv
```
2. Create and activate virtualenv
```bash
virtualenv venv
source ./venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Migrate database
```bash
python3 manage.py migrate
```
5. Create superuser
```bash
python3 manage.py createsuperuser
```
6. Run server
```bash
python3 runserver localhost:8000
```
## Production Site
- [Main Site](https://givitoo.isnan.me "Main Site") 
- [API Endpoint](https://api.givitoo.isnan.me "API Endpoint")
- [Admin Dashboard](https://api.givitoo.isnan.me/admin "Admin Dashboard")
- [Documentation](https://docs.google.com/document/d/1LkiHrknyDJxfp2XZ6Ieqon531dBKE3I_V_pPXRJVuu0/edit?usp=sharing "Documentation")
