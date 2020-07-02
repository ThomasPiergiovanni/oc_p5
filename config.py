#-*-coding:utf-8 -*
"""Programm congiguration file"""

# Description:OpenFoodActs categories endpoint.
# Mandatory : Yes.
# Settings: "https://fr-en.openfoodfacts.org/categories.json" (default).
# Comments: Endpoint return the products categories list.
CATEGORIES_ENDPOINT = "https://fr-en.openfoodfacts.org/categories.json"

# Description:Headers.
# Mandatory : Yes.
# Settings: {'User-Agent': 'ThomasApp - Web - Version 0.0'} (default).
# Comments: Application general inforamtions.
HEADER = {'User-Agent': 'ThomasApp - Web - Version 0.0'}

# Description:Database name.
# Mandatory : Yes.
# Settings: project_5 (default).
# Comments: Can be changed. If a database with that name already exist, it will be overwritten.
HOST= "project_5"

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
# Comments: Shou.
SELECTED_CATEGORIES= ["en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals","en:meals"]
