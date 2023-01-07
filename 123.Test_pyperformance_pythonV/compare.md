### 0.Source
|    | Task                    | 3.7.16               | 3.8.0                | 3.9.0                | 3.10.0               | 3.11.0               | 3.11.1               |
|---:|:------------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
|  0 | 2to3                    | 775 ms +- 48 ms      | 826 ms +- 36 ms      | 795 ms +- 89 ms      | 766 ms +- 17 ms      | 667 ms +- 101 ms     | 594 ms +- 31 ms      |
|  1 | async_generators        | 665 ms +- 19 ms      | 759 ms +- 28 ms      | 771 ms +- 131 ms     | 727 ms +- 30 ms      | 744 ms +- 195 ms     | 544 ms +- 24 ms      |
|  2 | async_tree_none         | 1.49 sec +- 0.10 sec | 1.65 sec +- 0.10 sec | 1.67 sec +- 0.34 sec | 1.58 sec +- 0.06 sec | 1.38 sec +- 0.22 sec | 1.19 sec +- 0.04 sec |
|  3 | async_tree_cpu_io_mixed | 2.07 sec +- 0.10 sec | 2.28 sec +- 0.12 sec | 2.85 sec +- 0.64 sec | 2.21 sec +- 0.12 sec | 1.81 sec +- 0.09 sec | 1.79 sec +- 0.07 sec |
|  4 | async_tree_io           | 3.49 sec +- 0.14 sec | 3.68 sec +- 0.21 sec | 4.41 sec +- 0.79 sec | 3.63 sec +- 0.22 sec | 2.74 sec +- 0.12 sec | 2.56 sec +- 0.14 sec |
|  5 | async_tree_memoization  | 1.86 sec +- 0.06 sec | 1.99 sec +- 0.15 sec | 1.88 sec +- 0.09 sec | 2.05 sec +- 0.13 sec | 1.64 sec +- 0.09 sec | 1.71 sec +- 0.20 sec |
|  6 | chameleon               | 28.3 ms +- 0.4 ms    | 29.9 ms +- 2.1 ms    | 28.1 ms +- 2.2 ms    | 25.9 ms +- 0.4 ms    | 22.0 ms +- 1.5 ms    | 21.8 ms +- 0.7 ms    |
|  7 | chaos                   | 284 ms +- 16 ms      | 288 ms +- 11 ms      | 280 ms +- 11 ms      | 268 ms +- 33 ms      | 197 ms +- 10 ms      | 204 ms +- 45 ms      |
|  8 | bench_mp_pool           | 114 ms +- 3 ms       | 22.6 ms +- 3.3 ms    | 22.7 ms +- 2.6 ms    | 23.1 ms +- 3.6 ms    | 23.6 ms +- 5.0 ms    | 22.4 ms +- 2.3 ms    |
|  9 | bench_thread_pool       | 108 ms +- 4 ms       | 3.47 ms +- 0.43 ms   | 3.50 ms +- 0.36 ms   | 3.43 ms +- 0.32 ms   | 3.34 ms +- 0.25 ms   | 3.35 ms +- 0.31 ms   |
| 10 | coroutines              | 72.5 ms +- 2.6 ms    | 78.2 ms +- 3.8 ms    | 76.1 ms +- 3.8 ms    | 63.3 ms +- 2.8 ms    | 58.9 ms +- 1.5 ms    | 58.4 ms +- 1.4 ms    |
| 11 | coverage                | 94.3 ms +- 1.7 ms    | 94.3 ms +- 5.2 ms    | 99.1 ms +- 2.2 ms    | 114 ms +- 3 ms       | 208 ms +- 11 ms      | 204 ms +- 10 ms      |
| 12 | crypto_pyaes            | 233 ms +- 3 ms       | 251 ms +- 47 ms      | 238 ms +- 8 ms       | 237 ms +- 9 ms       | 178 ms +- 12 ms      | 183 ms +- 8 ms       |
| 13 | deepcopy                | 1.40 ms +- 0.06 ms   | 1.44 ms +- 0.10 ms   | 1.35 ms +- 0.09 ms   | 1.26 ms +- 0.06 ms   | 1.07 ms +- 0.07 ms   | 1.06 ms +- 0.07 ms   |
| 14 | deepcopy_reduce         | 12.8 us +- 0.7 us    | 12.6 us +- 0.3 us    | 11.6 us +- 0.5 us    | 11.2 us +- 0.6 us    | 9.36 us +- 0.12 us   | 9.52 us +- 0.34 us   |
| 15 | deepcopy_memo           | 168 us +- 8 us       | 204 us +- 18 us      | 162 us +- 7 us       | 156 us +- 10 us      | 125 us +- 8 us       | 124 us +- 6 us       |
| 16 | deltablue               | 17.5 ms +- 1.1 ms    | 17.2 ms +- 0.8 ms    | 17.2 ms +- 1.1 ms    | 15.5 ms +- 0.4 ms    | 10.4 ms +- 0.4 ms    | 10.4 ms +- 1.6 ms    |
| 17 | django_template         | 146 ms +- 3 ms       | 149 ms +- 6 ms       | 142 ms +- 5 ms       | 134 ms +- 8 ms       | 108 ms +- 11 ms      | 112 ms +- 34 ms      |
| 18 | docutils                | 7.46 sec +- 0.33 sec | 7.61 sec +- 1.25 sec | 7.05 sec +- 0.32 sec | 7.32 sec +- 0.29 sec | 6.08 sec +- 0.18 sec | 6.50 sec +- 0.17 sec |
| 19 | dulwich_log             | 189 ms +- 29 ms      | 169 ms +- 8 ms       | 167 ms +- 17 ms      | 160 ms +- 10 ms      | 137 ms +- 8 ms       | 148 ms +- 9 ms       |
| 20 | fannkuch                | 1.39 sec +- 0.05 sec | 1.28 sec +- 0.03 sec | 1.25 sec +- 0.04 sec | 1.23 sec +- 0.03 sec | 972 ms +- 16 ms      | 1.13 sec +- 0.64 sec |
| 21 | float                   | 268 ms +- 11 ms      | 275 ms +- 12 ms      | 272 ms +- 13 ms      | 248 ms +- 6 ms       | 193 ms +- 8 ms       | 201 ms +- 13 ms      |
| 22 | generators              | 89.4 ms +- 5.1 ms    | 86.1 ms +- 6.7 ms    | 84.0 ms +- 3.2 ms    | 82.2 ms +- 4.2 ms    | 76.8 ms +- 4.5 ms    | 89.9 ms +- 25.4 ms   |
| 23 | genshi_text             | 95.6 ms +- 8.4 ms    | 90.7 ms +- 10.5 ms   | 86.4 ms +- 4.3 ms    | 78.9 ms +- 1.9 ms    | 63.5 ms +- 3.3 ms    | 71.5 ms +- 15.8 ms   |
| 24 | genshi_xml              | 189 ms +- 9 ms       | 180 ms +- 9 ms       | 173 ms +- 8 ms       | 167 ms +- 7 ms       | 142 ms +- 3 ms       | 151 ms +- 18 ms      |
| 25 | go                      | 611 ms +- 27 ms      | 585 ms +- 15 ms      | 590 ms +- 63 ms      | 521 ms +- 11 ms      | 376 ms +- 11 ms      | 380 ms +- 34 ms      |
| 26 | hexiom                  | 24.9 ms +- 0.5 ms    | 24.2 ms +- 1.0 ms    | 22.2 ms +- 0.9 ms    | 21.3 ms +- 1.1 ms    | 16.2 ms +- 0.6 ms    | 16.1 ms +- 1.3 ms    |
| 27 | html5lib                | 211 ms +- 15 ms      | 201 ms +- 11 ms      | 200 ms +- 14 ms      | 186 ms +- 14 ms      | 160 ms +- 16 ms      | 159 ms +- 17 ms      |
| 28 | json_dumps              | 34.3 ms +- 2.9 ms    | 34.6 ms +- 1.8 ms    | 34.0 ms +- 1.8 ms    | 33.3 ms +- 3.2 ms    | 33.4 ms +- 2.7 ms    | 33.8 ms +- 3.3 ms    |
| 29 | json_loads              | 62.9 us +- 10.9 us   | 61.4 us +- 4.1 us    | 56.7 us +- 2.9 us    | 57.1 us +- 3.2 us    | 56.8 us +- 2.9 us    | 56.5 us +- 1.5 us    |
| 30 | logging_format          | 25.9 us +- 2.0 us    | 24.8 us +- 1.6 us    | 24.2 us +- 0.5 us    | 24.1 us +- 1.2 us    | 20.7 us +- 1.9 us    | 21.7 us +- 6.6 us    |
| 31 | logging_silent          | 467 ns +- 17 ns      | 589 ns +- 216 ns     | 483 ns +- 16 ns      | 458 ns +- 44 ns      | 388 ns +- 10 ns      | 376 ns +- 26 ns      |
| 32 | logging_simple          | 23.4 us +- 2.4 us    | 23.1 us +- 2.5 us    | 22.2 us +- 1.5 us    | 22.1 us +- 1.2 us    | 19.3 us +- 1.9 us    | 18.9 us +- 0.7 us    |
| 33 | mako                    | 44.9 ms +- 2.6 ms    | 42.7 ms +- 0.4 ms    | 39.2 ms +- 1.0 ms    | 36.2 ms +- 0.9 ms    | 26.3 ms +- 5.5 ms    | 25.6 ms +- 1.9 ms    |
| 34 | mdp                     | 8.53 sec +- 0.15 sec | 8.26 sec +- 0.85 sec | 7.80 sec +- 0.07 sec | 7.54 sec +- 0.16 sec | 7.46 sec +- 0.06 sec | 7.20 sec +- 0.07 sec |
| 35 | meteor_contest          | 245 ms +- 25 ms      | 230 ms +- 12 ms      | 215 ms +- 23 ms      | 212 ms +- 4 ms       | 207 ms +- 6 ms       | 207 ms +- 12 ms      |
| 36 | nbody                   | 303 ms +- 9 ms       | 320 ms +- 25 ms      | 311 ms +- 10 ms      | 306 ms +- 11 ms      | 222 ms +- 15 ms      | 212 ms +- 5 ms       |
| 37 | nqueens                 | 261 ms +- 27 ms      | 259 ms +- 11 ms      | 240 ms +- 6 ms       | 241 ms +- 9 ms       | 212 ms +- 9 ms       | 214 ms +- 10 ms      |
| 38 | pathlib                 | 54.4 ms +- 5.5 ms    | 57.7 ms +- 1.8 ms    | 49.4 ms +- 0.8 ms    | 52.4 ms +- 1.2 ms    | 49.2 ms +- 2.0 ms    | 51.5 ms +- 5.8 ms    |
| 39 | pickle                  | 34.4 us +- 2.1 us    | 23.0 us +- 1.9 us    | 22.6 us +- 1.2 us    | 22.5 us +- 5.2 us    | 21.8 us +- 3.5 us    | 20.6 us +- 0.6 us    |
| 40 | pickle_dict             | 147 us +- 8 us       | 70.2 us +- 3.6 us    | 69.0 us +- 2.8 us    | 69.2 us +- 3.0 us    | 64.4 us +- 5.3 us    | 62.9 us +- 3.6 us    |
| 41 | pickle_list             | 18.1 us +- 0.9 us    | 10.5 us +- 0.8 us    | 10.3 us +- 0.5 us    | 10.0 us +- 0.3 us    | 8.67 us +- 0.26 us   | 8.70 us +- 0.54 us   |
| 42 | pickle_pure_python      | 1.29 ms +- 0.04 ms   | 1.45 ms +- 0.15 ms   | 1.32 ms +- 0.04 ms   | 1.25 ms +- 0.02 ms   | 992 us +- 288 us     | 940 us +- 65 us      |
| 43 | pidigits                | 303 ms +- 11 ms      | 288 ms +- 15 ms      | 288 ms +- 23 ms      | 285 ms +- 10 ms      | 289 ms +- 14 ms      | 283 ms +- 8 ms       |
| 44 | pprint_pformat          | 4.76 sec +- 0.14 sec | 4.77 sec +- 0.08 sec | 4.46 sec +- 0.05 sec | 5.80 sec +- 0.09 sec | 4.52 sec +- 0.06 sec | 5.02 sec +- 1.05 sec |
| 45 | pyflate                 | 1.71 sec +- 0.04 sec | 1.67 sec +- 0.04 sec | 1.66 sec +- 0.02 sec | 1.61 sec +- 0.03 sec | 1.22 sec +- 0.09 sec | 1.21 sec +- 0.07 sec |
| 46 | python_startup          | 34.3 ms +- 5.4 ms    | 34.2 ms +- 25.4 ms   | 33.0 ms +- 19.6 ms   | 30.2 ms +- 3.9 ms    | 36.3 ms +- 25.6 ms   | 34.7 ms +- 18.3 ms   |
| 47 | python_startup_no_site  | 18.6 ms +- 9.3 ms    | 17.8 ms +- 12.7 ms   | 16.0 ms +- 2.6 ms    | 15.2 ms +- 1.8 ms    | 19.4 ms +- 2.3 ms    | 19.1 ms +- 1.8 ms    |
| 48 | raytrace                | 1.26 sec +- 0.07 sec | 1.27 sec +- 0.04 sec | 1.26 sec +- 0.12 sec | 1.20 sec +- 0.01 sec | 854 ms +- 30 ms      | 851 ms +- 23 ms      |
| 49 | regex_compile           | 444 ms +- 15 ms      | 411 ms +- 7 ms       | 391 ms +- 7 ms       | 395 ms +- 11 ms      | 318 ms +- 5 ms       | 315 ms +- 9 ms       |
| 50 | regex_dna               | 554 ms +- 25 ms      | 565 ms +- 17 ms      | 560 ms +- 22 ms      | 538 ms +- 14 ms      | 453 ms +- 14 ms      | 456 ms +- 15 ms      |
| 51 | regex_effbot            | 11.5 ms +- 1.0 ms    | 11.6 ms +- 0.2 ms    | 11.5 ms +- 1.0 ms    | 11.4 ms +- 0.3 ms    | 9.88 ms +- 0.15 ms   | 10.1 ms +- 0.6 ms    |
| 52 | regex_v8                | 81.3 ms +- 1.3 ms    | 82.5 ms +- 5.2 ms    | 79.2 ms +- 2.9 ms    | 82.3 ms +- 2.9 ms    | 63.7 ms +- 1.2 ms    | 64.6 ms +- 4.2 ms    |
| 53 | richards                | 181 ms +- 9 ms       | 174 ms +- 10 ms      | 167 ms +- 3 ms       | 174 ms +- 7 ms       | 137 ms +- 9 ms       | 136 ms +- 7 ms       |
| 54 | scimark_fft             | 1.02 sec +- 0.03 sec | 1.08 sec +- 0.02 sec | 1.13 sec +- 0.03 sec | 1.17 sec +- 0.03 sec | 996 ms +- 40 ms      | 996 ms +- 28 ms      |
| 55 | scimark_lu              | 508 ms +- 31 ms      | 434 ms +- 21 ms      | 443 ms +- 21 ms      | 436 ms +- 8 ms       | 360 ms +- 29 ms      | 339 ms +- 9 ms       |
| 56 | scimark_monte_carlo     | 290 ms +- 16 ms      | 292 ms +- 9 ms       | 296 ms +- 10 ms      | 288 ms +- 7 ms       | 216 ms +- 11 ms      | 217 ms +- 14 ms      |
| 57 | scimark_sor             | 598 ms +- 20 ms      | 608 ms +- 16 ms      | 607 ms +- 9 ms       | 600 ms +- 11 ms      | 392 ms +- 11 ms      | 389 ms +- 14 ms      |
| 58 | scimark_sparse_mat_mult | 17.4 ms +- 1.2 ms    | 18.5 ms +- 0.4 ms    | 20.4 ms +- 0.8 ms    | 21.2 ms +- 0.3 ms    | 18.4 ms +- 1.4 ms    | 18.8 ms +- 0.9 ms    |
| 59 | spectral_norm           | 390 ms +- 15 ms      | 428 ms +- 11 ms      | 433 ms +- 22 ms      | 417 ms +- 7 ms       | 302 ms +- 10 ms      | 304 ms +- 10 ms      |
| 60 | sqlalchemy_declarative  | 374 ms +- 27 ms      | 331 ms +- 49 ms      | 310 ms +- 20 ms      | 305 ms +- 27 ms      | 313 ms +- 42 ms      | 270 ms +- 24 ms      |
| 61 | sqlalchemy_imperative   | 55.7 ms +- 5.0 ms    | 57.4 ms +- 4.2 ms    | 45.4 ms +- 2.8 ms    | 40.9 ms +- 3.6 ms    | 40.4 ms +- 2.8 ms    | 37.1 ms +- 2.8 ms    |
| 62 | sqlglot_parse           | 6.25 ms +- 0.45 ms   | 5.40 ms +- 0.39 ms   | 5.42 ms +- 0.33 ms   | 4.93 ms +- 0.34 ms   | 3.91 ms +- 0.39 ms   | 3.82 ms +- 0.22 ms   |
| 63 | sqlglot_transpile       | 7.03 ms +- 0.22 ms   | 6.06 ms +- 0.17 ms   | 5.85 ms +- 0.16 ms   | 5.69 ms +- 0.33 ms   | 4.57 ms +- 0.36 ms   | 4.50 ms +- 0.28 ms   |
| 64 | sqlglot_optimize        | 205 ms +- 7 ms       | 163 ms +- 9 ms       | 156 ms +- 5 ms       | 158 ms +- 7 ms       | 133 ms +- 4 ms       | 134 ms +- 4 ms       |
| 65 | sqlglot_normalize       | 454 ms +- 18 ms      | 361 ms +- 14 ms      | 340 ms +- 9 ms       | 353 ms +- 30 ms      | 291 ms +- 10 ms      | 301 ms +- 47 ms      |
| 66 | sqlite_synth            | 8.22 us +- 0.09 us   | 8.32 us +- 0.18 us   | 8.34 us +- 0.47 us   | 7.62 us +- 0.57 us   | 6.46 us +- 0.47 us   | 6.52 us +- 0.51 us   |
| 67 | sympy_expand            | 1.45 sec +- 0.04 sec | 1.17 sec +- 0.02 sec | 1.16 sec +- 0.02 sec | 1.20 sec +- 0.39 sec | 1.05 sec +- 0.02 sec | 1.06 sec +- 0.05 sec |
| 68 | sympy_integrate         | 65.7 ms +- 3.4 ms    | 52.2 ms +- 0.7 ms    | 50.9 ms +- 4.0 ms    | 67.3 ms +- 51.3 ms   | 46.2 ms +- 4.4 ms    | 45.8 ms +- 4.1 ms    |
| 69 | sympy_sum               | 466 ms +- 51 ms      | 379 ms +- 13 ms      | 367 ms +- 12 ms      | 407 ms +- 49 ms      | 366 ms +- 26 ms      | 365 ms +- 38 ms      |
| 70 | sympy_str               | 848 ms +- 28 ms      | 708 ms +- 10 ms      | 687 ms +- 21 ms      | 728 ms +- 26 ms      | 640 ms +- 26 ms      | 690 ms +- 96 ms      |
| 71 | telco                   | 18.6 ms +- 1.3 ms    | 19.3 ms +- 0.7 ms    | 17.7 ms +- 0.7 ms    | 19.1 ms +- 1.2 ms    | 17.3 ms +- 1.0 ms    | 23.7 ms +- 9.0 ms    |
| 72 | tornado_http            | 341 ms +- 27 ms      | 303 ms +- 15 ms      | 300 ms +- 17 ms      | 317 ms +- 22 ms      | 258 ms +- 26 ms      | 357 ms +- 156 ms     |
| 73 | unpack_sequence         | 128 ns +- 2 ns       | 144 ns +- 6 ns       | 146 ns +- 3 ns       | 153 ns +- 31 ns      | 133 ns +- 3 ns       | 144 ns +- 28 ns      |
| 74 | unpickle                | 36.4 us +- 2.3 us    | 36.6 us +- 1.9 us    | 34.5 us +- 2.1 us    | 36.4 us +- 3.4 us    | 35.3 us +- 0.8 us    | 45.3 us +- 18.3 us   |
| 75 | unpickle_list           | 11.2 us +- 0.9 us    | 10.6 us +- 0.3 us    | 11.3 us +- 0.3 us    | 11.5 us +- 1.1 us    | 11.6 us +- 0.8 us    | 12.8 us +- 1.9 us    |
| 76 | unpickle_pure_python    | 1.06 ms +- 0.09 ms   | 987 us +- 31 us      | 969 us +- 149 us     | 945 us +- 51 us      | 674 us +- 29 us      | 744 us +- 69 us      |
| 77 | xml_etree_parse         | 450 ms +- 17 ms      | 425 ms +- 32 ms      | 419 ms +- 21 ms      | 461 ms +- 23 ms      | 447 ms +- 18 ms      | 578 ms +- 174 ms     |
| 78 | xml_etree_iterparse     | 290 ms +- 19 ms      | 278 ms +- 6 ms       | 268 ms +- 13 ms      | 291 ms +- 19 ms      | 259 ms +- 16 ms      | 309 ms +- 69 ms      |
| 79 | xml_etree_generate      | 287 ms +- 14 ms      | 265 ms +- 14 ms      | 234 ms +- 6 ms       | 249 ms +- 17 ms      | 210 ms +- 10 ms      | 240 ms +- 78 ms      |
| 80 | xml_etree_process       | 240 ms +- 16 ms      | 220 ms +- 10 ms      | 197 ms +- 7 ms       | 207 ms +- 8 ms       | 157 ms +- 15 ms      | 158 ms +- 8 ms       |
| 81 | pprint_safe_repr        | /                    | /                    | /                    | 2.80 sec +- 0.05 sec | 2.15 sec +- 0.04 sec | 2.15 sec +- 0.03 sec |

