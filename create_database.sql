
CREATE TABLE IF NOT EXISTS product(
    id_product SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_origin VARCHAR(250) NOT NULL,
    product_name VARCHAR(250) NOT NULL,
    nutriscore_grade VARCHAR(250) NOT NULL,
    category_id SMALLINT UNSIGNED NOT NULL,
    url LONGTEXT NOT NULL,
    stores VARCHAR(250),
    PRIMARY KEY (id_product),
    FOREIGN KEY (category_id) REFERENCES category(id_category)
    )ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS substitute(
    product_product_id SMALLINT UNSIGNED NOT NULL,
    substitute_product_id SMALLINT UNSIGNED NOT NULL,
    FOREIGN KEY (product_product_id) REFERENCES product(id_product),
    FOREIGN KEY (substitute_product_id) REFERENCES product(id_product)
    )ENGINE=INNODB;