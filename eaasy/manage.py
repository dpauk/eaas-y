from flask.cli import FlaskGroup
# import pytest 

from project import app

cli = FlaskGroup(app)

# @cli.command
# def test():
#     """Runs tests without code coverage"""
#     pytest.

if __name__ == '__main__':
    cli()
