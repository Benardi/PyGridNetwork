![pygrid-logo](https://raw.githubusercontent.com/OpenMined/design-assets/master/logos/PyGrid/horizontal-primary-trans.png)

<p align="center">
    <a href="https://img.shields.io/github/license/OpenMined/GridNetwork">
        <img src="https://img.shields.io/github/license/OpenMined/GridNetwork"
            alt="License"/></a>
    <a href="https://img.shields.io/pypi/v/gridnetwork">
        <img src="https://img.shields.io/pypi/v/gridnetwork"
            alt="Version"/></a>
    <a href="https://img.shields.io/opencollective/all/openmined">
        <img src="https://img.shields.io/opencollective/all/openmined"
            alt="OpenCollective"/></a>
</p> 

<p align="center">
    <a href="https://deploy.cloud.run">
        <img src="https://deploy.cloud.run/button.svg"
            alt="Run on Google Cloud"/></a>
</p> 

# GridNetwork

GridNetwork is a network router used by the PyGrid platform. GridNetwork makes use of [WebRTC](https://webrtc.org/) to provide transparent connection between workers.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gridnetwork.

```bash
pip install gridnetwork
```

## Usage

```python
from gridnetwork import create_app, raise_grid


if __name__ == "__main__":
    app,server = raise_grid()
else:
    app = create_app()
```

* Once the package is installed the application gridnetwork can also be executed by running the command `raise_grid` 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors

See the list of [contributors](https://github.com/OpenMined/GridNetwork/contributors) who participated in this project.

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
