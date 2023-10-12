from setuptools import setup, find_packages

# Package metadata
NAME = "keyword_extraction"
VERSION = "1.0.0"
DESCRIPTION = "A FastAPI application for keyword extraction and classification."
AUTHOR = "kalpitha"
AUTHOR_EMAIL = "Kalpitha@email.com"
URL = "https://github.com/kalpitha23/Keyword_extraction1"  

# List of dependencies
INSTALL_REQUIRES = [
    "openai>=0.95.2",
    "fastapi>=0.27.0",
    "pydantic>=1.10.8",
    "requests>=2.31.0",
    "python-dotenv>=1.0.0",
    "uvicorn>=0.22.0"
]

# Create the package
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)
