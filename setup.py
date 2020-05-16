import os
from setuptools import find_packages, setup

def get_requirements(req_file):
  """Read requirements file and return packages and git repos separately"""
  requirements = []
  dependency_links = []
  lines = read(req_file).split("\n")
  for line in lines:
      if line.startswith("git+"):
          dependency_links.append(line)
      else:
          requirements.append(line)
  return requirements, dependency_links


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

core_reqs, core_dependency_links = get_requirements("requirements.txt")



setup(
  name="gridnetwork",
  version="0.1.0",
  author="OpenMined",
  author_email="contact@openmined.org",
  description="A network router used by the PyGrid platform.",
  long_description=read("README.md"),
  long_description_content_type="text/markdown",
  url="https://github.com/OpenMined/GridNetwork",
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  setup_requires=['wheel', 'gevent', 'flask'],
  install_requires=core_reqs,
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
