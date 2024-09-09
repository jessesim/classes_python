# class initializing parents and children together
class Parents_Children: 
    def __init__(self, parent, child):
        self.parent = parent 
        self.child = child
# class initializing dog name, breed, and behavior
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # dog biting function
    def bite(self, family):
        return f"The {self.breed} named {self.name} bit {family.parent}'s child, {family.child}... shame on them"
# parents and children stored by family last name
smiths = Parents_Children("Bob and Martha", "Florence")
patels = Parents_Children("Reese and Pablo", "Michael")
# dog name and breed stored by family name
smiths_dog = Dog("Fido", "Pitbull")
patels_dog = Dog("Bruce", "German Shepard")   
# dog bite sccenarios 
bite_1 = smiths_dog.bite(patels)
bite_2 = patels_dog.bite(smiths)

print(bite_1)
print(f"In retaliation {bite_2} as well")