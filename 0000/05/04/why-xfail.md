# Why should I care?
<br/>

<div>
<h2>Document your acceptance criteria</h2>

Adding a failing test to the test suite documents the conditions necessary to fix the bug.
</div>
<br/>
<div class="fragment">
<h2>Test your tests!</h2>
Start by writing the xfailing test, if it doesn't fail, your test won't catch the regression.
</div>
<br/>
<div class="fragment">
<h2>Impose regression tests early!</h2>

Your test suite will fail if you accidentally fix a bug - remove the `xfail` and you'll prevent regressions from the moment you merged!
</div>
