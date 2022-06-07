import setuptools

setuptools.setup(
    name="analytic_dados_enem",
    packages=setuptools.find_packages(exclude=["analytic_dados_enem_tests"]),
    install_requires=[
        "dagster==0.14.12",
        "dagit==0.14.12",
        "pytest",
    ],
)
