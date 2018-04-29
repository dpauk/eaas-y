import pytest

from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)


@cli.command()
def test():
    """Runs tests without code coverage"""
    # tests = pytest.main.
    pytest.main(['project/tests'])


if __name__ == '__main__':
    cli()
