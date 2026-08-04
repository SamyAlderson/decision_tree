from setuptools import setup, find_packages

try:
    with open("pyproject.toml", "r") as f:
        config = f.read()
except FileNotFoundError:
    print("Warning: pyproject.toml not found, skipping long description.")

setup(
    name="decision_tree",
    version="1.0",
    description="A simple decision tree implementation in Python for data science tasks",
    long_description=config if config else "No long description available.",
    long_description_content_type="text/plain",  # Changed to text/plain
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
    keywords="decision_tree data_science python",
    python_requires=">=3.9",  # Added python version requirement
)