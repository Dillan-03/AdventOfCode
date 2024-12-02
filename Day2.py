# Data where it contains reports, levels are separated by spaces
# Levels are safe if the adjacent values are increasing or decreasing by 1,2 or 3


def format_report(data):
    # Convert the string to a list of lists
    reports = [list(map(int, line.split())) for line in data.splitlines()]

    return reports
    
def is_valid(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check if the difference is valid (between 1 and 3), if not then exit report
        if not (1 <= abs(diff) <= 3):
            return False

        # First item is increasing        
        if diff > 0: 
            if not all(report[j + 1] >= report[j] for j in range(i + 1, len(report) - 1)):
                return False
        # First item is decreasing
        if diff < 0: 
            if not all(report[j + 1] <= report[j] for j in range(i + 1, len(report) - 1)):
                return False

    return True

def Day2(data): 
    reports = format_report(data)
    safe = 0
    
    for report in reports:
        # First, check if the report is valid as is
        if is_valid(report):
            safe += 1
            continue


    return safe

def Day2Problem_Dampener(data):
    reports = format_report(data)
    safe = 0

    for report in reports:
        # First, check if the report is valid as is
        if is_valid(report):
            safe += 1
            continue

        # Try removing each level through slicing and check if the report is valid
        for k in range(len(report)):
            modified_report = report[:k] + report[k+1:] 
            if is_valid(modified_report):
                safe += 1
                break

    return safe


test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

input_data = """92 94 97 98 97
26 27 28 31 33 34 37 37
56 59 60 61 62 65 69
42 44 46 48 55
15 18 19 22 21 24 26
74 76 77 76 77 78 75
60 62 64 65 64 64
61 64 67 64 67 68 72
71 74 73 76 82
25 26 27 29 29 32
27 28 30 30 32 35 34
6 7 7 9 9
33 34 34 35 39
17 19 20 23 23 25 26 32
29 30 31 35 37 38 39 41
22 25 29 32 33 34 37 34
15 18 20 24 26 27 30 30
44 45 48 52 54 55 58 62
35 37 38 39 42 46 49 55
71 74 77 84 86 89 91
23 25 27 32 29
14 15 16 18 25 25
10 11 14 19 21 24 28
40 41 46 47 49 55
12 10 11 13 15 18 20
50 48 49 51 53 55 56 55
18 16 18 21 24 27 28 28
51 48 51 54 58
81 78 80 82 87
35 34 31 32 35
60 57 59 60 62 61 60
29 26 24 25 28 28
28 27 26 28 31 35
80 78 77 80 83 88
87 85 85 88 90
91 89 89 91 92 89
87 86 88 90 93 93 93
32 29 31 34 37 39 39 43
8 5 5 8 9 15
85 83 85 88 92 93 95
34 33 37 39 40 41 42 40
26 25 27 28 30 32 36 36
18 16 19 23 25 28 32
13 12 16 18 20 26
18 17 18 19 21 27 28
15 12 18 19 18
57 55 60 62 62
68 65 67 68 75 77 78 82
70 67 74 77 78 81 84 90
48 48 50 53 55 57
11 11 12 15 17 18 20 19
20 20 23 25 28 30 30
12 12 13 16 18 20 21 25
41 41 44 47 49 51 54 61
5 5 7 5 6 7
82 82 81 84 87 85
10 10 11 8 8
6 6 9 7 9 12 16
32 32 30 32 35 40
25 25 25 28 31
31 31 32 32 33 36 38 35
18 18 19 19 21 23 26 26
7 7 9 12 12 14 18
24 24 24 26 27 32
74 74 77 78 82 84
26 26 30 32 30
52 52 54 57 60 64 64
57 57 60 64 65 69
30 30 31 35 38 45
52 52 55 56 58 65 68
12 12 17 19 21 19
49 49 52 53 59 61 61
6 6 8 15 19
65 65 66 72 79
47 51 54 55 57 59 62 63
63 67 68 69 71 73 74 72
67 71 72 74 77 80 81 81
6 10 12 15 16 18 22
55 59 62 63 68
20 24 26 28 25 27 30 33
57 61 63 62 64 65 63
41 45 44 46 46
26 30 32 30 32 36
62 66 68 65 68 74
76 80 80 83 84 85
83 87 89 89 88
60 64 64 66 67 70 71 71
1 5 7 7 8 12
28 32 32 34 35 38 44
1 5 8 10 14 17
56 60 63 65 69 66
53 57 61 62 63 66 66
63 67 70 74 78
85 89 90 94 99
21 25 26 31 33 35
8 12 13 20 18
40 44 47 53 56 56
72 76 81 84 87 91
45 49 51 54 59 60 65
27 33 34 36 37 38
33 40 41 44 42
20 25 28 30 33 33
35 40 42 44 47 51
49 55 56 57 58 65
46 52 53 54 53 56
27 32 34 35 33 32
71 77 75 77 77
40 45 42 45 47 51
50 55 58 59 58 64
44 49 49 50 52 53 56
75 82 82 83 85 84
83 90 92 92 92
59 64 66 69 71 71 75
14 20 22 23 26 27 27 33
57 62 64 65 67 71 73
15 20 24 27 25
11 17 19 23 26 26
22 29 30 33 37 38 40 44
76 83 86 87 91 94 99
32 38 39 45 47
60 65 68 70 77 78 75
75 81 82 83 88 91 94 94
3 8 11 18 20 24
10 16 22 25 26 27 34
5 4 3 2 1 2
65 63 60 59 59
96 95 93 92 89 87 85 81
67 66 65 62 60 57 56 49
29 26 29 26 24
77 76 74 75 74 72 69 70
13 12 10 13 11 10 10
64 61 60 57 59 56 52
59 57 55 54 57 52
50 48 48 46 44
46 44 44 41 38 35 36
56 53 53 50 48 46 46
59 58 58 57 55 51
38 35 34 31 28 25 25 19
75 73 69 66 64 63 61
42 39 36 34 30 32
34 31 27 24 24
52 49 45 42 39 37 33
26 25 24 21 20 16 9
96 94 89 88 86
19 17 10 9 8 10
52 51 50 49 46 39 39
44 41 38 37 34 29 25
24 22 20 19 13 10 8 3
56 59 58 55 53 51 49 48
51 53 52 50 49 47 44 46
45 46 44 42 41 41
21 23 21 19 16 12
81 83 82 80 77 70
44 47 48 47 46 43
29 32 31 32 29 27 25 27
23 26 23 26 23 23
63 66 65 66 64 61 59 55
55 56 53 52 55 52 49 44
61 64 61 61 60 59 58 56
21 22 20 20 22
67 68 68 66 65 62 62
35 38 38 37 36 32
44 46 46 43 41 39 37 31
46 47 43 42 41 40
36 39 35 34 31 28 25 26
66 69 68 67 65 61 61
22 23 19 18 16 13 10 6
91 92 91 87 82
83 86 81 80 79
53 54 48 46 43 42 43
61 62 61 54 51 50 50
74 76 70 67 65 62 58
39 41 38 35 28 25 20
40 40 37 34 33 30 27 26
18 18 17 16 18
82 82 80 79 79
25 25 22 20 16
22 22 20 18 16 15 8
50 50 47 50 47 45
40 40 42 41 38 41
39 39 42 41 41
98 98 96 94 95 93 90 86
62 62 65 64 63 60 55
94 94 92 92 90 88
69 69 68 68 70
42 42 41 39 39 39
39 39 36 35 33 33 29
45 45 45 42 41 39 33
21 21 20 17 15 11 10
59 59 57 53 51 48 49
84 84 82 80 76 76
32 32 28 27 26 23 22 18
55 55 51 48 46 44 38
80 80 73 72 69 66 63
12 12 10 4 7
35 35 32 31 26 25 25
27 27 25 23 18 17 13
64 64 61 54 53 51 44
43 39 36 33 32 29 28
79 75 73 72 71 73
70 66 65 63 60 57 56 56
51 47 46 44 40
85 81 79 78 71
98 94 91 89 90 87 84
62 58 56 55 52 55 54 56
20 16 18 15 15
73 69 72 69 68 67 63
41 37 34 31 32 31 26
76 72 70 68 68 65 63
54 50 49 48 48 47 50
82 78 76 75 75 74 74
94 90 88 85 83 83 79
28 24 21 20 18 18 16 10
52 48 44 42 39 38
32 28 26 24 21 17 19
27 23 21 19 15 13 10 10
33 29 28 26 22 18
62 58 54 52 51 48 42
99 95 92 86 83
91 87 85 83 77 78
22 18 13 11 9 7 7
98 94 89 87 85 82 80 76
43 39 38 37 34 28 23
47 40 39 38 35 32
17 12 10 8 7 4 2 3
84 77 74 73 70 69 69
64 57 54 52 48
90 83 82 80 78 75 72 67
90 85 87 84 81 78 76
29 24 22 24 23 21 19 20
84 79 77 80 78 77 77
63 57 54 56 52
38 32 33 31 30 27 25 18
32 25 25 22 20
19 13 13 12 10 11
18 13 12 12 12
13 8 7 6 6 2
40 34 31 31 28 23
81 74 71 67 64 63
75 70 68 65 63 62 58 60
60 55 52 48 48
91 85 83 80 76 73 72 68
79 74 71 70 67 63 57
86 81 75 73 72 71 69
31 25 20 19 21
75 68 67 65 60 60
68 62 59 58 51 50 47 43
71 64 59 57 54 48
61 64 66 69 70 68
68 71 72 75 76 76
4 5 6 9 13
1 4 7 8 10 11 16
11 12 13 15 14 16 19
56 57 59 56 54
85 86 85 86 88 90 91 91
40 41 42 39 41 43 45 49
15 18 21 22 25 23 30
69 71 71 74 75
3 6 9 9 7
83 86 86 87 88 89 89
90 93 95 95 99
2 3 5 5 10
49 52 53 55 59 61 64 65
58 60 64 65 64
5 7 8 12 12
80 82 84 86 88 89 93 97
37 39 43 45 47 54
79 81 83 90 91
41 42 47 48 45
76 79 84 86 89 90 91 91
3 6 7 13 15 17 21
79 80 82 83 88 95
42 40 41 44 45 47
55 53 54 57 60 63 61
29 26 29 30 33 35 37 37
83 80 82 83 84 88
47 44 46 49 56
91 90 88 91 92 95 97
24 22 23 24 25 27 24 21
20 19 22 20 23 25 25
43 40 41 40 43 46 48 52
27 24 25 27 29 27 29 34
46 44 45 48 48 49 51
45 44 47 47 44
66 64 64 67 68 70 71 71
94 93 93 95 99
22 21 21 24 29
24 23 27 29 32 34 36
72 70 73 77 78 76
16 14 17 21 22 22
39 36 39 40 44 47 48 52
71 68 72 75 81
70 69 76 77 78 79 81 84
11 8 10 15 17 14
75 74 75 76 78 84 85 85
28 26 32 33 34 38
8 7 13 15 16 19 26
45 45 47 50 51
77 77 79 82 83 86 88 87
13 13 15 16 17 20 20
54 54 55 58 60 64
34 34 37 40 42 48
20 20 19 21 23 26 28
22 22 24 27 25 27 28 26
38 38 37 38 41 42 42
24 24 21 24 25 27 31
4 4 5 3 5 6 13
35 35 37 37 39 42
31 31 32 35 38 38 35
30 30 32 32 35 35
12 12 15 15 19
80 80 82 82 84 89
28 28 30 34 36
49 49 50 54 53
35 35 37 38 39 43 44 44
53 53 56 60 64
56 56 60 62 63 64 70
20 20 23 28 29
57 57 58 61 66 69 71 69
2 2 4 9 9
61 61 64 65 68 75 78 82
46 46 51 53 55 57 63
30 34 37 39 41 44 46
39 43 44 45 46 47 48 45
69 73 75 76 78 81 81
60 64 67 70 71 75
84 88 90 91 96
61 65 63 66 67
88 92 95 92 95 92
79 83 85 87 90 89 89
19 23 26 28 30 33 32 36
82 86 83 86 89 95
26 30 32 33 33 36 38
61 65 67 70 73 74 74 72
39 43 45 48 51 51 51
60 64 65 68 70 70 74
66 70 73 73 75 77 83
17 21 23 26 30 31 32
27 31 34 38 39 36
48 52 53 54 58 58
3 7 8 12 16
44 48 51 53 55 59 66
74 78 85 86 88
25 29 34 37 34
23 27 30 36 36
58 62 64 71 74 78
50 54 55 58 59 62 67 74
26 33 35 37 40 43
71 77 79 80 82 83 84 81
6 12 14 16 18 21 23 23
38 43 46 47 48 49 53
20 27 28 31 36
49 55 56 55 58
82 88 90 88 87
54 60 58 59 59
34 39 41 39 43
65 71 72 70 76
48 54 54 55 56
36 43 45 48 48 51 54 52
16 23 25 28 30 30 30
18 25 25 27 31
74 80 82 84 84 85 90
14 19 20 24 25 27 29 32
38 44 48 51 54 52
21 27 29 31 35 38 38
31 38 42 45 46 47 51
73 78 80 81 85 88 93
49 56 62 64 66
20 25 27 30 37 36
68 75 78 83 83
37 42 43 44 45 50 54
32 38 40 45 47 48 49 55
47 46 45 44 46
93 92 90 87 85 82 80 80
32 29 27 26 25 22 19 15
22 21 18 17 14 12 6
31 28 25 26 24 22 19 18
25 23 21 24 21 23
90 87 85 83 85 85
18 16 14 16 13 12 10 6
58 56 55 52 54 53 51 44
38 36 33 33 32 30 28
53 52 51 51 50 49 50
63 61 58 57 56 56 56
35 34 32 30 28 28 25 21
69 66 65 65 60
30 27 26 25 21 18
88 86 84 83 79 80
90 87 84 82 81 77 77
27 24 21 17 13
34 32 29 25 22 21 20 13
97 94 93 87 86
85 83 76 74 77
77 75 72 70 63 63
27 24 21 18 11 7
36 33 30 28 22 19 13
83 86 85 84 81 79 78
94 96 95 93 90 87 86 87
61 62 60 58 57 56 56
14 17 16 13 11 7
81 82 79 76 73 70 69 62
19 21 20 17 15 14 15 13
29 32 33 31 30 31
63 65 68 65 65
60 63 60 57 59 57 56 52
93 95 93 91 88 90 83
30 32 32 29 26 23 20
30 31 31 30 28 27 26 29
76 78 78 76 76
18 19 19 17 14 10
58 60 60 59 54
50 53 52 48 46 44 43
94 97 93 91 88 90
84 87 83 80 79 79
59 61 58 55 53 49 45
86 88 87 85 84 82 78 72
92 94 91 88 87 86 80 77
48 49 47 44 43 37 38
68 69 63 60 58 56 55 55
58 61 60 54 51 47
84 86 85 80 74
43 43 41 40 39
71 71 68 65 66
21 21 20 18 17 15 12 12
61 61 59 58 57 53
86 86 85 84 82 81 80 73
26 26 23 20 17 20 18
86 86 83 82 85 82 83
29 29 28 25 23 24 22 22
54 54 51 52 51 49 45
40 40 39 38 36 39 33
87 87 85 85 84 81
60 60 60 59 56 57
11 11 8 6 6 5 3 3
61 61 60 60 58 57 54 50
92 92 91 88 85 83 83 77
38 38 35 31 30
15 15 11 10 13
89 89 85 84 81 81
28 28 27 23 22 20 16
73 73 71 67 66 61
51 51 50 48 46 41 40
90 90 88 82 80 79 77 78
82 82 77 76 75 74 74
78 78 76 75 70 66
66 66 60 57 52
38 34 33 31 30
73 69 68 66 69
56 52 51 50 50
48 44 41 39 35
59 55 54 52 51 48 41
19 15 12 13 12 9
56 52 54 53 56
80 76 74 73 75 75
35 31 30 32 29 28 24
51 47 48 46 45 44 38
80 76 76 74 72
75 71 70 67 67 68
75 71 70 67 67 67
48 44 42 39 36 36 34 30
74 70 68 68 67 60
32 28 26 25 22 21 17 15
99 95 91 88 87 89
38 34 30 28 26 23 23
25 21 17 14 13 12 8
58 54 50 49 47 42
78 74 71 70 68 67 61 60
23 19 13 11 13
19 15 10 7 7
81 77 71 69 65
87 83 78 77 74 67
17 10 7 5 3
28 22 19 18 17 15 17
62 55 53 52 49 49
61 54 52 50 49 45
69 63 62 59 57 55 52 45
91 84 81 84 81
49 42 39 36 37 36 39
14 9 10 9 9
41 35 33 31 28 29 28 24
96 91 88 90 88 82
79 73 73 71 70 68 65 63
76 69 69 68 67 69
51 46 43 41 38 37 37 37
66 59 56 53 53 49
43 37 36 36 35 33 31 24
35 30 28 24 21 20 18
45 40 37 34 30 31
54 47 44 40 38 38
91 86 84 80 78 74
62 55 54 51 47 45 44 38
48 41 40 35 33 30 27
89 82 79 77 70 68 67 68
31 26 24 21 20 18 12 12
51 45 39 38 37 34 30
71 66 61 59 58 56 51
78 79 82 85 88 85
49 50 52 54 54
55 56 57 59 63
35 38 41 44 45 47 49 55
10 13 12 13 14
4 5 8 5 8 6
77 80 81 84 85 83 83
28 30 27 28 30 34
20 23 24 27 28 31 29 36
9 12 12 14 17
52 53 53 56 55
31 34 34 37 37
27 30 31 34 34 35 39
79 80 81 83 84 86 86 92
36 37 38 42 43
7 10 13 17 19 18
51 52 54 58 60 62 62
15 18 22 24 27 28 32
23 24 25 29 30 31 32 38
61 63 66 68 75 76 77
43 44 45 47 54 52
28 30 32 39 41 42 42
43 46 47 54 55 58 60 64
15 18 25 27 29 32 37
88 85 88 89 92 95
45 43 46 48 45
45 44 47 49 51 53 56 56
9 6 7 9 11 12 13 17
34 32 33 35 36 41
11 8 10 12 15 18 17 19
58 57 58 56 54
24 23 22 25 26 29 30 30
93 91 94 95 94 98
68 65 68 66 71
34 31 31 32 33 35 38 40
86 83 85 85 87 90 93 91
38 36 38 41 41 43 45 45
27 26 26 27 31
48 45 46 46 52
7 6 7 11 14 16 17 18
57 54 56 57 58 59 63 61
41 40 43 47 47
26 23 25 27 31 33 37
48 46 49 51 53 57 64
64 61 62 68 69 72 75
85 84 85 91 92 94 91
80 79 80 86 89 89
45 42 48 50 53 57
13 12 15 21 24 26 33
74 74 77 80 81 83 85
22 22 25 27 28 30 33 30
39 39 42 44 47 49 50 50
87 87 90 92 94 98
66 66 69 72 75 76 78 85
88 88 89 86 87
19 19 17 19 17
11 11 12 9 11 11
1 1 3 1 4 5 8 12
37 37 36 37 43
34 34 37 37 38 39
33 33 36 38 38 39 40 37
79 79 80 80 81 84 87 87
12 12 14 14 18
32 32 33 36 36 38 41 46
78 78 82 84 85 86 89
21 21 24 26 30 33 35 32
7 7 10 14 16 19 19
81 81 84 88 89 91 95
68 68 69 72 75 79 84
49 49 56 57 60 62 64
44 44 46 49 56 58 60 59
36 36 39 40 42 44 51 51
63 63 65 67 72 76
69 69 71 74 81 83 89
85 89 90 91 92 93
11 15 18 20 21 18
22 26 27 29 29
5 9 11 12 16
58 62 63 64 65 66 71
77 81 82 80 82 85 86
83 87 85 86 84
6 10 11 8 10 10
41 45 47 49 51 52 51 55
54 58 57 58 61 64 65 71
27 31 31 33 36 38
76 80 80 83 86 85
7 11 11 12 12
31 35 36 37 37 41
60 64 67 67 73
28 32 34 37 38 42 45 46
53 57 60 61 62 65 69 67
10 14 18 21 21
83 87 89 93 97
67 71 73 77 84
4 8 10 12 15 17 23 26
70 74 79 81 83 81
78 82 84 90 90
63 67 74 75 78 79 83
10 14 17 23 26 29 30 37
38 44 47 49 50 51 53 54
37 44 47 50 51 53 52
81 86 89 90 91 91
43 48 50 52 54 58
10 16 18 20 26
85 92 91 93 95 97
25 32 35 34 35 37 36
38 45 46 47 49 47 47
20 27 24 25 29
84 89 90 93 91 98
57 63 63 65 68
75 82 84 84 87 89 90 87
33 38 40 43 43 43
59 64 64 66 68 71 75
26 33 33 36 39 41 42 48
51 57 59 63 65 67
15 22 25 29 28
78 83 84 88 90 92 92
70 76 80 82 85 88 92
33 39 41 42 46 53
27 32 39 42 43 45 48
21 27 33 36 37 36
42 47 49 55 56 56
19 26 28 35 36 38 42
12 17 20 23 26 33 34 41
56 54 53 52 51 48 47 48
20 17 16 14 11 9 9
25 23 20 17 15 13 9
78 77 75 72 69 62
37 34 35 33 30 29
19 17 14 13 12 15 17
30 27 25 22 20 23 23
31 28 27 26 28 24
40 39 40 39 37 36 31
58 55 54 54 53
66 64 64 61 58 55 56
53 51 48 48 45 45
42 39 39 38 34
57 54 52 50 50 44
65 63 59 58 57 55
42 40 39 35 33 30 28 30
14 12 10 8 4 4
16 13 12 8 5 1
36 34 31 27 26 24 23 18
94 91 88 81 78
21 18 13 11 13
70 68 61 60 58 58
40 38 35 32 25 21
76 74 69 67 64 61 60 55
77 79 76 74 72 70
48 50 48 45 46
19 20 18 17 17
34 35 32 29 28 25 22 18
60 62 61 58 57 51
57 59 58 57 58 56
84 86 88 86 84 83 82 85
82 85 82 80 77 79 79
16 19 17 16 15 13 15 11
57 59 58 56 54 57 55 48
70 72 72 70 67 66
65 68 66 66 63 64
62 63 63 60 58 55 54 54
10 11 10 10 6
63 66 64 63 63 58
33 35 33 29 26 24 23
61 64 62 58 56 58
41 42 40 36 36
93 96 93 90 87 83 79
54 56 53 49 42
16 17 11 8 6
66 69 66 61 62
30 33 32 31 30 23 20 20
71 72 70 68 61 60 56
35 36 31 30 28 23
79 79 78 77 75 73
38 38 35 32 30 31
17 17 16 14 13 13
85 85 82 80 77 75 71
53 53 52 50 49 47 45 39
75 75 73 71 74 72 70 68
25 25 24 27 25 28
50 50 47 45 43 42 44 44
40 40 42 40 36
86 86 84 82 84 78
70 70 70 67 66 65
62 62 60 57 57 56 54 56
13 13 13 11 10 9 8 8
32 32 30 28 28 24
69 69 68 67 67 65 62 56
54 54 51 47 46
51 51 49 46 43 39 42
27 27 26 23 22 18 15 15
60 60 59 57 54 50 48 44
26 26 24 20 14
39 39 36 30 27 25
94 94 92 85 83 86
96 96 90 88 86 85 82 82
77 77 70 68 66 65 61
60 60 59 58 57 50 45
59 55 53 50 49
71 67 64 63 62 64
93 89 86 84 82 82
14 10 9 7 3
34 30 27 25 24 22 19 14
26 22 24 22 20 17
98 94 93 90 93 90 93
46 42 40 42 40 40
29 25 23 25 24 23 19
23 19 20 19 13
12 8 5 4 4 3 2
26 22 20 20 23
91 87 84 83 82 82 79 79
66 62 59 58 55 55 51
34 30 29 29 28 23
44 40 37 35 31 29 27
48 44 41 37 40
41 37 33 30 29 29
65 61 59 55 51
76 72 69 67 65 61 55
49 45 43 40 34 31 28 26
87 83 82 77 75 76
94 90 83 82 81 81
77 73 66 64 63 61 58 54
31 27 24 17 11
61 54 52 51 50 47
84 79 77 75 72 69 72
61 56 53 50 47 46 44 44
69 62 60 59 57 56 54 50
49 42 41 39 38 35 34 28
21 16 17 15 14 12
27 21 18 17 18 16 13 15
31 26 28 26 26
29 22 20 19 18 21 19 15
59 52 50 52 50 47 46 41
24 18 16 16 13
19 13 10 10 7 4 7
84 78 78 75 72 72
41 35 32 29 29 26 22
26 20 18 16 16 13 7
22 16 15 11 10
26 19 17 16 12 9 10
85 80 79 75 73 71 71
74 68 66 62 61 59 57 53
77 71 70 67 65 61 56
54 47 44 41 35 34 32
35 28 26 21 18 20
79 72 71 66 64 64
56 49 44 41 37
87 80 78 77 76 69 63
10 12 14 16 18 15 15
3 8 15 18 19 18
1 3 2 4 9
21 21 20 22 25 28 31 35
80 74 72 71 71 69
36 40 43 48 45
65 60 59 56 52
94 89 89 86 79
9 13 16 16 19 23
47 42 40 40 42
39 35 32 31 27 24 25
99 94 92 90 85 82
38 43 44 44 44
59 62 61 60 58 58 57 51
26 31 34 36 39 42 46 50
10 11 10 6 3 6
29 33 36 39 41 39 42 40
89 88 85 84 82 81 79 75
60 66 69 66 67
9 6 7 4 5 7 10 9
4 5 8 10 13 14 15 18
86 85 83 81 78 77 75 74
29 30 32 35 37 40 42 44
44 42 40 37 36
82 83 84 86 89 92 95
68 66 63 60 58 55 53 51
24 22 19 18 16 13 12 10
39 38 35 33 30 29 27
14 11 9 6 5 2
17 16 14 12 9 7 6
85 88 89 91 92 94 95
71 74 75 77 78
14 16 19 21 23 26 28
57 59 61 63 65
54 55 57 58 60 63 64 66
11 8 7 6 4
88 87 85 82 79
14 17 18 20 21 24 26
39 38 35 32 30 27 24 21
84 85 87 90 91 93 94 97
46 47 49 52 55 56
59 62 64 66 69 72
39 42 45 46 47 49 52
81 79 76 73 70 67 64
75 78 79 82 83 86 89 91
53 56 59 61 64 67 70 73
35 32 30 28 27 26 25 22
3 4 5 7 9 11
49 48 45 44 41 40 39
16 18 19 20 21
21 22 23 24 26 27 28 30
74 72 69 68 67
54 51 49 47 44 42 40
82 80 78 75 72 69 66 63
66 69 70 73 75
57 54 51 50 49 47 44
68 71 72 74 77 79 82 85
12 14 15 16 17 18
32 31 29 28 27 25
72 74 75 78 81
73 76 78 81 83 85 88 89
50 47 46 44 42 40 38
60 58 56 54 53 50 47 45
84 81 80 79 76 75 74 72
85 86 89 91 93 96
37 35 32 30 27 26 23 21
67 64 61 59 56 53 50
76 73 71 68 67 66 64
68 66 64 63 60 58 55 53
42 44 45 48 51 52 53 56
21 22 25 26 28 29
97 94 93 91 88 85
97 95 92 91 89
6 9 12 14 16 19
66 65 63 60 58 56
22 19 18 16 13 11 9
64 65 67 68 69 72 74 76
50 47 44 41 38 36
22 21 20 17 15 12
53 54 55 56 58 59 61
83 86 87 88 89 90
67 65 64 61 60
68 65 64 63 61 58
13 12 11 8 7 6 4 3
33 32 29 27 24 23 21
79 77 74 71 68
57 55 52 51 48
35 32 29 26 25
79 82 83 85 86
49 51 53 54 57 60
92 90 89 87 84
49 51 52 53 54 57 58
3 5 8 10 12
66 65 63 60 57 55
6 5 4 2 1
75 76 77 79 82 83 85
45 42 39 38 36 33 31
60 59 57 54 51 48
94 92 90 89 87
97 95 93 90 89
23 26 29 31 32 33
27 28 30 33 34
85 87 89 91 94 97 99
78 79 81 84 86
87 84 81 80 78
46 49 52 55 58 60
82 79 78 77 76 74 71 68
93 90 89 87 84 82 80 78
34 31 28 25 22
97 94 92 91 90 88 87
99 97 96 93 91
18 21 24 26 27 30
79 76 75 74 71 70 69 68
52 55 56 58 61 64 67
74 73 71 68 66
92 90 88 85 82 80 78
36 34 33 30 29 27
36 35 34 32 29
15 17 18 20 22 23 24 26
11 14 16 18 19 21
64 61 59 56 53
78 81 83 86 87 88
8 10 13 14 15 18 21
92 89 86 85 82
65 64 63 62 61 58
13 12 10 7 4
71 73 75 77 79
83 82 81 80 79 77 74
66 68 70 72 74 77
88 87 84 83 80
65 64 61 60 58 56 54 53
29 32 34 37 38 40 43 45
75 78 80 81 82
1 3 5 6 8 11 12 15
21 18 17 16 13 11
51 52 53 55 56 59 61 64
65 67 68 71 73 75 77
75 76 79 80 81 82 83
49 50 52 53 55 58 59
83 84 85 87 90 92 95
36 35 33 30 29 28 25 24
8 11 13 16 19 20 23 24
85 88 90 91 92 95
21 22 23 26 27 29
92 89 87 84 83 81 78 76
92 91 89 86 84 83 82 80
18 21 22 25 27 29 32 34
28 26 23 22 20 17 14 12
73 76 77 80 82 83
84 82 80 77 76 75 74
76 75 73 72 70 67 64 63
54 51 49 46 45
39 42 44 45 46
45 47 48 50 53 55
34 37 40 41 42
1 4 7 10 12 13 14 15
69 68 65 63 60
29 28 27 24 21 19 17
19 22 23 26 28 30 32
49 50 52 54 55 57
17 20 22 23 25 26 28 29
12 9 8 7 5 4 3 2
83 85 87 90 93 96 97
9 11 14 15 16 18 21
80 83 85 87 89 91
60 58 56 55 54 53 52
51 50 48 47 46 44
39 36 33 31 30
44 41 38 35 32 29 26
29 27 26 23 20 19 17
89 86 85 83 82 80 79 77
44 46 48 50 52
74 73 71 70 69 68 66
78 77 74 72 69 67
43 42 40 37 36 35 34
92 93 95 96 99
23 26 29 32 34 37 38 40
45 42 40 38 37 36 35
66 67 68 69 70 71 74
56 59 62 63 64 66
61 62 64 67 68
29 32 34 36 39
73 70 68 65 63 62
53 51 50 47 44 43 41
28 30 33 36 38 39 40
42 39 36 35 34
57 56 55 52 51
12 13 14 16 17 20
13 11 9 6 4
49 46 43 42 41 39 38 37
43 44 47 48 49
69 68 67 65 62
72 74 76 78 81 84 87 90
45 44 41 39 38
93 90 87 86 85
60 58 56 53 52 50
97 95 94 92 90 89
68 66 65 63 61 58 56
66 63 60 57 54 53
3 6 8 10 11 13
87 88 89 91 92 94 96 97
94 93 92 89 87 84
36 37 40 41 44 45 47
83 81 80 78 76 73
40 42 43 46 48 50 52 53
39 36 33 31 30 27 24
63 65 66 69 71
13 16 17 19 21 23
69 68 67 65 63 62 60 58
83 86 89 91 94 97 98
79 78 76 74 72
16 17 19 21 23 24 27
87 86 85 84 83 80
21 22 23 26 28 29 31 33
46 48 51 52 54 57
81 79 77 76 74
78 80 82 84 87 89 91 92
53 54 55 58 60 62 64 67
75 72 69 66 63 62 61 60
75 72 69 67 66 65
15 18 19 20 21 22 25 27
79 82 84 87 89 90 91
47 44 43 41 39 38
76 79 80 83 85 88
12 9 7 5 2
41 44 46 49 52 53
83 85 87 90 93 94
32 29 27 24 22 19 16 14
68 67 66 64 61 58 57 56
49 46 43 42 40 39 37 34
72 69 66 65 63 62 59
34 37 38 40 42 44
45 44 42 41 38 37 36 35
25 23 21 20 17 14 11
34 31 29 28 25 22
61 62 65 67 69 72
28 30 32 33 36 38 41
28 30 33 35 36
6 8 9 12 14 15
90 92 93 94 96 98
55 58 60 63 64 67
17 20 21 23 25 27 30
82 83 86 89 91 93 94
83 81 78 75 73 72 70 69
74 75 77 80 82 84 85
81 83 86 87 88
50 48 47 45 43 42 39
42 45 48 49 50
80 81 84 86 89 92
63 65 66 68 71 74
33 31 29 26 23 21 19 16
24 27 28 29 32 33
54 56 58 59 61 64 65 67
75 77 78 80 82 83 85
71 74 75 76 78 80 82
36 38 39 41 44 45"""


print(Day2(input_data))
print(Day2Problem_Dampener(input_data))