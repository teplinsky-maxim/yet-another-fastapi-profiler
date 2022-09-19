from setuptools import setup, find_packages

setup(
    name='yet_another_fastapi_profiler',
    version='1.0.0',
    license='MIT',
    author="Maxim Teplinsky",
    author_email='email@example.com',
    packages=find_packages('yet_another_fastapi_profiler'),
    package_dir={'': 'yet_another_fastapi_profiler'},
    url='https://github.com/teplinsky-maxim/yet-another-fastapi-profiler',
    keywords='fastapi yet_another_fastapi_profiler filter minimal time',
    install_requires=[
        'fastapi',
    ],
)
