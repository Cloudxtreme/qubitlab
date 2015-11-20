#!/usr/bin/env python

from lib.qclib import *


def get_title():
    return 'Quantum Teleportation Protocol'


def get_results_for_step(step=None):

    L = Arbitrary(s2 * array([ [ 1, -1],[1, 1],]))
    R = Arbitrary(s2 * array([ [1, 1], [-1, 1],]))
    S = Arbitrary([ [ 1j, 0], [0, 1], ])
    T = Arbitrary([ [-1, 0], [ 0, -1j], ])

    psi = Qubit([[2.0 / 7 * (cos(pi / 2 / 9) + 1.0j * sin(pi / 2 / 9))],
        [sqrt(45) / 7 * (cos(pi / 3 * 2) + 1.0j * sin(pi / 3 * 2))], ])

    input = psi ** ket0 ** ket0
    if 0 == step:
        return {
            'quantum_state': input.dirac(),
            'measure_results': None
        }

    step1a = I ** L ** I
    state_step1 = step1a(input)
    if 1 == step:
        return {
            'quantum_state': state_step1.dirac(),
            'measure_results': None
        }

    step2a = step1a * (I ** cnot)
    state_step2 = step2a(input)
    if 2 == step:
        return {
            'quantum_state': state_step2.dirac(),
            'measure_results': None
        }

    step3a = step2a * (cnot ** I)
    state_step3 = step3a(input)
    if 3 == step:
        return {
            'quantum_state': state_step3.dirac(),
            'measure_results': None
        }

    step4a = step3a * (R ** I ** I)
    state_step4 = step4a(input)
    if 4 == step:
        return {
            'quantum_state': state_step4.dirac(),
            'measure_results': None
        }

    measure_step5 = state_step4.measure(1, 2)
    if 5 == step:
        return {
            'quantum_state': state_step4.dirac(),
            'measure_results': measure_step5.dirac()
        }

    step1b = S ** cnot
    state_step6 = step1b(state_step4)
    if 6 == step:
        return {
            'quantum_state': state_step6.dirac(),
            'measure_results': None
        }

    step2b = step1b * (I ** Swap())
    state_step7 = step2b(state_step4)
    if 7 == step:
        return {
            'quantum_state': state_step7.dirac(),
            'measure_results': None
        }

    step3b = step2b * (cnot2 ** I)
    state_step8 = step3b(state_step4)
    if 8 == step:
        return {
            'quantum_state': state_step8.dirac(),
            'measure_results': None
        }

    step4b = step3b * (I ** Swap())
    state_step9 = step4b(state_step4)
    if 9 == step:
        return {
            'quantum_state': state_step9.dirac(),
            'measure_results': None
        }

    step5b = step4b * (S ** I ** T)
    state_step10 = step5b(state_step4)
    if 10 == step:
        return {
            'quantum_state': state_step10.dirac(),
            'measure_results': None
        }

    step6b = step5b * (I ** Swap())
    state_step11 = step6b(state_step4)
    if 11 == step:
        return {
            'quantum_state': state_step11.dirac(),
            'measure_results': None
        }

    step7b = step6b * (cnot2 ** I)
    state_step12 = step7b(state_step4)
    if 12 == step:
        return {
            'quantum_state': state_step12.dirac(),
            'measure_results': None
        }

    step8b = step7b * (I ** Swap())
    state_step13 = step8b(state_step4)
    return {
            'quantum_state': state_step13.dirac(),
            'measure_results': None
    }
