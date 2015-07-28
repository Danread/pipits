#!/usr/bin/env python

############################################################
# Argument Options

import argparse
parser = argparse.ArgumentParser("Re-format taxonomy assignment output from RDP-CLASSIFIER.")
parser.add_argument("-i, --in",
                    action = "store",
                    dest = "input",
                    metavar = "input",
                    help = "[REQUIRED] taxonomy assignment output from RDP-CLASSIFIER",
                    required = True)
parser.add_argument("-o, --out",
                    action = "store",
                    dest = "output",
                    metavar = "output",
                    help = "[REQUIRED] reformatted taxonomy assignment file",
                    required = True)
parser.add_argument("-c",
                    action = "store",
                    dest = "confidence",
                    metavar = "confidence",
                    help = "[REQUIRED] Minimum confidence to record an assignment",
                    required = True)
options = parser.parse_args()

############################################################

import sys

THRESHOLD = float(options.confidence)

handle_input = open(options.input, "rU")
handle_output = open(options.output, "w")

conf = [7, 10, 13, 16, 19, 22, 25];
cl  =   [5, 8, 11, 14, 17, 20, 23];
cl_lvl = ["k__", "p__", "c__", "o__", "f__" , "g__", "s__"]

for line in handle_input:
    e = line.rstrip().split("\t")
    BOOTSTRAP = 0.0
    taxonomy = []

    for i in range(0, 7):
    
        if float(e[conf[i]]) >= THRESHOLD:
            taxonomy.append(cl_lvl[i] + e[cl[i]])
            BOOTSTRAP = e[conf[i]]
        else:
            taxonomy.append(cl_lvl[i])
    
    handle_output.write(e[0] + "\t")
    handle_output.write("; ".join(taxonomy) + "\t")
    handle_output.write(str(BOOTSTRAP) + "\n")

handle_input.close()
handle_output.close()
