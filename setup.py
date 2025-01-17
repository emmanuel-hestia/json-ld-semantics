import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json-ld-semantics",
    version="0.0.1",
    author="Hugo 'Stache' Hueber",
    author_email="hugo.hueber@hestia.ai",
    description="JSON-LD semantics helper for model generation and usage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hestiaAI/json-ld-semantics",
    project_urls={
        "Bug Tracker": "https://github.com/hestiaAI/json-ld-semantics/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["deepdiff"],
    python_requires=">=3.7",
)
