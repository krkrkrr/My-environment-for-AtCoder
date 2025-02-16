# My Environment for AtCoder

## Requirements
### WSL
1. Install chromium
    ```
    $ sudo apt-get install -y chromium-browser chromium-chromedriver
    ```
1. Check chromedriver parent path
    ```
    $ which chromedriver
    ```
1. Add chromedriver path to environment
    ```
    $ export PATH=$PATH:<chrome driver parent path>
    $ export CHROMEDRIVER_PATH=<chrome driver parent path>/chromedriver
    ```


## Usage
### Quick Start
1. Initialize environment
    ```
    $ cd modules/InitializeEnvironment
    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    $ pip install .
    $ cd ../../
    $ python modules/InitializeEnvironment/src/initialize_environment.py https://atcoder.jp/contests/{contest_name}
    $ deactivate
    ```
1. Install packages for pytest
    ```
    $ python -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    $ pip install '.[test]'
    ```
1. Test with pytest
    ```
    $ pytest -vv
    ```