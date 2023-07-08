@echo off

@REM მოდულების დასაყენებლად წაუშალეთ ყველას @@REM  და ..\py\python.exe app.py დაუწერეთ წინ @REM

@REM py\python.exe get_pip.py


py\python.exe -m pip install flask

@REM py\python.exe -m pip install flask_sqlalchemy
@REM py\python.exe -m pip install PyQt5
@REM py\python.exe -m pip install pip install PyQtWebEngine
@REM py\python.exe -m pip install pip install pandas
@REM py\python.exe -m pip install pip install openpyxl
py\python.exe app.py




pause