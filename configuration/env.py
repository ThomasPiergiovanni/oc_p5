# -*-coding:utf-8 -*
"""Program configuration file containing sensible information
"""
# DESCRIPTION: The database name to use when connecting with the MySQL server.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "HPA" (HealthyProduuctApp).
# CUSTOM SETTINGS: Database name can be changed. Note that if
# a database using that name already exists, it will be overwritten.
DATABASE_NAME = "HPA"

# DESCRIPTION: Host name i.e. The server on which MySQL is running.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "localhost".
# CUSTOM SETTINGS: Can be changed if different. Can be an IP
# address as well if the MySQL server is not the local machine.
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