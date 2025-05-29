# PRESENCE CONDITION ANALYSIS SUMMARY

## djpeg
==================================================
Total Conditions Analyzed: 120
Total Bits Discovered: 2899

### PERFORMANCE-BASED SUMMARY
=========================

1. High Performance (≥50 bits)
   Total Bits: 2677 (92.3%)
   Conditions: 6
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var == 44) (1411 bits)
   - Not(options['vafuzz_opt_0'].z3_var == 44) (926 bits)
   - And(options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (125 bits)
   ... and 3 more

2. Low Performance (<10 bits)
   Total Bits: 79 (2.7%)
   Conditions: 108
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_16'].z3_var == 85.131259, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 44))) (9 bits)
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2, (Not(options['vafuzz_opt_0'].z3_var == 33))) (7 bits)
   - And(options['vafuzz_opt_20'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 34))) (7 bits)
   ... and 105 more

3. Medium Performance (10-49 bits)
   Total Bits: 143 (4.9%)
   Conditions: 6
   - And(options['vafuzz_opt_0'].z3_var == 53, options['vafuzz_opt_6'].z3_var) (42 bits)
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_0'].z3_var == 22, options['vafuzz_opt_9'].z3_var, Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_21'].z3_var)) (42 bits)
   - Not(options['vafuzz_opt_0'].z3_var == 33) (22 bits)
   ... and 3 more

### STRUCTURE-BASED SUMMARY
=======================

1. Conjunction (AND)
   Total Bits: 1733 (59.8%)
   Conditions: 89
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var == 44) (1411 bits)
   - And(options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (125 bits)
   - And(options['vafuzz_opt_1'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 44))) (52 bits)
   ... and 86 more

2. Equality Check
   Total Bits: 167 (5.8%)
   Conditions: 12
   - (options['vafuzz_opt_0'].z3_var == 69) (93 bits)
   - (options['vafuzz_opt_0'].z3_var == 22) (70 bits)
   - options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0 (2 bits)
   ... and 9 more

3. Negated
   Total Bits: 985 (34.0%)
   Conditions: 14
   - Not(options['vafuzz_opt_0'].z3_var == 44) (926 bits)
   - Not(options['vafuzz_opt_0'].z3_var == 33) (22 bits)
   - Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2) (17 bits)
   ... and 11 more

4. Simple Boolean
   Total Bits: 14 (0.5%)
   Conditions: 5
   - (options['vafuzz_opt_5'].z3_var) (10 bits)
   - (options['vafuzz_opt_7'].z3_var) (3 bits)
   - (options['vafuzz_opt_8'].z3_var) (1 bits)
   ... and 2 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var == 44)
   1411 bits (48.7%)

2. Not(options['vafuzz_opt_0'].z3_var == 44)
   926 bits (31.9%)

3. And(options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0))
   125 bits (4.3%)

4. (options['vafuzz_opt_0'].z3_var == 69)
   93 bits (3.2%)

5. (options['vafuzz_opt_0'].z3_var == 22)
   70 bits (2.4%)
