#!/bin/bash

sudo goaccess ../part_04/*.log --log-format=COMBINED -a -o index.html
python3 -m http.server 8090