### 1.Change(UNIT:ms)
|     | Task                    | 3.7.16     | 3.8.0      | 3.9.0      | 3.10.0     | 3.11.0    | 3.11.1     |
|:----|:------------------------|:-----------|:-----------|:-----------|:-----------|:----------|:-----------|
| 0   | 2to3                    | 775.0      | 826.0      | 795.0      | 766.0      | 667.0     | 594.0      |
| 1   | async_generators        | 665.0      | 759.0      | 771.0      | 727.0      | 744.0     | 544.0      |
| 2   | async_tree_none         | 1490.0     | 1650.0     | 1670.0     | 1580.0     | 1380.0    | 1190.0     |
| 3   | async_tree_cpu_io_mixed | 2070.0     | 2280.0     | 2850.0     | 2210.0     | 1810.0    | 1790.0     |
| 4   | async_tree_io           | 3490.0     | 3680.0     | 4410.0     | 3630.0     | 2740.0    | 2560.0     |
| 5   | async_tree_memoization  | 1860.0     | 1990.0     | 1880.0     | 2050.0     | 1640.0    | 1710.0     |
| 6   | chameleon               | 28.3       | 29.9       | 28.1       | 25.9       | 22.0      | 21.8       |
| 7   | chaos                   | 284.0      | 288.0      | 280.0      | 268.0      | 197.0     | 204.0      |
| 8   | bench_mp_pool           | 114.0      | 22.6       | 22.7       | 23.1       | 23.6      | 22.4       |
| 9   | bench_thread_pool       | 108.0      | 3.47       | 3.5        | 3.43       | 3.34      | 3.35       |
| 10  | coroutines              | 72.5       | 78.2       | 76.1       | 63.3       | 58.9      | 58.4       |
| 11  | coverage                | 94.3       | 94.3       | 99.1       | 114.0      | 208.0     | 204.0      |
| 12  | crypto_pyaes            | 233.0      | 251.0      | 238.0      | 237.0      | 178.0     | 183.0      |
| 13  | deepcopy                | 1.4        | 1.44       | 1.35       | 1.26       | 1.07      | 1.06       |
| 14  | deepcopy_reduce         | 0.0128     | 0.0126     | 0.0116     | 0.0112     | 0.0094    | 0.0095     |
| 15  | deepcopy_memo           | 0.168      | 0.204      | 0.162      | 0.156      | 0.125     | 0.124      |
| 16  | deltablue               | 17.5       | 17.2       | 17.2       | 15.5       | 10.4      | 10.4       |
| 17  | django_template         | 146.0      | 149.0      | 142.0      | 134.0      | 108.0     | 112.0      |
| 18  | docutils                | 7460.0     | 7610.0     | 7050.0     | 7320.0     | 6080.0    | 6500.0     |
| 19  | dulwich_log             | 189.0      | 169.0      | 167.0      | 160.0      | 137.0     | 148.0      |
| 20  | fannkuch                | 1390.0     | 1280.0     | 1250.0     | 1230.0     | 972.0     | 1130.0     |
| 21  | float                   | 268.0      | 275.0      | 272.0      | 248.0      | 193.0     | 201.0      |
| 22  | generators              | 89.4       | 86.1       | 84.0       | 82.2       | 76.8      | 89.9       |
| 23  | genshi_text             | 95.6       | 90.7       | 86.4       | 78.9       | 63.5      | 71.5       |
| 24  | genshi_xml              | 189.0      | 180.0      | 173.0      | 167.0      | 142.0     | 151.0      |
| 25  | go                      | 611.0      | 585.0      | 590.0      | 521.0      | 376.0     | 380.0      |
| 26  | hexiom                  | 24.9       | 24.2       | 22.2       | 21.3       | 16.2      | 16.1       |
| 27  | html5lib                | 211.0      | 201.0      | 200.0      | 186.0      | 160.0     | 159.0      |
| 28  | json_dumps              | 34.3       | 34.6       | 34.0       | 33.3       | 33.4      | 33.8       |
| 29  | json_loads              | 0.0629     | 0.0614     | 0.0567     | 0.0571     | 0.0568    | 0.0565     |
| 30  | logging_format          | 0.0259     | 0.0248     | 0.0242     | 0.0241     | 0.0207    | 0.0217     |
| 31  | logging_silent          | 0.0005     | 0.0006     | 0.0005     | 0.0005     | 0.0004    | 0.0004     |
| 32  | logging_simple          | 0.0234     | 0.0231     | 0.0222     | 0.0221     | 0.0193    | 0.0189     |
| 33  | mako                    | 44.9       | 42.7       | 39.2       | 36.2       | 26.3      | 25.6       |
| 34  | mdp                     | 8530.0     | 8260.0     | 7800.0     | 7540.0     | 7460.0    | 7200.0     |
| 35  | meteor_contest          | 245.0      | 230.0      | 215.0      | 212.0      | 207.0     | 207.0      |
| 36  | nbody                   | 303.0      | 320.0      | 311.0      | 306.0      | 222.0     | 212.0      |
| 37  | nqueens                 | 261.0      | 259.0      | 240.0      | 241.0      | 212.0     | 214.0      |
| 38  | pathlib                 | 54.4       | 57.7       | 49.4       | 52.4       | 49.2      | 51.5       |
| 39  | pickle                  | 0.0344     | 0.023      | 0.0226     | 0.0225     | 0.0218    | 0.0206     |
| 40  | pickle_dict             | 0.147      | 0.0702     | 0.069      | 0.0692     | 0.0644    | 0.0629     |
| 41  | pickle_list             | 0.0181     | 0.0105     | 0.0103     | 0.01       | 0.0087    | 0.0087     |
| 42  | pickle_pure_python      | 1.29       | 1.45       | 1.32       | 1.25       | 0.992     | 0.94       |
| 43  | pidigits                | 303.0      | 288.0      | 288.0      | 285.0      | 289.0     | 283.0      |
| 44  | pprint_pformat          | 4760.0     | 4770.0     | 4460.0     | 5800.0     | 4520.0    | 5020.0     |
| 45  | pyflate                 | 1710.0     | 1670.0     | 1660.0     | 1610.0     | 1220.0    | 1210.0     |
| 46  | python_startup          | 34.3       | 34.2       | 33.0       | 30.2       | 36.3      | 34.7       |
| 47  | python_startup_no_site  | 18.6       | 17.8       | 16.0       | 15.2       | 19.4      | 19.1       |
| 48  | raytrace                | 1260.0     | 1270.0     | 1260.0     | 1200.0     | 854.0     | 851.0      |
| 49  | regex_compile           | 444.0      | 411.0      | 391.0      | 395.0      | 318.0     | 315.0      |
| 50  | regex_dna               | 554.0      | 565.0      | 560.0      | 538.0      | 453.0     | 456.0      |
| 51  | regex_effbot            | 11.5       | 11.6       | 11.5       | 11.4       | 9.88      | 10.1       |
| 52  | regex_v8                | 81.3       | 82.5       | 79.2       | 82.3       | 63.7      | 64.6       |
| 53  | richards                | 181.0      | 174.0      | 167.0      | 174.0      | 137.0     | 136.0      |
| 54  | scimark_fft             | 1020.0     | 1080.0     | 1130.0     | 1170.0     | 996.0     | 996.0      |
| 55  | scimark_lu              | 508.0      | 434.0      | 443.0      | 436.0      | 360.0     | 339.0      |
| 56  | scimark_monte_carlo     | 290.0      | 292.0      | 296.0      | 288.0      | 216.0     | 217.0      |
| 57  | scimark_sor             | 598.0      | 608.0      | 607.0      | 600.0      | 392.0     | 389.0      |
| 58  | scimark_sparse_mat_mult | 17.4       | 18.5       | 20.4       | 21.2       | 18.4      | 18.8       |
| 59  | spectral_norm           | 390.0      | 428.0      | 433.0      | 417.0      | 302.0     | 304.0      |
| 60  | sqlalchemy_declarative  | 374.0      | 331.0      | 310.0      | 305.0      | 313.0     | 270.0      |
| 61  | sqlalchemy_imperative   | 55.7       | 57.4       | 45.4       | 40.9       | 40.4      | 37.1       |
| 62  | sqlglot_parse           | 6.25       | 5.4        | 5.42       | 4.93       | 3.91      | 3.82       |
| 63  | sqlglot_transpile       | 7.03       | 6.06       | 5.85       | 5.69       | 4.57      | 4.5        |
| 64  | sqlglot_optimize        | 205.0      | 163.0      | 156.0      | 158.0      | 133.0     | 134.0      |
| 65  | sqlglot_normalize       | 454.0      | 361.0      | 340.0      | 353.0      | 291.0     | 301.0      |
| 66  | sqlite_synth            | 0.0082     | 0.0083     | 0.0083     | 0.0076     | 0.0065    | 0.0065     |
| 67  | sympy_expand            | 1450.0     | 1170.0     | 1160.0     | 1200.0     | 1050.0    | 1060.0     |
| 68  | sympy_integrate         | 65.7       | 52.2       | 50.9       | 67.3       | 46.2      | 45.8       |
| 69  | sympy_sum               | 466.0      | 379.0      | 367.0      | 407.0      | 366.0     | 365.0      |
| 70  | sympy_str               | 848.0      | 708.0      | 687.0      | 728.0      | 640.0     | 690.0      |
| 71  | telco                   | 18.6       | 19.3       | 17.7       | 19.1       | 17.3      | 23.7       |
| 72  | tornado_http            | 341.0      | 303.0      | 300.0      | 317.0      | 258.0     | 357.0      |
| 73  | unpack_sequence         | 0.0001     | 0.0001     | 0.0001     | 0.0002     | 0.0001    | 0.0001     |
| 74  | unpickle                | 0.0364     | 0.0366     | 0.0345     | 0.0364     | 0.0353    | 0.0453     |
| 75  | unpickle_list           | 0.0112     | 0.0106     | 0.0113     | 0.0115     | 0.0116    | 0.0128     |
| 76  | unpickle_pure_python    | 1.06       | 0.987      | 0.969      | 0.945      | 0.674     | 0.744      |
| 77  | xml_etree_parse         | 450.0      | 425.0      | 419.0      | 461.0      | 447.0     | 578.0      |
| 78  | xml_etree_iterparse     | 290.0      | 278.0      | 268.0      | 291.0      | 259.0     | 309.0      |
| 79  | xml_etree_generate      | 287.0      | 265.0      | 234.0      | 249.0      | 210.0     | 240.0      |
| 80  | xml_etree_process       | 240.0      | 220.0      | 197.0      | 207.0      | 157.0     | 158.0      |
| SUM |                         | 49191.7789 | 48725.9928 | 48288.3423 | 48173.6334 | 40660.816 | 41241.1019 |
| AVG |                         | 607.3059   | 601.5555   | 596.1524   | 594.7362   | 501.9854  | 509.1494   |
| UP% |                         | 100.0000%  | 100.9559%  | 101.8709%  | 102.1135%  | 120.9808% | 119.2785%  |

