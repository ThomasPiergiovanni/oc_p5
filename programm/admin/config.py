#-*-coding:utf-8 -*
"""Programm congiguration file"""

# Description: OpenFoodActs categories endpoint. It returns
# the categories list.
# Mandatory : Yes.
# Default settings: "https://fr-en.openfoodfacts.org/categories.json".
# Comments: Default settings cannot be modified. For more information
# on the API endpoint please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"

# Description: OpenFoodActs products endpoint.It return the
# products per category list.
# Mandatory : Yes.
# Default settings: "https://fr.openfoodfacts.org/cgi/search.pl".
# Comments: Default settings cannot be modified. For more information
# on the API endpoint please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
PRODUCTS_ENDPOINT= "https://fr.openfoodfacts.org/cgi/search.pl"


# Description: Headers, i.e. the application general informations, among other,
# its name and version number.
# Mandatory : Yes.
# Default settings: {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}.
# Comments: Settings can be changed but must kee the following structure
# {'User-Agent': 'your informations'}
HEADER = {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}

# Description: The database name you want to use for the application.
# Mandatory : Yes.
# Default settings: "HPA" (HealthyProduuctApp).
# Comments: Can be changed. Note that if a database using that name already
# exists, it will be overwritten.
DATABASE_NAME= "project_6"

# Description: Host name i.e. The server on which MySQL is running.
# Mandatory : Yes.
# Default settings: "localhost".
# Comments: Can be an IP adress as well if the MySQL server is not the 
# local machine. Please check "https://dev.mysql.com/doc/connector-python/en/"
# for more informations.
HOST= "localhost"

# Description: The user name used to authenticate with the MySQL server.
# Mandatory : Yes.
# Default settings: "root".
# Comments: Can be changed but user must have at least the following MySQL privileges:
# CREATE, DROP, EXECUTE, INSERT, REFERENCES, SELECT, SHOW DATABASE. 
# Please check "https://dev.mysql.com/doc/refman/5.7/en/grant.html#grant-privileges"
# for more informations on privilveges.
USER= "root"

# Description: Password for DB connection.
# Mandatory : Yes.
# Settings: root (default).
# Comments: username.
PASSWORD= "root"

# Description: SQL file for database creation.
# Mandatory : Yes.
# Settings: "create_database.sql" (default).
# Comments: Shou.
SQL_FILE= "create_database.sql"

# Description: Product categories used.
# Mandatory : Yes.
# Settings: ["en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals","en:meals"] (default).
# Comments: MUST contain 5 catgories.
SELECTED_CATEGORIES= ["en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals","en:meals"]

# Description: Maximum amount of product to store in DB per product category.
# Mandatory : Yes.
# Settings: 1000 (default).
# Comments: Shou.
PRODUCTS_AMOUNT= 10
