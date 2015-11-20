#!/usr/bin/env python

from lib.qclib import *
import cPickle
import os.path
import re


class TeleportationModule:

    def __init__(self):
        self.title = 'Quantum Teleportation Protocol'

        self.module_name = re.sub(r'module$', '', self.__class__.__name__).lower()
        self.cache_file = 'tmp/' + self.module_name + '.pkl'
        self.simulation_data = []

    def get_title(self):
        return self.title

    def run_simulation(self):

        L = Arbitrary(s2 * array([[ 1, -1], [1, 1]]))
        R = Arbitrary(s2 * array([[1, 1], [-1, 1]]))
        S = Arbitrary([[ 1j, 0], [0, 1]])
        T = Arbitrary([[-1, 0], [0, -1j]])

        psi = Qubit([[2.0 / 7 * (cos(pi / 2 / 9) + 1.0j * sin(pi / 2 / 9))],
            [sqrt(45) / 7 * (cos(pi / 3 * 2) + 1.0j * sin(pi / 3 * 2))], ])

        circuit_input = psi ** ket0 ** ket0
        step1a = I ** L ** I
        state_step1 = step1a(circuit_input)
        step2a = step1a * (I ** cnot)
        state_step2 = step2a(circuit_input)
        step3a = step2a * (cnot ** I)
        state_step3 = step3a(circuit_input)
        step4a = step3a * (R ** I ** I)
        state_step4 = step4a(circuit_input)
        measure_step5 = state_step4.measure(1, 2)
        step1b = S ** cnot
        state_step6 = step1b(state_step4)
        step2b = step1b * (I ** Swap())
        state_step7 = step2b(state_step4)
        step3b = step2b * (cnot2 ** I)
        state_step8 = step3b(state_step4)
        step4b = step3b * (I ** Swap())
        state_step9 = step4b(state_step4)
        step5b = step4b * (S ** I ** T)
        state_step10 = step5b(state_step4)
        step6b = step5b * (I ** Swap())
        state_step11 = step6b(state_step4)
        step7b = step6b * (cnot2 ** I)
        state_step12 = step7b(state_step4)
        step8b = step7b * (I ** Swap())
        state_step13 = step8b(state_step4)

        self.simulation_data = [
            {'quantum_state': circuit_input.dirac(), 'measure_results': None},
            {'quantum_state': state_step1.dirac(), 'measure_results': None},
            {'quantum_state': state_step2.dirac(), 'measure_results': None},
            {'quantum_state': state_step3.dirac(), 'measure_results': None},
            {'quantum_state': state_step4.dirac(), 'measure_results': None},
            {'quantum_state': state_step4.dirac(), 'measure_results': measure_step5.dirac()},
            {'quantum_state': state_step6.dirac(), 'measure_results': None},
            {'quantum_state': state_step7.dirac(), 'measure_results': None},
            {'quantum_state': state_step8.dirac(), 'measure_results': None},
            {'quantum_state': state_step9.dirac(), 'measure_results': None},
            {'quantum_state': state_step10.dirac(), 'measure_results': None},
            {'quantum_state': state_step11.dirac(), 'measure_results': None},
            {'quantum_state': state_step12.dirac(), 'measure_results': None},
            {'quantum_state': state_step13.dirac(), 'measure_results': None}
        ]

        self.save_to_cache()

    def is_data_cached(self):
        return os.path.isfile(self.cache_file)

    def save_to_cache(self):
        cPickle.dump(self.simulation_data, open(self.cache_file, 'wb'))
        print ""

    def get_from_cache(self):
        self.simulation_data = cPickle.load(open(self.cache_file, 'rb'))

    def get_results_for_step(self, step=None, reset=False):

        if self.is_data_cached() and False is reset:
            self.get_from_cache()
        else:
            self.run_simulation()

        step_is_none = None is step
        if step_is_none:
            step = -1
        else:
            if step < 0:
                step = 0
            step_numb = len(self.simulation_data)
            if step > step_numb - 1:
                step = step_numb - 1

        return self.simulation_data[step]
