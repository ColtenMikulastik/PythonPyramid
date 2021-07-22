
print("Hello, I'm going to pyramid your text string that you give me!")
in_pyr = input("What would you like to pyramid?")

# create the print thing
print_me = []
# make string into a list
in_pyr = list(in_pyr)
print(in_pyr)


# start with popping letters off of the input string
for i in range(0, len(in_pyr)):
    print_me.append(in_pyr[i])
    print(print_me)

# go back the way you came boi
for i in range(0, len(in_pyr)):
    print_me.pop()
    print(print_me)

# or we can do the other pyr
# variable for length of your input
l_of_in = len(in_pyr)
# and space amount
spaces_am = l_of_in
# reversed input string variable
rev_in = in_pyr.copy()
rev_in.reverse()

for i in range(0, l_of_in):
    spaces_am = spaces_am - 1
    # first buffer loop
    for sp1 in range(0, spaces_am):
        print(' ', end='')
    # printing list backwards
    for j in range(spaces_am, l_of_in):
        print(rev_in[j], end='')
    # print list normally
    for j in range(1, l_of_in - spaces_am):
        print(in_pyr[j], end='')
    # print ending spaces
    for sp1 in range(0, spaces_am):
        print(' ', end='')
    print('\n', end='')
# this is gonna suck



