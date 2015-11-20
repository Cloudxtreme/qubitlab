#!/usr/bin/env python

from core.diagram import Diagram
import sys
import os
import getopt
import importlib


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "c:s:o:hlr", ["help", "list"])
    except getopt.GetoptError:
        print "[ERROR] Wrong parameters."
        sys.exit(2)

    step = None
    circuit = None
    reset = False

    for opt, value in opts:
        if opt in ("-c", "--circuit"):
            circuit = value
            if not os.path.isdir("data/circuits/" + circuit):
                print 'ERROR: Circuit "' + circuit + '" is not available.'
                sys.exit(0)
        if opt in ("-r"):
            reset = True
        if opt in ("-s"):
            step = value
        if opt in ("-o"):
            sys.stdout = open(value, 'w')
        if opt in ("-h", "--help"):
            display_help()
            sys.exit(0)
        if opt in ("-l", "--list"):
            display_circuit_list()
            sys.exit(0)

    if circuit is None:
        print 'ERROR: Option "-c <circuit>" is required or "-h" (help).'
        sys.exit(0)

    if step is not None:
        step = int(step)

    circuit_package = importlib.import_module("data.circuits." + circuit + "." + circuit + "_module")
    circuit_class = getattr(circuit_package, circuit.capitalize() + 'Module')
    circuit_module = circuit_class()

    step_results = circuit_module.get_results_for_step(step, reset)

    print
    print "== Quantum state =="
    print
    print step_results['quantum_state'].replace('> +', '>\n+')
    print
    print

    if None is not step_results['measure_results']:
        print "== Measure results =="
        print
        print step_results['measure_results'].replace('> +', '>\n+')
        print
        print

    diagram = Diagram()
    diagram.display(circuit_module.get_title(), 'data/circuits/' + circuit + '/' + circuit + '_diagram.txt', step)
    print
    print

    # diagram.test_colors()
    # print


def display_help():
    print
    print "== QubitLab help =="
    print
    print "Usage:"
    print "$ ./qubitlab.py [options]"
    print
    print "Available options:"
    print "\t-h, --help             Show help."
    print "\t-l, --list             List of available circuits."
    print "\t-c <circuit_name>      Specify circuit. Required if -h and -l option are not used."
    print "\t-s <step>              Step number."
    print "\t-r                     Reset simulation results (clear cache for given circuit)."
    print "\t-o <file_name>         Specify output file."
    print
    print "Example of usage:"
    print "$ ./qubitlab.py -c teleportation -s 5 -r"
    print


def display_circuit_list():
    print
    print "== QubitLab circuits =="
    print
    print "teleportation"
    print


if __name__ == "__main__":
    main(sys.argv[1:])
