from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'ajit kumar patel',
    author_email= '1ajitkumarpatel@gmail.com',
    packages= find_packages(),   # it will look for construcor file (__init__.py) to make that file as local packages
    install_requires = []        # it will install the the Dependeny present in requirements.txt

)

# ---------------ANOTHER WAY TO DO ----------------------------
# import setuptools

# # It helps to display the README.md file in pypy website
# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

# __version__ = "0.0.0"
# REPO_NAME = "Medical-Chatbot-Using-Llama2"
# AUTHOR_USER_NAME = "ajitkumarpatel1"
# SRC_REPO = "Medical Chatbot"
# AUTHOR_EMAIL = "1ajitkumarpatel@gmail.com"

# setuptools.setup(
#     name=SRC_REPO,
#     version=__version__,
#     author=AUTHOR_USER_NAME,
#     author_email=AUTHOR_EMAIL,
#     description="A small python package for CNN app",
#     long_description=long_description,
#     long_description_content="text/markdown",
#     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
#     package_dir={"": "src"},
#     packages=setuptools.find_packages(where="src")