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

### 3.2. Python 3 install.

### 3.3. Create & activate a virtual environnement (recommended).

### 3.4. MySQL server install.

### 3.5. Play.

### 3.6. Deactivate a virtual environnement.

### 3.7. Uninstall.

## 4. Settings.

### 4.1. Config file.

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