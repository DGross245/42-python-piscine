def NULL_not_found(object: any) -> int:
	objType = type(object)

	if (object is None):
		print("Nothing:", object, objType)
	elif (object != object):
		print("Cheese:", object, objType)
	elif (object == 0 and objType is int):
		print("Zero:", object, objType)
	elif (object == ""):
		print("Empty:", objType)
	elif (object is False):
		print("Fake:", object, objType)
	else:
		print("Type not Found")
		return (1)
	return (0)