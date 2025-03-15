
import itertools
import random
import string
from z3 import *
import sys
from generator_helpers import *
import pickle
from heapq import heappush, heappop
import pprint
import os
import math
import re

options = {
    'vafuzz_opt_0': Option('vafuzz_opt_0', 'bool', '-', '='),
    'vafuzz_opt_1': Option('vafuzz_opt_1', 'bool', '-', '='),
    'vafuzz_opt_2': Option('vafuzz_opt_2', 'choice', '--', '=', choices=['vafuzz_opt_2_choice_0', 'vafuzz_opt_2_choice_1', 'vafuzz_opt_2_choice_2', 'vafuzz_opt_2_choice_3', 'vafuzz_opt_2_choice_4', 'vafuzz_opt_2_choice_5', 'vafuzz_opt_2_choice_6', 'vafuzz_opt_2_choice_7', 'vafuzz_opt_2_choice_8']),
    'vafuzz_opt_3': Option('vafuzz_opt_3', 'bool', '--', '='),
    'vafuzz_opt_4': Option('vafuzz_opt_4', 'bool', '--', '='),
    'vafuzz_opt_5': Option('vafuzz_opt_5', 'bool', '--', '='),
    'vafuzz_opt_6': Option('vafuzz_opt_6', 'bool', '-', '='),
    'vafuzz_opt_7': Option('vafuzz_opt_7', 'bool', '--', '='),
    'vafuzz_opt_8': Option('vafuzz_opt_8', 'choice', '--', '=', choices=['vafuzz_opt_8_choice_0', 'vafuzz_opt_8_choice_1', 'vafuzz_opt_8_choice_2', 'vafuzz_opt_8_choice_3']),
    'vafuzz_opt_9': Option('vafuzz_opt_9', 'bool', '-', '='),
    'vafuzz_opt_10': Option('vafuzz_opt_10', 'bool', '-', '='),
    'vafuzz_opt_11': Option('vafuzz_opt_11', 'bool', '-', '='),
    'vafuzz_opt_12': Option('vafuzz_opt_12', 'bool', '-', '='),
    'vafuzz_opt_13': Option('vafuzz_opt_13', 'bool', '-', '='),
    'vafuzz_opt_14': Option('vafuzz_opt_14', 'bool', '-', '='),
    'vafuzz_opt_15': Option('vafuzz_opt_15', 'bool', '-', '='),
    'vafuzz_opt_16': Option('vafuzz_opt_16', 'bool', '--', '='),
    'vafuzz_opt_17': Option('vafuzz_opt_17', 'bool', '--', '='),
    'vafuzz_opt_18': Option('vafuzz_opt_18', 'bool', '--', '='),
    'vafuzz_opt_19': Option('vafuzz_opt_19', 'bool', '--', '='),
    'vafuzz_opt_20': Option('vafuzz_opt_20', 'choice', '--', '=', choices=['vafuzz_opt_20_choice_0', 'vafuzz_opt_20_choice_1', 'vafuzz_opt_20_choice_2']),
    'vafuzz_opt_21': Option('vafuzz_opt_21', 'choice', '--', '=', choices=['vafuzz_opt_21_choice_0', 'vafuzz_opt_21_choice_1', 'vafuzz_opt_21_choice_2', 'vafuzz_opt_21_choice_3', 'vafuzz_opt_21_choice_4', 'vafuzz_opt_21_choice_5', 'vafuzz_opt_21_choice_6', 'vafuzz_opt_21_choice_7', 'vafuzz_opt_21_choice_8', 'vafuzz_opt_21_choice_9', 'vafuzz_opt_21_choice_10', 'vafuzz_opt_21_choice_11', 'vafuzz_opt_21_choice_12', 'vafuzz_opt_21_choice_13', 'vafuzz_opt_21_choice_14', 'vafuzz_opt_21_choice_15', 'vafuzz_opt_21_choice_16', 'vafuzz_opt_21_choice_17', 'vafuzz_opt_21_choice_18', 'vafuzz_opt_21_choice_19', 'vafuzz_opt_21_choice_20', 'vafuzz_opt_21_choice_21', 'vafuzz_opt_21_choice_22', 'vafuzz_opt_21_choice_23', 'vafuzz_opt_21_choice_24', 'vafuzz_opt_21_choice_25', 'vafuzz_opt_21_choice_26', 'vafuzz_opt_21_choice_27', 'vafuzz_opt_21_choice_28', 'vafuzz_opt_21_choice_29', 'vafuzz_opt_21_choice_30', 'vafuzz_opt_21_choice_31', 'vafuzz_opt_21_choice_32', 'vafuzz_opt_21_choice_33', 'vafuzz_opt_21_choice_34', 'vafuzz_opt_21_choice_35', 'vafuzz_opt_21_choice_36', 'vafuzz_opt_21_choice_37', 'vafuzz_opt_21_choice_38', 'vafuzz_opt_21_choice_39', 'vafuzz_opt_21_choice_40', 'vafuzz_opt_21_choice_41', 'vafuzz_opt_21_choice_42', 'vafuzz_opt_21_choice_43', 'vafuzz_opt_21_choice_44', 'vafuzz_opt_21_choice_45', 'vafuzz_opt_21_choice_46', 'vafuzz_opt_21_choice_47', 'vafuzz_opt_21_choice_48', 'vafuzz_opt_21_choice_49', 'vafuzz_opt_21_choice_50', 'vafuzz_opt_21_choice_51', 'vafuzz_opt_21_choice_52', 'vafuzz_opt_21_choice_53', 'vafuzz_opt_21_choice_54', 'vafuzz_opt_21_choice_55', 'vafuzz_opt_21_choice_56', 'vafuzz_opt_21_choice_57', 'vafuzz_opt_21_choice_58', 'vafuzz_opt_21_choice_59', 'vafuzz_opt_21_choice_60', 'vafuzz_opt_21_choice_61', 'vafuzz_opt_21_choice_62', 'vafuzz_opt_21_choice_63', 'vafuzz_opt_21_choice_64', 'vafuzz_opt_21_choice_65', 'vafuzz_opt_21_choice_66', 'vafuzz_opt_21_choice_67', 'vafuzz_opt_21_choice_68', 'vafuzz_opt_21_choice_69', 'vafuzz_opt_21_choice_70', 'vafuzz_opt_21_choice_71', 'vafuzz_opt_21_choice_72', 'vafuzz_opt_21_choice_73', 'vafuzz_opt_21_choice_74', 'vafuzz_opt_21_choice_75', 'vafuzz_opt_21_choice_76', 'vafuzz_opt_21_choice_77', 'vafuzz_opt_21_choice_78', 'vafuzz_opt_21_choice_79', 'vafuzz_opt_21_choice_80', 'vafuzz_opt_21_choice_81', 'vafuzz_opt_21_choice_82', 'vafuzz_opt_21_choice_83', 'vafuzz_opt_21_choice_84', 'vafuzz_opt_21_choice_85', 'vafuzz_opt_21_choice_86', 'vafuzz_opt_21_choice_87', 'vafuzz_opt_21_choice_88', 'vafuzz_opt_21_choice_89', 'vafuzz_opt_21_choice_90', 'vafuzz_opt_21_choice_91', 'vafuzz_opt_21_choice_92', 'vafuzz_opt_21_choice_93', 'vafuzz_opt_21_choice_94', 'vafuzz_opt_21_choice_95', 'vafuzz_opt_21_choice_96', 'vafuzz_opt_21_choice_97', 'vafuzz_opt_21_choice_98', 'vafuzz_opt_21_choice_99', 'vafuzz_opt_21_choice_100', 'vafuzz_opt_21_choice_101', 'vafuzz_opt_21_choice_102', 'vafuzz_opt_21_choice_103', 'vafuzz_opt_21_choice_104', 'vafuzz_opt_21_choice_105', 'vafuzz_opt_21_choice_106', 'vafuzz_opt_21_choice_107', 'vafuzz_opt_21_choice_108', 'vafuzz_opt_21_choice_109', 'vafuzz_opt_21_choice_110', 'vafuzz_opt_21_choice_111', 'vafuzz_opt_21_choice_112', 'vafuzz_opt_21_choice_113', 'vafuzz_opt_21_choice_114', 'vafuzz_opt_21_choice_115', 'vafuzz_opt_21_choice_116', 'vafuzz_opt_21_choice_117', 'vafuzz_opt_21_choice_118', 'vafuzz_opt_21_choice_119', 'vafuzz_opt_21_choice_120', 'vafuzz_opt_21_choice_121', 'vafuzz_opt_21_choice_122', 'vafuzz_opt_21_choice_123', 'vafuzz_opt_21_choice_124', 'vafuzz_opt_21_choice_125', 'vafuzz_opt_21_choice_126', 'vafuzz_opt_21_choice_127', 'vafuzz_opt_21_choice_128', 'vafuzz_opt_21_choice_129', 'vafuzz_opt_21_choice_130', 'vafuzz_opt_21_choice_131', 'vafuzz_opt_21_choice_132', 'vafuzz_opt_21_choice_133', 'vafuzz_opt_21_choice_134', 'vafuzz_opt_21_choice_135', 'vafuzz_opt_21_choice_136', 'vafuzz_opt_21_choice_137', 'vafuzz_opt_21_choice_138', 'vafuzz_opt_21_choice_139', 'vafuzz_opt_21_choice_140', 'vafuzz_opt_21_choice_141', 'vafuzz_opt_21_choice_142', 'vafuzz_opt_21_choice_143', 'vafuzz_opt_21_choice_144', 'vafuzz_opt_21_choice_145', 'vafuzz_opt_21_choice_146', 'vafuzz_opt_21_choice_147', 'vafuzz_opt_21_choice_148', 'vafuzz_opt_21_choice_149', 'vafuzz_opt_21_choice_150', 'vafuzz_opt_21_choice_151', 'vafuzz_opt_21_choice_152', 'vafuzz_opt_21_choice_153', 'vafuzz_opt_21_choice_154', 'vafuzz_opt_21_choice_155', 'vafuzz_opt_21_choice_156', 'vafuzz_opt_21_choice_157', 'vafuzz_opt_21_choice_158', 'vafuzz_opt_21_choice_159', 'vafuzz_opt_21_choice_160', 'vafuzz_opt_21_choice_161', 'vafuzz_opt_21_choice_162', 'vafuzz_opt_21_choice_163', 'vafuzz_opt_21_choice_164', 'vafuzz_opt_21_choice_165', 'vafuzz_opt_21_choice_166', 'vafuzz_opt_21_choice_167', 'vafuzz_opt_21_choice_168', 'vafuzz_opt_21_choice_169', 'vafuzz_opt_21_choice_170', 'vafuzz_opt_21_choice_171', 'vafuzz_opt_21_choice_172', 'vafuzz_opt_21_choice_173', 'vafuzz_opt_21_choice_174', 'vafuzz_opt_21_choice_175', 'vafuzz_opt_21_choice_176', 'vafuzz_opt_21_choice_177', 'vafuzz_opt_21_choice_178', 'vafuzz_opt_21_choice_179', 'vafuzz_opt_21_choice_180', 'vafuzz_opt_21_choice_181', 'vafuzz_opt_21_choice_182', 'vafuzz_opt_21_choice_183', 'vafuzz_opt_21_choice_184', 'vafuzz_opt_21_choice_185', 'vafuzz_opt_21_choice_186', 'vafuzz_opt_21_choice_187', 'vafuzz_opt_21_choice_188', 'vafuzz_opt_21_choice_189', 'vafuzz_opt_21_choice_190', 'vafuzz_opt_21_choice_191', 'vafuzz_opt_21_choice_192', 'vafuzz_opt_21_choice_193', 'vafuzz_opt_21_choice_194', 'vafuzz_opt_21_choice_195', 'vafuzz_opt_21_choice_196', 'vafuzz_opt_21_choice_197', 'vafuzz_opt_21_choice_198', 'vafuzz_opt_21_choice_199', 'vafuzz_opt_21_choice_200', 'vafuzz_opt_21_choice_201', 'vafuzz_opt_21_choice_202', 'vafuzz_opt_21_choice_203', 'vafuzz_opt_21_choice_204', 'vafuzz_opt_21_choice_205', 'vafuzz_opt_21_choice_206', 'vafuzz_opt_21_choice_207', 'vafuzz_opt_21_choice_208', 'vafuzz_opt_21_choice_209', 'vafuzz_opt_21_choice_210', 'vafuzz_opt_21_choice_211', 'vafuzz_opt_21_choice_212', 'vafuzz_opt_21_choice_213', 'vafuzz_opt_21_choice_214', 'vafuzz_opt_21_choice_215', 'vafuzz_opt_21_choice_216', 'vafuzz_opt_21_choice_217', 'vafuzz_opt_21_choice_218', 'vafuzz_opt_21_choice_219', 'vafuzz_opt_21_choice_220', 'vafuzz_opt_21_choice_221', 'vafuzz_opt_21_choice_222', 'vafuzz_opt_21_choice_223', 'vafuzz_opt_21_choice_224', 'vafuzz_opt_21_choice_225', 'vafuzz_opt_21_choice_226', 'vafuzz_opt_21_choice_227', 'vafuzz_opt_21_choice_228', 'vafuzz_opt_21_choice_229', 'vafuzz_opt_21_choice_230', 'vafuzz_opt_21_choice_231', 'vafuzz_opt_21_choice_232', 'vafuzz_opt_21_choice_233', 'vafuzz_opt_21_choice_234', 'vafuzz_opt_21_choice_235', 'vafuzz_opt_21_choice_236', 'vafuzz_opt_21_choice_237', 'vafuzz_opt_21_choice_238', 'vafuzz_opt_21_choice_239', 'vafuzz_opt_21_choice_240', 'vafuzz_opt_21_choice_241', 'vafuzz_opt_21_choice_242', 'vafuzz_opt_21_choice_243', 'vafuzz_opt_21_choice_244', 'vafuzz_opt_21_choice_245', 'vafuzz_opt_21_choice_246', 'vafuzz_opt_21_choice_247', 'vafuzz_opt_21_choice_248', 'vafuzz_opt_21_choice_249', 'vafuzz_opt_21_choice_250', 'vafuzz_opt_21_choice_251', 'vafuzz_opt_21_choice_252', 'vafuzz_opt_21_choice_253', 'vafuzz_opt_21_choice_254']),
    'vafuzz_opt_22': Option('vafuzz_opt_22', 'bool', '-', '='),
    'vafuzz_opt_23': Option('vafuzz_opt_23', 'bool', '--', '='),
}

