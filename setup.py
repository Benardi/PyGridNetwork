from setuptools import find_package, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name="grid-network",
  version="0.1.0",
  author="Ionesio Junior",
  author_email="contact@openmined.org",
  description="A network router used by the PyGrid platform.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/OpenMined/GridNetwork",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
