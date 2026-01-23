# an example of a superclass
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# an example of a subclass
class Fish(Animal):
    def __init__(self):
        super().__init__()  # superclass invocation! this invokes the (Animal) constructor class onto the Fish class

    def breathe(self):
        super().breathe()  # do everything the parent class does in its breathe method
        print(
            "doing this underwater."
        )  # and add on top of it to tweak it into our own breathe method

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
