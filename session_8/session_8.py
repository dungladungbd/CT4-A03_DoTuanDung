class Pet:
    def __init__(self):
        self.name = 'hehe'
        self.weight = 5
        self.skills = []

    def feed(self):
        self.weight += 1

    def teach(self, skill):
        self.skills.append(skill)


class Dog(Pet):
    def roar(self):
        print("Chit chit")
    def hi(self):
        print(self.kind)

class Timer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1

    def reset(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0


def get_seconds(hours, minutes, seconds):
    time = 3600 * hours + 60 * minutes + seconds
    return time

# number_of_second = get_seconds(25, 60, 1)
# timer = Timer()
# for i in range(number_of_second):
#     timer.tick()

# print(timer.hours, timer.minutes, timer.seconds)
