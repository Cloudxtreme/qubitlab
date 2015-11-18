
def get_title():
    return 'Quantum Teleportation Protocol'


def get_quantum_state_for_step(step):
    if None is step:
        return 'quantum state for final step...'
    return 'quantum state for step ' + str(step) + '...'


def get_measure_results_for_step(step):
    if None is step:
        return 'measure results for final step...'
    return 'measure results for step ' + str(step) + '...'
