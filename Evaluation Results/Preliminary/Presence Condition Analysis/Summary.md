# Presence Condition Based Summary

## djpeg

### PRESENCE CONDITION ANALYSIS SUMMARY
==================================================
Total Conditions Analyzed: 120
Total Bits Discovered: 2899

PERFORMANCE-BASED SUMMARY
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

STRUCTURE-BASED SUMMARY
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

VARIABLE-BASED SUMMARY
======================

1. Multi: default_settings_for_all, options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_14, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(default_settings_for_all, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0), options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_0'].z3_var == 47, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_21'].z3_var) (0 bits)

2. Multi: default_settings_for_all, options, vafuzz_opt_0, vafuzz_opt_13, vafuzz_opt_9, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_13'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 44)), default_settings_for_all) (0 bits)

3. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_14, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_18, vafuzz_opt_2, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_8, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_0'].z3_var == 3.926337, options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_16'].z3_var == 42.941404, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_10'].z3_var), (Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)), Not(options['vafuzz_opt_9'].z3_var)) (0 bits)

4. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_1, vafuzz_opt_13, vafuzz_opt_14, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_18, vafuzz_opt_19, vafuzz_opt_2, vafuzz_opt_20, vafuzz_opt_21, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_14'].z3_var), Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var), (Not(options['vafuzz_opt_16'].z3_var == 39.328529)), Not(options['vafuzz_opt_19'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 44))) (0 bits)

5. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_10, vafuzz_opt_14, vafuzz_opt_15, vafuzz_opt_16, vafuzz_opt_2, vafuzz_opt_20, vafuzz_opt_4, vafuzz_opt_5, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_16'].z3_var == 62.238665, options['vafuzz_opt_20'].z3_var, Not(options['vafuzz_opt_10'].z3_var), (Not(options['vafuzz_opt_15'].z3_var == 4)), Not(options['vafuzz_opt_14'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 34))) (0 bits)

6. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_10, vafuzz_opt_3, vafuzz_opt_6, vafuzz_opt_8, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_10'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 41))) (0 bits)

7. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_11, vafuzz_opt_11_choice_2, vafuzz_opt_12, vafuzz_opt_12_choice_1, vafuzz_opt_2, vafuzz_opt_8, z3_choices, z3_var
   Total Bits: 4 (0.1%)
   Conditions: 1
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_2), options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1), options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var == 44) (4 bits)

8. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_11, vafuzz_opt_11_choice_2, vafuzz_opt_12, vafuzz_opt_12_choice_1, vafuzz_opt_8, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_2, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, Not(options['vafuzz_opt_1'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 44))) (0 bits)

9. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_14, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_18, vafuzz_opt_19, vafuzz_opt_2, vafuzz_opt_20, vafuzz_opt_21, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, z3_var
   Total Bits: 3 (0.1%)
   Conditions: 2
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_16'].z3_var == 39.328529, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_6'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 44))) (3 bits)
   - And(options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_7'].z3_var), (Not(options['vafuzz_opt_16'].z3_var == 39.328529)), Not(options['vafuzz_opt_19'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 44))) (0 bits)

10. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_18, vafuzz_opt_19, vafuzz_opt_2, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, z3_var
   Total Bits: 9 (0.3%)
   Conditions: 1
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_16'].z3_var == 85.131259, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 44))) (9 bits)

11. Multi: options, vafuzz_opt_0, vafuzz_opt_1, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(Not(options['vafuzz_opt_5'].z3_var), options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_0'].z3_var == 69) (0 bits)

12. Multi: options, vafuzz_opt_0, vafuzz_opt_1, z3_var
   Total Bits: 1463 (50.5%)
   Conditions: 4
   - And(options['vafuzz_opt_1'].z3_var, options['vafuzz_opt_0'].z3_var == 44) (1411 bits)
   - And(options['vafuzz_opt_1'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 44))) (52 bits)
   - And(options['vafuzz_opt_0'].z3_var == 74, options['vafuzz_opt_1'].z3_var) (0 bits)
   ... and 1 more

13. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_11, vafuzz_opt_11_choice_0, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_13, vafuzz_opt_14, vafuzz_opt_15, vafuzz_opt_2, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 2 (0.1%)
   Conditions: 1
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, options['vafuzz_opt_13'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_15'].z3_var == 98.776969, (Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)), Not(options['vafuzz_opt_21'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 74)), Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_9'].z3_var)) (2 bits)

14. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_11, vafuzz_opt_11_choice_0, vafuzz_opt_12, vafuzz_opt_12_choice_1, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_18, vafuzz_opt_19, vafuzz_opt_20, vafuzz_opt_21, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, options['vafuzz_opt_16'].z3_var == 7.778728, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 75))) (0 bits)

15. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_14, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 55 (1.9%)
   Conditions: 25
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_0'].z3_var == 22, options['vafuzz_opt_9'].z3_var, Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_21'].z3_var)) (42 bits)
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_9'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 33))) (5 bits)
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_21'].z3_var, options['vafuzz_opt_0'].z3_var == 74, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_9'].z3_var, Not(options['vafuzz_opt_6'].z3_var)) (3 bits)
   ... and 22 more

16. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_0, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_10'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 65)), options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (0 bits)

17. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_2, vafuzz_opt_14, vafuzz_opt_17, vafuzz_opt_20, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_4'].z3_var), Not(options['vafuzz_opt_9'].z3_var), Not(options['vafuzz_opt_10'].z3_var), Not(options['vafuzz_opt_14'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 33))) (0 bits)

18. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_12, vafuzz_opt_12_choice_2, vafuzz_opt_14, vafuzz_opt_21, vafuzz_opt_3, vafuzz_opt_4, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_4'].z3_var, options['vafuzz_opt_5'].z3_var, options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_21'].z3_var, (Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2)), (Not(options['vafuzz_opt_0'].z3_var == 33))) (0 bits)

19. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_14, vafuzz_opt_15, vafuzz_opt_16, vafuzz_opt_17, vafuzz_opt_20, vafuzz_opt_21, vafuzz_opt_8, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_20'].z3_var, options['vafuzz_opt_21'].z3_var, Not(options['vafuzz_opt_10'].z3_var), (Not(options['vafuzz_opt_16'].z3_var == 20)), (Not(options['vafuzz_opt_15'].z3_var == 4)), (Not(options['vafuzz_opt_0'].z3_var == 34))) (0 bits)

20. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_14, vafuzz_opt_15, vafuzz_opt_16, vafuzz_opt_18, vafuzz_opt_8, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_18'].z3_var, Not(options['vafuzz_opt_10'].z3_var), (Not(options['vafuzz_opt_16'].z3_var == 20)), (Not(options['vafuzz_opt_15'].z3_var == 4)), Not(options['vafuzz_opt_14'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 34))) (1 bits)

