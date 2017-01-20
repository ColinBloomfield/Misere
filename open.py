with open(/home/colin/workspace/MathCode/triangle.txt, 'r', encoding='utf-8') as a_file:
	S = [tuple(int(x) for x in line.split()) for line in a_file]

print(S)