prefixes = ['-', '--']

connectors = ['=']

opt_name_map = {
    'vafuzz_opt_0': 'a',
    'vafuzz_opt_1': 'A',
    'vafuzz_opt_2': 'demangle',
    'vafuzz_opt_3': 'no-demangle',
    'vafuzz_opt_4': 'recurse-limit',
    'vafuzz_opt_5': 'no-recurse-limit',
    'vafuzz_opt_6': 'D',
    'vafuzz_opt_7': 'defined-only',
    'vafuzz_opt_8': 'format',
    'vafuzz_opt_9': 'g',
    'vafuzz_opt_10': 'l',
    'vafuzz_opt_11': 'n',
    'vafuzz_opt_12': 'p',
    'vafuzz_opt_13': 'r',
    'vafuzz_opt_14': 'S',
    'vafuzz_opt_15': 's',
    'vafuzz_opt_16': 'quiet',
    'vafuzz_opt_17': 'size-sort',
    'vafuzz_opt_18': 'special-syms',
    'vafuzz_opt_19': 'synthetic',
    'vafuzz_opt_20': 'radix',
    'vafuzz_opt_21': 'target',
    'vafuzz_opt_22': 'u',
    'vafuzz_opt_23': 'with-symbol-versions',
}

opt_name_map_keys = sorted(opt_name_map.keys(), reverse=True)

opt_name_revert_map = {
    'a': 'vafuzz_opt_0',
    'A': 'vafuzz_opt_1',
    'demangle': 'vafuzz_opt_2',
    'no-demangle': 'vafuzz_opt_3',
    'recurse-limit': 'vafuzz_opt_4',
    'no-recurse-limit': 'vafuzz_opt_5',
    'D': 'vafuzz_opt_6',
    'defined-only': 'vafuzz_opt_7',
    'format': 'vafuzz_opt_8',
    'g': 'vafuzz_opt_9',
    'l': 'vafuzz_opt_10',
    'n': 'vafuzz_opt_11',
    'p': 'vafuzz_opt_12',
    'r': 'vafuzz_opt_13',
    'S': 'vafuzz_opt_14',
    's': 'vafuzz_opt_15',
    'quiet': 'vafuzz_opt_16',
    'size-sort': 'vafuzz_opt_17',
    'special-syms': 'vafuzz_opt_18',
    'synthetic': 'vafuzz_opt_19',
    'radix': 'vafuzz_opt_20',
    'target': 'vafuzz_opt_21',
    'u': 'vafuzz_opt_22',
    'with-symbol-versions': 'vafuzz_opt_23',
}

opt_name_revert_map_keys = sorted(opt_name_revert_map.keys(), reverse=True)

choice_map = {
    'vafuzz_opt_2_choice_0': 'auto',
    'vafuzz_opt_2_choice_1': 'gnu',
    'vafuzz_opt_2_choice_2': 'lucid',
    'vafuzz_opt_2_choice_3': 'arm',
    'vafuzz_opt_2_choice_4': 'hp',
    'vafuzz_opt_2_choice_5': 'edg',
    'vafuzz_opt_2_choice_6': 'gnu-v3',
    'vafuzz_opt_2_choice_7': 'java',
    'vafuzz_opt_2_choice_8': 'gnat',
    'vafuzz_opt_8_choice_0': 'bsd',
    'vafuzz_opt_8_choice_1': 'sysv',
    'vafuzz_opt_8_choice_2': 'posix',
    'vafuzz_opt_8_choice_3': 'just-symbols',
    'vafuzz_opt_20_choice_0': 'x',
    'vafuzz_opt_20_choice_1': 'd',
    'vafuzz_opt_20_choice_2': 'o',
    'vafuzz_opt_21_choice_0': 'elf64-x86-64',
    'vafuzz_opt_21_choice_1': 'elf32-bigaarch64',
    'vafuzz_opt_21_choice_2': 'elf32-littleaarch64',
    'vafuzz_opt_21_choice_3': 'elf64-bigaarch64',
    'vafuzz_opt_21_choice_4': 'elf64-bigaarch64-cloudabi',
    'vafuzz_opt_21_choice_5': 'elf64-littleaarch64',
    'vafuzz_opt_21_choice_6': 'elf64-littleaarch64-cloudabi',
    'vafuzz_opt_21_choice_7': 'mach-o-arm64',
    'vafuzz_opt_21_choice_8': 'ecoff-littlealpha',
    'vafuzz_opt_21_choice_9': 'elf64-alpha',
    'vafuzz_opt_21_choice_10': 'elf64-alpha-freebsd',
    'vafuzz_opt_21_choice_11': 'vms-alpha',
    'vafuzz_opt_21_choice_12': 'vms-libtxt',
    'vafuzz_opt_21_choice_13': 'elf32-am33lin',
    'vafuzz_opt_21_choice_14': 'elf32-bigarc',
    'vafuzz_opt_21_choice_15': 'elf32-littlearc',
    'vafuzz_opt_21_choice_16': 'elf32-bigarm',
    'vafuzz_opt_21_choice_17': 'elf32-littlearm',
    'vafuzz_opt_21_choice_18': 'elf32-bigarm-fdpic',
    'vafuzz_opt_21_choice_19': 'elf32-littlearm-fdpic',
    'vafuzz_opt_21_choice_20': 'elf32-bigarm-vxworks',
    'vafuzz_opt_21_choice_21': 'elf32-littlearm-vxworks',
    'vafuzz_opt_21_choice_22': 'mach-o-arm',
    'vafuzz_opt_21_choice_23': 'pe-arm-big',
    'vafuzz_opt_21_choice_24': 'pe-arm-little',
    'vafuzz_opt_21_choice_25': 'pe-arm-wince-big',
    'vafuzz_opt_21_choice_26': 'pe-arm-wince-little',
    'vafuzz_opt_21_choice_27': 'pei-arm-big',
    'vafuzz_opt_21_choice_28': 'pei-arm-little',
    'vafuzz_opt_21_choice_29': 'pei-arm-wince-big',
    'vafuzz_opt_21_choice_30': 'pei-arm-wince-little',
    'vafuzz_opt_21_choice_31': 'elf32-avr',
    'vafuzz_opt_21_choice_32': 'elf32-bfin',
    'vafuzz_opt_21_choice_33': 'elf32-bfinfdpic',
    'vafuzz_opt_21_choice_34': 'elf32-cr16',
    'vafuzz_opt_21_choice_35': 'a.out-cris',
    'vafuzz_opt_21_choice_36': 'elf32-cris',
    'vafuzz_opt_21_choice_37': 'elf32-us-cris',
    'vafuzz_opt_21_choice_38': 'elf32-crx',
    'vafuzz_opt_21_choice_39': 'elf32-csky-big',
    'vafuzz_opt_21_choice_40': 'elf32-csky-little',
    'vafuzz_opt_21_choice_41': 'elf32-d10v',
    'vafuzz_opt_21_choice_42': 'elf32-d30v',
    'vafuzz_opt_21_choice_43': 'elf32-dlx',
    'vafuzz_opt_21_choice_44': 'elf32-big',
    'vafuzz_opt_21_choice_45': 'elf32-little',
    'vafuzz_opt_21_choice_46': 'elf64-big',
    'vafuzz_opt_21_choice_47': 'elf64-little',
    'vafuzz_opt_21_choice_48': 'elf32-epiphany',
    'vafuzz_opt_21_choice_49': 'elf32-fr30',
    'vafuzz_opt_21_choice_50': 'elf32-frv',
    'vafuzz_opt_21_choice_51': 'elf32-frvfdpic',
    'vafuzz_opt_21_choice_52': 'elf32-h8300',
    'vafuzz_opt_21_choice_53': 'elf32-h8300-linux',
    'vafuzz_opt_21_choice_54': 'elf32-hppa',
    'vafuzz_opt_21_choice_55': 'elf32-hppa-linux',
    'vafuzz_opt_21_choice_56': 'elf32-hppa-netbsd',
    'vafuzz_opt_21_choice_57': 'elf64-hppa',
    'vafuzz_opt_21_choice_58': 'elf64-hppa-linux',
    'vafuzz_opt_21_choice_59': 'som',
    'vafuzz_opt_21_choice_60': 'a.out-i386',
    'vafuzz_opt_21_choice_61': 'a.out-i386-bsd',
    'vafuzz_opt_21_choice_62': 'a.out-i386-lynx',
    'vafuzz_opt_21_choice_63': 'coff-i386',
    'vafuzz_opt_21_choice_64': 'coff-go32',
    'vafuzz_opt_21_choice_65': 'coff-go32-exe',
    'vafuzz_opt_21_choice_66': 'coff-i386-lynx',
    'vafuzz_opt_21_choice_67': 'elf32-i386',
    'vafuzz_opt_21_choice_68': 'elf32-i386-freebsd',
    'vafuzz_opt_21_choice_69': 'elf32-i386-sol2',
    'vafuzz_opt_21_choice_70': 'elf32-i386-vxworks',
    'vafuzz_opt_21_choice_71': 'mach-o-i386',
    'vafuzz_opt_21_choice_72': 'msdos',
    'vafuzz_opt_21_choice_73': 'pe-i386',
    'vafuzz_opt_21_choice_74': 'pe-bigobj-i386',
    'vafuzz_opt_21_choice_75': 'pei-i386',
    'vafuzz_opt_21_choice_76': 'elf32-iamcu',
    'vafuzz_opt_21_choice_77': 'elf64-bpfbe',
    'vafuzz_opt_21_choice_78': 'elf64-bpfle',
    'vafuzz_opt_21_choice_79': 'elf32-ia64-hpux-big',
    'vafuzz_opt_21_choice_80': 'elf64-ia64-big',
    'vafuzz_opt_21_choice_81': 'elf64-ia64-little',
    'vafuzz_opt_21_choice_82': 'elf64-ia64-hpux-big',
    'vafuzz_opt_21_choice_83': 'elf64-ia64-vms',
    'vafuzz_opt_21_choice_84': 'pei-ia64',
    'vafuzz_opt_21_choice_85': 'elf32-ip2k',
    'vafuzz_opt_21_choice_86': 'elf32-iq2000',
    'vafuzz_opt_21_choice_87': 'elf64-k1om',
    'vafuzz_opt_21_choice_88': 'elf64-k1om-freebsd',
    'vafuzz_opt_21_choice_89': 'elf64-l1om',
    'vafuzz_opt_21_choice_90': 'elf64-l1om-freebsd',
    'vafuzz_opt_21_choice_91': 'elf32-lm32',
    'vafuzz_opt_21_choice_92': 'elf32-m32c',
    'vafuzz_opt_21_choice_93': 'elf32-m32r',
    'vafuzz_opt_21_choice_94': 'elf32-m32rle',
    'vafuzz_opt_21_choice_95': 'elf32-m32r-linux',
    'vafuzz_opt_21_choice_96': 'elf32-m32rle-linux',
    'vafuzz_opt_21_choice_97': 'elf32-m68hc11',
    'vafuzz_opt_21_choice_98': 'elf32-m68hc12',
    'vafuzz_opt_21_choice_99': 'elf32-m68k',
    'vafuzz_opt_21_choice_100': 'elf32-s12z',
    'vafuzz_opt_21_choice_101': 'mach-o-be',
    'vafuzz_opt_21_choice_102': 'mach-o-le',
    'vafuzz_opt_21_choice_103': 'mach-o-fat',
    'vafuzz_opt_21_choice_104': 'elf32-mcore-big',
    'vafuzz_opt_21_choice_105': 'elf32-mcore-little',
    'vafuzz_opt_21_choice_106': 'pe-mcore-big',
    'vafuzz_opt_21_choice_107': 'pe-mcore-little',
    'vafuzz_opt_21_choice_108': 'pei-mcore-big',
    'vafuzz_opt_21_choice_109': 'pei-mcore-little',
    'vafuzz_opt_21_choice_110': 'elf32-mep',
    'vafuzz_opt_21_choice_111': 'elf32-metag',
    'vafuzz_opt_21_choice_112': 'elf32-microblaze',
    'vafuzz_opt_21_choice_113': 'ecoff-bigmips',
    'vafuzz_opt_21_choice_114': 'ecoff-littlemips',
    'vafuzz_opt_21_choice_115': 'ecoff-biglittlemips',
    'vafuzz_opt_21_choice_116': 'elf32-bigmips',
    'vafuzz_opt_21_choice_117': 'elf32-littlemips',
    'vafuzz_opt_21_choice_118': 'elf32-nbigmips',
    'vafuzz_opt_21_choice_119': 'elf32-nlittlemips',
    'vafuzz_opt_21_choice_120': 'elf32-ntradbigmips',
    'vafuzz_opt_21_choice_121': 'elf32-ntradlittlemips',
    'vafuzz_opt_21_choice_122': 'elf32-ntradbigmips-freebsd',
    'vafuzz_opt_21_choice_123': 'elf32-ntradlittlemips-freebsd',
    'vafuzz_opt_21_choice_124': 'elf32-tradbigmips',
    'vafuzz_opt_21_choice_125': 'elf32-tradlittlemips',
    'vafuzz_opt_21_choice_126': 'elf32-tradbigmips-freebsd',
    'vafuzz_opt_21_choice_127': 'elf32-tradlittlemips-freebsd',
    'vafuzz_opt_21_choice_128': 'elf32-bigmips-vxworks',
    'vafuzz_opt_21_choice_129': 'elf32-littlemips-vxworks',
    'vafuzz_opt_21_choice_130': 'elf64-bigmips',
    'vafuzz_opt_21_choice_131': 'elf64-littlemips',
    'vafuzz_opt_21_choice_132': 'elf64-tradbigmips',
    'vafuzz_opt_21_choice_133': 'elf64-tradlittlemips',
    'vafuzz_opt_21_choice_134': 'elf64-tradbigmips-freebsd',
    'vafuzz_opt_21_choice_135': 'elf64-tradlittlemips-freebsd',
    'vafuzz_opt_21_choice_136': 'elf64-mmix',
    'vafuzz_opt_21_choice_137': 'mmo',
    'vafuzz_opt_21_choice_138': 'elf32-mn10200',
    'vafuzz_opt_21_choice_139': 'elf32-mn10300',
    'vafuzz_opt_21_choice_140': 'elf32-bigmoxie',
    'vafuzz_opt_21_choice_141': 'elf32-littlemoxie',
    'vafuzz_opt_21_choice_142': 'elf32-msp430',
    'vafuzz_opt_21_choice_143': 'elf32-mt',
    'vafuzz_opt_21_choice_144': 'elf32-nds32be',
    'vafuzz_opt_21_choice_145': 'elf32-nds32le',
    'vafuzz_opt_21_choice_146': 'elf32-nds32be-linux',
    'vafuzz_opt_21_choice_147': 'elf32-nds32le-linux',
    'vafuzz_opt_21_choice_148': 'elf64-nfp',
    'vafuzz_opt_21_choice_149': 'elf32-bignios2',
    'vafuzz_opt_21_choice_150': 'elf32-littlenios2',
    'vafuzz_opt_21_choice_151': 'a.out-pc532-mach',
    'vafuzz_opt_21_choice_152': 'a.out-ns32k-netbsd',
    'vafuzz_opt_21_choice_153': 'elf32-or1k',
    'vafuzz_opt_21_choice_154': 'a.out-pdp11',
    'vafuzz_opt_21_choice_155': 'pef',
    'vafuzz_opt_21_choice_156': 'pef-xlib',
    'vafuzz_opt_21_choice_157': 'elf32-pj',
    'vafuzz_opt_21_choice_158': 'elf32-pjl',
    'vafuzz_opt_21_choice_159': 'ppcboot',
    'vafuzz_opt_21_choice_160': 'elf32-powerpc',
    'vafuzz_opt_21_choice_161': 'elf32-powerpcle',
    'vafuzz_opt_21_choice_162': 'elf32-powerpc-freebsd',
    'vafuzz_opt_21_choice_163': 'elf32-powerpc-vxworks',
    'vafuzz_opt_21_choice_164': 'elf64-powerpc',
    'vafuzz_opt_21_choice_165': 'elf64-powerpcle',
    'vafuzz_opt_21_choice_166': 'elf64-powerpc-freebsd',
    'vafuzz_opt_21_choice_167': 'elf64-powerpcle-freebsd',
    'vafuzz_opt_21_choice_168': 'elf32-pru',
    'vafuzz_opt_21_choice_169': 'elf32-littleriscv',
    'vafuzz_opt_21_choice_170': 'elf64-littleriscv',
    'vafuzz_opt_21_choice_171': 'elf32-bigriscv',
    'vafuzz_opt_21_choice_172': 'elf64-bigriscv',
    'vafuzz_opt_21_choice_173': 'elf32-rl78',
    'vafuzz_opt_21_choice_174': 'aixcoff64-rs6000',
    'vafuzz_opt_21_choice_175': 'aix5coff64-rs6000',
    'vafuzz_opt_21_choice_176': 'aixcoff-rs6000',
    'vafuzz_opt_21_choice_177': 'elf32-rx-be',
    'vafuzz_opt_21_choice_178': 'elf32-rx-be-ns',
    'vafuzz_opt_21_choice_179': 'elf32-rx-le',
    'vafuzz_opt_21_choice_180': 'elf32-s390',
    'vafuzz_opt_21_choice_181': 'elf64-s390',
    'vafuzz_opt_21_choice_182': 'elf32-bigscore',
    'vafuzz_opt_21_choice_183': 'elf32-littlescore',
    'vafuzz_opt_21_choice_184': 'coff-sh',
    'vafuzz_opt_21_choice_185': 'coff-shl',
    'vafuzz_opt_21_choice_186': 'coff-sh-small',
    'vafuzz_opt_21_choice_187': 'coff-shl-small',
    'vafuzz_opt_21_choice_188': 'elf32-sh',
    'vafuzz_opt_21_choice_189': 'elf32-shl',
    'vafuzz_opt_21_choice_190': 'elf32-shbig-fdpic',
    'vafuzz_opt_21_choice_191': 'elf32-sh-fdpic',
    'vafuzz_opt_21_choice_192': 'elf32-sh-linux',
    'vafuzz_opt_21_choice_193': 'elf32-shbig-linux',
    'vafuzz_opt_21_choice_194': 'elf32-sh-nbsd',
    'vafuzz_opt_21_choice_195': 'elf32-shl-nbsd',
    'vafuzz_opt_21_choice_196': 'elf32-sh-vxworks',
    'vafuzz_opt_21_choice_197': 'elf32-shl-vxworks',
    'vafuzz_opt_21_choice_198': 'pe-shl',
    'vafuzz_opt_21_choice_199': 'pei-shl',
    'vafuzz_opt_21_choice_200': 'elf32-sparc',
    'vafuzz_opt_21_choice_201': 'elf32-sparc-sol2',
    'vafuzz_opt_21_choice_202': 'elf32-sparc-vxworks',
    'vafuzz_opt_21_choice_203': 'elf64-sparc',
    'vafuzz_opt_21_choice_204': 'elf64-sparc-freebsd',
    'vafuzz_opt_21_choice_205': 'elf64-sparc-sol2',
    'vafuzz_opt_21_choice_206': 'elf32-spu',
    'vafuzz_opt_21_choice_207': 'sym',
    'vafuzz_opt_21_choice_208': 'coff-tic30',
    'vafuzz_opt_21_choice_209': 'coff0-beh-c54x',
    'vafuzz_opt_21_choice_210': 'coff0-c54x',
    'vafuzz_opt_21_choice_211': 'coff1-beh-c54x',
    'vafuzz_opt_21_choice_212': 'coff1-c54x',
    'vafuzz_opt_21_choice_213': 'coff2-beh-c54x',
    'vafuzz_opt_21_choice_214': 'coff2-c54x',
    'vafuzz_opt_21_choice_215': 'elf32-tic6x-be',
    'vafuzz_opt_21_choice_216': 'elf32-tic6x-le',
    'vafuzz_opt_21_choice_217': 'elf32-tilegx-be',
    'vafuzz_opt_21_choice_218': 'elf32-tilegx-le',
    'vafuzz_opt_21_choice_219': 'elf64-tilegx-be',
    'vafuzz_opt_21_choice_220': 'elf64-tilegx-le',
    'vafuzz_opt_21_choice_221': 'elf32-tilepro',
    'vafuzz_opt_21_choice_222': 'elf32-ft32',
    'vafuzz_opt_21_choice_223': 'elf32-v850-rh850',
    'vafuzz_opt_21_choice_224': 'elf32-v850',
    'vafuzz_opt_21_choice_225': 'a.out-vax1k-netbsd',
    'vafuzz_opt_21_choice_226': 'a.out-vax-netbsd',
    'vafuzz_opt_21_choice_227': 'elf32-vax',
    'vafuzz_opt_21_choice_228': 'elf32-visium',
    'vafuzz_opt_21_choice_229': 'wasm',
    'vafuzz_opt_21_choice_230': 'elf32-wasm32',
    'vafuzz_opt_21_choice_231': 'coff-x86-64',
    'vafuzz_opt_21_choice_232': 'elf32-x86-64',
    'vafuzz_opt_21_choice_233': 'elf64-x86-64-cloudabi',
    'vafuzz_opt_21_choice_234': 'elf64-x86-64-freebsd',
    'vafuzz_opt_21_choice_235': 'elf64-x86-64-sol2',
    'vafuzz_opt_21_choice_236': 'mach-o-x86-64',
    'vafuzz_opt_21_choice_237': 'pe-x86-64',
    'vafuzz_opt_21_choice_238': 'pe-bigobj-x86-64',
    'vafuzz_opt_21_choice_239': 'pei-x86-64',
    'vafuzz_opt_21_choice_240': 'elf32-xc16x',
    'vafuzz_opt_21_choice_241': 'elf32-xgate',
    'vafuzz_opt_21_choice_242': 'elf32-xstormy16',
    'vafuzz_opt_21_choice_243': 'elf32-xtensa-be',
    'vafuzz_opt_21_choice_244': 'elf32-xtensa-le',
    'vafuzz_opt_21_choice_245': 'coff-z80',
    'vafuzz_opt_21_choice_246': 'elf32-z80',
    'vafuzz_opt_21_choice_247': 'coff-z8k',
    'vafuzz_opt_21_choice_248': 'srec',
    'vafuzz_opt_21_choice_249': 'symbolsrec',
    'vafuzz_opt_21_choice_250': 'verilog',
    'vafuzz_opt_21_choice_251': 'tekhex',
    'vafuzz_opt_21_choice_252': 'binary',
    'vafuzz_opt_21_choice_253': 'ihex',
    'vafuzz_opt_21_choice_254': 'plugin',
}

