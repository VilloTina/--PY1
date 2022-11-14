from pprint import pprint# TODO решить с помощью list comprehension и распечатать его
end = 15

pprint([{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(end+1)])