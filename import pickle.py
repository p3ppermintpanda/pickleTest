import pickle

example_dict = {1:"100", 2:"200", 3:"300"}

pickle_out = open("dict.pickle", "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
print("finished")

pickle_in = open("dict.pickle", "rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[3])

