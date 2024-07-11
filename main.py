# Imports
import sys
import typing as t
from dotenv import load_dotenv

load_dotenv()


# noinspection PyUnresolvedReferences
def main(argc: int, argv: t.List[str]):
    """ Program's entry point."""
    from backend.application import run
    from backend.routes import index
    run()


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
