from setuptools import setup, find_packages

with open("pyproject.toml", "r") as f:
    config = f.read()

setup(
    name="decision_tree",
    version="1.0",
    description="A simple decision tree implementation in Python for data science tasks",
    long_description=config,
    long_description_content_type="text/markdown",
    author="Samy Alderson",
    author_email="samy.alderson@example.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["numpy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="decision_tree data_science python"
)