# INSTRUCTIONS

- The first part of this document contains our analysis on coverage gained per mutator.
  - Each table here represents a target program that was run using VAFuzz.
  - We randomly selected 1 out of the 5 trials to conduct our preliminary analysis.
  
- The second part consists of coverage gained per presence condition.
  - We provide an analysis for each target program.
  - Each analysis is divided as follows:
     1. Performance Based Summary
     2. Structure Based Summary
     3. Top 5 Performing Conditions

# MUTATOR ANALYSIS SUMMARY

**djpeg**

| Mutator               | New Bits Discovered | Percentage Breakdown |
|-----------------------|---------------------|-----------------------|
| Mutator 1 | 287                 | 9.9%                  |
| Mutator 2 | 1810                | 62.4%                 |
| Mutator 3     | 802                 | 27.7%                 |
| **Total**             | **2899**            | **100%**              |

**jpegtran**

| Mutator               | New Bits Discovered | Percentage Breakdown |
|-----------------------|---------------------|-----------------------|
| Mutator 1 | 953                 | 17.5%                 |
| Mutator 2 | 3820                | 70.2%                 |
| Mutator 3     | 672                 | 12.3%                 |
| **Total**             | **5445**            | **100%**              |

**xmllint**

| Mutator               | New Bits Discovered | Percentage Breakdown |
|-----------------------|---------------------|-----------------------|
| Mutator 1 | 460                 | 9.2%                  |
| Mutator 1  | 525                 | 10.5%                 |
| Mutator 2      | 4035                | 80.4%                 |
| **Total**             | **5020**            | **100%**              |

**readelf**

| Mutator               | New Bits Discovered | Percentage Breakdown |
|-----------------------|---------------------|-----------------------|
| Mutator 1 | 937                 | 25.5%                 |
| Mutator 2 | 952                 | 25.9%                 |
| Mutator 3     | 1782                | 48.5%                 |
| **Total**             | **3671**            | **100%**              |


# PRESENCE CONDITION ANALYSIS SUMMARY

## djpeg
==================================================

Total Conditions Analyzed: 120
Total Bits Discovered: 2899

### PERFORMANCE-BASED SUMMARY
=============================

1. High Performance (≥50 bits)
   Total Bits: 2677 (92.3%)
   Conditions: 6
   - And(optimize, copy == 44) (1411 bits)
   - Not(copy == 44) (926 bits)
   - And(debug, maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (125 bits)
   ... and 3 more

2. Low Performance (<10 bits)
   Total Bits: 79 (2.7%)
   Conditions: 108
   - And(optimize, progressive, grayscale, perfect, rotate, transpose, verbose == 85.131259, debug, options['vafuzz_opt_18'].z3_var, options['vafuzz_opt_19'].z3_var, (Not(copy == 44))) (9 bits)
   - And(maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2, (Not(copy == 33))) (7 bits)
   - And(options['vafuzz_opt_20'].z3_var, (Not(copy == 34))) (7 bits)
   ... and 105 more

3. Medium Performance (10-49 bits)
   Total Bits: 143 (4.9%)
   Conditions: 6
   - And(copy == 53, rotate) (42 bits)
   - And(flip, perfect, report, transpose, arithmetic, maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0, rotate, copy == 22, trim, Not(grayscale), Not(options['vafuzz_opt_21'].z3_var)) (42 bits)
   - Not(copy == 33) (22 bits)
   ... and 3 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 1733 (59.8%)
   Conditions: 89
   - And(optimize, copy == 44) (1411 bits)
   - And(debug, maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0)) (125 bits)
   - And(optimize, (Not(copy == 44))) (52 bits)
   ... and 86 more

2. Equality Check
   Total Bits: 167 (5.8%)
   Conditions: 12
   - (copy == 69) (93 bits)
   - (copy == 22) (70 bits)
   - maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0 (2 bits)
   ... and 9 more

