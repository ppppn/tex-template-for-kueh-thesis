#!/usr/bin/env python3
#coding: UTF-8
import re
from optparse import OptionParser


def CountBodyNumCharacter(filename, verbose=False):
  raw_contents = open(filename, 'r').read()

  convert_sequence = [
    re.compile('\\\\begin{comment}.*?\\\\end{comment}', re.DOTALL),
    re.compile('%.*'),
    re.compile('\\\\endnote{.*{\\\\it .*}.*}'),
    re.compile('\\\\endnote{.*label{.*}.*}'),
    re.compile('\\\\endnote{.*ref{.*}.*}'),
    re.compile('\\\\endnote{.*}'),
    re.compile('\\\\.*section{'),
    re.compile('\\\\.*section\*{'),
    re.compile('{\\\\it '),
    re.compile('\\\\newpage'),
    re.compile('\\\\addcontentsline.*\n'),
    re.compile('\n'),
    re.compile('}'),
  ]

  body = raw_contents.split('%BEGINBODY')[1]
  body = body.split('%ENDBODY')[0]

  for current_replace in convert_sequence:
    body = current_replace.sub('', body)

  if verbose == True:
    print(body)
    input('Continue to Enter...')
  return len(body)

def main():
  parser = OptionParser()
  verbose = False
  parser.add_option("-v", action="store_true", dest="verbose", default=False)
  (options, args) = parser.parse_args()
  verbose = options.verbose
  filename = args[0]
  print('{num} characters in {filename}'
          .format(num=CountBodyNumCharacter(filename, verbose),
                  filename=filename))

if __name__ == '__main__':
  main()
