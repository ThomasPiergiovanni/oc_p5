#-*-coding:utf-8 -*
"""Programm congiguration file"""

# Description:OpenFoodActs categories endpoint.
# Mandatory : Yes.
# Settings: "https://fr-en.openfoodfacts.org/categories.json" (default).
# Comments: Endpoint return the products categories list.
CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"

# Description:OpenFoodActs products per category ENDPOINT.
# Mandatory : Yes.
# Settings: "https://fr-en.openfoodfacts.org/categories.json" (default).
# Comments: Endpoint return the products categories list.
PRODUCTS_ENDPOINT= "https://fr.openfoodfacts.org/cgi/search.pl"

# Description:Headers.
# Mandatory : Yes.
# Settings: {'User-Agent': 'ThomasApp - Web - Version 0.0'} (default).
# Comments: Application general inforamtions.
HEADER = {'User-Agent': 'ThomasApp - Web - Version 0.0'}

# Description:Database name.
# Mandatory : Yes.
# Settings: project_5 (default).
# Comments: Can be changed. If a database with that name already exist, it will be overwritten.
DATABASE_NAME= "project_6"

# Description:Host server.
# Mandatory : Yes.
# Settings: localhost (default).
# Comments: Can be changed if server is not on local machine.
HOST= "localhost"

# Description: Username for DB connection.
# Mandatory : Yes.
# Settings: root (default).
# Comments: username.
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
