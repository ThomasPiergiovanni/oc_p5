#-*-coding:utf-8 -*
"""Program configuration file
"""

# DESCRIPTION: OpenFoodFacts (OFF) API categories list endpoint. It returns
# the categories list per country.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/categories.json".
# CUSTOM SETTINGS: To change the country, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/categories.json" for Spain).
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"

# DESCRIPTION: OFF API products research functionality endpoint.
# It returns the product research functionality per country.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/cgi/search.pl".
# CUSTOM SETTINGS: To change the country, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/cgi/search.pl").
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
PRODUCTS_ENDPOINT = "https://fr.openfoodfacts.org/cgi/search.pl"

# DESCRIPTION: Headers, i.e. the application general informations, among other,
# its name and version number.
# MANDATORY: Yes.
# DEFAULT SETTINGS: {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}.
# CUSTOM SETTINGS: Settings can be changed but must keep the following
# structure {'User-Agent': 'your information'}.
# For more information, please check "https://documenter.getpostman.
# com/view/8470508/SVtN3Wzy?version=latest#intro".
HEADER = {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}

# DESCRIPTION: The database name to use when connecting with the MySQL server.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "HPA" (HealthyProduuctApp).
# COMMENTS: Can be changed. Note that if a database using that name already
# exists, it will be overwritten.
DATABASE_NAME = "HPA"

# DESCRIPTION: Host name i.e. The server on which MySQL is running.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "localhost".
# CUSTOM SETTINGS: Can be changed. Can be an IP address as well if the
# MySQL server is not the local machine.
# For more information, please check "https://dev.mysql.
# com/doc/connector-python/en/".
HOST = "localhost"

# DESCRIPTION: The user name used to authenticate with the MySQL server.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "root".
# CUSTOM SETTINGS: User must have at least the following MySQL
# privileges CREATE, DROP, EXECUTE, INSERT, REFERENCES, SELECT,
# and SHOW DATABASE.
# For more information, please check "https://dev.mysql.
# com/doc/connector-python/en/".
# For more information specifically on privileges, please check
# "https://dev.mysql.com/doc/refman/5.7/en/grant.html#grant-privileges".
USER = "root"

# DESCRIPTION: The password to authenticate the user with the MySQL server.
# MANDATORY: Yes.
# DEFAULT SETTINGS: root.
# CUSTOM SETTINGS: Must be the password of the user corresponding account.
# For more information, please check "https://dev.mysql.
# com/doc/connector-python/en/".
PASSWORD = "root"

# DESCRIPTION: OFF API products categories type used in the application.
# MANDATORY: Yes.
# DEFAULT SETTINGS: ["en:snacks", "en:desserts", "en:breads",
# "en:breakfast-cereals", "en:meals"].
# CUSTOM SETTINGS: Categories can be changed. Value to use can be found in
# "https://world.openfoodfacts.org/categories.json" in the
# category "tags" "id".
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
SELECTED_CATEGORIES = ["en:snacks", "en:desserts", "en:breads",\
"en:breakfast-cereals", "en:meals"]

# DESCRIPTION: Amount of product to get from OFF API per product category.
# MANDATORY: Yes.
# DEFAULT SETTINGS: 1000.
# CUSTOM SETTINGS: Can be changed but should not exceed 2000 to avoid
# upload failure.
PRODUCTS_AMOUNT = 10

# DESCRIPTION: Message displayed when user input number is out of range.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "Only numbers included in above list can be used. Retry"
# CUSTOM SETTINGS: Message can be changed but should keep sense.
MESSAGE_OOR = "Only numbers included in the list can be used. Retry"

# DESCRIPTION: Message displayed when user input should
# be "y"(yes) or "n" (no) and is not.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "Only numbers included in above list can be used. Retry"
# CUSTOM SETTINGS: Message can be changed but should keep sense.
MESSAGE_YN = "Answer must be y/n . Retry"
