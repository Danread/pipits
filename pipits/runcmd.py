#!/usr/bin/env python

import os, subprocess

__author__ = "Hyun Soon Gweon"
__copyright__ = "Copyright 2015, The PIPITS Project"
__credits__ = ["Hyun Soon Gweon", "Anna Oliver", "Joanne Taylor", "Tim Booth", "Melanie Gibbs", "Daniel S. Read", "Robert I. Griffiths", "Karsten Schonrogge"]
__license__ = "GPL"
__maintainer__ = "Hyun Soon Gweon"
__email__ = "hyugwe@ceh.ac.uk"


# This is for well-behaving third party tools i.e. ones that give proper STDOUT and STDERR
def run_cmd(command, logger, verbose):
    logger.debug(command)
    FNULL = open(os.devnull, 'w')
    if verbose:
        p = subprocess.Popen(command, shell=True)
    else:
        p = subprocess.Popen(command, shell=True, stdout=FNULL)
    p.wait()
    FNULL.close()
    if p.returncode != 0:
        logger.error("None zero returncode: " + command)
        exit(1)


# Run ITSx. Chop reads into regions. Re-orientate where needed
# ITSx always prints something to STDERR and outputs nothing to STDOUT, so need to supress stdout in non-verbose mode
# Returncode is always 0 no matter what... so way to tell whether it quits with an error or not other than by capturing STDERR with a phrase "FATAL ERROR" - not implemented 
def run_cmd_ITSx(command, logger, verbose):
    logger.debug(command)
    FNULL = open(os.devnull, 'w')
    if verbose:
        p = subprocess.Popen(command, shell=True)
    else:
        p = subprocess.Popen(command, shell=True, stderr=FNULL)
    p.wait()
    FNULL.close()
    if p.returncode != 0:
        logger.error("None zero returncode: " + command)
        exit(1)

# VSEARCH outputs copyright info and licence to STDOUT; and the running outputs to STDERRDATA
def run_cmd_VSEARCH(command, logger, verbose):
    logger.debug(command)
    FNULL = open(os.devnull, 'w')
    if verbose:
        p = subprocess.Popen(command, shell=True)
    else:
        p = subprocess.Popen(command, shell=True, stdout=FNULL, stderr=FNULL)
    p.wait()
    FNULL.close()
    if p.returncode != 0:
        logger.error("None zero returncode: " + command)
        exit(1)

