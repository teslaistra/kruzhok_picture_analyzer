#!/usr/bin/env bash

cd "$(dirname "$0")" || exit
DIR=$(cd "$(dirname "$0")" && pwd)

result_file='./test_example.txt'
rm -f $result_file

{
  # AKAZE test
  OUTPUT=$("$DIR"/checker.py "$DIR"/example.bmp -t "$DIR"/logo.jpg -a AKAZE);
  echo "Testing AKAZE: ${OUTPUT}";
  echo "-----"

  # ORB test
  OUTPUT=$("$DIR"/checker.py "$DIR"/example.bmp -t "$DIR"/logo.jpg -a ORB);
  echo "Testing ORB: ${OUTPUT}";
  echo "-----"

  # TEMPLATE test
  OUTPUT=$("$DIR"/checker.py "$DIR"/example.bmp -t "$DIR"/templates/ -a TEMPLATE);
  echo "Testing TEMPLATE: ${OUTPUT}";

} >> $result_file
