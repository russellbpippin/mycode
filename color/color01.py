#!/usr/bin/env python3

import crayons

def main():
    print(crayons.red("red string"))
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
    crayons.disable()
    crayons.DISABLE_COLOR = False
    print(crayons.red('red string', bold=true))

main()


