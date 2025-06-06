#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if "opensn_console" not in globals():
    from mpi4py import MPI
    size = MPI.COMM_WORLD.size
    rank = MPI.COMM_WORLD.rank
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../")))
    from pyopensn.math import Vector3
    from pyopensn.logvol import SphereLogicalVolume

if __name__ == "__main__":

    lv1 = SphereLogicalVolume(r=1.3, x=1.0, y=-1.0, z=2.0)
    print("lv1 test 1:", lv1.Inside(Vector3(1.0, -1.0, 2.0)))
    print("lv1 test 2:", lv1.Inside(Vector3(1.0 + 1.3, -1.0, 2.0)))
    print("lv1 test 3:", lv1.Inside(Vector3(1.0 + 1.301, -1.0, 2.0)))
