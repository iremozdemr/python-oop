class Car:

    wheels = 4
    num_of_cars = 0
    #class variable
    #tüm objeler aynı variable'ı kullanır

    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color
        #her objenin kendi variable'ı vardır

        Car.num_of_cars += 1
        #her obje oluşturulduğunda 1 arttırılır
    #constructor

    def __str__(self):
        return f"{self.model} {self.year} {self.color}"

    def drive(self):
        print(f"you drive the {self.model}")
    #self yazılmazsa hata veriyor

    def stop(self):
        print(f"you stop the {self.model}")
    #self yazılmazsa hata veriyor

    def describe(self):
        print(f"model:{self.model} year:{self.year} color:{self.color}")