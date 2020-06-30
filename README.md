# P5 - Utilisez les données publiques d'Open Food Acts

## API OFF

### Endpoints

Products catgeories:

    https://fr-en.openfoodfacts.org/categories.json

Products per category:

    https://fr-en.openfoodfacts.org/category/*.json

Countries taxonomy:

    https://fr-en.openfoodfacts.org/data/taxonomies/countries.json


### DB Model

Class category:
    id_category :
    original_id_category:

Example:

    "id": "3245390031341",

Class product:
* id:
    * Origin: OFF API
    * Descritpion: product id
    * Status: mandatory
    * Type : integer
    * Constraints: unique, primarykey TO CHECK UNIQUENESS
* id_product:
    * Origin: system
    * Descritpion: product id
    * Status: mandatory
    * Type : integer
    * Constraints: unique, primarykey
* code:
    * Origin: OFF API
    * Descritpion: barcode of the product.
    * Status: mandatorys
    * Type : integer
    * Constraints: unique
* url:
    * Origin: OFF API
    * Descritpion: url of the product page
    * Status: mandatory
* product_name:
    * Origin: OFF API
    * Descritpion: product name
    * Status: mandatory - OK

* product_name:
    * Origin: OFF API
    * Descritpion: product name in french
    * Status: TO CHECK
* categories:
    * Origin: OFF API
    * Descritpion: categories of the product
    * Status: mandatory - OK

Example:
    
      "categories": "Produits laitiers,Produits fermentés,Produits laitiers fermentés,Fromages,Frais,Fromages de France,Fromages de chèvre,Fromages à pâte molle à croûte naturelle,Fromages au lait cru,Rocamadour,en:aoc-cheeses,en:labeled-cheeses",

* categories_tags:
    * Origin: OFF API
    * Descritpion: catgories tag
    * Status: mandatory

* categories_hierarchy:
    * Origin: OFF API
    * Descritpion: catgories tag
    * Status: TO CHECK

* countries:
    * Origin: OFF API
    * Descritpion: list of countries where the product is sold
    * Status: mandatory

Example:

    "countries": "France",
* countries_tags:
    * Origin: OFF API
    * Descritpion: countries tag
    * Status: mandatory
* nutrition_grade_fr:
    * Origin: OFF API
    * Descritpion: nutrition grade ('a' to 'e')
    * Status: mandatory
* nutriscore_grade:
    * Origin: OFF API
    * Descritpion: nutrition grade ('a' to 'e')
    * Status: mandatory
* stores:
    * Origin: OFF API
    * Descritpion: distributor name
    * Status: optionnal
* purchase_places:
    * Origin: OFF API
    * Descritpion: country, state and/or city where the product can be purchased
    * Status: optionnal
* purchase_places_tags:
    * Origin: OFF API
    * Descritpion: purchased place tag
    * Status: TO CHECK
 



### Notes - TO DELETE

You can retrieve a list of products that belong to a specific category. For example, "cheeses":

    https://world.openfoodfacts.org/category/cheeses.json
    https://fr-en.openfoodfacts.org/category/cheeses.json

    GET https://fr-en.openfoodfacts.org/category/pizzas.json

Usefull endpoints:

Categories à récupérer:

    https://fr.openfoodfacts.org/categories.json

Puis une fois les categories récupérée

    https://fr.openfoodfacts.org/categorie/fromages.json

    https://us.openfoodfacts.org/api/v0/product/ 