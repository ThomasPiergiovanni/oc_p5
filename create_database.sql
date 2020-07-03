DROP DATABASE IF EXISTS p5;
CREATE DATABASE IF NOT EXISTS p5 CHARACTER SET 'utf8';

USE p5;

DROP TABLE IF EXISTS p5.category, p5.product, p5.registration;

CREATE TABLE IF NOT EXISTS p5.category(
    id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) NOT NULL,
    name_origin VARCHAR(250) NOT NULL,
    url_origin LONGTEXT NOT NULL,
    products_origin INTEGER,
    PRIMARY KEY (id_category)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.product(
    id_product SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) UNIQUE,
    product_name_origin VARCHAR(250),
    url_origin VARCHAR(250),
    countries_origin VARCHAR(250),
    countries_tags_origin VARCHAR(250),
    nutriscore_grade_origin VARCHAR(250),
    stores_origin VARCHAR(250),
    purchase_places_origin VARCHAR(250),
    purchase_places_tags_origin VARCHAR(250),
    category_id SMALLINT UNSIGNED NOT NULL,
    categories_tags_origin VARCHAR(250),
    categories_origin VARCHAR(250),
    PRIMARY KEY (id_product),
    FOREIGN KEY (category_id) REFERENCES p5.category(id_category)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.registration(
    id_registration SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_product_id SMALLINT UNSIGNED NOT NULL,
    substitut_product_id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_registration),
    FOREIGN KEY (product_product_id) REFERENCES p5.product(id_product),
    FOREIGN KEY (substitut_product_id) REFERENCES p5.product(id_product)
    )ENGINE=INNODB;