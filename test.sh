#!/bin/bash

cd "$(dirname "$0")" || exit
DIR="$(cd "$(dirname "$0")" && pwd)"

result_file='./test_example.txt'
rm -f $result_file

echo 'Testing our program:' >> "$result_file"

# AKAZE test
echo "Testing AKAZE: " >> "$result_file"
$DIR/checker.py example.bmp -a AKAZE >> "$result_file"
echo $'\n' >> "$result_file"

# OBR test
echo 'Testing OBR: ' >> "$result_file"
$DIR/checker.py example.bmp -a OBR >> "$result_file"
echo $'\n' >> "$result_file"

# TEMPLATE test
echo 'Testing OBR: ' >> "$result_file"
$DIR/checker.py example.bmp -t ./templates/ -a TEMPLATE >> "$result_file"
