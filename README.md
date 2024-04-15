# SQLi Fuzzer

SQLi Fuzzer is a tool made for personal use to fuzz for URL or input parameters vulnerable to SQL Injections. The file `url_fuzz.txt` currently contains basic `ORDER BY` SQL queries passed in URL parameter. The default wordlist includes SQL queries in plaintext, url encoding and hex encoding.

_Warning: The tool is currently under development. I cannot gurantee successful utilisation._

### Installation
Clone this repository on your local machine:
```
git clone https://github.com/sapphicart/sqli-fuzzer.git
cd sqli-fuzzer
```
Install requirements:
```python
pip install -r requirements.txt
```

### Usage: </br>
```python
python sqlifuzzer.py -u https://redtiger.labs.overthewire.org/level1.php -v False -w url_fuzz.txt
```