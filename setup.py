import setuptools

setuptools.setup(
    name="analytic_iris",
    packages=setuptools.find_packages(exclude=["analytic_iris_tests"]),
    install_requires=[
        "dagster==0.14.12",
        "dagit==0.14.12",
        "pytest",
    ],
)
