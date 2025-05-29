# PRESENCE CONDITION ANALYSIS SUMMARY

Mutator Analysis: [link](../Mutator_Analysis.md)

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

===================================
===================================

## jpegtran
==================================================

Total Conditions Analyzed: 120
Total Bits Discovered: 5445

### PERFORMANCE-BASED SUMMARY
=============================

1. High Performance (≥50 bits)
   Total Bits: 5167 (94.9%)
   Conditions: 5
   - And(options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, options['vafuzz_opt_12'].z3_var == 48) (3132 bits)
   - Not(options['vafuzz_opt_13'].z3_var == 94) (1176 bits)
   - And(Not(options['vafuzz_opt_13'].z3_var == 94), options['vafuzz_opt_15'].z3_var, options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (612 bits)
   ... and 2 more

2. Low Performance (<10 bits)
   Total Bits: 70 (1.3%)
   Conditions: 107
   - And(options['vafuzz_opt_11'].z3_var == 34, options['vafuzz_opt_13'].z3_var == 86, options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_3)) (6 bits)
   - And(options['vafuzz_opt_11'].z3_var == 39, options['vafuzz_opt_16'].z3_var, Not(options['vafuzz_opt_17'].z3_var)) (6 bits)
   - And(options['vafuzz_opt_8'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0))) (5 bits)
   ... and 104 more

3. Medium Performance (10-49 bits)
   Total Bits: 208 (3.8%)
   Conditions: 8
   - (options['vafuzz_opt_11'].z3_var == 46) (47 bits)
   - And(Not(options['vafuzz_opt_12'].z3_var == 48), options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (39 bits)
   - (options['vafuzz_opt_11'].z3_var == 7) (29 bits)
   ... and 5 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 4012 (73.7%)
   Conditions: 93
   - And(options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, options['vafuzz_opt_12'].z3_var == 48) (3132 bits)
   - And(Not(options['vafuzz_opt_13'].z3_var == 94), options['vafuzz_opt_15'].z3_var, options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (612 bits)
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_11'].z3_var == 7) (108 bits)
   ... and 90 more

2. Equality Check
   Total Bits: 80 (1.5%)
   Conditions: 11
   - (options['vafuzz_opt_11'].z3_var == 46) (47 bits)
   - (options['vafuzz_opt_11'].z3_var == 7) (29 bits)
   - (options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_3) (4 bits)
   ... and 8 more

3. Negated
   Total Bits: 1336 (24.5%)
   Conditions: 13
   - Not(options['vafuzz_opt_13'].z3_var == 94) (1176 bits)
   - Not(options['vafuzz_opt_11'].z3_var == 7) (139 bits)
   - Not(options['vafuzz_opt_6'].z3_var == options['vafuzz_opt_6'].z3_choices.vafuzz_opt_6_choice_2) (14 bits)
   ... and 10 more

4. Simple Boolean
   Total Bits: 17 (0.3%)
   Conditions: 3
   - default_settings_for_all (17 bits)
   - (options['vafuzz_opt_1'].z3_var) (0 bits)
   - (options['vafuzz_opt_10'].z3_var) (0 bits)

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, options['vafuzz_opt_12'].z3_var == 48)
   3132 bits (57.5%)

2. Not(options['vafuzz_opt_13'].z3_var == 94)
   1176 bits (21.6%)

3. And(Not(options['vafuzz_opt_13'].z3_var == 94), options['vafuzz_opt_15'].z3_var, options['vafuzz_opt_0'].z3_var == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0))
   612 bits (11.2%)

4. Not(options['vafuzz_opt_11'].z3_var == 7)
   139 bits (2.6%)

5. And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_11'].z3_var == 7)
   108 bits (2.0%)

===============================================================
===============================================================

## xmllint
==================================================

Total Conditions Analyzed: 114
Total Bits Discovered: 5020

### PERFORMANCE-BASED SUMMARY
=============================

1. High Performance (≥50 bits)
   Total Bits: 4403 (87.7%)
   Conditions: 10
   - (null) (3258 bits)
   - And(options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_19'].z3_var) (317 bits)
   - And(options['vafuzz_opt_0'].z3_var, debugent, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_37'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_42'].z3_var, options['vafuzz_opt_45'].z3_var, options['vafuzz_opt_46'].z3_var, options['vafuzz_opt_47'].z3_var, options['vafuzz_opt_50'].z3_var) (200 bits)
   ... and 7 more

