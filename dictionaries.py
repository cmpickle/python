dict = { "one":1, "two":2, "three":3}

print("Print out the dictionary:")

print(dict)

print("print the key value of dict[\"one\"]")

print(dict["one"])

print("update the dictionary to binary values and add the value of four and print it out:")

dict["one"] = '001'
dict["two"] = '010'
dict["three"] = '011'
dict.update({"four":'100'})

print(dict)