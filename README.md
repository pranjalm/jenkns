# mmnyc-survey
Automation Code for survey

* Inside folder
* Tree  View
```
	├─── Automation_add.py
	├─── Automation_delete.py
	├─── Automation_update.py
	├─── chromedriver.exe
	├─── constants.py
	├─── survey_cred.json     (Expire in 15 days)
	├─── README.md
```
# Installation

* python
* package manager pip > [get-pip.py]

# Modules 

* selenium > [pip install -U selenium]
* oauth2client > [pip install oauth2client]
* gspread > [pip install gspread]

# Web driver

* To start a web browser, the Selenium module needs a web driver
* chromedriver.exe [https://chromedriver.chromium.org › downloads]

# Accessing Google Spreadsheet data using python

* Google API Manager [https://console.developers.google.com/]
* create new project
* google drive API enable 
* create some credentials
* downlode JSON file 
* open the JSON file in a text editor 
* inside JSON, take the email address from “client_email”.
* share spreadsheet with the email address to provide access.
* enable spreadsheet API

# Insert Data in Spreadsheet

* change the values of variables (data2Insert, insertIndex) in constants.py to insert the data in spreadsheet
* data2Insert [taka data in list form check the sample in constants.py]
* insertIndex [take row number; where to insert the data ]
* after that run Automation_add.py

# Update Data in Spreadsheet

* change values of variables (updateRowNumber, updateColNumber, updateValue) in constants.py to update the cell values
* updateRowNumber [take row number of sheet]
* updateColNumber [take column number of sheet]
* updateValue [take string; which we want to update in sheet]
* after that run Automation_update.py

# Delete Data from Spreadsheet

* change value of varaible (deleteRow) in constants.pyto delete the row from spreadsheet
* deleteRow [take row number; which we want to delete]
* after that run Automation_delete.py
