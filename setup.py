import os
from setuptools import setup, find_packages

# Load requirements from requirements.txt
with open("requirement.txt") as f:
    required_packages = f.read().splitlines()