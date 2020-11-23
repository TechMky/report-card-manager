# ReadMe

## Add these dependencies before running the project


* sqlalchemy
* mysqlclient
* rich
* PyInputPlus
* names

For Example `pip install rich`

## Create the Database in MySql

1.  Install MySql server and create a database with name 'report_card_manager'.
2.  Run the program ( as shown below ) and choose option '9' to seed the database with data.

## How to run the program

**Note: Make sure that you have created the Database as state above**

Go to the root directory of the project and execute the `app.py` python file.

For example:
```
PS H:\Projects\report_card_manager> python app.py
```

## Configurations

The file `config.py` contains variables to customized options like DB name, host, user and password etc.

Change these according to your needs if required.