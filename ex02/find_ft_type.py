def all_thing_is_obj(object: any) -> int:
	objType = type(object)
	types = {
		list : "List",
		tuple : "Tuple",
		set : "Set",
		dict : "Dict",
	}
	found_type = types.get(objType)

	if (objType == str):
		print(object, "is in the kitchen :", objType)
	elif (objType != int):
		print(found_type + " :", objType)
	else:
		print("Type not found")
	return (42)