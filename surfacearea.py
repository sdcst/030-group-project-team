def surfacearea():
    import math
    done=0
    while done==0:
        shape=input("Which shape's surface are do you want to find? cube [c] or sphere [s]: ")
        try:
      
         if  shape == "cube" or shape == "Cube" or shape == "c" or shape == "C":
            x=float(input("What is the side length? "))
            surface_area = 6 * (x ** 2)
            surface_area=round(surface_area,2)
            print(f"The surface area of the cube is {surface_area}")
            done=1
         elif shape == "sphere" or shape == "Sphere" or shape == "S" or shape == "s":
            r=float(input("What is the radius? "))
            surface_area = 4 * math.pi * r** 2
            surface_area = round(surface_area,2)
            print(f"The surface area of the sphere is {surface_area}")
            done=1
         else:
            print("error: invalid answer, try again: ")
        except:
            print("error, not a number")

if __name__ == "__main__":
    surfacearea()