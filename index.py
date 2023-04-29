import sys

TOKEN="TICKET"
TEMPLATE_URL="https://url/option="+TOKEN
file_path = str(sys.argv[1])

print("File name {}".format(file_path))

# reading file line by line 
file1 = open(file_path, "r")
lines = file1.readlines()

# for each content of the file
for line in lines:

    # creating the API call
    URL=TEMPLATE_URL.replace(TOKEN, line.strip())

    print("{}".format(URL))