choice_map_keys = sorted(choice_map.keys(), reverse=True)

choice_revert_map = {
    'auto': 'vafuzz_opt_2_choice_0',
    'gnu': 'vafuzz_opt_2_choice_1',
    'lucid': 'vafuzz_opt_2_choice_2',
    'arm': 'vafuzz_opt_2_choice_3',
    'hp': 'vafuzz_opt_2_choice_4',
    'edg': 'vafuzz_opt_2_choice_5',
    'gnu-v3': 'vafuzz_opt_2_choice_6',
    'java': 'vafuzz_opt_2_choice_7',
    'gnat': 'vafuzz_opt_2_choice_8',
    'bsd': 'vafuzz_opt_8_choice_0',
    'sysv': 'vafuzz_opt_8_choice_1',
    'posix': 'vafuzz_opt_8_choice_2',
    'just-symbols': 'vafuzz_opt_8_choice_3',
    'x': 'vafuzz_opt_20_choice_0',
    'd': 'vafuzz_opt_20_choice_1',
    'o': 'vafuzz_opt_20_choice_2',
    'elf64-x86-64': 'vafuzz_opt_21_choice_0',
    'elf32-bigaarch64': 'vafuzz_opt_21_choice_1',
    'elf32-littleaarch64': 'vafuzz_opt_21_choice_2',
    'elf64-bigaarch64': 'vafuzz_opt_21_choice_3',
    'elf64-bigaarch64-cloudabi': 'vafuzz_opt_21_choice_4',
    'elf64-littleaarch64': 'vafuzz_opt_21_choice_5',
    'elf64-littleaarch64-cloudabi': 'vafuzz_opt_21_choice_6',
    'mach-o-arm64': 'vafuzz_opt_21_choice_7',
    'ecoff-littlealpha': 'vafuzz_opt_21_choice_8',
    'elf64-alpha': 'vafuzz_opt_21_choice_9',
    'elf64-alpha-freebsd': 'vafuzz_opt_21_choice_10',
    'vms-alpha': 'vafuzz_opt_21_choice_11',
    'vms-libtxt': 'vafuzz_opt_21_choice_12',
    'elf32-am33lin': 'vafuzz_opt_21_choice_13',
    'elf32-bigarc': 'vafuzz_opt_21_choice_14',
    'elf32-littlearc': 'vafuzz_opt_21_choice_15',
    'elf32-bigarm': 'vafuzz_opt_21_choice_16',
    'elf32-littlearm': 'vafuzz_opt_21_choice_17',
    'elf32-bigarm-fdpic': 'vafuzz_opt_21_choice_18',
    'elf32-littlearm-fdpic': 'vafuzz_opt_21_choice_19',
    'elf32-bigarm-vxworks': 'vafuzz_opt_21_choice_20',
    'elf32-littlearm-vxworks': 'vafuzz_opt_21_choice_21',
    'mach-o-arm': 'vafuzz_opt_21_choice_22',
    'pe-arm-big': 'vafuzz_opt_21_choice_23',
    'pe-arm-little': 'vafuzz_opt_21_choice_24',
    'pe-arm-wince-big': 'vafuzz_opt_21_choice_25',
    'pe-arm-wince-little': 'vafuzz_opt_21_choice_26',
    'pei-arm-big': 'vafuzz_opt_21_choice_27',
    'pei-arm-little': 'vafuzz_opt_21_choice_28',
    'pei-arm-wince-big': 'vafuzz_opt_21_choice_29',
    'pei-arm-wince-little': 'vafuzz_opt_21_choice_30',
    'elf32-avr': 'vafuzz_opt_21_choice_31',
    'elf32-bfin': 'vafuzz_opt_21_choice_32',
    'elf32-bfinfdpic': 'vafuzz_opt_21_choice_33',
    'elf32-cr16': 'vafuzz_opt_21_choice_34',
    'a.out-cris': 'vafuzz_opt_21_choice_35',
    'elf32-cris': 'vafuzz_opt_21_choice_36',
    'elf32-us-cris': 'vafuzz_opt_21_choice_37',
    'elf32-crx': 'vafuzz_opt_21_choice_38',
    'elf32-csky-big': 'vafuzz_opt_21_choice_39',
    'elf32-csky-little': 'vafuzz_opt_21_choice_40',
    'elf32-d10v': 'vafuzz_opt_21_choice_41',
    'elf32-d30v': 'vafuzz_opt_21_choice_42',
    'elf32-dlx': 'vafuzz_opt_21_choice_43',
    'elf32-big': 'vafuzz_opt_21_choice_44',
    'elf32-little': 'vafuzz_opt_21_choice_45',
    'elf64-big': 'vafuzz_opt_21_choice_46',
    'elf64-little': 'vafuzz_opt_21_choice_47',
    'elf32-epiphany': 'vafuzz_opt_21_choice_48',
    'elf32-fr30': 'vafuzz_opt_21_choice_49',
    'elf32-frv': 'vafuzz_opt_21_choice_50',
    'elf32-frvfdpic': 'vafuzz_opt_21_choice_51',
    'elf32-h8300': 'vafuzz_opt_21_choice_52',
    'elf32-h8300-linux': 'vafuzz_opt_21_choice_53',
    'elf32-hppa': 'vafuzz_opt_21_choice_54',
    'elf32-hppa-linux': 'vafuzz_opt_21_choice_55',
    'elf32-hppa-netbsd': 'vafuzz_opt_21_choice_56',
    'elf64-hppa': 'vafuzz_opt_21_choice_57',
    'elf64-hppa-linux': 'vafuzz_opt_21_choice_58',
    'som': 'vafuzz_opt_21_choice_59',
    'a.out-i386': 'vafuzz_opt_21_choice_60',
    'a.out-i386-bsd': 'vafuzz_opt_21_choice_61',
    'a.out-i386-lynx': 'vafuzz_opt_21_choice_62',
    'coff-i386': 'vafuzz_opt_21_choice_63',
    'coff-go32': 'vafuzz_opt_21_choice_64',
    'coff-go32-exe': 'vafuzz_opt_21_choice_65',
    'coff-i386-lynx': 'vafuzz_opt_21_choice_66',
    'elf32-i386': 'vafuzz_opt_21_choice_67',
    'elf32-i386-freebsd': 'vafuzz_opt_21_choice_68',
    'elf32-i386-sol2': 'vafuzz_opt_21_choice_69',
    'elf32-i386-vxworks': 'vafuzz_opt_21_choice_70',
    'mach-o-i386': 'vafuzz_opt_21_choice_71',
    'msdos': 'vafuzz_opt_21_choice_72',
    'pe-i386': 'vafuzz_opt_21_choice_73',
    'pe-bigobj-i386': 'vafuzz_opt_21_choice_74',
    'pei-i386': 'vafuzz_opt_21_choice_75',
    'elf32-iamcu': 'vafuzz_opt_21_choice_76',
    'elf64-bpfbe': 'vafuzz_opt_21_choice_77',
    'elf64-bpfle': 'vafuzz_opt_21_choice_78',
    'elf32-ia64-hpux-big': 'vafuzz_opt_21_choice_79',
    'elf64-ia64-big': 'vafuzz_opt_21_choice_80',
    'elf64-ia64-little': 'vafuzz_opt_21_choice_81',
    'elf64-ia64-hpux-big': 'vafuzz_opt_21_choice_82',
    'elf64-ia64-vms': 'vafuzz_opt_21_choice_83',
    'pei-ia64': 'vafuzz_opt_21_choice_84',
    'elf32-ip2k': 'vafuzz_opt_21_choice_85',
    'elf32-iq2000': 'vafuzz_opt_21_choice_86',
    'elf64-k1om': 'vafuzz_opt_21_choice_87',
    'elf64-k1om-freebsd': 'vafuzz_opt_21_choice_88',
    'elf64-l1om': 'vafuzz_opt_21_choice_89',
    'elf64-l1om-freebsd': 'vafuzz_opt_21_choice_90',
    'elf32-lm32': 'vafuzz_opt_21_choice_91',
    'elf32-m32c': 'vafuzz_opt_21_choice_92',
    'elf32-m32r': 'vafuzz_opt_21_choice_93',
    'elf32-m32rle': 'vafuzz_opt_21_choice_94',
    'elf32-m32r-linux': 'vafuzz_opt_21_choice_95',
    'elf32-m32rle-linux': 'vafuzz_opt_21_choice_96',
    'elf32-m68hc11': 'vafuzz_opt_21_choice_97',
    'elf32-m68hc12': 'vafuzz_opt_21_choice_98',
    'elf32-m68k': 'vafuzz_opt_21_choice_99',
    'elf32-s12z': 'vafuzz_opt_21_choice_100',
    'mach-o-be': 'vafuzz_opt_21_choice_101',
    'mach-o-le': 'vafuzz_opt_21_choice_102',
    'mach-o-fat': 'vafuzz_opt_21_choice_103',
    'elf32-mcore-big': 'vafuzz_opt_21_choice_104',
    'elf32-mcore-little': 'vafuzz_opt_21_choice_105',
    'pe-mcore-big': 'vafuzz_opt_21_choice_106',
    'pe-mcore-little': 'vafuzz_opt_21_choice_107',
    'pei-mcore-big': 'vafuzz_opt_21_choice_108',
    'pei-mcore-little': 'vafuzz_opt_21_choice_109',
    'elf32-mep': 'vafuzz_opt_21_choice_110',
    'elf32-metag': 'vafuzz_opt_21_choice_111',
    'elf32-microblaze': 'vafuzz_opt_21_choice_112',
    'ecoff-bigmips': 'vafuzz_opt_21_choice_113',
    'ecoff-littlemips': 'vafuzz_opt_21_choice_114',
    'ecoff-biglittlemips': 'vafuzz_opt_21_choice_115',
    'elf32-bigmips': 'vafuzz_opt_21_choice_116',
    'elf32-littlemips': 'vafuzz_opt_21_choice_117',
    'elf32-nbigmips': 'vafuzz_opt_21_choice_118',
    'elf32-nlittlemips': 'vafuzz_opt_21_choice_119',
    'elf32-ntradbigmips': 'vafuzz_opt_21_choice_120',
    'elf32-ntradlittlemips': 'vafuzz_opt_21_choice_121',
    'elf32-ntradbigmips-freebsd': 'vafuzz_opt_21_choice_122',
    'elf32-ntradlittlemips-freebsd': 'vafuzz_opt_21_choice_123',
    'elf32-tradbigmips': 'vafuzz_opt_21_choice_124',
    'elf32-tradlittlemips': 'vafuzz_opt_21_choice_125',
    'elf32-tradbigmips-freebsd': 'vafuzz_opt_21_choice_126',
    'elf32-tradlittlemips-freebsd': 'vafuzz_opt_21_choice_127',
    'elf32-bigmips-vxworks': 'vafuzz_opt_21_choice_128',
    'elf32-littlemips-vxworks': 'vafuzz_opt_21_choice_129',
    'elf64-bigmips': 'vafuzz_opt_21_choice_130',
    'elf64-littlemips': 'vafuzz_opt_21_choice_131',
    'elf64-tradbigmips': 'vafuzz_opt_21_choice_132',
    'elf64-tradlittlemips': 'vafuzz_opt_21_choice_133',
    'elf64-tradbigmips-freebsd': 'vafuzz_opt_21_choice_134',
    'elf64-tradlittlemips-freebsd': 'vafuzz_opt_21_choice_135',
    'elf64-mmix': 'vafuzz_opt_21_choice_136',
    'mmo': 'vafuzz_opt_21_choice_137',
    'elf32-mn10200': 'vafuzz_opt_21_choice_138',
    'elf32-mn10300': 'vafuzz_opt_21_choice_139',
    'elf32-bigmoxie': 'vafuzz_opt_21_choice_140',
    'elf32-littlemoxie': 'vafuzz_opt_21_choice_141',
    'elf32-msp430': 'vafuzz_opt_21_choice_142',
    'elf32-mt': 'vafuzz_opt_21_choice_143',
    'elf32-nds32be': 'vafuzz_opt_21_choice_144',
    'elf32-nds32le': 'vafuzz_opt_21_choice_145',
    'elf32-nds32be-linux': 'vafuzz_opt_21_choice_146',
    'elf32-nds32le-linux': 'vafuzz_opt_21_choice_147',
    'elf64-nfp': 'vafuzz_opt_21_choice_148',
    'elf32-bignios2': 'vafuzz_opt_21_choice_149',
    'elf32-littlenios2': 'vafuzz_opt_21_choice_150',
    'a.out-pc532-mach': 'vafuzz_opt_21_choice_151',
    'a.out-ns32k-netbsd': 'vafuzz_opt_21_choice_152',
    'elf32-or1k': 'vafuzz_opt_21_choice_153',
    'a.out-pdp11': 'vafuzz_opt_21_choice_154',
    'pef': 'vafuzz_opt_21_choice_155',
    'pef-xlib': 'vafuzz_opt_21_choice_156',
    'elf32-pj': 'vafuzz_opt_21_choice_157',
    'elf32-pjl': 'vafuzz_opt_21_choice_158',
    'ppcboot': 'vafuzz_opt_21_choice_159',
    'elf32-powerpc': 'vafuzz_opt_21_choice_160',
    'elf32-powerpcle': 'vafuzz_opt_21_choice_161',
    'elf32-powerpc-freebsd': 'vafuzz_opt_21_choice_162',
    'elf32-powerpc-vxworks': 'vafuzz_opt_21_choice_163',
    'elf64-powerpc': 'vafuzz_opt_21_choice_164',
    'elf64-powerpcle': 'vafuzz_opt_21_choice_165',
    'elf64-powerpc-freebsd': 'vafuzz_opt_21_choice_166',
    'elf64-powerpcle-freebsd': 'vafuzz_opt_21_choice_167',
    'elf32-pru': 'vafuzz_opt_21_choice_168',
    'elf32-littleriscv': 'vafuzz_opt_21_choice_169',
    'elf64-littleriscv': 'vafuzz_opt_21_choice_170',
    'elf32-bigriscv': 'vafuzz_opt_21_choice_171',
    'elf64-bigriscv': 'vafuzz_opt_21_choice_172',
    'elf32-rl78': 'vafuzz_opt_21_choice_173',
    'aixcoff64-rs6000': 'vafuzz_opt_21_choice_174',
    'aix5coff64-rs6000': 'vafuzz_opt_21_choice_175',
    'aixcoff-rs6000': 'vafuzz_opt_21_choice_176',
    'elf32-rx-be': 'vafuzz_opt_21_choice_177',
    'elf32-rx-be-ns': 'vafuzz_opt_21_choice_178',
    'elf32-rx-le': 'vafuzz_opt_21_choice_179',
    'elf32-s390': 'vafuzz_opt_21_choice_180',
    'elf64-s390': 'vafuzz_opt_21_choice_181',
    'elf32-bigscore': 'vafuzz_opt_21_choice_182',
    'elf32-littlescore': 'vafuzz_opt_21_choice_183',
    'coff-sh': 'vafuzz_opt_21_choice_184',
    'coff-shl': 'vafuzz_opt_21_choice_185',
    'coff-sh-small': 'vafuzz_opt_21_choice_186',
    'coff-shl-small': 'vafuzz_opt_21_choice_187',
    'elf32-sh': 'vafuzz_opt_21_choice_188',
    'elf32-shl': 'vafuzz_opt_21_choice_189',
    'elf32-shbig-fdpic': 'vafuzz_opt_21_choice_190',
    'elf32-sh-fdpic': 'vafuzz_opt_21_choice_191',
    'elf32-sh-linux': 'vafuzz_opt_21_choice_192',
    'elf32-shbig-linux': 'vafuzz_opt_21_choice_193',
    'elf32-sh-nbsd': 'vafuzz_opt_21_choice_194',
    'elf32-shl-nbsd': 'vafuzz_opt_21_choice_195',
    'elf32-sh-vxworks': 'vafuzz_opt_21_choice_196',
    'elf32-shl-vxworks': 'vafuzz_opt_21_choice_197',
    'pe-shl': 'vafuzz_opt_21_choice_198',
    'pei-shl': 'vafuzz_opt_21_choice_199',
    'elf32-sparc': 'vafuzz_opt_21_choice_200',
    'elf32-sparc-sol2': 'vafuzz_opt_21_choice_201',
    'elf32-sparc-vxworks': 'vafuzz_opt_21_choice_202',
    'elf64-sparc': 'vafuzz_opt_21_choice_203',
    'elf64-sparc-freebsd': 'vafuzz_opt_21_choice_204',
    'elf64-sparc-sol2': 'vafuzz_opt_21_choice_205',
    'elf32-spu': 'vafuzz_opt_21_choice_206',
    'sym': 'vafuzz_opt_21_choice_207',
    'coff-tic30': 'vafuzz_opt_21_choice_208',
    'coff0-beh-c54x': 'vafuzz_opt_21_choice_209',
    'coff0-c54x': 'vafuzz_opt_21_choice_210',
    'coff1-beh-c54x': 'vafuzz_opt_21_choice_211',
    'coff1-c54x': 'vafuzz_opt_21_choice_212',
    'coff2-beh-c54x': 'vafuzz_opt_21_choice_213',
    'coff2-c54x': 'vafuzz_opt_21_choice_214',
    'elf32-tic6x-be': 'vafuzz_opt_21_choice_215',
    'elf32-tic6x-le': 'vafuzz_opt_21_choice_216',
    'elf32-tilegx-be': 'vafuzz_opt_21_choice_217',
    'elf32-tilegx-le': 'vafuzz_opt_21_choice_218',
    'elf64-tilegx-be': 'vafuzz_opt_21_choice_219',
    'elf64-tilegx-le': 'vafuzz_opt_21_choice_220',
    'elf32-tilepro': 'vafuzz_opt_21_choice_221',
    'elf32-ft32': 'vafuzz_opt_21_choice_222',
    'elf32-v850-rh850': 'vafuzz_opt_21_choice_223',
    'elf32-v850': 'vafuzz_opt_21_choice_224',
    'a.out-vax1k-netbsd': 'vafuzz_opt_21_choice_225',
    'a.out-vax-netbsd': 'vafuzz_opt_21_choice_226',
    'elf32-vax': 'vafuzz_opt_21_choice_227',
    'elf32-visium': 'vafuzz_opt_21_choice_228',
    'wasm': 'vafuzz_opt_21_choice_229',
    'elf32-wasm32': 'vafuzz_opt_21_choice_230',
    'coff-x86-64': 'vafuzz_opt_21_choice_231',
    'elf32-x86-64': 'vafuzz_opt_21_choice_232',
    'elf64-x86-64-cloudabi': 'vafuzz_opt_21_choice_233',
    'elf64-x86-64-freebsd': 'vafuzz_opt_21_choice_234',
    'elf64-x86-64-sol2': 'vafuzz_opt_21_choice_235',
    'mach-o-x86-64': 'vafuzz_opt_21_choice_236',
    'pe-x86-64': 'vafuzz_opt_21_choice_237',
    'pe-bigobj-x86-64': 'vafuzz_opt_21_choice_238',
    'pei-x86-64': 'vafuzz_opt_21_choice_239',
    'elf32-xc16x': 'vafuzz_opt_21_choice_240',
    'elf32-xgate': 'vafuzz_opt_21_choice_241',
    'elf32-xstormy16': 'vafuzz_opt_21_choice_242',
    'elf32-xtensa-be': 'vafuzz_opt_21_choice_243',
    'elf32-xtensa-le': 'vafuzz_opt_21_choice_244',
    'coff-z80': 'vafuzz_opt_21_choice_245',
    'elf32-z80': 'vafuzz_opt_21_choice_246',
    'coff-z8k': 'vafuzz_opt_21_choice_247',
    'srec': 'vafuzz_opt_21_choice_248',
    'symbolsrec': 'vafuzz_opt_21_choice_249',
    'verilog': 'vafuzz_opt_21_choice_250',
    'tekhex': 'vafuzz_opt_21_choice_251',
    'binary': 'vafuzz_opt_21_choice_252',
    'ihex': 'vafuzz_opt_21_choice_253',
    'plugin': 'vafuzz_opt_21_choice_254',
}

