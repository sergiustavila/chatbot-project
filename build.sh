#!/bin/bash

rm -r build/*
rm -r docs/
make html
cp -r build/html/. docs
