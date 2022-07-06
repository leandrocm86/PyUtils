import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyUtils',
    version='0.19',
    author='Leandro Medeiros',
    author_email='leandrocm86@gmail.com',
    description='Utility classes for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/leandrocm86/PyUtils',
    project_urls = {
        "Bug Tracker": "https://github.com/leandrocm86/PyUtils/issues"
    },
    license='MIT',
    packages=['pyutils'],
    install_requires=[],
)
