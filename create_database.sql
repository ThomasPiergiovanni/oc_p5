CREATE DATABASE IF NOT EXISTS p5 CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS p5.category(
    id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) NOT NULL,
    name VARCHAR(250) NOT NULL,
    url LONGTEXT NOT NULL,
    PRIMARY KEY (id_category)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.product(
    id_product SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) NOT NULL,
    product_name VARCHAR(250) NOT NULL,
    nutriscore_grade VARCHAR(250) NOT NULL,
    category_id SMALLINT UNSIGNED NOT NULL,
    url LONGTEXT NOT NULL,
    stores VARCHAR(250),
    PRIMARY KEY (id_product),
    FOREIGN KEY (category_id) REFERENCES p5.category(id_category)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS p5.substitute(
    product_product_id SMALLINT UNSIGNED NOT NULL,
    substitut_product_id SMALLINT UNSIGNED NOT NULL,
    FOREIGN KEY (product_product_id) REFERENCES p5.substitute(id_product),
    FOREIGN KEY (substitut_product_id) REFERENCES p5.substitute(id_product)
    )ENGINE=INNODB;