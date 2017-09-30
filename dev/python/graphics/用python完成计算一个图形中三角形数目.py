
#!/usr/bin/python

"""
---------------------------------------------------------------------------------------------------
2015.07.23  Grey　 www.iplaypy.com
***************************************************************************************************
Counter all the triangles in a picture
---------------------------------------------------------------------------------------------------
"""

import itertools,string

def CounterTriangle():
	print "All the triangles we can find in the picture are as follows:"
	triangle_number    = 0
	sides_match_list   = ['abh','acgi','adfj','aek','bcde','efgh','hijk']
	dot_list           = []
	i = 0
	while i < 26:
		dot_list.append(string.lowercase[i])
		if string.lowercase[i] == 'k':
			break
		else:
			i += 1
	for each_combination in itertools.combinations(dot_list,3):
		triangle_flag = True
		for each_dot_combination in itertools.combinations(each_combination,2):
			for each_side in sides_match_list:
				if each_dot_combination[0] in each_side and each_dot_combination[1] in each_side:
					triangle_flag = True
					break
				else:
					triangle_flag = False
			else:
				triangle_flag = False
				break
		line_flag = False
		for each_side in sides_match_list:
			if each_combination[0] in each_side and each_combination[1] in each_side and each_combination[2] in each_side:
				line_flag = True
		if triangle_flag == True and line_flag == False:
			triangle_number += 1
			print "%d : %s" % (triangle_number,each_combination)
	print "The number of triangles in the picture is : %d" % triangle_number

CounterTriangle()
		
