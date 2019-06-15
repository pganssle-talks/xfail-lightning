# What about `pytest.mark.skip`?

- `xfail` runs the test and checks if it fails
- `skip` doesn't run the test
<br/>
<br/>
Use `skip` when the test only makes sense in some conditions:

```python
@pytest.mark.skip(not sys.platform.startswith("win"),
                  reason="Windows-specific tests")
def test_windows_stuff():
    from ctypes import wintypes

    ... # Do a bunch of Windows-specific stuff
```
