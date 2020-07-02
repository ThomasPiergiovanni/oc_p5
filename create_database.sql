DROP DATABASE IF EXISTS p6;
CREATE DATABASE IF NOT EXISTS p6 CHARACTER SET 'utf8';

USE p6;

DROP TABLE IF EXISTS p6.category, p6.product, p6.registration;

CREATE TABLE IF NOT EXISTS p6.category(
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) NOT NULL,
    name_origin VARCHAR(250) NOT NULL,
    url_origin LONGTEXT NOT NULL,
    PRIMARY KEY (id)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p6.product(
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) UNIQUE,
    product_name_origin VARCHAR(250),
    url_origin VARCHAR(250),
    countries VARCHAR(250),
    countries_tag_origin VARCHAR(250),
    nutriscore_grade_origin VARCHAR(250),
    stores_origin VARCHAR(250),
    purchase_places_origin VARCHAR(250),
    purchase_places_tags_origin VARCHAR(250),
    category_id SMALLINT UNSIGNED NOT NULL,
    categories_tags_origin VARCHAR(250),
    categories_origin VARCHAR(250),
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES p6.category(id)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p6.registration(
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_product_id SMALLINT UNSIGNED NOT NULL,
    substitut_product_id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_product_id) REFERENCES p6.product(id),
    FOREIGN KEY (substitut_product_id) REFERENCES p6.product(id)
    )ENGINE=INNODB;