choice_revert_map_keys = sorted(choice_revert_map.keys(), reverse=True)



def request_config_generation(constraint_file, 
                              configs_to_generate, 
                              generator_number=1,
                              pc_rand_selection=0.0):
    solver = Solver()
    # Conflict constraints

    solver.add(Or(Not(options['defined-only'].z3_var), Not(options['u'].z3_var)))

    solver.add(Or(Not(options['n'].z3_var), Not(options['p'].z3_var)))

    solver.add(Or(Not(options['n'].z3_var), Not(options['r'].z3_var)))

    solver.add(Or(Not(options['n'].z3_var), Not(options['size-sort'].z3_var)))

    solver.add(Or(Not(options['p'].z3_var), Not(options['r'].z3_var)))

    solver.add(Or(Not(options['p'].z3_var), Not(options['size-sort'].z3_var)))

    solver.add(Or(Not(options['r'].z3_var), Not(options['size-sort'].z3_var)))

    solver.add(Or(Not(options['demangle'].z3_var), Not(options['no-demangle'].z3_var)))

    solver.add(Or(Not(options['recurse-limit'].z3_var), Not(options['no-recurse-limit'].z3_var)))
   # Dependency constraints: TODO make fixes to non boolean as necessary
    # Constraints


    # Generator helpers
    configs_to_generate = int(configs_to_generate)
    var_s = set()
    
    # Checked if we have pickled the pqeue
    pqeue = []
    try:
        with open(constraint_file, "rb") as file:
            pqeue = pickle.load(file)
    except OSError:
        # print("No file found")
        with open(constraint_file, "wb") as file:
            pickle.dump(pqeue, file)

    # GENERATOR 3
    if generator_number == 3:
        if len(pqeue) < 2:
            print("Pqeue doesnt have enough elements")
            exit(1)
        # print("PC Queue: " + str(pqeue))
        pc_0 = None
        random_float_0 = random.uniform(0, 1)
        if random_float_0 < (pc_rand_selection / 2.0):
            random_idx = random.randint(0, len(pqeue) - 1)
            pc_0 = pqeue[random_idx]
        else:
            pc_0 = heappop(pqeue)
            
        # print("PC" + str(pc_0))
    
    if pqeue == []:
        print("Empty pqeue")
    else:
        # print("PC Queue: " + str(pqeue))

        random_float = random.uniform(0, 1)
        
        pc = None
        if random_float < pc_rand_selection:
            random_idx = random.randint(0, len(pqeue) - 1)
            pc = pqeue[random_idx]
        else:
            pc = heappop(pqeue)
            # energy = abs(pc[0])
        # print("PC" + str(pc))
        # Check if the pqeue is empty
        # if len(pqeue) == 0:
        if not pc[1] == "default_settings_for_all":        
            condition = "solver.add(" + pc[1] + ")"
            # print("Cond:", condition)
            var_s.update(extract_option_names(condition))
            print(condition)
            # print(options['c'].z3_choices)
            exec(condition)
            
        
        # if pc[1] == "default_settings_for_all" and generator_number == 3:
        #   print("PC 1: " + str(pc))
        #   print("PC 0: " + str(pc_0))
            
        #     pc = pc_0


    # GENERATOR 1
    if generator_number == 1 or generator_number == 3:
        combinations = []
        variables = list(var_s)
        
        for idx, var in enumerate(variables):
            opt_each = options[var]
            
            if (isinstance(opt_each.z3_var, DatatypeSortRef)):
                variables.pop(idx)
                            
        def backtrack(current_assignment, idx):
            # Stop if we've generated enough configurations
            if len(combinations) >= configs_to_generate:
                return True  # Return True to indicate we should stop
            
            if idx == len(variables):
                combinations.append(current_assignment.copy())
                return False  # Return False to continue generating
            
            var_name = variables[idx]
            
            var = options[var_name]
            
            
            # RETURN HERE
            if var.opt_type == "bool":
                for value in [True, False]:
                    current_assignment[var_name] = (value, options[var_name].connector)
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif var.opt_type == "int":
                for value in [False] +                     random.sample(range(options[var_name].range_l, 
                                        options[var_name].range_h + 1), 3):
                    current_assignment[var_name] = (value, options[var_name].connector)
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif var.opt_type == "real":
                for value in [False] + [random.uniform(
                    options[var_name].range_l, options[var_name].range_h + 1)                         for _ in range(3)]:
                    current_assignment[var_name] = (value, options[var_name].connector)
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            elif var.opt_type == "choice":
                choices = var.z3_var.sort().num_constructors()
                for choice_idx in range(choices + 1):
                    if choice_idx == choices:
                        current_assignment[var_name] = (False, options[var_name].connector)
                    else:
                        choice_opt_set = str(var.z3_var.sort().constructor(choice_idx))
                        if choice_opt_set in choice_map:
                            current_assignment[var_name] = (choice_map[choice_opt_set], options[var_name].connector)
                        else:
                            current_assignment[var_name] = (var.z3_var.sort().constructor(choice_idx), options[var_name].connector)
                    if backtrack(current_assignment, idx + 1):
                        return True
            
            return False

        backtrack({}, 0)
        config_string_struct = generate_config_strings(combinations, pc)
        # pprint.pp(config_string_struct)
        # print("Generated Config Str:" + str(config_string_struct[2]))
        
        # Check SAT
        # if solver.check() == sat:
        #     # print('SAT')
        
        # F = Not(And(a == True, b == True))
        # G = Or(Not(a), Not(b))
        # # print(is_equivalent(F == G))


    # GENERATOR 2
    elif generator_number == 2:
        combinations = []
        for var_name in options.keys():
            # print("Var name: " + var_name)
            combinations_entry = {}
            choices_added = False
            var = options[var_name].z3_var
            
            if is_bool(var):
                combinations_entry[var_name] = (True, options[var_name].connector)
            elif is_int(var):
                combinations_entry[var_name] = (random.randint(options[var_name].range_l,
                                   options[var_name].range_h + 1), options[var_name].connector)
            elif is_real(var):
                combinations_entry[var_name] = (random.uniform(options[var_name].range_l,
                                   options[var_name].range_h), options[var_name].connector)
            elif isinstance(var, DatatypeRef): # choices
                choices = var.sort().num_constructors()
                choices_added = True
                for i in range(choices):
                    combinations_entry = {}
                    combinations_entry[var_name + options[var_name].connector +                        str(var.sort().constructor(i))] = (True, options[var_name].connector)
                    combinations.append(combinations_entry)
            
            if not choices_added:
                combinations.append(combinations_entry)

        # randomly select 50 configurations
        if (len(combinations) > 50):
            combinations = random.sample(combinations, 50)
        
        config_string_struct = generate_config_strings(combinations)
    
    # GENERATOR 4
    elif (generator_number == 4):
        if not pc[1] == "default_settings_for_all":
            configs = []
            
            var_names = extract_variable_names_and_values(pc[1])
            # print("Var names: " + str(var_names))
            for each in var_names:
                configs.append({each: var_names[each]})
            
            config_string_struct = generate_config_strings(configs, pc)
        else:
            config_string_struct = generate_config_strings([{}], pc)
        
        # pprint.pp(config_string_struct)
    
    
    
    # Configs have been generated and stored in config_string_struct
    
    if generator_number == 3:
        if not pc_0[1] == "default_settings_for_all":  
            condition = "solver.add(" + pc_0[1] + ")"
            # print("Cond Gen 3:", condition)
            # energy = abs(pc_0[0])            
            gen_3_var_s = extract_option_names(condition)
            
            no_similar = True
            # print("Var s: " + str(var_s))
            # print("Gen 3 var s: " + str(gen_3_var_s))
            for each in gen_3_var_s:
                if each in var_s:
                    no_similar = False
                    break
            
            if no_similar:    
                var_s.update(extract_option_names(condition))
                
                
                exec(condition)
                config_ext_s = extract_variable_names_and_values(condition)
                config_ext_dict = {}
                
                for each in config_ext_s:
                    each_opt_name = list(extract_option_names(each))[0]
                    
                    if options[each_opt_name].opt_type == "bool":    
                        config_ext_dict[each_opt_name] = (True, options[each_opt_name].connector)
                    else:
                        each_opt_set = config_ext_s[each]
                        if type(each_opt_set) == str and 'z3_choices' in each_opt_set:
                            # keep the part after the dot
                            each_opt_set = each_opt_set.split(".")[-1]
                            
                        config_ext_dict[each_opt_name] = (each_opt_set, options[each_opt_name].connector)
                    # elif options[each_opt_name].opt_type == "int" or                     #      options[each_opt_name].opt_type == "real":
                             
                
                # print("Config ext dict: " + str(config_ext_dict))
                
                for each in config_ext_dict:
                    if options[each].opt_type == "choice":
                        if config_ext_dict[each][0] in choice_map:
                            config_ext_dict[each] = (choice_map[config_ext_dict[each][0]], options[each].connector)
                
                config_ext_string_struct = generate_config_strings([config_ext_dict], pc_0)
                # print("Config ext string struct: " + str(config_ext_string_struct[0]))
                config_ext_str = config_ext_string_struct[0][0]
                # print("Config ext str: " + str(config_ext_str))
                
                # Add to original config string struct
                for idx in range(len(config_string_struct[0])):
                    config_string_struct[0][idx] = config_string_struct[0][idx].strip()
                    ext_ls = config_ext_str.strip().split(" ")
                    # print("Ext ls: " + str(ext_ls))
                    for j in range(len(ext_ls)):
                        # found = False
                        option_setting = ext_ls[j]
                        option_setting = option_setting.strip()
                        # print("Checking if: " + option_setting + " is in " + config_string_struct[0][idx])
                        if  option_setting not in config_string_struct[0][idx]:
                            # print("Adding: " + option_setting)
                            config_string_struct[0][idx] += " " + option_setting
                        # else:
                            
                    # if not found:
                    #     config_string_struct[0][idx] += " " + config_ext_str + " "
            
                cur_pc = config_string_struct[2][1]
                
                # remove )
                # print("CUR pc: " + str(cur_pc))
                # print("config_ext_dict: " + str(config_ext_dict))
                if cur_pc[0:3] == "Not":
                    pass
                elif ")" in cur_pc:
                    cur_pc = cur_pc[:-1]
                for new_var in config_ext_dict:
                    if options[new_var].opt_type == "bool":
                        cur_pc += ", " + "options['" + new_var + "'].z3_var"
                    elif options[new_var].opt_type == "int" or options[new_var].opt_type == "real":
                        cur_pc += ", " + "options['" + new_var + "'].z3_var == " + str(config_ext_dict[new_var][0])
                    elif options[new_var].opt_type == "choice":
                        if config_ext_dict[new_var][0] in choice_revert_map:
                            config_ext_dict[new_var] =                                 (choice_revert_map[config_ext_dict[new_var][0]], config_ext_dict[new_var][1])
                        cur_pc += ", " + "options['" + new_var + "'].z3_var == " + "options['" + new_var + "'].z3_choices." + str(config_ext_dict[new_var][0]) + ')'
                                           
                    # print("New var: " + new_var)
                cur_pc += ")"
                
                if "And" not in cur_pc:
                    if cur_pc[0:3] == "Not":
                        cur_pc = "(" + cur_pc
                    
                    if "(" == cur_pc[0]:
                        cur_pc = "And" + cur_pc
                    else:
                        cur_pc = "And(" + cur_pc
                
                # print("CUR pc: " + str(cur_pc))
                config_string_struct[2] = (0, cur_pc)
            
            else: # Some similar
                print("Some similar")
                pass
    
        else: # Default settings for all
            condition = "solver.add(" + pc[1] + ")"      
            config_ext_dict = {}
            cur_pc = config_string_struct[2][1]
            
            if cur_pc[0:3] == "Not":
                pass
            elif ")" in cur_pc:
                cur_pc = cur_pc[:-1]
                
                cur_pc += ", " + 'default_settings_for_all'

            cur_pc += ")"
            
            if "And" not in cur_pc:
                if cur_pc[0:3] == "Not":
                    cur_pc = "(" + cur_pc
                    
                if "(" == cur_pc[0]:
                    cur_pc = "And" + cur_pc
                else:
                    cur_pc = "And(" + cur_pc

            config_string_struct[2] = (0, cur_pc)
    
    
    favoured_list = []
    # data favoured list
    if generator_number != 2:
        try :
            with open("/tmp/data_info.pkl", "rb") as file:
                data_asso_info = pickle.load(file)

                for each in data_asso_info:
                    each_ls, var = each[0], each[1]
                    if "(" in var:
                        var = var[1:]
                    if ")" in var:
                        var = var[:-1]
                        
                    # print("Searching for: " + var + " in " + str(var_s))
                    if var in var_s:
                        favoured_list.extend(each_ls)
        
            # print("Favoured list: " + str(favoured_list))

        except OSError:
            # print("No data info file found")
            exit(1)
    
    
    config_string_struct.append(favoured_list)
    # config_string_struct.append(energy)
    # print("Config string struct: " + str(config_string_struct))
    # save pqeue
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)    
    return config_string_struct


