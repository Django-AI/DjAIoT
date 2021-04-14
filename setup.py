import json
from setuptools import find_packages, setup
from types import SimpleNamespace


metadata = SimpleNamespace(**json.load(open('metadata.json')))


setup(
    name=metadata.PACKAGE,
    version=metadata.VERSION,
    description=metadata.DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=metadata.AUTHOR,
    author_email=metadata.AUTHOR_EMAIL,
    maintainer=metadata.AUTHOR,
    maintainer_email=metadata.AUTHOR_EMAIL,
    url=metadata.URL,
    download_url=metadata.DOWNLOAD_URL,
    packages=find_packages(where='src', exclude=(), include=['djai.*']),
    py_modules=[],
    scripts=['djai/util/cli/djai',
             'djai/util/cli/aws-eb/djai-aws'],
    classifiers=metadata.CLASSIFIERS,
    license='MIT',
    keywords=metadata.KEYWORDS,
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').readlines(),
    entry_points={},
    extras_require={},
    python_requires='>= 3.7',
    setup_requires=[],
    namespace_packages=[]
)
