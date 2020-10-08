from setuptools import setup, find_packages, find_namespace_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
        name='mirge3.0-build',
        version='0.0.4',
        author='Arun Patil and Marc Halushka',
        author_email='mhalush1@jhmi.edu',
        url='https://test.pypi.org/legacy/',
        description='miRge3.0-build: Building libraries of small RNA sequencing Data', 
        long_description=long_description,
        keywords=['miRge-build', 'small RNA analysis', 'NGS', 'bioinformatics tools'],  
        license='MIT',
        package_dir={'mirge_build':'mirge_build'},
        packages=find_packages(),
        entry_points={'console_scripts': ['miRge3.0-build = mirge_build.__main__:main']},
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
            ],
        include_package_data=True,
        python_requires='>=3.8',
)
