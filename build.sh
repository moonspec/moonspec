#!/usr/bin/env bash

make -C docs documentation
python3 setup.py sdist
