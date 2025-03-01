import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REPO_NAME="Text_Summarizer"
AUTHOR_USER_NAME="jainam2425"
SRC_REPO="txtsum"
AUTHOR_EMAIL="jainamshah2425@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A project to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
