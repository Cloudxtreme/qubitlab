#!/usr/bin/env python

from core.diagram import Diagram

print
print "QubitLab"
print
diagram = Diagram()
diagram.display('Quantum Teleportation Protocol', 'data/circuits/tele/tele_diagram.txt', 3)
print
print
