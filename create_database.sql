DROP DATABASE IF EXISTS p5;
CREATE DATABASE IF NOT EXISTS p5 CHARACTER SET 'utf8';

USE p5;

DROP TABLE IF EXISTS p5.category, p5.product, p5.registration;

CREATE TABLE IF NOT EXISTS p5.category(
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) UNIQUE,
    name_origin VARCHAR(250),
    url_origin VARCHAR (250),
    PRIMARY KEY (id)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.product(
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
    FOREIGN KEY (category_id) REFERENCES p5.category(id)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.registration(
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_product_id SMALLINT UNSIGNED NOT NULL,
    substitut_product_id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_product_id) REFERENCES p5.product(id),
    FOREIGN KEY (substitut_product_id) REFERENCES p5.product(id)
    # CONSTRAINT FK_product_substitut FOREIGN KEY (product_product_id)
    # REFERENCES p5.product(id),
    # CONSTRAINT FK_product_substitut2 FOREIGN KEY (substitut_product_id)
    # REFERENCES p5.product(id)
    )ENGINE=INNODB;

DESCRIBE p5.category;
DESCRIBE p5.product;
DESCRIBE p5.registration;


