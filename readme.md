### UDP Server/Client

<br>

---

<br>


#### Make with
- PostgreSQL
- Python

<br>

---

<br>

#### Dependencies

```bash
# OS dependencies
python-mysqlclient python-mysql-connector python-pymysql psutil python-psutil python2-psutil
```

```bash
# Arch Linux
sudo pacman -S python-mysqlclient python-mysql-connector python-pymysql psutil python-psutil python2-psutil pymysql mysqlclient
```

```bash
# Python pip dependencies
pip install psutil mysqlclient pymysql socket
```

<br>

---

<br>


#### Create tables for all columns, exemple

```sql
CREATE TABLE ip_address (
    ip_address_id int NOT NULL AUTO_INCREMENT,
    ip_address LONGTEXT,
	  timestamps TIMESTAMP,
    PRIMARY KEY (ip_address_id)
)
```

## References

- [Gravando e Lendo dados no Mysql com Python](https://medeubranco.wordpress.com/2008/06/04/gravando-e-lendo-dados-no-mysql-com-python/)
- [Python Socket](https://wiki.python.org.br/SocketBasico)
- [Inserir dados no database](https://www.devmedia.com.br/forum/inserir-dados-em-uma-tabela-pelo-python/598838)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [MySQL timestamp](https://www.mysqltutorial.org/mysql-timestamp.aspx)
- [MySQL Autoincrement](https://www.w3schools.com/sql/sql_autoincrement.asp)
- [UDP Communication](https://wiki.python.org/moin/UdpCommunication)
