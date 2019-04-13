Read Me File
-------------

Author: Avinash Shanker
UTA ID: 1001668570
NET ID: AXS8570
Date: 31-Jan-2019

This program has been written in Python Version 3.0

Usage Information:
For Uninformed Search
>>python find_route.py input1.txt Bremen Kassel

For Informed Search with heuristic Data
>>python find_route.py input1.txt Bremen Kassel h_kassel.txt

General Flow of Program.
1. If three arguments are passed to the code main function will check the number of arguments and perform Uninformed Search
2. If four arguments are passed to the code main will perform Informed Search
3. Based on the number of arguments called Main() will call ISearch() or USearch() Class
4. USearch class will call Setup_Map() which will setup the Graph from the input provided
5. Fringe variable of dqueue type is taken which expandes nodes based in on only f(n) value
5. ISearch class will call Setup_Map() and Setup_Heuristic() which will setup Graph and heuristic Data
7. In Informed search Frige will expand based on f(n)+g(n) value