2. Low Performance (<10 bits)
   Total Bits: 126 (2.5%)
   Conditions: 79
   - And(options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_32'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_40'].z3_var, options['vafuzz_opt_46'].z3_var, options['vafuzz_opt_48'].z3_var, Not(debugent), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_11'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_18'].z3_var), Not(options['vafuzz_opt_19'].z3_var), Not(options['vafuzz_opt_20'].z3_var), Not(options['vafuzz_opt_21'].z3_var), Not(options['vafuzz_opt_26'].z3_var), Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_37'].z3_var), Not(options['vafuzz_opt_45'].z3_var), Not(options['vafuzz_opt_49'].z3_var), Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_41'].z3_var), Not(options['vafuzz_opt_50'].z3_var), Not(options['vafuzz_opt_33'].z3_var), Not(options['vafuzz_opt_34'].z3_var), Not(options['vafuzz_opt_35'].z3_var), Not(options['vafuzz_opt_39'].z3_var)) (9 bits)
   - And(options['vafuzz_opt_10'].z3_var, debugent) (9 bits)
   - And(options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_50'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_3'].z3_var, Not(options['vafuzz_opt_11'].z3_var), Not(debugent), Not(options['vafuzz_opt_47'].z3_var), Not(options['vafuzz_opt_37'].z3_var)) (9 bits)
   ... and 76 more

3. Medium Performance (10-49 bits)
   Total Bits: 491 (9.8%)
   Conditions: 25
   - And(options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_33'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_35'].z3_var, options['vafuzz_opt_37'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, Not(options['vafuzz_opt_22'].z3_var)) (41 bits)
   - And(options['vafuzz_opt_0'].z3_var, debugent, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_32'].z3_var, options['vafuzz_opt_37'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_45'].z3_var, options['vafuzz_opt_48'].z3_var, options['vafuzz_opt_49'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_41'].z3_var), Not(options['vafuzz_opt_50'].z3_var), Not(options['vafuzz_opt_33'].z3_var), Not(options['vafuzz_opt_34'].z3_var), Not(options['vafuzz_opt_35'].z3_var), Not(options['vafuzz_opt_39'].z3_var), Not(options['vafuzz_opt_22'].z3_var)) (37 bits)
   - And(options['vafuzz_opt_0'].z3_var, debugent, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_50'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_20'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_41'].z3_var), Not(options['vafuzz_opt_33'].z3_var), Not(options['vafuzz_opt_34'].z3_var), Not(options['vafuzz_opt_35'].z3_var), Not(options['vafuzz_opt_37'].z3_var), Not(options['vafuzz_opt_38'].z3_var), Not(options['vafuzz_opt_22'].z3_var)) (35 bits)
   ... and 22 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 1533 (30.5%)
   Conditions: 110
   - And(options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_19'].z3_var) (317 bits)
   - And(options['vafuzz_opt_0'].z3_var, debugent, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_37'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_42'].z3_var, options['vafuzz_opt_45'].z3_var, options['vafuzz_opt_46'].z3_var, options['vafuzz_opt_47'].z3_var, options['vafuzz_opt_50'].z3_var) (200 bits)
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_33'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_35'].z3_var, options['vafuzz_opt_36'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_50'].z3_var) (189 bits)
   ... and 107 more

2. Simple Boolean
   Total Bits: 3487 (69.5%)
   Conditions: 4
   - (null) (3258 bits)
   - (options['vafuzz_opt_22'].z3_var) (101 bits)
   - (options['vafuzz_opt_13'].z3_var) (76 bits)
   ... and 1 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. (null)
   3258 bits (64.9%)

2. And(options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_19'].z3_var)
   317 bits (6.3%)

3. And(options['vafuzz_opt_0'].z3_var, debugent, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_37'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_42'].z3_var, options['vafuzz_opt_45'].z3_var, options['vafuzz_opt_46'].z3_var, options['vafuzz_opt_47'].z3_var, options['vafuzz_opt_50'].z3_var)
   200 bits (4.0%)

4. And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_26'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_30'].z3_var, options['vafuzz_opt_33'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_35'].z3_var, options['vafuzz_opt_36'].z3_var, options['vafuzz_opt_38'].z3_var, options['vafuzz_opt_39'].z3_var, options['vafuzz_opt_50'].z3_var)
   189 bits (3.8%)

5. (options['vafuzz_opt_22'].z3_var)
   101 bits (2.0%)

   =====================================================
   =====================================================

## readelf

==================================================

Total Conditions Analyzed: 183
Total Bits Discovered: 3671

### PERFORMANCE-BASED SUMMARY
=============================

1. High Performance (≥50 bits)
   Total Bits: 2128 (58.0%)
   Conditions: 18
   - And(options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_0'].z3_var) (588 bits)
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_4'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var)) (173 bits)
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_13'].z3_var, Not(options['vafuzz_opt_1'].z3_var), Not(options['vafuzz_opt_5'].z3_var), Not(options['vafuzz_opt_0'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_23'].z3_var), Not(options['vafuzz_opt_18'].z3_var), Not(options['vafuzz_opt_6'].z3_var)) (138 bits)
   ... and 15 more

