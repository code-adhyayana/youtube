sample_html = '''<!DOCTYPE html><html><head><style>table,th,td {border: 1px solid black;border-collapse: collapse;padding: 6px;}</style></head><body style="text-align:center"><table align="center"><tr><th>Job Name</th><th>Batch</th></tr>'''

process_data = [('Job_1', 20),
                ('Job_2', 20),
                ('Job_3', 20),
                ('Job_4', 30),
                ('Job_5', 30),
                ('Job_6', 40)]

count_value = 0
seq_details = []

def add_to_sequence(seq_list, count_value):
	already_noted = False
	for i in range(count_value):
		if not already_noted:
			seq_list.append(count_value)
			already_noted = True
		else:
			seq_list.append(0)

pre_value = None

for process in process_data:
	num_value = process[1]
	if pre_value == num_value:
		count_value += 1
	else:
		add_to_sequence(seq_details, count_value)
		pre_value = num_value	
		count_value = 1

add_to_sequence(seq_details, count_value)

table_data = ""
i = 0
for item in process_data:
	table_data += f'<tr><td>{item[0]}</td>'
	if seq_details[i]:
		table_data += f'<td rowspan="{seq_details[i]}">{item[1]}</td>'
	table_data += '</tr>'
	i += 1

sample_html += table_data
sample_html += '''</table></body></html>'''

with open('report.html','w') as w_file:
	w_file.write(sample_html)
