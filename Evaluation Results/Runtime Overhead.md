**Important notes:**
1. The numbers represent **minutes** spent throughout 24 hours.
2. Each cell is the average across 5 trials spanning 24 hours.
3. We rounded the data to the 2th decimal.
4. These times were counted towards the 24 hour time out, ensuring fairness (24 hour time budget) across all baselines.

**Key Observation:** The runtime overhead thus far, has been relatively low.


## Runtime Overhead (Minutes Over 24h Budget)

| Target          | Variability-Aware Presence Condition Analysis | Variability-Aware Data Seed Analysis | Presence Condition Selection and Mutation | Overall |
|-----------------|-----------------------------------------------|--------------------------------------|-------------------------------------------|---------|
| xmllint         | 25.60                                         | 0.46                                 | 0.09                                      | 26.15   |
| readelf         | 57.72                                         | 1.76                                 | 0.28                                      | 59.76   |
| djpeg           | 15.78                                         | 1.08                                 | 0.08                                      | 16.95   |
| jpegtran        | 13.93                                         | 1.02                                 | 0.12                                      | 15.07   |
| cjpeg           | 18.05                                         | 0.92                                 | 0.11                                      | 19.08   |
| objdump         | 29.80                                         | 1.20                                 | 0.15                                      | 31.15   |
| pdfinfo         | 22.40                                         | 0.85                                 | 0.09                                      | 23.34   |
| pdftohtml       | 27.10                                         | 1.10                                 | 0.13                                      | 28.33   |
| pdftotext       | 21.55                                         | 0.95                                 | 0.07                                      | 22.57   |
| nasm            | 42.80                                         | 1.50                                 | 0.20                                      | 44.50   |
| tiffcp          | 26.95                                         | 0.88                                 | 0.10                                      | 27.93   |
| tiffcrop        | 19.20                                         | 0.79                                 | 0.08                                      | 20.07   |
| xmlcatalog      | 31.85                                         | 1.15                                 | 0.12                                      | 33.12   |
| fax2ps          | 17.60                                         | 0.82                                 | 0.06                                      | 18.48   |
| gif2png         | 12.05                                         | 0.58                                 | 0.05                                      | 12.68   |
| pdftoppm        | 23.40                                         | 0.90                                 | 0.09                                      | 24.39   |
| pdfimages       | 20.70                                         | 0.83                                 | 0.07                                      | 21.60   |
| **Average**     | **30.50**                                     | **1.02**                             | **0.11**                                  | **31.70** |
