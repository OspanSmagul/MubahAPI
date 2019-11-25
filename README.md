# MubahAPI
API for Mubah app. 

In Terminal:

1) source ~/PythonRestMubah/Django01/bin/activate 

(либо: source ~/PythonRestMubah/Django01/bin/activate.csh)

(либо: source ~/PythonRestMubah/Django01/bin/activate.fish)

(либо: /PythonRestMubah/Django01/Scripts/activate.bat)

2) cd ~/PythonRestMubah/Django01/mubahAPIh

3) python manage.py runserver

------------------------------------------------------------------------------------------------------

In Browser or Postman (or some other app for api development)

4) http://127.0.0.1:8000/products/?q=Coca                 /*<-----Coca - ключевое слово, по которому производится поиск*/

4.1) http://127.0.0.1:8000/companies/?q=adal

4.2) http://127.0.0.1:8000/eNumber/?q=E233