def is_equivalent(claim, show=False, **keywords):
    s = Solver()
    s.set(**keywords)
    s.add(Not(claim))
    if show:
        print(s)
    r = s.check()
    if r == unsat:
        return True
    
    else:
        return False


#configs: [{'b': True}, {'b': False}] choice value is in the key
def generate_config_strings(configs, presence_cond_used=(0, "")):
    config_strings = []
    z3_config_strings = []
    option_indices = {}
    # print("Configs: " + str(configs))
    for idx, config in enumerate(configs):
        # Create a string representation of each configuration
        config_str = []
        z3_config_str = []
        for key, value in config.items():
            each_con = value[1]
            value = value[0]
            choice_val = None
            
            if key in opt_name_map: # TODO: store the unchanged
                key_to_add = opt_name_map[key]
            else: # Maybe a choice                
                maybe_choice_opt = key.split(each_con)[0]
                
                if maybe_choice_opt in opt_name_map:
                    key_to_add = opt_name_map[maybe_choice_opt]
                else:
                    print("This should never happen")
                    exit(1)
            key_to_store = key
            
            if isinstance(value, bool):
                if value:  # If the boolean is True, include the flag (-key)
                    opt_ls = key.split(each_con)
                    opt_only = opt_ls[0]
                    
                    if len(opt_ls) > 1:
                        choice_val = opt_ls[1]
                        choice_val_to_store = choice_val
                        if choice_val in choice_map_keys: # TODO: store the unchanged
                            choice_val = choice_map[choice_val]
                    
                        print("Choice val: " + str(choice_val))
                        print("Choice val to store: " + str(choice_val_to_store))                            
                    
                    prefix = options[opt_only].prefix
                    
                    if choice_val is None:
                        config_str.append(f"{prefix}{key_to_add}")
                        z3_config_str.append(f"{prefix}{key_to_store}")
                        
                    else:
                        config_str.append(f"{prefix}{key_to_add}{each_con}{choice_val}")
                        z3_config_str.append(f"{prefix}{opt_only}{each_con}{choice_val_to_store}")

                    if f"{prefix}{key_to_add}" not in option_indices:
                        option_indices[f"{prefix}{key_to_add}"] = []
                    option_indices[f"{prefix}{key_to_add}"].append(idx)
            else:
                if value is False:
                    continue
                
                if isinstance(value, FuncDeclRef):
                    value = str(value)
                opt_only = key.split(each_con)[0]
                prefix = options[opt_only].prefix
                option_str = f"{prefix}{key_to_add}{each_con}{value}"
                
                choice_to_store = None
                if options[opt_only].opt_type == "choice":
                    if value in choice_revert_map_keys:
                        choice_to_store = choice_revert_map[value]
                    else:
                        print("This should never happen: choice")
                        exit(1)
                else: # int or real
                    choice_to_store = value
                
                z3_option_str = f"{prefix}{key_to_store}{each_con}{choice_to_store}"
                # print(option_str)
                config_str.append(option_str)
                z3_config_str.append(z3_option_str)
                
                
                if option_str not in option_indices:
                    option_indices[option_str] = []
                option_indices[option_str].append(idx)

        # Join all key=value pairs into a single string for this configuration
        final_str = " ".join(config_str)
        if final_str == "":
            final_str = " "
        config_strings.append(final_str)
        
        z3_final_str = " ".join(z3_config_str)
        if z3_final_str == "":
            z3_final_str = " "
        z3_config_strings.append(z3_final_str)

        print("New Config: " + str(final_str))
        print("New Z3 Config: " + str(z3_final_str))
    
    return [config_strings, option_indices, presence_cond_used, z3_config_strings]


