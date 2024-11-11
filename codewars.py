
# Even Or Odd

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# Convert a number to a string
def number_to_string(num):
    return str(num)
    x = str(124)
    print(x)

# Vowel Count
def get_count(sentence):
    count = 0
    for i in sentence:
        if i in "aeiouAEIOU":
            count = count + 1
    return count
