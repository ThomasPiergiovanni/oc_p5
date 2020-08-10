# P5 - Utilisez les données publiques d'Open Food Facts!

## 1. Introduction.
This program is named **"HealthyProductApp"**. It consists of offering to "Pur Beurre", a French restaurant in Montmartre Paris, a solution for finding healthier food substitutes to products one is usually consuming. After having selected the product the user wants to find substitute for, the program presents to him/her a list of healthier substitutes. The user can then select a substitute and decide to record/register its choice for later review.  
Note that this program is designed for "Pur Beurre" users and its language is therefore french.

## 2. Prerequisite.
This program requires the following components:
* Python 3
* MySQL server 8.0
* mysql-connector-python==8.0.20
* requests==2.24.0

## 3. Installation.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best. 

### 3.2. Python 3 install.
Make sure you have Python 3 installed.  
> python3 --version

If not, you can download it and install it from the [python official website](https://www.python.org/). You will find the necessary documentation there.

### 3.3. MySQL server install and start.
Make sure to have MySQL server installed.
> mysql --version

If not you can download it from the [MySQL official website](https://www.mysql.com/).  

Once installed, make sure to have MySQL server running. Window users can check ths using the following statement in their bash:
> NET START mysql80

Please refer to the [MySQL official website](https://www.mysql.com/) for more information.

### 3.4. Create & activate a virtual environment (recommended).
In order to avoid system conflicts:

1. Go into your local repository and create a virtual environment using venv package.
> python3 -m venv env

2. Activate the virtual environment.
> source env/Scripts/activate

Documentation is also available on the [python official website](https://www.python.org/).

### 3.5. MySQL Connector and Requests install.
Install **MySQL connector** and **Requests** on you virtual environement using the requirements.txt file.

    pip install -r requirements.txt

Please refer to the [MySQL Connectors and API official website](https://dev.mysql.com/doc/index-connectors.html) for more information.  

Please refer to the [Requests certified documentation](https://requests.readthedocs.io/en/master/) for more information.  

### 3.6. Application mandatory settings.
1. Rename **configuration/env.py.example** file into **configuration/env.py**.
2. Change all constants with the appropriate value into **env.py**:
    * DATABASE_NAME = "my_db_name"
    * HOST = "my_host"
    * etc.  

For more information details on application settings, please check *4.1. env.py* section bellow.

### 3.7. Use "HealthyProductApp".
The program is now ready to use. You can start it using **main.py** with your bash.
> python3 main.py

For more information on the application uses, please check *5. Users' guide* section bellow.

### 3.8. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.9. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.

* Changing settings **must be** done in **env.py** file. Make sure to read *3.6. Application mandatory settings*.
* Changing settings **can be** done in **config.py** file.

### 4.1. env.py.
Located in **configuration/** package.

#### 4.1.1. DATABASE_NAME.
DESCRIPTION: The database name to use when connecting with the MySQL server.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "db_name".  
CUSTOM SETTINGS: Database name can be changed. Note that if a database using that name already exists, it will be overwritten.

#### 4.1.2. HOST.
DESCRIPTION: Host name i.e. The server on which MySQL is running.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "db_host".  
CUSTOM SETTINGS: Can be an IP address if the MySQL server is not the local machine.  
For more information, please check "https://dev.mysql.com/doc/connector-python/en/".

#### 4.1.3. USER.
DESCRIPTION: The user name used to authenticate with the MySQL server.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "db_user".  
CUSTOM SETTINGS: User must have at least the following MySQL privileges CREATE, DROP, EXECUTE, INSERT, REFERENCES, SELECT, and SHOW DATABASE.  
For more information, please check "https://dev.mysql.com/doc/connector-python/en/".  
For more information specifically on privileges, please check
"https://dev.mysql.com/doc/refman/5.7/en/grant.html#grant-privileges".

#### 4.1.4. PASSWORD.
DESCRIPTION: The password to authenticate the user with the MySQL server.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "db_password".  
CUSTOM SETTINGS: Must be the password of the user corresponding account.  
For more information, please check "https://dev.mysql.com/doc/connector-python/en/".

### 4.2. config.py.
Located in **configuration/** package.

#### 4.2.1. CATGEORIES_ENDPOINT.
DESCRIPTION: OpenFoodFacts (OFF) API categories list endpoint. It returns the categories list per country.   
MANDATORY: Yes.  
DEFAULT SETTINGS: "ht<span>tps://</span>fr.openfoodfacts.org/categories.json".  
CUSTOM SETTINGS: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/categories.json" for Spain).  
For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.2. PRODUCTS_ENDPOINT.
DESCRIPTION: OFF API products research functionality endpoint. It returns the product research functionality per country.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "ht<span>tps://</span>fr.openfoodfacts.org/cgi/search.pl".  
CUSTOM SETTINGS: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/cgi/search.pl").  
For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.3. HEADER.
DESCRIPTION: Headers, i.e. the application general information, among other, its name and version number.  
MANDATORY: Yes.  
DEFAULT SETTINGS: {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}.  
CUSTOM SETTINGS: If you modify this app this settings must be changed but keeping the following structure {'User-Agent': 'your information'}.  
For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.4. SELECTED_CATEGORIES.
DESCRIPTION: OFF API products categories type used in the application.  
MANDATORY: Yes.  
DEFAULT SETTINGS: ["en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals", "en:meals"].  
CUSTOM SETTINGS: Categories can be changed. Available values to use can be found on  "https://world.openfoodfacts.org/categories.json" in the
category "tags"/"id".  
For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.5. PRODUCTS_AMOUNT.
DESCRIPTION: Amount of product to get from OFF API per product category.  
MANDATORY: Yes.  
DEFAULT SETTINGS: 1000.  
CUSTOM SETTINGS: Can be changed but should not exceed 2000 to avoid upload failure.

## 5. Users' guide.

### 5.1. Program functionalities
This program provide the following functionalities:
* The user can select a product and the system returns back a list of substitutes (of the same category) having a better nutriscore grade (A-E).
* The user can see details about the selected substitute (e.g. nutriscore, stores where to buy it and the url with all details about the product). 
* The user can save its research. The system will store the pair (product & substitute) into the database.
* The user can see its recorded products & substitutes.
* The user can re-initiate the database in order to get the latest data from OFF API.

### 5.2. How to.
* Start the program running **main.py** (using the bash). 
* Select one of the options proposed in the and navigate as proposed by the system:
    * 1 - Search for healthier food substitute.
    * 2 - See your saved substitutes.
    * 3 - Reinitiate the database.
    * 4 - Quit the program.
* Use keyboard numbers to make your choice.
* Use keyboards "o"/ "n" letters (french for yes/no) to confirm some decisions.


*NB: the first time the program is used, the system will proceed to data upload and database initialization*.
