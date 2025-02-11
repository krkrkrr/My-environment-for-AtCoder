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
### Get test cases
1. Install the package
```
$ pip install .[test]
```

1. Run the script
```
$ python tools/get_test_cases.py
```