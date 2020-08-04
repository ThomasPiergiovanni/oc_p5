# P5 - Utilisez les données publiques d'Open Food Facts

*UNDER CONSTRUCTION*

## 1. Introduction.
This program is named **"HealthyProductApp"**. It consists of offering to "Pur Beurre", a French restaurant in Montmartre Paris, a solution for finding healthier food substitutes to products one is usually consuming. After having selected the product the user wants to find substitute for, the program presents to him/her a list of healthier substitutes. The user can then select a substitute and decide to record/register its choice for later review..

## 2. Prerequisite.
This program requires the following components:
* python 3
* requests==2.24.0
* mysql-connector-python==8.0.20

## 3. Installation.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best. 

### 3.2. Python 3 install.
Make sure you have Python 3 installed. If not, you can download it and install it from the [python offical website](https://www.python.org/). You'll find the necessary documentation there.

### 3.3. Create & activate a virtual environnement (recommended).
In order to avoid system conflicts:

1. Go into your local repository and create a virtual environment using venv package.
> python3 -m venv env

2. Activate the virtual envrionment.
> source env/Scripts/activate

Documentation is also available on the [python offical website](https://www.python.org/).

### 3.4. MySQL server install.
Make sure to have MySQL server installed. If not you can download it from the [MySQL official website](https://www.mysql.com/).

### 3.5. MySQL server start.
Make sure to have MySQL server running. Please refer to the [MySQL official website](https://www.mysql.com/) for this.

### 3.6. Application mandatory settings.
1. Rename env.py.example.txt file into env.py
2. Change all constants with the approporiate value into env.py(e.g. the appropirate DB_NAME, DB_USER_NAME, etc.)
For more informations details on application setting, check the detailed section bellow.

### 3.7. Use "HealthyProductApp".
The programm is now ready to use. You can start it using **main.py** with your bash.
> python3 main.py


### 3.8. Deactivate the virtual environnement.
Once you're done using the programm, you should leave the virtual environement. Simply type the following statement in your bash.
> deactivate

### 3.9. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.

* Changing settings must be done in **program/admin/env.py** file. Make sure to read *3.6. Application mandoatory settings* section first.
* Changing settings can be done to the following constants in **program/admin/config.py** file.

### 4.1. env.py.

#### 4.1.1. DATABASE_NAME.
**DESCRIPTION**: The database name to use when connecting with the MySQL server.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "HPA" (HealthyProductApp).  
**CUSTOM SETTINGS**: Can be changed. Note that if a database using that name already exists, it will be overwritten.

#### 4.1.2. HOST.
**DESCRIPTION**: Host name i.e. The server on which MySQL is running.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "localhost".  
**CUSTOM SETTINGS**: Can be changed if different. Can be an IP address as well if the MySQL server is not the local machine. For more information, please check [MySQL connector API official website](https://dev.mysql.com/doc/connector-python/en/).

#### 4.1.3. USER.
**DESCRIPTION**: The user name used to authenticate with the MySQL server.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "root".  
**CUSTOM SETTINGS**: User must have at least the following MySQL privileges CREATE, DROP, EXECUTE, INSERT, REFERENCES, SELECT, and SHOW DATABASE. For more information, please check [MySQL connector API official website](https://dev.mysql.com/doc/connector-python/en/). For more information specifically on privileges, please check [MySQL official website](https://www.mysql.com/).

#### 4.1.4. PASSWORD.
**DESCRIPTION**: The password to authenticate the user with the MySQL server.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: root.  
**CUSTOM SETTINGS**: Must be the password of the user's corresponding account.
For more information, please check [MySQL connector API official website](https://dev.mysql.com/doc/connector-python/en/)

### 4.2. config.py.

#### 4.2.1. CATGEORIES_ENDPOINT.
**DESCRIPTION**: OpenFoodFacts (OFF) API categories list endpoint. It returns the categories list per country.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "ht<span>tps://</span>fr.openfoodfacts.org/categories.json".  
**CUSTOM SETTINGS**: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/categories.json" for Spain). For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.2. PRODUCTS_ENDPOINT.
**DESCRIPTION**: OFF API products research functionality endpoint. It returns the product research functionality per country.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "ht<span>tps://</span>fr.openfoodfacts.org/cgi/search.pl".  
**CUSTOM SETTINGS**: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/cgi/search.pl"). For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.3. HEADER.
**DESCRIPTION**: Headers, i.e. the application general informations, among other, its name and version number.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}.  
**CUSTOM SETTINGS**: Iy ou modify this app this settings must be changed but keeping the following structure {'User-Agent': 'your information'}. For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.4. SELECTED_CATEGORIES.
**DESCRIPTION**: OFF API products categories type used in the application.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: ["en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals", "en:meals"].  
**CUSTOM SETTINGS**: Categories can be changed. Available values to use can be found on  "https://world.openfoodfacts.org/categories.json" in the
category "tags"/"id". For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

#### 4.2.5. PRODUCTS_AMOUNT.
**DESCRIPTION**: Amount of product to get from OFF API per product category.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: 1000.  
**CUSTOM SETTINGS**: Can be changed but should not exceed 2000 to avoid upload failure.

## 5. User guide.

### 5.1. Program functionalities
This program provide the following functionalities:
* The user can select a product and the system returns back a list of substititutes (of the same catagory) having a better nutriscore grade (A-E).
* The user can see details about the selected substitute (e.g. nutriscore, stores where to buy it and the url with all details about the product). 
* The user can save its research. The system will store the pair (product & substitute) into the database.
* The user can see its recorded products & substitutes.
* The user can re-initiate the database in order to get the latests datas from OFF API.

### 5.2. How to.
* Start the program running **main.py** (using the bash). 
* Select one of the options proposed in the and navigate as proposed by the system:
    * 1 - Search for healthier food substitute.
    * 2 - See your saved substitutes.
    * 3 - Reinitiate the database.
    * 4 - Quit the program.  
* Use keyboard numbers to make your choice.
* Use keyboards "y"/ "n" letters to confirm some decisions.

  
*NB: the first time the program is used, the system will proceed to datas upload and database initialization*.