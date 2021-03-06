# Need to change these variables
input_file = None
output_file = None
num_columns = None

# Make sure user changes input variables
if num_columns == None or input_file == None or output_file == None:
    return "Please change input variables"

# Open the txt file
file = open(input_file, 'r', encoding = "utf-8")

# Read the file
new_text = file.readlines()

# Create a list to keep all the words in file
words = []
line_break = 0

# Add all the words in file to list
for x in range(0, len(new_text)):
    for word in new_text[x].split():
        words.append(word + ',')

# Write words into csv file
f = open(output_file,'w')
for x in range(0, len(words)):
    if (line_break == num_columns):
        f.write('\n')
        f.write(words[x])
        line_break = 1
    else:
        f.write(words[x])
        line_break += 1
f.close()
