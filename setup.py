from setuptools import setup, find_packages

setup(
    name="jarvis_api_library",
    version="1.1.2",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
    ],
    author="Samuel Lewis",
    description="A library for interacting with API's to be used within The J.A.R.V.I.S. Project.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)
