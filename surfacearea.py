import math

def surfacearea():
    shape=input("Which shape' surface are do you want to find? cube or sphere?")
    done=0
    while done==0:
        try:
      
         if  shape == "cube":
            x=float(input("What is side length?"))
            surface_area = 6 * (x ** 2)
            surface_area=round(surface_area,2)
            print(f"The surface area of the cube is {surface_area}")
            done=1
         elif shape == "sphere":
            r=float(input("What is radius?"))
            surface_area = 4 * math.pi * r** 2
            surface_area = round(surface_area,2)
            print(f"The surface area of sphere is {surface_area}")
            done=1
         else:
            print("incorrect")
            done=1
        except:
            print("Error, not a number")

if __name__ == "__main__":
    surfacearea()

    
