from binaryninja.plugin import BackgroundTaskThread

from .heuristics import *


class BGTask(BackgroundTaskThread):
    def __init__(self, bv, msg, f):
        BackgroundTaskThread.__init__(self, msg, True)
        self.f = f
        self.bv = bv

    def run(self):
        self.f(self.bv)


def find_flattened_functions_bg(bv):
    background_task = BGTask(
        bv, "Finding flattened functions", find_flattened_functions)
    background_task.start()


def find_complex_functions_bg(bv):
    background_task = BGTask(
        bv, "Finding complex functions", find_complex_functions)
    background_task.start()


def find_large_basic_blocks_bg(bv):
    background_task = BGTask(
        bv, "Finding large basic blocks", find_large_basic_blocks)
    background_task.start()


def find_uncommon_instruction_sequences_bg(bv):
    background_task = BGTask(
        bv, "Finding uncomming instruction sequences", find_uncommon_instruction_sequences)
    background_task.start()


def find_instruction_overlapping_bg(bv):
    background_task = BGTask(
        bv, "Finding instruction overlapping", find_instruction_overlapping)
    background_task.start()


def find_most_called_functions_bg(bv):
    background_task = BGTask(
        bv, "Finding most called functions", find_most_called_functions)
    background_task.start()


def find_loop_frequency_functions_bg(bv):
    background_task = BGTask(
        bv, "Finding functions with a high loop frequency", find_loop_frequency_functions)
    background_task.start()


def find_xor_decryption_loops_bg(bv):
    background_task = BGTask(
        bv, "Finding functions with xor decryption loops", find_xor_decryption_loops)
    background_task.start()


def find_rc4_bg(bv):
    background_task = BGTask(
        bv, "Finding functions which potentially implement RC4", find_rc4)
    background_task.start()


def detect_obfuscation_bg(bv):
    background_task = BGTask(
        bv, "Detecting obfuscated functions", detect_obfuscation)
    background_task.start()


def detect_obfuscation(bv):
    # find flattened functions
    find_flattened_functions(bv)

    # find complex functions
    find_complex_functions(bv)

    # find large basic blocks
    find_large_basic_blocks(bv)

    # find uncommon instruction sequences
    find_uncommon_instruction_sequences(bv)

    # find overlapping instructions
    find_instruction_overlapping(bv)

    # find most-called functions
    find_most_called_functions(bv)

    # find iterative complex functions
    find_iterative_complex_functions(bv)

    # find functions with xor decryption loops
    find_xor_decryption_loops(bv)

    # find functions with xor decryption loops
    find_rc4(bv)

