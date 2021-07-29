# setup.py

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Easykiwi",
    version="1.3",
    author="Nelson Carrasquel",
    author_email="carrasquel@outlook.com",
    description="Easykiwi is a Framework for Queue Messaging Application Development for Python and RabbitMQ.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/carrasquel/easykiwi",
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'kiwi = easykiwi:cli',
        ],
    },
    install_requires=[
        'kiwipy',
        'aio-pika',
        'pyyaml',
        'Click==7.0',
        'python-dotenv==0.18.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
