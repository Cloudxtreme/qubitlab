#!/usr/bin/env python

from core.diagram import Diagram
import sys
import os
import getopt
import importlib


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "c:s:o:h", ["circuit=", "output=", "step=", "help"])
    except getopt.GetoptError:
        print "[ERROR] Wrong parameters."
        sys.exit(2)

    step = None
    circuit = None

    for opt, value in opts:
        if opt in ("-c", "--circuit"):
            circuit = value
            if not os.path.isdir("data/circuits/" + circuit):
                print 'ERROR: Circuit "' + circuit + '" is not available.'
                sys.exit(0)
        if opt in ("-s", "--step"):
            step = value
        if opt in ("-o", "--output"):
            sys.stdout = open(value, 'w')
        if opt in ("-h", "--help"):
            display_help()
            sys.exit(0)

    if circuit is None:
        print 'ERROR: Circuit is required. Use "-c" or "--circuit" option.'
        sys.exit(0)

    if step is not None:
        step = int(step)

    circuit_module = importlib.import_module("data.circuits." + circuit + ".module")

    print
    print "== Quantum state =="
    print
    print circuit_module.get_quantum_state_for_step(step)
    print
    print
    print "== Measure results =="
    print
    print circuit_module.get_measure_results_for_step(step)
    print
    print
    diagram = Diagram()
    diagram.display(circuit_module.get_title(), 'data/circuits/' + circuit + '/diagram.txt', step)
    print
    print

    # diagram.test_colors()
    # print


def display_help():
    print
    print "QubitLab help..."
    print
    print "Example of usage:"
    print "$ ./qubitlab.py -c teleportation -s 3"
    print


if __name__ == "__main__":
    main(sys.argv[1:])