3. Negated
   Total Bits: 985 (34.0%)
   Conditions: 14
   - Not(copy == 44) (926 bits)
   - Not(copy == 33) (22 bits)
   - Not(maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_2) (17 bits)
   ... and 11 more

4. Simple Boolean
   Total Bits: 14 (0.5%)
   Conditions: 5
   - (perfect) (10 bits)
   - (transpose) (3 bits)
   - (transverse) (1 bits)
   ... and 2 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(optimize, copy == 44)
   1411 bits (48.7%)

2. Not(copy == 44)
   926 bits (31.9%)

3. And(debug, maxmemory == options['vafuzz_opt_12'].z3_choices.vafuzz_opt_12_choice_0))
   125 bits (4.3%)

4. (copy == 69)
   93 bits (3.2%)

5. (copy == 22)
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
   - And(copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, maxmemory == 48) (3132 bits)
   - Not(maxscans == 94) (1176 bits)
   - And(Not(maxscans == 94), strict, copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (612 bits)
   ... and 2 more

2. Low Performance (<10 bits)
   Total Bits: 70 (1.3%)
   Conditions: 107
   - And(restart == 34, maxscans == 86, copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_3)) (6 bits)
   - And(restart == 39, verbose, Not(debug)) (6 bits)
   - And(transverse, (Not(copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0))) (5 bits)
   ... and 104 more

3. Medium Performance (10-49 bits)
   Total Bits: 208 (3.8%)
   Conditions: 8
   - (restart == 46) (47 bits)
   - And(Not(maxmemory == 48), copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (39 bits)
   - (restart == 7) (29 bits)
   ... and 5 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 4012 (73.7%)
   Conditions: 93
   - And(copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, maxmemory == 48) (3132 bits)
   - And(Not(maxscans == 94), strict, copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0)) (612 bits)
   - And(progressive, restart == 7) (108 bits)
   ... and 90 more

2. Equality Check
   Total Bits: 80 (1.5%)
   Conditions: 11
   - (restart == 46) (47 bits)
   - (restart == 7) (29 bits)
   - (copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_3) (4 bits)
   ... and 8 more

3. Negated
   Total Bits: 1336 (24.5%)
   Conditions: 13
   - Not(maxscans == 94) (1176 bits)
   - Not(restart == 7) (139 bits)
   - Not(rotate == options['vafuzz_opt_6'].z3_choices.vafuzz_opt_6_choice_2) (14 bits)
   ... and 10 more

4. Simple Boolean
   Total Bits: 17 (0.3%)
   Conditions: 3
   - default_settings_for_all (17 bits)
   - (optimize) (0 bits)
   - (arithmetic) (0 bits)

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0, maxmemory == 48)
   3132 bits (57.5%)

2. Not(maxscans == 94)
   1176 bits (21.6%)

3. And(Not(maxscans == 94), strict, copy == options['vafuzz_opt_0'].z3_choices.vafuzz_opt_0_choice_0))
   612 bits (11.2%)

4. Not(restart == 7)
   139 bits (2.6%)

5. And(progressive, restart == 7)
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
   - And(noblanks, html) (317 bits)
   - And(debug, debugent, recover, noent, noenc, load-trace, nocompact, htmlout, nowrap, valid, timing, insert, html, nodefdtd, push, memory, nowarning, noblanks, format, dropdtd, exc-c14n, catalogs, nocatalogs, auto, nofixup-base-uris, stream, walker, chkregister, oldxml10) (200 bits)
   ... and 7 more

