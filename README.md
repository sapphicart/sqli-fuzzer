<h1 align="center">SQLi Fuzzer</h1>

<p align="center">
  <a href="#summary">Summary</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#to-do">To Do</a> •
  <a href="#license">License</a>
</p>

## Summary

SQLi Fuzzer is a tool made for personal use. This tool fuzzes for URL or input parameters vulnerable to SQL Injections. The file `url_fuzz.txt` currently contains basic `ORDER BY` SQL queries passed in URL parameter. The default wordlist includes SQL queries in plaintext, url encoding and hex encoding.

**Warning: The tool is currently under development. I cannot gurantee successful utilisation.**

## Requirements
- Python 3.xx

## Installation
There are two ways to install `sqlifuzzer`:

Install the tool directly with `pip`
```bash
pip install sqlifuzzer
```

Or, you can build from source. Download the latest [release](https://github.com/sapphicart/sqli-fuzzer/releases).

## Usage 
Use the `--help` switch to read the `OPTIONS` available.
```bash
$ sqlifuzzer --help
Usage: sqlifuzzer.py [OPTIONS]

Options:
  -u, --url TEXT        The URL to fuzz
  -v, --verify BOOLEAN  SSL certificate verification. Default True
  -w, --wordlist TEXT   /path/to/wordlist.txt
  --help                Show this message and exit.
```
Example:
```bash
$ sqlifuzzer -u https://redtiger.labs.overthewire.org/level1.php -v False -w url_fuzz.txt
```

## Notes
A generic wordlist named `url_fuzz.txt` is available in the source code. You can use this wordlist or create your own!

Upcoming features:
- Input parameters fuzzing
- HTTP Verbs (GET, POST, PUT) fuzzing
- Diverse wordlist

## Contributions
All contributions are welcome. Just fork this repository, make your changes and open a pull request!

## License
Distributed under [MIT](LICENSE) License.