21. Multi: options, vafuzz_opt_0, vafuzz_opt_10, vafuzz_opt_14, vafuzz_opt_15, vafuzz_opt_16, z3_var
   Total Bits: 4 (0.1%)
   Conditions: 3
   - And(options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_16'].z3_var == 20, options['vafuzz_opt_15'].z3_var == 4, Not(options['vafuzz_opt_14'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 34))) (3 bits)
   - And(options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_14'].z3_var, options['vafuzz_opt_15'].z3_var == 24.961177, options['vafuzz_opt_16'].z3_var == 52.563347, (Not(options['vafuzz_opt_0'].z3_var == 34))) (1 bits)
   - And(options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_16'].z3_var == 5, options['vafuzz_opt_15'].z3_var == 8, Not(options['vafuzz_opt_14'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 34))) (0 bits)

22. Multi: options, vafuzz_opt_0, vafuzz_opt_10, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 3
   - And(options['vafuzz_opt_0'].z3_var == 65, Not(options['vafuzz_opt_10'].z3_var)) (0 bits)
   - And(options['vafuzz_opt_0'].z3_var == 74, options['vafuzz_opt_10'].z3_var) (0 bits)
   - And(options['vafuzz_opt_10'].z3_var, options['vafuzz_opt_0'].z3_var == 41) (0 bits)

23. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_0, vafuzz_opt_17, vafuzz_opt_8, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, options['vafuzz_opt_17'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 69))) (0 bits)

24. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_0, vafuzz_opt_2, vafuzz_opt_3, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 6
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_5'].z3_var), (Not(options['vafuzz_opt_0'].z3_var == 74))) (0 bits)
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, options['vafuzz_opt_0'].z3_var == 51, options['vafuzz_opt_3'].z3_var, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_5'].z3_var)) (0 bits)
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_0, options['vafuzz_opt_0'].z3_var == 58, Not(options['vafuzz_opt_6'].z3_var), Not(options['vafuzz_opt_7'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_5'].z3_var)) (0 bits)
   ... and 3 more

25. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_1, vafuzz_opt_13, vafuzz_opt_5, vafuzz_opt_8, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_13'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 74)), (Not(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1)), options['vafuzz_opt_5'].z3_var) (0 bits)

26. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_1, vafuzz_opt_13, vafuzz_opt_8, vafuzz_opt_9, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_8'].z3_var, options['vafuzz_opt_9'].z3_var, options['vafuzz_opt_13'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 74)), (Not(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1))) (0 bits)

27. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_1, vafuzz_opt_2, vafuzz_opt_3, vafuzz_opt_5, vafuzz_opt_6, vafuzz_opt_7, z3_choices, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_6'].z3_var, options['vafuzz_opt_7'].z3_var, Not(options['vafuzz_opt_2'].z3_var), Not(options['vafuzz_opt_3'].z3_var), Not(options['vafuzz_opt_5'].z3_var), (Not(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1)), (Not(options['vafuzz_opt_0'].z3_var == 74))) (1 bits)

28. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_1, vafuzz_opt_2, vafuzz_opt_3, vafuzz_opt_5, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_2'].z3_var, options['vafuzz_opt_3'].z3_var, options['vafuzz_opt_5'].z3_var, (Not(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1)), (Not(options['vafuzz_opt_0'].z3_var == 74))) (0 bits)

29. Multi: options, vafuzz_opt_0, vafuzz_opt_11, vafuzz_opt_11_choice_1, z3_choices, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 2
   - And(Not(options['vafuzz_opt_0'].z3_var == 74), options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1)) (1 bits)
   - And(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_1, options['vafuzz_opt_0'].z3_var == 74) (0 bits)

30. Multi: options, vafuzz_opt_0, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_17, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_17'].z3_var, (Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)), options['vafuzz_opt_0'].z3_var == 65) (0 bits)

31. Multi: options, vafuzz_opt_0, vafuzz_opt_12, vafuzz_opt_12_choice_0, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(Not(options['vafuzz_opt_0'].z3_var == 69), options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (0 bits)

32. Multi: options, vafuzz_opt_0, vafuzz_opt_12, vafuzz_opt_12_choice_1, z3_choices, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 3
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, options['vafuzz_opt_0'].z3_var == 74) (1 bits)
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, (Not(options['vafuzz_opt_0'].z3_var == 44))) (0 bits)
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1, options['vafuzz_opt_0'].z3_var == 44) (0 bits)

33. Multi: options, vafuzz_opt_0, vafuzz_opt_12, vafuzz_opt_12_choice_2, vafuzz_opt_7, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2, (Not(options['vafuzz_opt_0'].z3_var == 44)), options['vafuzz_opt_7'].z3_var) (0 bits)

34. Multi: options, vafuzz_opt_0, vafuzz_opt_12, vafuzz_opt_12_choice_2, z3_choices, z3_var
   Total Bits: 14 (0.5%)
   Conditions: 4
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2, (Not(options['vafuzz_opt_0'].z3_var == 33))) (7 bits)
   - And(Not(options['vafuzz_opt_0'].z3_var == 33), options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2)) (6 bits)
   - And(Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2), options['vafuzz_opt_0'].z3_var == 33) (1 bits)
   ... and 1 more

35. Multi: options, vafuzz_opt_0, vafuzz_opt_15, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(Not(options['vafuzz_opt_15'].z3_var == 4), options['vafuzz_opt_0'].z3_var == 34) (0 bits)

36. Multi: options, vafuzz_opt_0, vafuzz_opt_19, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_19'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 75))) (0 bits)

