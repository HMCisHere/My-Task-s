
person1 = {"age": 25, "name": "Ali", "last_name": "Gay", "city": "Tehran", "gender": "Female"}
person2 = {"age": 30, "name": "Radin", "last_name": "Gay", "city": "Urmia", "gender": "Male"}
person3 = {"age": 40, "name": "Ali", "last_name": "Nmd", "city": "Urmia", "gender": "Male"}
person4 = {"age": 35, "name": "Radin", "last_name": "Lez", "city": "Urmia", "gender": "Female"}
person5 = {"age": 28, "name": "Radin", "last_name": "Nmd", "city": "Kish", "gender": "Female"}
person6 = {"age": 32, "name": "Mamad", "last_name": "Nmd", "city": "Urmia", "gender": "Male"}
person7 = {"age": 49, "name": "Radin", "last_name": "Lez", "city": "Tehran", "gender": "Male"}
person8 = {"age": 27, "name": "Mamad", "last_name": "Ob", "city": "Tehran", "gender": "Female"}
person9 = {"age": 38, "name": "Ali", "last_name": "Lez", "city": "Tehran", "gender": "Female"}
person10 = {"age": 3, "name": "Ibo", "last_name": "Gay", "city": "Tehran", "gender": "Male"}
people = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]
#-------------------------------------------------------------------------------------------------------
def filter_people(people, filters):
    filtered_people = people[:]
    for key, value in filters.items():
        if key == "age":
            min_age, max_age = map(int, value.split("-"))
            filtered_people = [person for person in filtered_people if min_age <= person["age"] <= max_age]
        else:
            filtered_people = [person for person in filtered_people if person[key] == value]
    return filtered_people
#-------------------------------------------------------------------------------------------------------
filters = {}
filters["name"] = input("name en(Enter bezan aghe ba in filter nmikoni): ")
filters["last_name"] = input("last name en(Enter bezan aghe ba in filter nmikoni): ")
filters["gender"] = input("gender en(Enter bezan aghe ba in filter nmikoni): ")
filters["city"] = input("city en(Enter bezan aghe ba in filter nmikoni): ")
age_filter = input("age nemoone => min_age-max_age en(Enter bezan aghe ba in filter nmikoni): ")
if age_filter:
    filters["age"] = age_filter
#-------------------------------------------------------------------------------------------------------
filtered_people = filter_people(people, {key: value for key, value in filters.items() if value})
if filtered_people:
    print("Filter shode ha:")
    for person in filtered_people:
        print(person)
else:
    print("baangh?")

