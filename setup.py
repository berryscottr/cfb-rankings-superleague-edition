import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cfbRankingsSuperleagueEdition',
    version='0.0.1',
    packages=['ranking'],
    url='https://github.com/berryscottr/cfb-rankings-superleague-edition',
    license='MIT',
    author='Scott Berry',
    author_email='berryscottr@gmail.com',
    description='The Definitive CFB Ranking',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    package_dir={"": "src"},
    python_requires="~=3.9.6",
)
