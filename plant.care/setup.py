from setuptools import setup, find_packages

setup(
    name="plant.care",
    version="0.1",
    description="BAC1 PlantCare",
    author='Peter Varga',
    author_email='varga.pter91@gmail.com',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={"": "src"},
    namespace_packages=["plant"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools",
                      "Zope"],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = Zope
    """,
    )