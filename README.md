# GiviTo.me
A backend source code of Generasi Gigih 2.0 Capstonian Project

## How to run
1. Install virtualenv
`python3 -m pip install virtualenv`
2. Create and activate virtualenv
`python3 -m virtualenv venv`
`source ./venv/bin/activate`
3. Install dependencies
`python3 -m pip install -r requirements.txt`
4. Migrate database
`python3 manage.py migrate`
5. Create superuser
`python3 manage.py createsuperuser`
6. Run server
`python3 runserver localhost:8000`

## Production Site
- [Main Site](https://givitoo.isnan.me "Main Site") 
- [API Endpoint](https://api.givitoo.isnan.me "API Endpoint")
- [Admin Dashboard](https://api.givitoo.isnan.me/admin "Admin Dashboard")
- [Documentation](https://docs.google.com/document/d/1LkiHrknyDJxfp2XZ6Ieqon531dBKE3I_V_pPXRJVuu0/edit?usp=sharing "Documentation")