
quitme = False



print("What problem do you want to solve?")
print("1. Floatation")
print("2. Springs")
escolha = input()
if(escolha=="1"):
    angle = 30
    velocity = 30
    viscosity = 1
    gravity = 9.81
    mass = 10
    densityObj= 0.2
    densityFlu= 1
    volumObj= 50
    volumFlu = 1

    print('Firing at %.2f degrees, at %.2f m/s' % (angle, velocity))
    print('Viscosity is %.2f, gravity is %.2f' % (viscosity, gravity))
    while(quitme == False):
        print('Object properties: Mass=%.2f, Density=%.2f, Volume=%.2f' % (mass, densityObj, volumObj))
        print('Fluid has a density of %.2f, gravity is %.2f' % (densityFlu, gravity))
        
        fb = densityFlu * gravity * volumObj
        fg = mass * gravity
        print('%f , %f' % (fb, fg))

        if(fb > fg):
            volumInW = fg / (densityFlu * gravity)
            depth = volumInW / ((volumObj ** (1/3)) ** 2)
            centerM = ((volumObj ** (1/3)) / 2) - depth
            print('Object would float at %f meters' % (centerM))

        else:
            print('The object would sink')
        



        first, changing, number = input().split()
        if (changing == "gravity"):
            gravity = float(number)
            print('%.2f' % (gravity))
        
        elif(changing == "mass"):
            mass = float(number)
            print('%.2f' % (mass))
            volumObj = mass / densityObj
            print('%.2f' % (volumObj))
            

        elif(changing == "volume"):
            volumObj = float(number)
            print('%.2f' % (volumObj))
            mass = volumObj * densityObj
            print('%.2f' % (mass))

        elif(changing == "densityF"):
            densityFlu = float(number)
            print('%.2f' % (densityFlu))
        else:
            print("Insert a valid change Ex: set gravity/densityF/mass/volume 10")


elif(escolha=="2"):
    mass = 1.5
    gravity = 9.81
    springR = 0.5
    constant = 0.2
    while (quitme == False):
        print("Object mass is %.2f, gravity is %.2f" % (mass, gravity))
        print("Base spring length is %.2f, constant = %.2f" % (springR, constant))
        
        fg = mass * -gravity
        print('%f'%(fg))
        L = (fg / -constant) + springR
        print('Spring would stretch to %f meters' % (L))


        first, changing, number = input().split()
        if (changing == "gravity"):
            gravity = float(number)
            print('%.2f' % (gravity))
            
        elif(changing == "mass"):
            mass = float(number)
            print('%.2f' % (mass))

        elif(changing == "springR"):
            springR = float(number)
            print('%.2f' % (springR))

        elif(changing == "constant"):
            constant = float(number)
            print('%.2f' % (constant))
        else:
            print("Insert a valid change Ex: set gravity/mass/springR/constant 10")

else:
    print("Pls select a valid problem (1 or 2)")