def save_pq():
    pqeue = []
    # heappush(pqeue, (0, "default_settings_for_all", [1, 2, 3]))
    heappush(pqeue, (-3, "And(Not(options['a'].z3_var), options['c'].z3_var==options['c'].z3_choices.opt3)", [1, 2, 3]))
    # heappush(pqeue, (0, "And(Not(options['a'].z3_var), options['d'].z3_var==2)", [1, 2, 3]))
    # heappush(pqeue, (0, "And(Not(options['a'].z3_var), options['e'].z3_var==2.5)", [1, 2, 3]))
    # heappush(pqeue, (0, "And(Not(options['a'].z3_var), options['b'].z3_var)", [1, 2, 3]))    
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)

def save_pq_2():
    pqeue = []
    # heappush(pqeue, (-2, "default_settings_for_all", [1, 2, 3]))
    # heappush(pqeue, (-1, "And(options['a'].z3_var, options['b'].z3_var)", [1, 1, 1]))
    heappush(pqeue, (-3, "(options['vafuzz_opt_0'].z3_var)", [1, 2, 3]))
    heappush(pqeue, (-2, "And(options['vafuzz_opt_18'].z3_var==vafuzz_opt_18_choice_0"))
    # heappush(pqeue, (0, "And(Not(a), b)"))

    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)

def save_data_info():
    data = []
    
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump(data, file)

def raw_to_z3_config(raw_config):
    if raw_config == " ":
        return " "
        
    z3_config = ""
    split_token_ls = connectors + prefixes
    split_pattern = "|".join(map(re.escape, split_token_ls))
    all_tokens = re.split(split_pattern, raw_config)
    
    matches = [(m.start(), m.end()) for m in re.finditer(split_pattern, raw_config)]
    
    non_token_indices = []
    start = 0

    for match_start, match_end in matches:
        if start < match_start:
            non_token_indices.append((start, match_start))  # Text before the token
        start = match_end  # Move start past the token

    # Add any remaining text after the last token
    if start < len(raw_config):
        non_token_indices.append((start, len(raw_config)))

    
    # clean up
    all_tokens = [item for item in all_tokens if item != ""]
    
    # print("All tokens:")
    # pprint.pp(all_tokens)
    # pprint.pp(non_token_indices)
    
    idx = 0
    each_token = None
    searching_for_a_token = False
    search_start = None
    token_lower = None
    
    while idx < len(all_tokens):
        # print()
        # print("Current idx: " + str(idx))
        
        
        
        if not searching_for_a_token:
            each_token = all_tokens[idx]
            token_lower = non_token_indices[idx][0]
        each_token = each_token.strip()

        # print("Searching for>" + each_token + "<")
        # TODO: Grammar map
        
        token_found = False
        connector_matches = False
        
        if each_token in opt_name_revert_map_keys:
            token_found = True
            temp_z3_opt = opt_name_revert_map[each_token]
            # print("Found>" + each_token + "<")
            
            if options[temp_z3_opt].opt_type != "bool":
                connector_to_find = options[temp_z3_opt].connector
                # Check for connector
                token_upper = non_token_indices[idx][1]
                # print("Searching for connector: " + connector_to_find + "<")
                # print("Token upper: " + str(token_upper))
                
                if raw_config[token_upper] == connector_to_find:
                    connector_matches = True
                else:
                    conncetor_matches = False
                

            else: # boolean
                # Check if its a space afterwards
                # print("Checking for space")
                
                if token_lower == None:
                    print("Token lower is None")
                    exit(1)
                
                space_maybe_idx = token_lower + len(each_token)
                
                if space_maybe_idx == len(raw_config):
                    connector_matches = True
                else:                    
                    if raw_config[space_maybe_idx] == " ":
                        connector_matches = True
        
        # print("Token found: " + str(token_found))
        # print("Connector matches: " + str(connector_matches))
        
        if token_found and connector_matches:
            searching_for_a_token = False
            z3_opt = opt_name_revert_map[each_token]
            
            # check if it is a non boolean.
            # If so, check if the connector is used.
            # If not, then we did not find a match YET
            
            
        else: # consume another token
            # print("Did not find>" + each_token + "<")
            if idx == len(all_tokens) - 1:
                print("Consumed the last token. No match found.")
                exit(1)
            
            if not searching_for_a_token:
                token_start = non_token_indices[idx][0]
            
            idx += 1
            new_token_end = non_token_indices[idx][1]
            each_token = raw_config[token_start:new_token_end]
            
            searching_for_a_token = True    
            continue
            
        # If not then we should try adding another token.
        # We continue until we find a match.
        # If not, we exit the program with an error message.
        
        z3_config += " " + options[z3_opt].prefix + z3_opt
        
        if options[z3_opt].opt_type != "bool":
            if options[z3_opt].opt_type != "choice":
                z3_config += options[z3_opt].connector + all_tokens[idx + 1]
            else: # choice
                # BUG: Consuming one token may not be enough
                choice_idx = idx + 1
                choice_opt_set_found = False
                token_start = non_token_indices[choice_idx][0]
                token_end = non_token_indices[choice_idx][1]
                
                # print("Choice found")
                
                while choice_idx < len(all_tokens) and not choice_opt_set_found:
                    stipped = False
                    token_to_find = raw_config[token_start:token_end]
                    # print("Searching for choice opt set>" + token_to_find + "<")
                    temp_token = token_to_find
                    token_to_find = token_to_find.strip()
                    
                    space_idx = token_end
                    
                    if token_to_find != temp_token:
                        space_idx = token_end - 1
                    
                    # print("Is this a space>" + raw_config[space_idx] + "<")
                    
                    
                    if token_to_find in choice_revert_map_keys and raw_config[space_idx] == " ":
                        z3_choice = choice_revert_map[token_to_find]
                        choice_opt_set_found = True
                    else: # choice not found
                        # print("failed to find>" + token_to_find + "<")
                        # We should consume another token till we find a match or exit
                        choice_idx += 1
                        token_end = non_token_indices[choice_idx][1]
                        
                if not choice_opt_set_found:
                    print("Failed to find a choice opt set")
                    exit(1)
                # print("Found choice opt set>" + z3_choice + "<")
                z3_config += options[z3_opt].connector + z3_choice
                
                # print("===============================")
                # print("idx before>" + str(idx))
                # print("choice_idx>" + str(choice_idx))
                # print("new token>" + all_tokens[choice_idx])
                # print(all_tokens)
                
                idx = choice_idx - 1
            idx += 1 # BUG: This does not always apply.
        idx+= 1
    
    return z3_config


def send_feedback(config_ls, trace_ls, presence_cond, virgin_bits, havoc_argv=0):
    # exit(1)
    # for idx, each_config in enumerate(config_ls):
        # for each_raw_opt_name in opt_name_revert_map:
        #     for each_connector in connectors:
        #         if each_raw_opt_name + each_connector in each_config:
        #             config_ls[idx] = config_ls[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
        #             print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
            
        #     if each_raw_opt_name + " " in each_config:
        #         config_ls[idx] = config_ls[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
        #         print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
            
        # for each_raw_choice_name in choice_revert_map:
        #     if each_raw_choice_name + " " in each_config:
        #         config_ls[idx] = config_ls[idx].replace(each_raw_choice_name, choice_revert_map[each_raw_choice_name])
        #         print("Replaced: " + each_raw_choice_name + " with " + choice_revert_map[each_raw_choice_name])
        
        # Lets not do this at all
        # for each_raw_opt_name in opt_name_revert_map_keys:
        #     if each_raw_opt_name in each_config:
        #         config_ls[idx] = config_ls[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
        #         # print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
        
        # # TODO We should only do this if the option is a choice
        # for each_raw_choice_name in choice_revert_map_keys:
        #     if each_raw_choice_name in each_config:
        #         config_ls[idx] = config_ls[idx].replace(each_raw_choice_name, choice_revert_map[each_raw_choice_name])
                # print("Replaced: " + each_raw_choice_name + " with " + choice_revert_map[each_raw_choice_name])
 
    if havoc_argv == "1":
        print("THIS HAS BEEN TRIGGERED")
        for idx, each_config in enumerate(config_ls):
            print("Config: " + each_config)
            config_ls[idx] = raw_to_z3_config(each_config)
            print("Z3 Config: " + config_ls[idx])
    feedback = list(zip(config_ls, trace_ls))
    analyze_feedback(feedback, presence_cond, virgin_bits)
    
    # open pqeue and see if length is too big
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        if len(pqeue) > 50: cull_pc_queue()

    # for each in feedback:
    #     save_presence_condition(each)
    return 0


def analyze_feedback(feedback, presence_cond, virgin_bits):
    # G = pretty == PrettyChoices.0
    # # print(PrettyChoices.opt1)
    # # print(PrettyChoices.name)
    # G1 = pretty == PrettyChoices.constructor(0)
    
    # print("Analyzing feedback!")
    # pprint.pp(feedback)
    # print("Presence cond: " + presence_cond + "<")
    
    if presence_cond == "default_settings_for_all":
        presence_cond = " "
    
    if presence_cond != " ":
        vars_to_analyze = extract_variable_names_and_values(presence_cond);
        # print("VARS TO ANALYZE")
        # print(vars_to_analyze)
        
    # Normalize virgin bits
    normalzied_virgin_bits = [0] * len(virgin_bits)
    for idx in range(len(virgin_bits)):
        normalzied_virgin_bits[idx] = virgin_bits[idx] / 255
    
    # Each config
    for each in feedback:
        config = each[0]
        trace = each[1]
    
    # Energy allocation

        energy = 0
        for idx, bit in enumerate(trace):
            if bit != 0:
                energy += (1 * normalzied_virgin_bits[idx])
        if (len(trace) == 0):
            energy = 0
        else:
            energy = math.ceil((energy / len(trace)) * 100)

        if presence_cond == " ":
            save_presence_condition((config, trace, energy))
        else:            
            save_presence_condition((config, trace, energy), use_pc_vars=True, pc_vars=vars_to_analyze)
                
    # each variable
    if presence_cond != " ":        
        for each_var in vars_to_analyze:
            pos_idx = set()
            
            # Find positives
            opt_name = list(extract_option_names(each_var))
            opt_var = options[opt_name[0]].z3_var
            if is_bool(opt_var):
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    # print("Config: " + config)
                    if "-" + each_var in config:
                        pos_idx.add(idx)
            
                
                final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                
                for idx, bit in enumerate(final_pos_trace):
                    if bit != 0:
                        energy += (1 * normalzied_virgin_bits[idx])
                
                if (len(final_pos_trace) == 0):
                    energy = 0
                else:
                    energy = math.ceil((energy / len(final_pos_trace)) * 100)
                # print("new energy: " + str(energy))
                # print("------")
                # print(each_var)
                # print(energy)
                # print("Final pos trace:")
                # print(final_pos_trace)
                save_presence_condition(("-" + each_var, final_pos_trace, energy))
                        
                        
            else: # Not a bool
                # print("NOT A BOOL")
                # exit(1)
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var + " " + str(vars_to_analyze[each_var]) in config:
                        pos_idx.add(idx)
            
                
                final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                
                energy = sum(1 for x in final_pos_trace if x != 0)
                
                # exit(1)
                save_presence_condition(("-" + each_var + " " + str(vars_to_analyze[each_var]),
                                         final_pos_trace, energy))

            
            # Find negatives
            neg_idx = set(range(len(feedback))) - pos_idx

            opt_name = list(extract_option_names(each_var))[0]
            pc_each = options[opt_name].z3_var
            
            if is_bool(pc_each):
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var not in config:
                        neg_idx.add(idx)
                
                
                final_neg_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in neg_idx])]            

                for idx, bit in enumerate(final_neg_trace):
                    if bit != 0:
                        energy += (1 * normalzied_virgin_bits[idx])
                
                if (len(final_neg_trace) == 0):
                    energy = 0
                else:
                    energy = math.ceil((energy / len(final_neg_trace)) * 100)
                
                # print("Final neg trace:")
                # print(final_neg_trace)
                save_presence_condition(("-" + each_var, final_neg_trace, energy), is_negated=True)
                            
            else: # Not a bool
                for idx in range(len(feedback)):
                    config, trace = feedback[idx]
                    if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                        neg_idx.add(idx)
                
                
                final_neg_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in neg_idx])]
                
                energy = sum(1 for x in final_neg_trace if x != 0)
                save_presence_condition(("-" + each_var + " " + str(vars_to_analyze[each_var]),
                                         final_neg_trace, energy), is_negated=True)
    # read_pq()