2. Low Performance (<10 bits)
   Total Bits: 257 (7.0%)
   Conditions: 108
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_36'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_23'].z3_var, Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_24'].z3_var)) (9 bits)
   - Not(options['vafuzz_opt_11'].z3_var) (9 bits)
   - And(options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_23'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_35'].z3_var, options['vafuzz_opt_36'].z3_var, Not(options['vafuzz_opt_13'].z3_var), Not(options['vafuzz_opt_26'].z3_var), Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_5'].z3_var), Not(options['vafuzz_opt_11'].z3_var)) (8 bits)
   ... and 105 more

3. Medium Performance (10-49 bits)
   Total Bits: 1286 (35.0%)
   Conditions: 57
   - And(options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_6'].z3_var, Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_22'].z3_var)) (49 bits)
   - And(options['vafuzz_opt_15'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_34'].z3_var, options['vafuzz_opt_36'].z3_var, Not(options['vafuzz_opt_1'].z3_var), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_5'].z3_var), Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_11'].z3_var), Not(options['vafuzz_opt_13'].z3_var), Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_16'].z3_var), Not(options['vafuzz_opt_21'].z3_var), Not(options['vafuzz_opt_22'].z3_var), Not(options['vafuzz_opt_0'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_23'].z3_var), Not(options['vafuzz_opt_7'].z3_var)) (46 bits)
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_16'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_22'].z3_var, Not(options['vafuzz_opt_20'].z3_var), Not(options['vafuzz_opt_11'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_19'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_15'].z3_var), Not(options['vafuzz_opt_9'].z3_var), Not(options['vafuzz_opt_0'].z3_var), Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_23'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_8'].z3_var), Not(options['vafuzz_opt_25'].z3_var)) (45 bits)
   ... and 54 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 3128 (85.2%)
   Conditions: 171
   - And(options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_0'].z3_var) (588 bits)
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_4'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var)) (173 bits)
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_13'].z3_var, Not(options['vafuzz_opt_1'].z3_var), Not(options['vafuzz_opt_5'].z3_var), Not(options['vafuzz_opt_0'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_23'].z3_var), Not(options['vafuzz_opt_18'].z3_var), Not(options['vafuzz_opt_6'].z3_var)) (138 bits)
   ... and 168 more

2. Negated
   Total Bits: 41 (1.1%)
   Conditions: 5
   - Not(options['vafuzz_opt_0'].z3_var) (15 bits)
   - Not(options['vafuzz_opt_20'].z3_var) (13 bits)
   - Not(options['vafuzz_opt_11'].z3_var) (9 bits)
   ... and 2 more

3. Simple Boolean
   Total Bits: 502 (13.7%)
   Conditions: 7
   - (options['vafuzz_opt_3'].z3_var) (131 bits)
   - (options['vafuzz_opt_0'].z3_var) (103 bits)
   - (options['vafuzz_opt_34'].z3_var) (91 bits)
   ... and 4 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_0'].z3_var)
   588 bits (16.0%)

2. And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_4'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var))
   173 bits (4.7%)

3. And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_11'].z3_var, options['vafuzz_opt_13'].z3_var, Not(options['vafuzz_opt_1'].z3_var), Not(options['vafuzz_opt_5'].z3_var), Not(options['vafuzz_opt_0'].z3_var), Not(options['vafuzz_opt_29'].z3_var), Not(options['vafuzz_opt_24'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_27'].z3_var), Not(options['vafuzz_opt_12'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_23'].z3_var), Not(options['vafuzz_opt_18'].z3_var), Not(options['vafuzz_opt_6'].z3_var))
   138 bits (3.8%)

4. And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_29'].z3_var, options['vafuzz_opt_24'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_27'].z3_var, options['vafuzz_opt_12'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_23'].z3_var, Not(options['vafuzz_opt_17'].z3_var), Not(options['vafuzz_opt_18'].z3_var), Not(options['vafuzz_opt_6'].z3_var))
   137 bits (3.7%)

5. (options['vafuzz_opt_3'].z3_var)
   131 bits (3.6%)

