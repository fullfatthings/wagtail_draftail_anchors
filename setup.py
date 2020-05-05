import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagtail_draftail_anchors",
    version="0.0.1",
    author="TODO",
    author_email="TODO",
    description="A Draftail extension to add anchor identifiers to rich text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobtoppm/wagtail_draftail_anchors",
    packages=setuptools.find_packages(),
    install_requires=[
        'wagtail>=2.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)