langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

langs.pop(3)
langs.pop()
print(langs)

langs.remove("Ruby")
print(langs)

langs = list()

langs.append("Python")
langs.append("Perl")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))
print(langs)