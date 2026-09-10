## Smoke-test Pyodide init + fix root response id

This branch contains two focused changes to make the GitHub Pages demo more reliable:

1. Replace the Pyodide initialization with a smoke test that only loads the runtime and runs a tiny Python snippet. This avoids heavy package installs during initial page load which often fail in browsers and prevents the loading UI from being replaced with an error.

2. Fix the root endpoint response ID logic so `testEndpoint('/')` maps to the existing `response-root` element.

After merging, test by visiting your GitHub Pages site and opening DevTools → Console. The loading message should change to "Python environment ready! (smoke test)" and the console should show the Pyodide smoke-test result.