2. Low Performance (<10 bits)
   Total Bits: 126 (2.5%)
   Conditions: 79
   - And(debug, copy, recover, noent, noout, nonet, valid, timing, push, memory, dropdtd, c14n, nocatalogs, xinclude, walker, sax1, Not(debugent), Not(huge), Not(nocompact), Not(htmlout), Not(nowrap), Not(insert), Not(html), Not(xmlout), Not(nodefdtd), Not(nowarning), Not(noblanks), Not(catalogs), Not(stream), Not(sax), Not(noenc), Not(postvalid), Not(format), Not(noxincludenode), Not(oldxml10), Not(c14n11), Not(exc-c14n), Not(nsclean), Not(auto)) (9 bits)
   - And(nocompact, debugent) (9 bits)
   - And(push, nodefdtd, oldxml10, debug, insert, format, nonet, dropdtd, memory, recover, Not(htmlout), Not(debugent), Not(chkregister), Not(catalogs)) (9 bits)
   ... and 76 more

3. Medium Performance (10-49 bits)
   Total Bits: 491 (9.8%)
   Conditions: 25
   - And(html, c14n11, exc-c14n, nsclean, catalogs, nocatalogs, auto, Not(push)) (41 bits)
   - And(debug, debugent, copy, recover, huge, noent, nonet, nocompact, htmlout, nowrap, valid, insert, html, xmlout, nodefdtd, memory, nowarning, noblanks, dropdtd, c14n, catalogs, nocatalogs, stream, sax1, sax, Not(noenc), Not(postvalid), Not(format), Not(noxincludenode), Not(oldxml10), Not(c14n11), Not(exc-c14n), Not(nsclean), Not(auto), Not(push)) (37 bits)
   - And(debug, debugent, copy, recover, huge, noent, load-trace, nonet, valid, insert, html, nodefdtd, auto, oldxml10, Not(noenc), Not(nocompact), Not(postvalid), Not(xmlout), Not(memory), Not(format), Not(noxincludenode), Not(c14n11), Not(exc-c14n), Not(nsclean), Not(catalogs), Not(nocatalogs), Not(push)) (35 bits)
   ... and 22 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 1533 (30.5%)
   Conditions: 110
   - And(noblanks, html) (317 bits)
   - And(debug, debugent, recover, noent, noenc, load-trace, nocompact, htmlout, nowrap, valid, timing, insert, html, nodefdtd, push, memory, nowarning, noblanks, format, dropdtd, exc-c14n, catalogs, nocatalogs, auto, nofixup-base-uris, stream, walker, chkregister, oldxml10) (200 bits)
   - And(copy, recover, noent, noenc, load-trace, nocompact, htmlout, nowrap, valid, timing, insert, html, nodefdtd, push, memory, nowarning, noblanks, dropdtd, c14n11, exc-c14n, nsclean, testIO, nocatalogs, auto, oldxml10) (189 bits)
   ... and 107 more

2. Simple Boolean
   Total Bits: 3487 (69.5%)
   Conditions: 4
   - (null) (3258 bits)
   - (push) (101 bits)
   - (valid) (76 bits)
   ... and 1 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. (null)
   3258 bits (64.9%)

2. And(noblanks, html)
   317 bits (6.3%)

3. And(debug, debugent, recover, noent, noenc, load-trace, nocompact, htmlout, nowrap, valid, timing, insert, html, nodefdtd, push, memory, nowarning, noblanks, format, dropdtd, exc-c14n, catalogs, nocatalogs, auto, nofixup-base-uris, stream, walker, chkregister, oldxml10)
   200 bits (4.0%)

4. And(copy, recover, noent, noenc, load-trace, nocompact, htmlout, nowrap, valid, timing, insert, html, nodefdtd, push, memory, nowarning, noblanks, dropdtd, c14n11, exc-c14n, nsclean, testIO, nocatalogs, auto, oldxml10)
   189 bits (3.8%)

5. (push)
   101 bits (2.0%)
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
   - And(sym-base=0, a) (588 bits)
   - And(h, a, sections, segments, c, l, z, sym-base=0, no-recurse-limit, recurse-limit, S, Not(g), Not(t)) (173 bits)
   - And(e, s, lto-syms, sym-base=8, Not(h), Not(sections), Not(a), Not(P), Not(c), Not(segments), Not(l), Not(z), Not(sym-base=0), Not(t), Not(recurse-limit), Not(S), Not(A), Not(no-recurse-limit), Not(g)) (138 bits)
   ... and 15 more

