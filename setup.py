from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'sqlifuzzer',
    version = '0.0.7',
    author = 'Shruti Priya',
    author_email = 'shrutipriya44@gmail.com',
    license = 'MIT Liecense',
    description = 'Python script to fuzz for SQL injection vulnerabilities in URL and input parameters.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/sapphicart/sqli-fuzzer',
    py_modules = ['sqlifuzzer'],
    package_dir={'':"src"},
    packages = find_packages("src"),
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'sqlifuzzer=sqlifuzzer:main',
        ]
    }
)