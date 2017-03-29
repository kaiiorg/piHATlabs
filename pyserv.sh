#!/bin/bash
ifconfig | grep "inet addr"
python3 -m http.server 8080