def analyze_feedback_data(config_list, 
                          data_obj_list, 
                          presence_cond, 
                          id_cutoff, 
                          pc_level_data_asso,
                          output_dir="/output/default",
                          havoc_argv=0):
    # print("Presence cond: " + presence_cond + "<")
    # print("Analyzing feedback!")
    # print("Config list:")
    # pprint.pp(config_list)
    # print("Data obj list:")
    # pprint.pp(data_obj_list)
    # print("Output dir: " + output_dir)
    
    # print(id_cutoff)
    
    # Not doing this
    # for idx, each_config in enumerate(config_list):
    #     # for each_raw_opt_name in opt_name_revert_map:
    #     #     for each_connector in connectors:
    #     #         if each_raw_opt_name + each_connector in each_config:
    #     #             config_ls[idx] = config_ls[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
    #     #             print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
            
    #     #     if each_raw_opt_name + " " in each_config:
    #     #         config_ls[idx] = config_ls[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
    #     #         print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
            
    #     # for each_raw_choice_name in choice_revert_map:
    #     #     if each_raw_choice_name + " " in each_config:
    #     #         config_ls[idx] = config_ls[idx].replace(each_raw_choice_name, choice_revert_map[each_raw_choice_name])
    #     #         print("Replaced: " + each_raw_choice_name + " with " + choice_revert_map[each_raw_choice_name])
        
    #     for each_raw_opt_name in opt_name_revert_map_keys:
    #         if each_raw_opt_name in each_config:
    #             config_list[idx] = config_list[idx].replace(each_raw_opt_name, opt_name_revert_map[each_raw_opt_name])
    #             # print("Replaced: " + each_raw_opt_name + " with " + opt_name_revert_map[each_raw_opt_name])
        
    #     for each_raw_choice_name in choice_revert_map_keys:
    #         if each_raw_choice_name in each_config:
    #             config_list[idx] = config_list[idx].replace(each_raw_choice_name, choice_revert_map[each_raw_choice_name])
    #             # print("Replaced: " + each_raw_choice_name + " with " + choice_revert_map[each_raw_choice_name])
    if havoc_argv == "1":
        for idx, each_config in enumerate(config_list):
            config_list[idx] = raw_to_z3_config(each_config)
    
    # Clean data for analysis
    cleaned_data_matrix = clean_data_arrs(data_obj_list, id_cutoff)
    important_data = keep_last_entries_by_id(cleaned_data_matrix)
    # pprint.pp(cleaned_data_matrix)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # pprint.pp(important_data)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    is_interesting = False

    for each_imp in important_data:
        # print("each imp")
        # print(each_imp)
        if each_imp != []:
            # print("TRIGGER?????")
            is_interesting = True
    
    # print("Is interesting?")
    # print(is_interesting)
    
    if not is_interesting:
        # print("No interesting data")
        return 0
    
    # save execution config
    suffix_ls = [0] * (id_cutoff + 1)
    
    os.makedirs(output_dir + "/queue_argvs/", exist_ok=True)
    # os.makedirs(output_dir + "/crashed_argv/", exist_ok=True)

    for idx in range(len(important_data)):
        each_imp_data = important_data[idx]
        for each_triple in each_imp_data:
            data_id = each_triple[0]
            data_has_bits = each_triple[1]
            data_crashed = each_triple[2]
            
            file_id = "id:" + str(data_id).zfill(6) + "_"
            suffix = suffix_ls[data_id]
            suffix_ls[data_id] += 1
            
            file_name = file_id + str(suffix)
            
            if data_has_bits == 2:
                file_name += "+cov"
            
            with open(output_dir + "/queue_argvs/" + file_name, "w") as file:
                z3_config = config_list[idx]
                
                for each_z3_opt in opt_name_map_keys:
                    z3_config = z3_config.replace(each_z3_opt, opt_name_map[each_z3_opt])
                
                for each_choice in choice_map_keys:
                    z3_config = z3_config.replace(each_choice, choice_map[each_choice])
                
                file.write(z3_config)
                
            # if data_crashed:
            #     with open(output_dir + "/crashed_argv/" + file_name, "w") as file:
            #         file.write(config_list[idx])
        
    
    data_traces = convert_to_bitmap(important_data)
    # pprint.pp(data_traces)    
    # print("Analyzing feedback!")
    if presence_cond != " ":
        vars_to_analyze = extract_variable_names_and_values(presence_cond);
        # print("VARS TO ANALYZE")
        # print(vars_to_analyze)
    
    if not pc_level_data_asso:
        # each variable
        if presence_cond != " ":
            for each_var in vars_to_analyze:
                # print("Analyzing variable: " + each_var + " with value: " + str(vars_to_analyze[each_var]))
                pos_idx = set()
                
                # Find positives
                opt_name = list(extract_option_names(each_var))
                opt_var = options[opt_name[0]].z3_var

                if is_bool(opt_var):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        # print("Config: " + config)
                        # print("Config list: " + str(config_list))
                        
                        # print("Each var 748: " + each_var)
                        if "z3_var" in each_var:
                            each_var_extracted = extract_variable_names_and_values(each_var)
                            # print("Each var extract: " + str(each_var_extracted))
                            extract_opt = list(extract_option_names(each_var))[0]
                            # print("Extract opt: " + str(extract_opt))
                        
                        
                        each_var = extract_opt
                        opt_prefix = options[each_var].prefix
                        if opt_prefix + each_var in config:
                            pos_idx.add(idx)
                
                    # print("Positives: " + str(pos_idx))
                    
                    final_pos_trace = [max(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]

                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print('FAV LS: ' + str(favoured_ls))
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                            
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        # print("Unprocessed each var: " + each_var)
                        # print("Config: " + config)
                        if "z3_var" in each_var:
                            each_var_extracted = extract_variable_names_and_values(each_var)
                            # print("Each var extract: " + str(each_var_extracted))
                            extract_opt = list(extract_option_names(each_var))[0]
                            # print("Extract opt: " + str(extract_opt))
                        
                        for each_connector in connectors:
                            if each_connector in extract_opt:
                                extract_opt = extract_opt.replace(each_connector, " ")
                        
                        extract_opt_ls = extract_opt.split(" ")
                        extract_opt = extract_opt_ls[0]
                        each_var = f"options['{extract_opt}'].z3_var"
                        # print("each var: " + each_var)
                        
                        if options[extract_opt].opt_type == "choice":
                            extract_set = vars_to_analyze[each_var].split("z3_choices.")[1]
                        else: # int or real
                            extract_set = str(vars_to_analyze[each_var])
                        
                        pref = options[extract_opt].prefix
                        conn = options[extract_opt].connector
                        extract_opt = extract_opt + options[extract_opt].connector + extract_set
                        
                        each_var = extract_opt
                        each_var = pref + each_var
                        # print("Processed each var: " + each_var)
                        # print("prefix: " + pref)
                        # print("each var: " + each_var)
                        # pprint.pp(config)
                        if each_var in config:
                            pos_idx.add(idx)
                
                    # print("Positives: " + str(pos_idx))
                    
                    final_pos_trace = [max(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    
                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   

                
                # Find negatives
                # neg_idx = set(range(len(config_list))) - pos_idx
                
                # if is_bool(globals()[each_var]):
                #     for idx in range(len(config_list)):
                #         config, trace = config_list[idx], data_traces[idx]
                #         if "-" + each_var not in config:
                #             neg_idx.add(idx)
                    
                #     # print("Negatives: " + str(neg_idx))
                    
                #     final_neg_trace = [max(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]

                #     # print("Final neg trace: " + str(final_neg_trace))
                    
                #     favoured_ls = []
                #     for idx, x in enumerate(final_neg_trace):
                #         if x != 0:
                #             favoured_ls.append(idx)
                #     # print(favoured_ls)
                #     save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                                
                # else: # Not a bool
                #     for idx in range(len(config_list)):
                #         config, trace = config_list[idx], data_traces[idx]
                #         if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                #             neg_idx.add(idx)
                    
                #     # print("Negatives: " + str(neg_idx))
                    
                #     final_neg_trace = [max(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]
                    
                #     favoured_ls = []
                #     for idx, x in enumerate(final_neg_trace):
                #         if x != 0:
                #             favoured_ls.append(idx)
                #     # print(favoured_ls)
                #     save_presence_condition_data_info(("-" + each_var, favoured_ls))  
    else:
        # print("WE DONT BELONG HERE")
        # Each config
        for idx in range(len(config_list)):
            config = config_list[idx]
            trace = data_traces[idx]
                        
            favoured_ls = []
            for idx, bit in enumerate(trace):
                if bit != 0:
                    favoured_ls.append(idx)
            
            # print("Config: " + config)
            # print("Favoured: " + str(favoured_ls))
            if presence_cond == " ":
                save_presence_condition_data_info((config, favoured_ls))
            else:
                save_presence_condition_data_info((config, favoured_ls), use_pc_vars=True, pc_vars=vars_to_analyze)

        # each variable
        if presence_cond != " ":
            for each_var in vars_to_analyze:
                # print("Analyzing variable: " + each_var + " with value: " + str(vars_to_analyze[each_var]))
                pos_idx = set()
                
                # Find positives
                opt_name = list(extract_option_names(each_var))
                opt_var = options[opt_name[0]].z3_var
                if is_bool(opt_var):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var in config:
                            pos_idx.add(idx)
                
                    # # print("Positives: " + str(pos_idx))
                    
                    # final_pos_trace = [min(col) for col in zip(*[feedback[idx][1] for idx in pos_idx])]
                    # final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]

                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                            
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        
                        if "-" + each_var + " " + str(vars_to_analyze[each_var]) in config:
                            pos_idx.add(idx)
                
                    # print("Positives: " + str(pos_idx))
                    
                    final_pos_trace = [min(col) for col in zip(*[data_traces[idx] for idx in pos_idx])]
                    
                    # Build favoured list
                    favoured_ls = []
                    for idx, x in enumerate(final_pos_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   

                
                # Find negatives
                neg_idx = set(range(len(config_list))) - pos_idx
                opt_name = list(extract_option_names(each_var))[0]
                pc_each = options[opt_name].z3_var

                if is_bool(pc_each):
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        if "-" + each_var not in config:
                            neg_idx.add(idx)
                    
                    # print("Negatives: " + str(neg_idx))
                    
                    final_neg_trace = [min(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]

                    # print("Final neg trace: " + str(final_neg_trace))
                    
                    favoured_ls = []
                    for idx, x in enumerate(final_neg_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls))                   
                                
                else: # Not a bool
                    for idx in range(len(config_list)):
                        config, trace = config_list[idx], data_traces[idx]
                        if "-" + each_var + " " + str(vars_to_analyze[each_var]) not in config:
                            neg_idx.add(idx)
                    
                    # print("Negatives: " + str(neg_idx))
                    
                    final_neg_trace = [min(col) for col in zip(*[data_traces[idx] for idx in neg_idx])]
                    
                    favoured_ls = []
                    for idx, x in enumerate(final_neg_trace):
                        if x != 0:
                            favoured_ls.append(idx)
                    # print(favoured_ls)
                    save_presence_condition_data_info(("-" + each_var, favoured_ls)) 
    # read_data_info()
    return 0


def save_presence_condition(analyzed_feedback, is_negated=False, pc_vars={}, use_pc_vars=False):    
    config = analyzed_feedback[0] + " "
    trace = analyzed_feedback[1]
    energy = int(analyzed_feedback[2])
    
    # Generate presence condition from config
    # print("Config>>>>: " + config + "<<<<")
    # print("Trace: " + str(trace))
    # print("Energy: " + str(energy))
    config = config.strip()
    pres_cond_str = generate_presence_condition(config, 
                                                is_negated=is_negated,
                                                pc_vars=pc_vars,
                                                use_pc_vars=use_pc_vars)
    # pres_cond = Preseonce_Condition(energy, "somefilepath", pres_cond_str)
    # print("Retrieved PC: " + pres_cond_str + " with energy: " + str(energy))
    pres_cond = None
    
    if (pres_cond_str == "default_settings_for_all"):
        pres_cond = "default_settings_for_all"
    else:
        # print("Pres cond str: " + pres_cond_str)
        pres_cond = eval(pres_cond_str)
        
    # Check if the presence condition is already in the pqeue
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        found = False
        for idx, each_pc in enumerate(pqeue):
            if pres_cond_str == "default_settings_for_all":
                if each_pc[1] == "default_settings_for_all":
                    if each_pc[0] > -energy:
                        each_pc = list(each_pc)
                        each_pc[0] = -energy
                        each_pc[2] = trace
                        pqeue[idx] = tuple(each_pc)
                    found = True
                    break
                # print("Default settings for all already in pqeue")
            else:
                if each_pc[1] == "default_settings_for_all":
                    continue
                # print("Cur str: " + each_pc[1])
                # print("Each pc: " + str(each_pc))
                cur = eval(each_pc[1])
                # print("Cur: " + str(cur))
                # print("Pres: " + str(pres_cond))
                if (is_equivalent(cur == pres_cond)):
                    if each_pc[0] > -energy:
                        each_pc = list(each_pc)
                        each_pc[0] = -energy
                        each_pc[2] = trace
                        pqeue[idx] = tuple(each_pc)
                    found = True
                    break
        if not found:
            heappush(pqeue, (-energy, pres_cond_str, trace))
    
    # print(pqeue)
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump(pqeue, file)
    
        

# A config would like like: "-a -b -c 3"
# So we have to parse the config and find out what the presence condition is
def generate_presence_condition(config, is_negated=False, pc_vars={}, use_pc_vars=False):
    # Create the regex pattern
    prefixes_sorted = sorted(prefixes, key=len, reverse=True)
    escaped_prefixes = [re.escape(p) for p in prefixes_sorted]
    pattern = r'\s(?=(?:' + '|'.join(escaped_prefixes) + r')\w)'

    config_ls_raw = re.split(pattern, config)
    config_ls = []

    for config in config_ls_raw:
        if config.strip():
            # Find the first matching prefix
            matched_prefix = next((p for p in prefixes_sorted if config.strip().startswith(p)), None)
            if matched_prefix:
                config_ls.append(config.strip()[len(matched_prefix):])

    multi = False
    pres_conds_str = ""
    
    if (is_negated):
        pres_conds_str = "Not("
    if len(config_ls) > 1:
        pres_conds_str = "And("
        multi = True
    # print(config_ls)
    if len(config_ls) == 0 or config_ls[0] == '':
        return "default_settings_for_all"

    # print("Config LS: " + str(config_ls))    
    for each in config_ls:
        # print("Each: " + each)
        split_pattern = "[" + re.escape("".join(connectors) + " ") + "]"
        
        opt_set = re.split(split_pattern, each)
        opt_set = list(filter(None, opt_set))
        if len(opt_set) <= 0:
            # print("Invalid config string")
            return
        # And(Not(options['a'].z3_var), options['c'].z3_var==options['c'].z3_choices.option3)
        opt_name = opt_set[0]
        # print("Opt name: " + opt_name)
        if "options" in opt_name:
            opt_name = list(extract_option_names(opt_name))[0]

        for each_pref in prefixes:
            if each_pref in opt_name:
                opt_name = opt_name.split(each_pref)[1]
        
        # if opt_name not in options:
        #     print("Invalid config string")
        opt = options[opt_name].z3_var
        
        # print("Opt: " + str(opt))
        # print("Opt set: " + str(opt_set))
        if len(opt_set) == 1:
            if is_bool(opt):
                pres_conds_str += f"options['{opt}'].z3_var, "
            else:
                print("Invalid config string")
                return
        else:
            set_value_str = opt_set[1]
            opt = options[opt_name].z3_var
            # Do something else
            if is_int(opt):
                # print("opt name: " + opt_name)
                # print("opt: " + str(opt))
                # print("set value str: " + set_value_str)
                pres_conds_str += f"options['{opt}'].z3_var == {set_value_str}, "
            elif is_real(opt):
                pres_conds_str += f"options['{opt}'].z3_var == {set_value_str}, "
            elif isinstance(opt, DatatypeRef):
                # print("opt name: " + opt_name)
                # print("set value str: " + set_value_str)
                if "z3_choices" in set_value_str:
                    pres_conds_str += f"options['{opt}'].z3_var == {set_value_str}, "
                else:
                    pres_conds_str += f"options['{opt}'].z3_var == options['{opt_name}'].z3_choices.{set_value_str}, "
                # print("Presence cond 935: " + pres_conds_str)
            else:
                pres_conds_str += f"{opt} == StringVal({set_value_str}), "
    
    #Opts in config ls
    config_ls_opts = []
    for each_part in config_ls:
        config_ls_opts.append(each_part.split(" ")[0])
    
    if multi:
        if use_pc_vars:
            for each in pc_vars:
                # print("Each: " + each)
                processed_each = list(extract_option_names(each))[0]
                if processed_each not in config_ls_opts:
                    opt_name_ls = list(extract_option_names(each))
                    z3_opt_processing = options[opt_name_ls[0]].z3_var
                    
                    if is_bool(z3_opt_processing):
                        pres_conds_str += f"Not({each}), "
                    else:
                        pres_conds_str += f"(Not({each} == {pc_vars[each]})), "
                        # print("Presence cond 985: " + pres_conds_str)
                        # print("Processed each: " + processed_each)
                        # print("Each: " + each)
                        # print("PC Vars: " + str(pc_vars))
                        # print("Config LS: " + str(config_ls))
                        # input()
        pres_conds_str = pres_conds_str[:-2] + ")"
    else:
        if use_pc_vars:
            pres_conds_str = "And(" + pres_conds_str
            for each in pc_vars:
                processed_each = list(extract_option_names(each))[0]
                if processed_each not in config_ls_opts:
                    # each1 = globals()[each]
                    opt_name_ls = list(extract_option_names(each))
                    z3_opt_processing = options[opt_name_ls[0]].z3_var
                    
                    if is_bool(z3_opt_processing):
                        pres_conds_str += f"Not({each}), "
                    else:
                        # print(pc_vars)
                        pres_conds_str += f"(Not({each} == {pc_vars[each]})), "
                        # print("Presence cond 1000: " + pres_conds_str)
                        # input()
                        
            pres_conds_str = pres_conds_str[:-2] + ")"
        else:
            pres_conds_str = pres_conds_str[:-2]
    if (is_negated):
        pres_conds_str += ")"
    
    # # print("BEFORE RET: " + pres_conds_str)
    # Check for commas in the whole str, if not, remove the And
    if pres_conds_str.count(",") == 0 and "And" in pres_conds_str:
        pres_conds_str = pres_conds_str[3:]
    # pres_conds_str = pres_conds_str.replace("-", "_")
    # pres_conds_str = pres_conds_str.replace(":", "colonoperator")
    # # print("BEFORE RET: " + pres_conds_str)
    return pres_conds_str


def save_presence_condition_data_info(analyzed_feedback, 
                                      is_negated=False, 
                                      pc_vars={}, 
                                      use_pc_vars=False):
    config, favoured_ls = analyzed_feedback[0], analyzed_feedback[1]
    
    # Generate presence condition from config
    # print("Config: " + config)
    pres_cond_str = generate_presence_condition(config, 
                                                is_negated=is_negated,
                                                pc_vars=pc_vars,
                                                use_pc_vars=use_pc_vars)
    # pres_cond = Preseonce_Condition(energy, "somefilepath", pres_cond_str)
    # print("Retrieved PC: " + pres_cond_str + " with list: " + str(favoured_ls))
    pres_cond = None
    
    if (pres_cond_str == "default_settings_for_all"):
        pres_cond = "default_settings_for_all"
    else:
        # print("Pres cond str: " + pres_cond_str)
        pres_cond = eval(pres_cond_str)

    # Check if the presence condition is already in the pqeue

    data_info_ls = []
    try:
        with open("/tmp/data_info.pkl", "rb") as file:
            data_info_ls = pickle.load(file)
    except OSError:
        # print("No file found")
        with open("/tmp/data_info.pkl", "wb") as file:
            pickle.dump(data_info_ls, file)




    with open("/tmp/data_info.pkl", "rb") as file:
        data_info_ls = pickle.load(file)
        found = False
        
        for idx, each_pc in enumerate(data_info_ls):
            if pres_cond_str == "default_settings_for_all":
                if each_pc[1] == "default_settings_for_all":
                    # if each_pc[0] > energy:
                    if favoured_ls != []:
                        each_pc = list(each_pc)
                        each_pc[0] = list(set(each_pc[0] + favoured_ls))
                        data_info_ls[idx] = tuple(each_pc)
                    found = True
                    break
                # print("Default settings for all already in ls")
            else:
                if each_pc[1] == "default_settings_for_all":
                    continue
                cur = eval(each_pc[1])
                if (is_equivalent(cur == pres_cond)):
                    if favoured_ls != []:
                        each_pc = list(each_pc)
                        each_pc[0] = list(set(each_pc[0] + favoured_ls))
                        data_info_ls[idx] = tuple(each_pc)
                    found = True
                    break
        if not found:
            data_info_ls.append((favoured_ls, pres_cond_str))
    # # print(data_info_ls)
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump(data_info_ls, file)


def read_data_info():
    with open("/tmp/data_info.pkl", "rb") as file:
        data = pickle.load(file)
        pprint.pp(data)


def read_pq():
    with open("/tmp/pqeue.pkl", "rb") as file:
        pqeue = pickle.load(file)
        
        counter = 0
        for each in pqeue:
            print("--------------------------------------------")
            print("PQ: " + str(counter))
            print("Energy: " + str(each[0]) + " PC: " + each[1])
            trace = each[2]
            for idx, bit in enumerate(trace):
                if bit != 0:
                    print("Bit: " + str(idx), end=" ")
                    # add newline here
            counter += 1


def clear_pq():
    with open("/tmp/pqeue.pkl", "wb") as file:
        pickle.dump([], file)


def clear_data_info():
    with open("/tmp/data_info.pkl", "wb") as file:
        pickle.dump([], file)


def init_info():
    return ([len(options)])

def main():

    # constraint_file = sys.argv[1]
    # configs_to_generate = int(sys.argv[2])
    # save_presence_condition(("-a -b", 10))
    # save_pq()
    # save_pq_2()
    # read_pq()
    # solutions = request_config_generation('/tmp/pqeue.pkl', 10, 1)
    # pprint.pp(solutions)
    # clear_pq()
    # analyze_feedback([
    #     ("-a +b", [0, 1, 0]),
    #     ("+b", [1, 1, 0]),
    #     ("-a", [0, 0, 0]),
    #     (" ", [0, 0, 0]) # BUG
    #     ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()
    
    # print("+++++++++++++++++++++++++++++++++")
    # clear_pq()
    # analyze_feedback([
    #     ("-a --c option1 +b", [0, 1, 0]),
    #     ("--c option1", [1, 1, 0]),
    #     ("-a", [0, 0, 0]),
    #     (" ", [0, 0, 0]) # BUG
    #     ], "And(Not(options['a'].z3_var), options['c'].z3_var==options['c'].z3_choices.option1, options['b'].z3_var)",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()
    
    # print("++++++++++++++++++++++++++++")
    # clear_pq()
    # analyze_feedback([
    #     ("-a _d 2", [0, 1, 0]),
    #     ("_d 2", [1, 1, 0]),
    #     ("-a", [0, 0, 0]),
    #     (" ", [0, 0, 0]) # BUG
    #     ], "And(Not(options['a'].z3_var), options['d'].z3_var==2)",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()
    
    # print("+++++++++++++++++++++++++++++++++")
    # clear_pq()
    # analyze_feedback([
    #     ("-a @e 2.33", [0, 1, 0]),
    #     ("@e 2.33", [1, 1, 0]),
    #     ("-a", [0, 0, 0]),
    #     (" ", [0, 0, 0]) # BUG
    #     ], "And(Not(options['a'].z3_var), options['e'].z3_var==2.33)",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()

    # print("+++++++++++++++++++++++++++++++++")
    # clear_pq()
    # analyze_feedback([
    #     (" ", [1, 1, 0]) # BUG
    #     ], " ",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()
    
    # print("+++++++++++++++++++++++++++++++++")
    # clear_pq()
    # analyze_feedback([
    #     ("-a", [0, 0, 0]),
    #     ("-e 2.3", [10, 10, 0]),
    #     ], " ",
    #     # ], "And(Not(options['a'].z3_var), options['b'].z3_var)",
    #     [1, 1, 1])
    # read_pq()

    # solutions = request_config_generation('/tmp/pqeue.pkl', 10, 2)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++")
    # print("RAW configs:")
    # print("+++++++++++++++++++++++++++++++++++++++++++++++")
    # pprint.pp(solutions[0])
    # print("+++++++++++++++++++++++++++++++++++++++++++++++")
    # print("Z3 configs:")
    # print("+++++++++++++++++++++++++++++++++++++++++++++++")
    # pprint.pp(solutions[3])
    # print("+++++++++++++++++++++++++++++++++++++++++++++++")
    
    clear_pq()
    save_data_info()
    read_pq()
    read_data_info()
    
    res = raw_to_z3_config("-h -x -D -S -G -L -t --target=a.out-i386-lynx --insn-width=197655867.907959 --special-syms --inline --dwarf-check --visualize-jumps")
    print(res)
    # analyze_feedback([
    #     ("-a", [1, 0, 0]), 
    #     ("-b", [1, 1, 0]), 
    #     ("", [0, 0, 0])
    #     ], " ")

    # save_data_info()
    
    # analyze_feedback_data(["-a", "-c=op-tion1", "-a -c=op-tion1", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(options['a'].z3_var), options['c'].z3_var==options['c'].z3_choices.opt1", 6, 0, "/tmp")
    
    # analyze_feedback_data(["-a", "+b", "-a +b", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(options['a'].z3_var, options['b'].z3_var)", 6, 0, "/tmp")

    # analyze_feedback_data(["-a", "@e=2.5", "-a @e=2.5", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(options['a'].z3_var), options['e'].z3_var==2.5", 6, 0, "/tmp")

    # analyze_feedback_data(["-a", "_d::2.5", "-a _d::2.5", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(options['a'].z3_var), options['d'].z3_var==2", 6, 0, "/tmp")

    # analyze_feedback_data(["-a", "--c=option1", "-a --c=option1", " "], 
    #                       [[(1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0), (3, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0)], 
    #                        [(1, 0, 0), (1, 0, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 0, 0), (5, 0, 0), (6, 1, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)],
    #                        [(1, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0)]], 
    #                       "And(options['a'].z3_var), options['c'].z3_var==options['c'].z3_choices.option1)", 6, 0, "/tmp")
    
    # analyze_feedback_data(["-a", "-b", "-c", "-d"], 
    #                   [[(10, 0, 0), (11, 1, 0), (12, 0, 0)], 
    #                    [(10, 0, 0), (11, 0, 0), (12, 1, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 0, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(a, b, c, d)", 12, 0)
    
    # analyze_feedback_data(["-a", "-b", "-a -b", " "], 
    #                   [[(10, 0, 0), (11, 1, 0), (12, 0, 0)], 
    #                    [(10, 0, 0), (11, 0, 0), (12, 1, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 0, 0)],
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(options['a'].z3_var), options['b'].z3_var)", 12, 0, "/tmp")
    
    # analyze_feedback_data(["-a", "-b"], 
    #                   [[(10, 0, 0), (11, 0, 0), (12, 0, 0)], 
    #                    [(10, 1, 0), (11, 0, 0), (12, 1, 0)]], 
    #                   "And(options['a'].z3_var), options['b'].z3_var)", 10, 0, "/tmp")


    
    # read_data_info()
    # # print(extract_variable_names_and_values("(And(Not(a), b, c==3))"))
    
    # F = Not(And(a == True, b == True))
        # G = Or(Not(a), Not(b))
        # # print(is_equivalent(F == G))

if __name__ == '__main__':
    main()
