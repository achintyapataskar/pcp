#!/usr/bin/python
#
# Copyright (C) 2012 Red Hat Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#

import os
import pmapi
import time
from pcp import *
from ctypes import *

def check_import (archive, hostname, timezone):

    pmi = pmiLogImport(archive)
    code = pmi.pmiSetHostname(hostname)

    code = pmi.pmiSetTimezone(timezone)

    pmid = pmi.pmiID(60, 2, 0)

    indom = pmi.pmiInDom(60, 2)

    units = pmi.pmiUnits(0,0,0,0,0,0)

    # create a metric with no instances (hinv.ncpu)
    code = pmi.pmiAddMetric("hinv.ncpu", PM_ID_NULL, PM_TYPE_U32, PM_INDOM_NULL, PM_SEM_DISCRETE, units)

    # give it a value
    code = pmi.pmiPutValue("hinv.ncpu", "", "42")

    # create a metric with instances (kernel.all.load)
    code = pmi.pmiAddMetric("kernel.all.load", pmid, PM_TYPE_FLOAT, indom, PM_SEM_DISCRETE, units)

    code = pmi.pmiAddInstance(indom, "1 minute", 1)

    code = pmi.pmiAddInstance(indom, "5 minute", 5)

    code = pmi.pmiAddInstance(indom, "15 minute", 15)

    # give them values
    code = pmi.pmiPutValue("kernel.all.load", "1 minute", "0.01")

    code = pmi.pmiPutValue("kernel.all.load", "5 minute", "0.05")

    code = pmi.pmiPutValue("kernel.all.load", "15 minute", "0.15")

    code = pmi.pmiWrite(time.gmtime().tm_sec,0)

    del pmi

if __name__ == '__main__':

    if (len(sys.argv) != 2):
        print "Usage: " + sys.argv[0] + " <path>"
        sys.exit(1)

    check_import(sys.argv[1], "www.abc.com", "EST-10")

