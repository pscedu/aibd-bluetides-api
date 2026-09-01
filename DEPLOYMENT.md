# bluetides/api — recovered from the deployed tree

This code was recovered from the running production server (`bluetides-api.psc.edu`), not cloned.
Its upstream repository has since been identified, but the deployed tree is **not** identical to it
(see below), and the deployed tree is the source of truth for this directory.
`README.upstream.md` is the project's own README as it existed on the server.

## Provenance (resolved)

- **Upstream: https://github.com/pscedu/aibd-bluetides-api** (`master` @ `24b94a1`, 2023-08-17,
  "Merge pull request #8 from pscedu/dependabot/pip/certifi-2023.7.22").
- The deployed tree is an **older checkout of that repo plus two uncommitted local path edits**.
  `master` differs from this directory in exactly three files:
  | file | upstream `master` | deployed (here) |
  |---|---|---|
  | `api/constants.py` | `PIG_BASE_DIR = '/pylon5/as5pi3p/bluetides3/'` | `/hildafs/datasets/public/BlueTides/PIG_files/` |
  | `original_scripts/header_parser.py` | `/pylon5/as5pi3p/bluetides3/PIG_*` | `/hildafs/datasets/public/BlueTides/PIG_FILES/PIG_*` |
  | `requirements.txt` | `certifi==2023.7.22` (dependabot) | `certifi==2020.4.5.2`, now repinned — see below |
  The two path edits are the Bridges-1 -> Bridges-2 dataset move; they were never committed, so
  before this recovery they existed only on `vm017`.
- **`pscedu/aibd-astrid-api` is a fork of this same repo that never diverged** — its `master` head is
  the same commit, `24b94a1`, which is why its `constants.py` pointed at BlueTides data. It is not a
  separate codebase to reconcile against, and it is not the ASTRID API's real source.
- **`reference/cosmo/bluetides-api`** (a clone of `pscedu/cosmo`) is a *publication*, not an
  upstream: the whole `api/` tree arrived there in one commit, `b992c40` "Adding API portal."
  (2022-07-09), hand-sanitized — absolute Bridges paths replaced with placeholders, README scrubbed,
  `.gitignore` added, a notebook dropped, and the **`numpy` pin hand-edited `1.18.5` -> `1.22`**.
  That edited pin was never installed anywhere; do not treat it as authoritative.
- The `pscedu/aibd-bluetides-webpage` remote configured on the deployed directory on `vm017` is
  simply wrong for this code.
- It ran under `/etc/systemd/system/cosmo_api.service`:
  `uvicorn api.main:app --reload --port=8001`, venv `/opt/environments/cosmo/api`.

## Dependency pins

`requirements.txt` is **repinned to the production venv's `pip freeze`** — the versions the running
API actually imported (`bigfile 0.1.51`, `fastapi 0.65.1`, `pydantic 1.8.2`, `uvicorn 0.13.4`,
`typing-extensions 4.1.1`, ...), which differ from the versions the repo's original
`requirements.txt` claimed. A plain `pip install -r` of that original file reproduces neither
production nor this image. The venv was shared with unrelated projects (vitessce, zarr, negspy,
google-api-*, fedex); that pollution is not listed, and it is why the venv's exact version set is
not pip-resolvable. Two pins therefore deviate from the freeze on purpose, each toward what the
package itself declares: `starlette==0.14.2` (fastapi 0.65.1's own requirement; the venv's 0.14.0 is
a combination fastapi considers wrong) and `click==7.1.2` (uvicorn 0.13.4's requirement; click only
runs in uvicorn's CLI entry point, which this image never uses — it serves via gunicorn +
UvicornWorker). `pip check` in the built image is clean. Rationale in the file's header comment.

## Containerization

- `api/constants.py` reads `PIG_BASE_DIR` from the environment, defaulting to `/data/bluetides/`
  (trailing slash is load-bearing: `utils.py` concatenates strings).
- `requirements.txt` adds `gunicorn==20.1.0` (last release supporting Python 3.8).
- `Dockerfile` serves `api.main:app` from `/app` with gunicorn + `UvicornWorker`, 2 workers, 600 s
  timeout, no `--reload`. `main.py` uses package-relative imports, so it must never be run from
  inside `api/`.
- These pins have no aarch64 wheels; build on x86_64 (or emulate — see the task report).

```bash
docker build -t bluetides-api:test .
docker run --rm -d --name btapi -p 127.0.0.1:18014:8000 \
  -v /hildafs/datasets/public/BlueTides/PIG_files:/data/bluetides:ro bluetides-api:test
```

## Still open

- Where this lands in git is a human decision: upstream `pscedu/aibd-bluetides-api` is the natural
  home (this tree is that repo plus the two path edits, and the containerization on top), but this
  directory is deliberately not a git repository.
- `api/tests/test_main.py::test_get_pig` asserts the exact `os.listdir()` ordering of PIG folders, so
  it will likely fail on a new mount for reasons unrelated to the API.

Full reconciliation and verification detail: the Task 5 report,
`.superpowers/sdd/2026-09-01-vera-migration-dockerization/task-5-report.md`.
