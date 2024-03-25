def get_cats_info(path):
    data_list =  []
    with open(path, "r+") as cat_info:

        cat_info.seek(0)
        cat_info.write("\n")

        for line in (cat_info):
            dictionary = {"id:" : "" , "name" : "" , "age" : ""}

            line = line.split(",")

            dictionary.update({"id:" : line[0]})
            dictionary.update({"name:" : line[1]})
            dictionary.update({"age:" : line[2]})

            data_list.append(dictionary)
    return data_list

print(get_cats_info("cats_info.txt"))