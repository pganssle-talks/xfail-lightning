# Fixing the issue

```python
def is_perfect_square(n):
    """Given an integer, return whether or not it is a perfect square.

    Specifically, this means that there is a real integer such that i*i == n
    """

    # Negative numbers are not squares given the definition of the function
    if n < 0:
        return False

    s = math.sqrt(n)
    return s == int(s)
```
<br/><br/>

<pre><tt class="hljs">
<span style="font-weight:bold;">============================= test session starts ==============================</span>
platform linux -- Python 3.7.3, pytest-4.6.3, py-1.8.0, pluggy-0.12.0
collected 16 items

tests/test_square_xpass.py <span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:olive;">X</span><span style="color:teal;">                              [100%]</span>

<span style="color:green;"></span><span style="color:green;font-weight:bold;">===================== 15 passed, 1 xpassed in 0.06 seconds =====================</span>
</tt></pre>

--

# Treating failure to fail as a failure
<br/>
```python
@pytest.mark.xfail(strict=True)
def test_negative():
    assert not is_perfect_square(-4)
```
<br/>

<pre><tt class="hljs">
<span style="font-weight:bold;">============================= test session starts ==============================</span>
platform linux -- Python 3.7.3, pytest-4.6.3, py-1.8.0, pluggy-0.12.0
collected 16 items

tests/test_square_xpass.py <span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:green;">.</span><span style="color:red;">F</span><span style="color:teal;">                              [100%]</span>

=================================== FAILURES ===================================
<span style="color:red;"></span><span style="color:red;font-weight:bold;">________________________________ test\_negative _________________________________</span>
[XPASS(strict)] 
<span style="color:red;"></span><span style="color:red;font-weight:bold;">===================== 1 failed, 15 passed in 0.04 seconds ======================</span>
</tt></pre>
<br/><br/>
Set globally in `setup.cfg`:<br/><br/>

```ini
[tool:pytest]
xfail_strict = true
```
