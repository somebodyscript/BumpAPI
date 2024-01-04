from setuptools import setup, find_packages

LONG_DESCRIPTION='''
    BumpAPI - A Python Library for Website Interaction
-------------------------------------------------

BumpAPI is a Python library developed by BumpAPI Labs to facilitate interaction with external APIs of websites. It empowers users to interact with the content and functionalities of various websites through a range of methods and commands.

Features:
- Fetch content from a specified URL.
- Retrieve text content from the page, removing HTML tags.
- Search for specific text occurrences on a page.
- Display HTML code from a webpage.
- Refresh or reload a web page.
- Retrieve links or images from a webpage.
- Generate a summary of the page content.
- Gather statistics about HTML tags used on the page.
- Fetch header information of the webpage.
- Compare two web pages for differences.
- Extract specific elements based on their titles.
- Simulate wait time between commands.
- Click on elements using their IDs.
- Send text inputs to the targeted webpage.

Usage:
The library offers a set of methods to interact with web content. Users can specify a target URL and perform various operations to extract, analyze, or interact with elements on the webpage. It's important to understand and adhere to the terms of service of the websites being accessed using this library.

Note:
BumpAPI is currently in a testing phase, and although efforts are being made to enhance its reliability and stability, users should expect potential bugs or errors during usage.

Contributions:
BumpAPI welcomes contributions and feedback from the community. Feel free to contribute to the project or report any issues encountered during usage.

Disclaimer:
Usage of this library to interact with websites should comply with ethical and legal standards. The developers assume no liability for the usage of BumpAPI beyond its intended functionality.

Support:
For any inquiries, suggestions, or issues, please reach out to BumpAPI Labs via ecomatedev@gmail.com

Thank you for considering BumpAPI for your web interaction needs!
'''

setup(
    name='bumpAPI',
    version='1.4',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    author="ecomatedev",
    author_email="ecomatedev@gmail.com",
    description="Python library for interacting with the site's external API.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/EcomateDev/bumpAPI",
)
