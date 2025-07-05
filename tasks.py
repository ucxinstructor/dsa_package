from invoke import task
import os
from pathlib import Path
import webbrowser

@task
def clean(c):
    """Remove build and doc artifacts"""
    c.run("rm -rf build dist *.egg-info .pytest_cache .mypy_cache docs/_build", warn=True)

@task
def lint(c):
    """Run linter (ruff)"""
    c.run("ruff .")

@task
def format(c):
    """Format code with black"""
    c.run("black .")

@task
def typecheck(c):
    """Run static type checker"""
    c.run("mypy .")

@task
def test(c):
    """Run test suite"""
    c.run("pytest tests")

@task(pre=[clean])
def build(c):
    """Build Python package"""
    c.run("python -m build")

@task(help={"clean": "Remove existing docs", "open": "Open docs in browser"})
def docs(c, clean=False, open=False):
    """Build Sphinx documentation"""
    if clean:
        c.run("rm -rf docs/_build")
    c.run("sphinx-build -b html docs/ docs/_build/html")
    print("📘 Docs built at docs/_build/html")
    if open:
        index = Path("docs/_build/html/index.html").resolve()
        webbrowser.open(f"file://{index}")

@task(pre=[lint, typecheck, test])
def check(c):
    """Run all checks: lint, type, test"""
    print("✔ All checks passed!")

@task(pre=[build, check, docs])
def release(c):
    """Prepare for release: build, check, and generate docs"""
    print("🚀 Ready to release!")

