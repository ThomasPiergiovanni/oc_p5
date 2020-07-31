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

### 3.6. Use "HealthierProductApplication".

The programm is now ready to use. You can start it using **main.py** with your bash.
> python3 main.py


### 3.7. Deactivate the virtual environnement.

Once you're done using the programm, you should leave the virtual environement. Simply type the following statement in your bash.
> deactivate

### 3.8. Uninstall.

If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.

Changing settings can be done to the following constants in **program/admin/config.py** file.

### 4.1. CATGEORIES_ENDPOINT

**DESCRIPTION**: OpenFoodFacts (OFF) API categories list endpoint. It returns the categories list per country.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "ht<span>tps://</span>fr.openfoodfacts.org/categories.json".  
**CUSTOM SETTINGS**: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/categories.json" for Spain). For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

### 4.2. PRODUCTS_ENDPOINT
**DESCRIPTION**: OFF API products research functionality endpoint. It returns the product research functionality per country.  
**MANDATORY**: Yes.  
**DEFAULT SETTINGS**: "ht<span>tps://</span>fr.openfoodfacts.org/cgi/search.pl".  
**CUSTOM SETTINGS**: To use the application with product references from another country than France, use the appropriate ISO-3166-1 Alpha 2 code and replace it in the endpoint (e.g. "ht<span>tps://</span>es.openfoodfacts.org/cgi/search.pl"). For more information, please check [OFF API official documentation](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro).

## 5. User guide.

### 5.1. Objective.

### 5.2. How to.




## API OFF

### Endpoints

Products catgeories:

    https://fr-en.openfoodfacts.org/categories.json

Products per category:

    https://fr-en.openfoodfacts.org/category/*.json

Countries taxonomy:

    https://fr-en.openfoodfacts.org/data/taxonomies/countries.json


### DB Model

[link](https://drive.google.com/drive/folders/1AgDhnDVAao_IKeIPdGskjCfVUt9Q0sc9)

#### OFF Data Description

##### Class category:

* id :
    * Descritpion: product id

Example:

    "id": "en:plant-based-foods-and-beverages",

* name :
    * Descritpion: category name

* url :
    * Descritpion: category url

* products :
    * Descritpion: count of product in category 

##### Class product:

* \_id:
    * Descritpion: product id

Exemple (Fromage, Comté):

    "_id": "2454495041334",

* id: (TO CHECK if \_id or id)
    * Descritpion: product id

Exemple (Fromage, Comté):

    "id": 2454495041334,  -- meme str que "_id" et "code"


* code:
    * Descritpion: barcode of the product.

Example (Fromage, Comté):

    "code": "2454495041334",

* url
    * Descritpion: url of the product page

Example:

    "url": "https://fr-en.openfoodfacts.org/product/2454495041334/comte",

* product_name:

    * Descritpion: product name
    * Status: mandatory - OK

Example (Fromage, Comté):

    "product_name": "Comté",

* categories:
    * Descritpion: categories of the product

Example:
    
      "categories": "Produits laitiers,Produits fermentés,Produits laitiers fermentés,Fromages,Frais,Fromages de France,Fromages de chèvre,Fromages à pâte molle à croûte naturelle,Fromages au lait cru,Rocamadour,en:aoc-cheeses,en:labeled-cheeses",

* categories_tags:
    * Descritpion: catgories tag

Example:

    "categories_tags": [
        "en:dairies",
        "en:fermented-foods",
        "en:fermented-milk-products",
        "en:cheeses",
        "en:cooked-pressed-cheeses",
        "en:french-cheeses",
        "fr:comte",
        "en:aoc-cheeses",
        "en:labeled-cheeses"
    ],

* countries:
    * Descritpion: list of countries where the product is sold


Example:

    "countries": "France",

* countries_tags:
    * Descritpion: countries tag

Example:

    "countries_tags": [
        "en:france"
    ],

* nutrition_grades:
    * Descritpion: nutrition grade ('a' to 'e')

Example (Fromage, Rocamadour):

    "nutrition_grades": "d",

* nutriscore_grade
    * Descritpion: nutrition grade ('a' to 'e')

Example (Fromage, Rocamadour):

    "nutriscore_grade": "d",

* nutrition_score_beverage:
    * Descritpion: nutrition score for beverages?

Example (Fromage, Rocamadour):

    "nutrition_score_beverage": 0,

* stores:
    * Descritpion: distributor name
    
* purchase_places:
    * Descritpion: country, state and/or city where the product can be purchased

Example (fromage, emmental):

    "purchase_places": "",

ou

    "purchase_places": "FRANCE,Saint-Ouen,Etréchy",

* purchase_places_tags:
    * Descritpion: purchased place tag
 
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