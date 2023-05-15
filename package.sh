#!/bin/bash

python3.11 -m build

python3 -m twine upload --repository testpypi dist/*