2. Low Performance (<10 bits)
   Total Bits: 257 (7.0%)
   Conditions: 108
   - And(h, lto-syms, segments, P, l, sym-base=0, t, recurse-limit, S, g, T, sections, a, no-recurse-limit, sym-base=8, A, Not(z), Not(dyn-syms), Not(c)) (9 bits)
   - Not(lto-syms) (9 bits)
   - And(a, h, no-demangle, recurse-limit, r, A, c, I, W, T, Not(sym-base=8), Not(L), Not(g), Not(sections), Not(lto-syms)) (8 bits)
   ... and 105 more

3. Medium Performance (10-49 bits)
   Total Bits: 1286 (35.0%)
   Conditions: 57
   - And(u, I, sections, sym-base=10, l, n, z, sym-base=8, g, Not(dyn-syms), Not(d)) (49 bits)
   - And(sym-base=16, no-recurse-limit, z, I, T, Not(h), Not(S), Not(sections), Not(g), Not(dyn-syms), Not(lto-syms), Not(sym-base=8), Not(sym-base=10), Not(no-demangle), Not(u), Not(d), Not(a), Not(P), Not(c), Not(segments), Not(l), Not(sym-base=0), Not(recurse-limit), Not(A), Not(t)) (46 bits)
   - And(h, l, segments, sections, g, t, sym-base=8, no-demangle, no-recurse-limit, u, d, Not(r), Not(lto-syms), Not(P), Not(n), Not(sym-base=0), Not(recurse-limit), Not(S), Not(sym-base=16), Not(s), Not(a), Not(sym-base=10), Not(c), Not(z), Not(A), Not(dyn-syms), Not(e), Not(D)) (45 bits)
   ... and 54 more

### STRUCTURE-BASED SUMMARY
===========================

1. Conjunction (AND)
   Total Bits: 3128 (85.2%)
   Conditions: 171
   - And(sym-base=0, a) (588 bits)
   - And(h, a, sections, segments, c, l, z, sym-base=0, no-recurse-limit, recurse-limit, S, Not(g), Not(t)) (173 bits)
   - And(e, s, lto-syms, sym-base=8, Not(h), Not(sections), Not(a), Not(P), Not(c), Not(segments), Not(l), Not(z), Not(sym-base=0), Not(t), Not(recurse-limit), Not(S), Not(A), Not(no-recurse-limit), Not(g)) (138 bits)
   ... and 168 more

2. Negated
   Total Bits: 41 (1.1%)
   Conditions: 5
   - Not(a) (15 bits)
   - Not(r) (13 bits)
   - Not(lto-syms) (9 bits)
   ... and 2 more

3. Simple Boolean
   Total Bits: 502 (13.7%)
   Conditions: 7
   - (segments) (131 bits)
   - (a) (103 bits)
   - (I) (91 bits)
   ... and 4 more

### TOP 5 PERFORMING CONDITIONS
==============================
1. And(sym-base=0, a)
   588 bits (16.0%)

2. And(h, a, sections, segments, c, l, z, sym-base=0, no-recurse-limit, recurse-limit, S, Not(g), Not(t))
   173 bits (4.7%)

3. And(e, s, lto-syms, sym-base=8, Not(h), Not(sections), Not(a), Not(P), Not(c), Not(segments), Not(l), Not(z), Not(sym-base=0), Not(t), Not(recurse-limit), Not(S), Not(A), Not(no-recurse-limit), Not(g))
   138 bits (3.8%)

4. And(h, a, sections, P, c, segments, l, z, sym-base=0, t, S, A, Not(recurse-limit), Not(no-recurse-limit), Not(g))
   137 bits (3.7%)

5. (segments)
   131 bits (3.6%)
