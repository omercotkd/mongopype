# 1. bump version in pyproject.toml, then commit & push
git add pyproject.toml && git commit -m "bump version to 0.1.0" && git push origin main

# 2. tag it — this triggers the publish job
git tag v0.1.0 && git push origin v0.1.0