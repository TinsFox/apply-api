from setuptools import setup, find_packages


setup(
    name='ApplyAPI',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pymysql==0.9.3',
        'requests==2.22.0',
        'flask-httpauth==3.3.0',
        'flask-sqlalchemy==2.4.0',
        'flask-wtf==0.14.2',
        'Flask==1.1.1',
    ]
)