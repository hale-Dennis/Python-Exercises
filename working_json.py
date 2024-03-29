import json 

person = {
    "Bob":{
        "name": "Bob",
        "city": "Accra",
        "phone": "495943"
    },
    "Dennis":{
        "name": "Dennis",
        "city": "Sunyani",
        "phone": "356234"
    }
}

s = json.dumps(person)

#f = open(r"C:\Users\MY SAMSUNG LAPTOP\Desktop\python\exercises\phone.txt", "w")
#f.write(s)

f = open(r"C:\Users\MY SAMSUNG LAPTOP\Desktop\python\exercises\phone.txt", "r")
new_dict = json.loads(f.read())
print(type(new_dict))