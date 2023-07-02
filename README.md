

<img src="intro.gif" style="max-width:100% !important "></img>


## Description

This is template for making windows software with **html,css,js** and **Python** as backend. At first I used Flask for making simple registration verification user information gathering aplication and then I added GUI with using **PyQt5**.

Using PyQt we have urls to flask websites and using as tabs in my application.  Urls are in localhost server and You can use your ip for going to that websites with smartphone, pc or laptop devices.

If you want to use that devices:
* Write command in terminal (CMD)
```cmd 
ipconfig
```
* Get IP4 address
* And use url https://your-ip-address:5000 

aplication has id and phone validation as well as  user management panel with search, also, its exporting data to excel "user_data.xlsx" file every time you adding users.

## To Build
At first you need to install following modules

```bash
pip install PyQt5
pip install flask
pip install sqlalchemy
pip install pandas
```


```bash
pip install pyinstaller
pyinstaller --distpath . app.py
```

## To Run

* from dist folder copy app.exe next to main.py file
* run app.exe 


