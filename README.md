```yaml
project:
  name: keboola-python-bug

services:
  - hostname: test
    type: python@3.11
    buildFromGit: https://github.com/fxck/keboola-python-bug
    enableSubdomainAccess: true
    envSecrets:
      WORKERS: 1
```
