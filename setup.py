import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diabetes-day-planner-marcus-falls",
    version="0.0.1",
    author="Marcus Falls",
    author_email="marcuspfalls@gmail.com",
    description="A package that calculates the time and size of insulin dosages ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcuspfalls/diabetes_day_planner",
    project_urls={
        "Bug Tracker": "https://github.com/marcuspfalls/diabetes_day_planner/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
