#!/usr/bin/python3.7
"""
Created on 03. 06. 2019

@author: ibisek

Converts KiCad data for pick-and-place fabrication to MTTool (chinese CharmHigh machine) format.

KiCad exports fabrication output in format:
    Ref,Val,Package,PosX,PosY,Rot,Side

while MTTool requires:
    Designator, Footprint, Mid X, Mid Y, Ref X, Ref Y, Pad X, Pad Y, TB, Rotation, Comment

"""

import sys


def processArgs():

    if len(sys.argv) != 3:
        print('Usage:\n ./kicad2mtTool.py [infilename] [outFilename]')
        sys.exit(1)

    inFn = sys.argv[1]
    outFn = sys.argv[2]

    print(f"inputFile: {inFn}\noutputFile: {outFn}")

    return inFn, outFn


if __name__ == '__main__':

    inFilename, outFilename = processArgs()

    of = open(outFilename, 'w')
    of.write('Designator, Footprint, Mid X, Mid Y, Ref X, Ref Y, Pad X, Pad Y, TB, Rotation, Comment\n')

    lineCount = 0
    with open(inFilename) as f:
        f.readline()    # skip first line
        for line in f:
            line = line.strip()
            # print('line:', line)
            items = line.split(',')
            # print('items', items)

            reference = items[0].strip()
            value = items[1].strip()
            package = items[2].strip()
            posX = items[3].strip()
            posY = items[4].strip()
            rotation = items[5].strip()
            side = items[6].strip()
            side = 'T' if side == 'top' else 'B'

            # Designator, Footprint, Mid X, Mid Y, Ref X, Ref Y, Pad X, Pad Y, TB, Rotation, Comment
            outLine = f"{reference},{package},{posX},{posY},{posX},{posY},{posX},{posY},{side},{rotation},{value}\n"
            # print('outLine:', outLine)
            of.write(outLine)

            lineCount += 1

    of.flush()
    of.close()

    print(f"Processed {lineCount} lines.")

    print("Done.")

