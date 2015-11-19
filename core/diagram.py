#!/usr/bin/env python

import re


class Diagram:
    def __init__(self):
        self.colors = {
            'invert': '\033[100m',
            'red': '\033[31m',
            'green': '\033[32m',
            'green2': '\033[92m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'violet': '\033[35m',
            'cyan': '\033[36m',
            'cyan2': '\033[96m',
            'gray': '\033[90m',
            'reset': '\033[0m'
        }

    @staticmethod
    def test_colors():
        for x in range(0, 255):
            print '\033[' + str(x) + 'm' + "CODE: " + str(x) + '\033[0m',

    def display(self, circuit_name, file_path, active_step=None):
        steps_line = self.get_steps_line(file_path)
        steps_numb = self.count_steps(steps_line)

        if active_step is None or active_step > steps_numb - 1:
            active_step = steps_numb - 1
        if active_step <= 0:
            active_step = 0

        step_pos = -1
        if active_step != steps_numb - 1:
            step_pos = self.get_step_pos(active_step, steps_line)

        active_color = self.colors['green2']
        inactive_color = self.colors['reset']
        reset_color = self.colors['reset']
        active_no_circ_color = self.colors['invert']
        no_circuit_color = self.colors['gray']

        print "{0}{1} (step {2} of {3}){4}\n".format(no_circuit_color, circuit_name, str(active_step),
                                                     str(steps_numb - 1), reset_color)

        with open(file_path) as f:
            for line in f:
                if self.check_if_is_no_circuit_line(line):
                    # print no_circuit_color + line.rstrip('\n') + reset_color
                    print "{0}{1}{2}{3}{4}{5}".format(active_no_circ_color, line[:step_pos].rstrip('\n'), reset_color,
                                                      no_circuit_color, line[step_pos:].rstrip('\n'), reset_color)
                else:
                    print "{0}{1}{2}{3}{4}{5}".format(active_color, line[:step_pos].rstrip('\n'), reset_color,
                                                      inactive_color, line[step_pos:].rstrip('\n'), reset_color)

    def get_steps_line(self, file_path):
        with open(file_path) as f:
            for line in f:
                if self.check_if_is_steps_line(line):
                    return line.rstrip()
        return ''

    @staticmethod
    def count_steps(steps_line):
        results = re.findall('(\|\d+\s*)', steps_line)
        return len(results)

    def check_if_is_no_circuit_line(self, line):
        if self.check_if_is_steps_line(line):
            return True
        if self.check_if_is_dots_line(line):
            return True
        return False

    @staticmethod
    def check_if_is_steps_line(line):
        steps_line_pattern = re.compile('\s*(\|\d+\s*)+\s*')
        line_match = steps_line_pattern.match(line)
        if line_match:
            return True
        return False

    @staticmethod
    def check_if_is_dots_line(line):
        steps_line_pattern = re.compile('\s*\.+\s*')
        line_match = steps_line_pattern.match(line)
        if line_match:
            return True
        return False

    @staticmethod
    def get_step_pos(step, steps_line):
        return re.search(("\|" + str(step) + "\s*(\||$)"), steps_line).end() - 1
