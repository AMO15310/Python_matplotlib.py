import matplotlib.pyplot as plt
import numpy as np


x = np.array([370,
371,
372,
373,
374,
375,
376,
377,
378,
379,
380,
381,
382,
383,
384,
385,
386,
387,
388,
389,
390,
391,
392,
393,
394,
395,
396,
397,
398,
399,
400,
401,
402,
403,
404,
405,
406,
407,
408,
409,
410,
411,
412,
413,
414,
415,
416,
417,
418,
419,
420,
421,
422,
423,
424,
425,
426,
427,
428,
429,
430,
431,
432,
433,
434,
435,
436,
437,
438,
439,
440,
441,
442,
443,
444,
445,
446,
447,
448,
449,
450,
451,
452,
453,
454,
455,
456,
457,
458,
459,
460,
461,
462,
463,
464,
465,
466,
467,
468,
469,
470,
471,
472,
473,
474,
475,
476,
477,
478,
479,
480,
481,
482,
483,
484,
485,
486,
487,
488,
489,
490,
491,
492,
493,
494,
495,
496,
497,
498,
499,
500,
501,
502,
503,
504,
505,
506,
507,
508,
509,
510,
511,
512,
513,
514,
515,
516,
517,
518,
519,
520,
521,
522,
523,
524,
525,
526,
527,
528,
529,
530,
531,
532,
533,
534,
535,
536,
537,
538,
539,
540,
541,
542,
543,
544,
545,
546,
547,
548,
549,
550,
551,
552,
553,
554,
555,
556,
557,
558,
559,
560,
561,
562,
563,
564,
565,
566,
567,
568,
569,
570,
571,
572,
573,
574,
575,
576,
577,
578,
579,
580,
581,
582,
583,
584,
585,
586,
587,
588,
589,
590,
591,
592,
593,
594,
595,
596,
597,
598,
599,
600,
])


y = np.array([483625,
291365,
179860,
124825,
99105,
92695,
96760,
105040,
115695,
123865,
133100,
139060,
143725,
148745,
152180,
154745,
156425,
160835,
163845,
171375,
175515,
186735,
195965,
208355,
225685,
241195,
258150,
281515,
301995,
328895,
354930,
382895,
414575,
439945,
474325,
501035,
531420,
560210,
590345,
615495,
633565,
653650,
673485,
688455,
700110,
710400,
718710,
721495,
734030,
732270,
730620,
735410,
731075,
733225,
735495,
738020,
736770,
742355,
745545,
746615,
754320,
756670,
758235,
760840,
768330,
766295,
766625,
758400,
760060,
751145,
743515,
739950,
731730,
719705,
706320,
694770,
679650,
663860,
650660,
631420,
623065,
608005,
594005,
583395,
567135,
557720,
541860,
528535,
517725,
507150,
496280,
486775,
476695,
463305,
451855,
438690,
427995,
419115,
405425,
396310,
386865,
375455,
367270,
359435,
350500,
339290,
329875,
317850,
307775,
300165,
291745,
283955,
271250,
264550,
256605,
246130,
240420,
235250,
224770,
217520,
212415,
207375,
201225,
193415,
189060,
183845,
176980,
172435,
166855,
161035,
156320,
151360,
147420,
143545,
137780,
136035,
129785,
127310,
122555,
118390,
116025,
112905,
108370,
106200,
100350,
98050,
93880,
92075,
88875,
85460,
83530,
81110,
76835,
75405,
72170,
70500,
68340,
66790,
65010,
61585,
60850,
58575,
56835,
55295,
53410,
52910,
51090,
49865,
48330,
47905,
46055,
45530,
43425,
43005,
41625,
39595,
40330,
38460,
36810,
36120,
35785,
34615,
33690,
33460,
32525,
31780,
30750,
29510,
29100,
28720,
27230,
26755,
26105,
24735,
24810,
24765,
23685,
22765,
22500,
21270,
21560,
20465,
19445,
19810,
18930,
18805,
18830,
18010,
17350,
17055,
16585,
16345,
15750,
15800,
14810,
14480,
13960,
14280,
13585,
13290,
13465,
12875,
13175,
11955,
12200,
11690,
11385,
11420,
10855,
10835,
10540,
])


plt.plot(x,y)
plt.title("Test Graph",loc = 'left')
plt.xlabel("X axis")
plt.ylabel("Y axis")
#ax = plt.axes()
#ax.yaxis.set_major_locator(plt.NullLocator())
#ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax = plt.subplots(4, 4, sharex=True, sharey=True)
plt.grid()
plt.show()