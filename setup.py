from setuptools import setup, find_packages

setup(
    name='officetimer',
    version='0.2.1',
    packages=find_packages(),
    url='https://github.com/adityakamble49/office-timer',
    license='Apache-2.0',
    author='adityakamble49',
    author_email='adityakamble49@gmail.com',
    description='Office Timer - Manage work life balance',
    entry_points={
        "console_scripts": [
            "office-timer = officetimer.timer_controller:main",
        ],
    },
)
