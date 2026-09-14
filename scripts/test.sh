#!/bin/bash

set -ex

ruff check .
ruff format --check .
mypy pwnedpwd
