#checking if an address is valid
#import re 
def check_web_address(text):
  pattern = r'^[a-zA-Z0-9_.+-]+[?:\[a-zA-Z]+)+$'
  result = re.search(pattern, text)
  return result is not None
#example usage
print(check_web_address("gmail.com"))
print(check_web_address("www@google.com"))


#import re
result = re.search(r"^(\W*) , (\w*)$", "lovelaca, ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])


#import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

#import re
def re_arrangename(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")
