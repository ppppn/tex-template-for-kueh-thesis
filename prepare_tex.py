#!/usr/bin/env python3
from datetime import datetime
from counter import CountBodyNumCharacter
from optparse import OptionParser
import re

def main(input_filename, output_filename):
  raw_contents = open(input_filename).read()
  TIMESTAMP=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
  counter=CountBodyNumCharacter(input_filename)
  supplied_contents = re.sub('==TIMESTAMP==', TIMESTAMP, raw_contents)
  supplied_contents = re.sub('==COUNTER==', str(counter), supplied_contents)
  f = open(output_filename, 'w')
  f.write(supplied_contents)

if __name__ == '__main__':
  parser = OptionParser()
  (options, args) = parser.parse_args()

  main(args[0], args[1])
