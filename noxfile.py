import nox

@nox.session
def tests(session):
    session.install(".", "pytest")
    session.run("pytest")


@nox.session
def build(session):
    session.run("coverage", "run", "-m", "pytest", *session.posargs)
    session.run("poetry", "build", external=True)

@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check")

@nox.session
def sanity(session):
    session.install("ruff")
    session.run("ruff", "check")
    session.install(".", "pytest")
    session.run("pytest")
    session.run("coverage", "run", "-m", "pytest", *session.posargs)
    session.run("poetry", "build", external=True)