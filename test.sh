#!/bin/bash

show_help() {
  echo """
  Commands
  ------------------
  tests:   run tests
  """
}

case "$1" in
  "tests" )
  # run python tests
  python3 tests.py
  ;;
  * )
  show_help
  ;;
esac
