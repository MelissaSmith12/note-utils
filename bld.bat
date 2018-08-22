mkdir %PREFIX%\bin
if errorlevel 1 exit 1
xcopy %RECIPE_DIR%\src\* %PREFIX%\bin\
if errorlevel 1 exit 1