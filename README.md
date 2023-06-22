# cfg_param_wrapper 1.0.0-2

a config wrapper I made. It's made to wrap simple functions, and intercept configurations in tandem with a CfgDict object.

Check the [Github](https://github.com/zeptofine/cfg-param_wrapper/) README! It's likely more up to date.

## Installation

```bash
# from pypi:
pip install cfg-param-wrapper

# from github:
git clone "https://github.com/zeptofine/cfg-param-wrapper"
cd cfg-param-wrapper
pip install -e .
```

## @wrap_config

The `wrap_config` decorator is meant to wrap a function, take their parameters and create a config file from it. Once a function is wrapped using `@wrap_config`, either the cfg can change and the function's default parameters are updated according to the argument names and such.

This is very useful in `Typer` and `Click` commands (wrap it before declaring a command).

## CfgDict

This is a dictionary subclass that takes a filename, and saves all the changes to the file using `json` or `toml`.


## Example

```python
from cfg_param_wrapper import wrap_config, CfgDict

cfg = CfgDict("test.json")
@wrap_config(cfg)
def test_function(s: str, is_real: bool = True): # I'd advise only wrapping functions with default parameters
    return f"{s} is {'real' if is_real else 'fake'}"

if __name__ == "__main__":
  print(test_function("We"))
  cfg['s'] = "us"
  print(test_function()) # Linters hate him!
```
