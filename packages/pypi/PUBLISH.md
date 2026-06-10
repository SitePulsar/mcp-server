# Publishing `sitepulsar-mcp` to PyPI

Founder checklist. Run these from inside the `c3-pypi/` package directory
(or wherever this package has been copied into the public repo).

## 0. Before you start

- [ ] Decide whether to ship the guidance-only shim or first implement the
      native stdio→remote bridge (see the TODO in `sitepulsar_mcp/__main__.py`).
      0.1.0 as written is an honest guidance shim — fine for a placeholder claim
      of the `sitepulsar-mcp` name on PyPI.
- [ ] Create accounts + API tokens:
      - TestPyPI: https://test.pypi.org/manage/account/token/
      - PyPI: https://pypi.org/manage/account/token/
      Scope the first token to "Entire account" (no project exists yet); after
      the first upload, rotate to a project-scoped token.
- [ ] Confirm the name `sitepulsar-mcp` is available on PyPI
      (https://pypi.org/project/sitepulsar-mcp/ should 404).

## 1. Build the distributions

```bash
python -m pip install --upgrade build twine
python -m build            # produces dist/*.whl and dist/*.tar.gz
```

## 2. Validate the artifacts

```bash
twine check dist/*         # validates README rendering + metadata
```

Confirm both a `.whl` and an `.sdist` (`.tar.gz`) were produced and pass.

## 3. Upload to TestPyPI first

```bash
twine upload --repository testpypi dist/*
# username: __token__
# password: <your TestPyPI API token, including the "pypi-" prefix>
```

Verify the install from TestPyPI in a clean virtualenv:

```bash
python -m venv /tmp/sp-test && source /tmp/sp-test/bin/activate
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple/ \
            sitepulsar-mcp
sitepulsar-mcp --version          # prints 0.1.0
sitepulsar-mcp                    # prints connection guidance to stderr, exits 1
deactivate
```

## 4. Upload to real PyPI

```bash
twine upload dist/*
# username: __token__
# password: <your PyPI API token, including the "pypi-" prefix>
```

## 5. Verify the published package

```bash
python -m venv /tmp/sp-prod && source /tmp/sp-prod/bin/activate
pip install sitepulsar-mcp
sitepulsar-mcp --version          # prints 0.1.0
deactivate
```

Also confirm the project page renders: https://pypi.org/project/sitepulsar-mcp/

## 6. Post-publish

- [ ] Rotate the upload token to a project-scoped token for future releases.
- [ ] Tag the release in the public repo (`github.com/SitePulsar/mcp-server`).
- [ ] Update https://www.sitepulsar.ai/llms.txt and install docs to reference
      `pip install sitepulsar-mcp`.
