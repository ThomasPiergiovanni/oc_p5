# -*-coding:utf-8 -*
"""Program configuration file
"""

# DESCRIPTION: OpenFoodFacts (OFF) API categories list endpoint. It returns
# the categories list per country.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/categories.json".
# CUSTOM SETTINGS: To use the application with product references from
# another country than France, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/categories.json" for Spain).
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"

# DESCRIPTION: OFF API products research functionality endpoint.
# It returns the product research functionality per country.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/cgi/search.pl".
# CUSTOM SETTINGS: To use the application with product references from
# another country than France, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/cgi/search.pl").
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
PRODUCTS_ENDPOINT = "https://fr.openfoodfacts.org/cgi/search.pl"

# DESCRIPTION: Headers, i.e. the application general informations, among other,
# its name and version number.
# MANDATORY: Yes.
# DEFAULT SETTINGS: {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}.
# CUSTOM SETTINGS: Iy ou modify this app this settings must be changed but
# keeping the following structure {'User-Agent': 'your information'}.
# For more information, please check "https://documenter.getpostman.
# com/view/8470508/SVtN3Wzy?version=latest#intro".
HEADER = {'User-Agent': 'HealthyProductApp - Web - Version 0.0'}

# DESCRIPTION: OFF API products categories type used in the application.
# MANDATORY: Yes.
# DEFAULT SETTINGS: ["en:snacks", "en:desserts", "en:breads",
# "en:breakfast-cereals", "en:meals"].
# CUSTOM SETTINGS: Categories can be changed. Value to use can be found in
# "https://world.openfoodfacts.org/categories.json" in the
# category "tags" "id".
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
SELECTED_CATEGORIES = ["en:snacks", "en:desserts", "en:breads",
                       "en:breakfast-cereals", "en:meals"]

# DESCRIPTION: Amount of product to get from OFF API per product category.
# MANDATORY: Yes.
# DEFAULT SETTINGS: 50.
# CUSTOM SETTINGS: Can be changed but should not exceed 2000 to avoid
# upload failure.
PRODUCTS_AMOUNT = 50

# DESCRIPTION: Message displayed when user input number is out of range.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "Only numbers included in above list can be used. Retry"
# CUSTOM SETTINGS: Cannot be changed.
MESSAGE_OOR = "Seulement des nombres inclus dans la liste peuvent être \
utilisés. Ré-essayez"

# DESCRIPTION: Message displayed when user input should
# be "y"(yes) or "n" (no) and is not.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "Only numbers included in above list can be used. Retry"
# CUSTOM SETTINGS: Cannot be changed.
MESSAGE_YN = "La réponse doit être o/n uniquement . Ré-essayez"
