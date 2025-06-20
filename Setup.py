from setuptools import setup, find_packages

setup(
    name="iot_sentinel",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": ["iot-sentinel=iot_sentinel.cli:main"]
    }
)
from setuptools import setup, find_packages

setup(
    name="iot_sentinel",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial>=3.5",
        "python-dotenv>=0.19.0",
        "scapy>=2.5.0"
    ],
    entry_points={
        "console_scripts": [
            "iot-sentinel=iot_sentinel.cli:main"
        ]
    }
)
