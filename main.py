from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QPlainTextEdit
from datetime import datetime, timedelta
import random
import time

gtime = datetime.now()

class animals:

    status_healthy = "Healthy"
    status_hurt  = "Hurt"
    status_dead = "Dead"
    __zoo = []
    max_cap = 100

    def __init__(self,idx):
        self.__idx = idx
        self.__status = self.status_healthy
        self.__healthlevel = 100

    def getIdx(self):
        return self.__idx

    @classmethod
    def saveobj(cls,animal):
        cls.__zoo.append(animal)

    @classmethod
    def getObjcount(cls):
        return len(animals.__zoo)

    @classmethod
    def getObjData(cls,idx):
        return animals.__zoo[idx]

    @classmethod
    def getanimalsinfo(cls):
        return cls.__zoo

    #All the methods will use by sub class
    def setAnimalType(self,animaltype):
        self.__animalType = animaltype

    def getAnimalType(self):
        return self.__animalType

    def setHealthStatus(self,status):
        self.__status = status

    def getHealthStatus(self):
        return self.__status

    def setHealthLevel(self, healthlevel):
        self.__healthlevel = float(healthlevel)

    def getHealthLevel(self):
        return self.__healthlevel

    #Print animals Information
    def print_animals_info(self):
         print(self.getAnimalType(), "is created with ", "ID=", self.getIdx(), ", Health Status=",
          self.getHealthStatus(), ", Health Level=", self.getHealthLevel())

    #Generate random floating point numbers between two specified numbers
    @classmethod
    def generate_Random(cls,min,max):
        return (round(random.uniform(min,max),2))

    #Update Each Animal Status
    def update_health_status(self):
        #Get Health Level of each animal
        if(self.getHealthStatus() == animals.status_dead):
            return 0
        elif((self.getAnimalType() == "Elephant") and (self.getHealthLevel() < self.getThreshold())):
            self.setHealthStatus(animals.status_hurt)
        elif((self.getAnimalType() == "Elephant") and (self.getHealthLevel() > self.getThreshold())):
            self.setHealthStatus(animals.status_healthy)
        elif(self.getHealthLevel() < self.getThreshold()):
            self.setHealthStatus(animals.status_dead)

    #Reduce animals health
    def reduce_health(self,value):
        new_health_value = round((self.getHealthLevel() - value),2)
        self.setHealthLevel(new_health_value)
        self.update_health_status()
        self.print_all_instances()

    #Increase animals health
    def feed_animal(self,value):
        new_health_value = round((self.getHealthLevel() + value), 2)
        self.setHealthLevel(new_health_value)
        #print("Feed, New Value=",value,"Current Level=",self.getHealthLevel(), "with ID=", self.getIdx())
        self.update_health_status()
        self.print_all_instances()

    #Test method starts
    def testmethod(self):
        print("Test method starts...")
        #for obj in animals.getanimalsinfo():
        #    print(obj.getAnimalType())
        print(animals.getObjData(2).getAnimalType())
        print("Test method ends...")
    #Test method ends


    def update_ui(self):
        totalanimals = animals.getObjcount()
        display_str = ''
        for i in range(0, totalanimals):
            display_str += animals.getObjData(i).getAnimalType() \
                     + animals.getObjData(i).getIdx() + ", Health: " + str(
                animals.getObjData(i).getHealthLevel()) + ", Health Status: " + animals.getObjData(
                i).getHealthStatus() + "\n"
        output_multi_text.setPlainText(display_str)


    def reduce_all_animals_health(self):
        print("Reduce Health All Animals......")
        display_str = ''
        for obj in animals.getanimalsinfo():
            value = animals.generate_Random(0,20)
            obj.reduce_health(value)
        self.update_ui()
        

    def feed_all_animals_health(self):

        print("Feed Health All Animals...")
        for obj in animals.getanimalsinfo():
            value = animals.generate_Random(10,25)
            if(obj.getHealthLevel() >= animals.max_cap):
                print("It is greater than 100" , obj.getHealthLevel(), obj.getIdx())
            else:
                obj.feed_animal(value)
        self.update_ui()



    def print_all_instances(self):
        self.print_animals_info()

class monkey(animals):

    __animaltype = "Monkey"
    __threshold = 30

    def __init__(self,idx):
        animals.__init__(self,idx)
        self.setAnimalType(self.__animaltype)
        self.print_animals_info()

    # class method used as factory method
    @classmethod
    def getMonkeyObj(cls,idx):
        return monkey(idx)

    def getThreshold(self):
        return self.__threshold

class elephant(animals):

    __animaltype = "Elephant"
    __threshold = 70

    def __init__(self,idx):
        animals.__init__(self,idx)
        self.setAnimalType(self.__animaltype)
        self.print_animals_info()

    #class method used as factory method
    @classmethod
    def getElephantObj(clsc,idx):
        return elephant(idx)

    def getThreshold(self):
        return self.__threshold

class giraffe(animals):

    __animaltype = "Giraffe"
    __threshold = 50

    def __init__(self,idx):
        animals.__init__(self,idx)
        self.setAnimalType(self.__animaltype)
        self.print_animals_info()

    #class method used as factory method
    @classmethod
    def getGiraffeObj(cls,idx):
        return giraffe(idx)

    def getThreshold(self):
        return self.__threshold

def reduceHealth():

    one_hour_lapse()
    #Call Class Method
    obj = animals.getObjData(1)
    if(obj):
        obj.reduce_all_animals_health()

def feedAnimals():
    obj = animals.getObjData(1)
    if(obj):
        obj.feed_all_animals_health()

def one_hour_lapse():
    global gtime
    one_hour_from_now = gtime + timedelta(hours=1)
    gtime = one_hour_from_now
    date_str = gtime.strftime("%H:%M:%S")
    output_label.setText(date_str)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Test Simulation')
layout = QVBoxLayout()

btnreduce_health = QPushButton('Reduce Health')
layout.addWidget(btnreduce_health)
btnreduce_health.clicked.connect(reduceHealth)

btnfeed_animals = QPushButton('Feed Animals')
layout.addWidget(btnfeed_animals)
btnfeed_animals.clicked.connect(feedAnimals)

output_multi_text = QPlainTextEdit('This is test')
layout.addWidget(output_multi_text)

display_text = QLabel('Time Zone')
layout.addWidget(display_text)

output_label = QLabel('')
layout.addWidget(output_label)


#Populate animals
idx = 0
for i in range(1,6):
    idx = idx + 1
    animals.saveobj(monkey.getMonkeyObj(str(idx)))
    idx = idx + 1
    animals.saveobj(giraffe.getGiraffeObj(str(idx)))
    idx = idx+1
    animals.saveobj(elephant.getElephantObj(str(idx)))


totalanimals = animals.getObjcount()
mydict = {}
strr = ''

for i in range(0,totalanimals):
    strr += animals.getObjData(i).getAnimalType() \
           + animals.getObjData(i).getIdx() + ", Health: "+str(animals.getObjData(i).getHealthLevel()) +", Health Status: "+animals.getObjData(i).getHealthStatus() + "\n"
output_multi_text.setPlainText(strr)

window.setLayout(layout)
window.show()
app.exec()