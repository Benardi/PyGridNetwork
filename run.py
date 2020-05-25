#!/bin/env python

from gridnetwork import create_app, raise_grid


if __name__ == "__main__":
    app,server = raise_grid()
else:
    app = create_app()