37. Multi: options, vafuzz_opt_0, vafuzz_opt_20, z3_var
   Total Bits: 7 (0.2%)
   Conditions: 3
   - And(options['vafuzz_opt_20'].z3_var, (Not(options['vafuzz_opt_0'].z3_var == 34))) (7 bits)
   - And(options['vafuzz_opt_0'].z3_var == 24, Not(options['vafuzz_opt_20'].z3_var)) (0 bits)
   - And(options['vafuzz_opt_0'].z3_var == 52, Not(options['vafuzz_opt_20'].z3_var)) (0 bits)

38. Multi: options, vafuzz_opt_0, vafuzz_opt_6, z3_var
   Total Bits: 42 (1.4%)
   Conditions: 1
   - And(options['vafuzz_opt_0'].z3_var == 53, options['vafuzz_opt_6'].z3_var) (42 bits)

39. Multi: options, vafuzz_opt_0, z3_var
   Total Bits: 1132 (39.0%)
   Conditions: 21
   - Not(options['vafuzz_opt_0'].z3_var == 44) (926 bits)
   - (options['vafuzz_opt_0'].z3_var == 69) (93 bits)
   - (options['vafuzz_opt_0'].z3_var == 22) (70 bits)
   ... and 18 more

40. Multi: options, vafuzz_opt_11, vafuzz_opt_11_choice_2, vafuzz_opt_12, vafuzz_opt_12_choice_0, z3_choices, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_11'].z3_var == options['vafuzz_opt_11'].z3_choices.vafuzz_opt_11_choice_2, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (0 bits)

41. Multi: options, vafuzz_opt_12, vafuzz_opt_12_choice_0, vafuzz_opt_17, z3_choices, z3_var
   Total Bits: 125 (4.3%)
   Conditions: 2
   - And(options['vafuzz_opt_17'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (125 bits)
   - And(options['vafuzz_opt_17'].z3_var, (Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0))) (0 bits)

42. Multi: options, vafuzz_opt_12, vafuzz_opt_12_choice_0, z3_choices, z3_var
   Total Bits: 3 (0.1%)
   Conditions: 3
   - options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0 (2 bits)
   - Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0) (1 bits)
   - And(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0) (0 bits)

43. Multi: options, vafuzz_opt_12, vafuzz_opt_12_choice_1, vafuzz_opt_7, z3_choices, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_7'].z3_var, options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_1)) (1 bits)

44. Multi: options, vafuzz_opt_12, vafuzz_opt_12_choice_2, z3_choices, z3_var
   Total Bits: 17 (0.6%)
   Conditions: 1
   - Not(options['vafuzz_opt_12'].z3_var == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2) (17 bits)

45. Multi: options, vafuzz_opt_4, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - (options['vafuzz_opt_4'].z3_var) (0 bits)

46. Multi: options, vafuzz_opt_5, vafuzz_opt_6, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - And(options['vafuzz_opt_6'].z3_var, Not(options['vafuzz_opt_5'].z3_var)) (0 bits)

47. Multi: options, vafuzz_opt_5, z3_var
   Total Bits: 10 (0.3%)
   Conditions: 2
   - (options['vafuzz_opt_5'].z3_var) (10 bits)
   - Not(options['vafuzz_opt_5'].z3_var) (0 bits)

48. Multi: options, vafuzz_opt_6, z3_var
   Total Bits: 0 (0.0%)
   Conditions: 1
   - Not(options['vafuzz_opt_6'].z3_var) (0 bits)

49. Multi: options, vafuzz_opt_7, z3_var
   Total Bits: 3 (0.1%)
   Conditions: 1
   - (options['vafuzz_opt_7'].z3_var) (3 bits)

50. Multi: options, vafuzz_opt_8, z3_var
   Total Bits: 1 (0.0%)
   Conditions: 1
   - (options['vafuzz_opt_8'].z3_var) (1 bits)

51. Single: default_settings_for_all
   Total Bits: 0 (0.0%)
   Conditions: 1
   - default_settings_for_all (0 bits)

TOP 5 PERFORMING CONDITIONS
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
