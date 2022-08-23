'''
    #This an acceptable code that generates n number rectangles that do not overlap on each other.

    #This is an optimised version where we can optimise the space on the 1000x1000 page.

    #Removing the perfect_square() check and perfect_square_rect() functions and using only one function that contains the break_value variable
    and renaming that to generate_rectangles()

    #In the optimised one if we provide n=9 then a 3x3 grid will be generated and 9 rectangles will be generated.

    #But now for n=9 a 4x4 grid will be generated and 9 rectangles are drawn leaving the other 7.
    And for n=15 a 4x4 grid will be generated and 15 rectangles are drawn leaving the ONE.

    #Rectangles are drawn like the numbers in the numberpad on our keyboard.
    Ex: for n=9;
    row1:1st rectangle will be generated at number 1 block,then 2,then 3,then4 ,and then row2 starts filling with the 4th on top of 1st....

    #Here space on the page is not optimised.

    #for every n there will be a k that satisfies k**2==n and if we provide n then instead of kxk grid (k+1)x(k+1) grid will be generated.

    #resulting a maximum of '(2k+1)' rectangles space being unoptimised and a minimum of 'ONE' rectangle space being unoptimised.

    Ex: for n=9 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 7(max 2k+1) rectangles space being unoptimised
    i.e., (2*3+1).
    Ex: for n=10 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 6 rectangles space being unoptimised
    i.e., ((2*3+1)-1).
    Ex: for n=11 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 5 rectangles space being unoptimised
    i.e., ((2*3+1)-2).
    Ex: for n=12 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 4 rectangles space being unoptimised
    i.e., ((2*3+1)-3).
    Ex: for n=13 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 3 rectangles space being unoptimised
    i.e., ((2*3+1)-4).
    Ex: for n=14 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 2 rectangles space being unoptimised
    i.e., ((2*3+1)-5).
    Ex: for n=15 we have k=3 i.e., 3**2==9 then 4x4 grid will be generated. resulting a maximum of 1(min 1) rectangles space being unoptimised
    i.e., ((2*3+1)-6).
    Ex: for n=16 we have k=4 i.e., 4**2==16 then 5x5 grid will be generated. resulting a maximum of 9(max 2k+1) rectangles space being unoptimised
    i.e., (2*4+1).

    #In the previous one we got maximum of 2k and minimum of 1 rectangle space being unoptimised.
    #But in this below code
                     we got a maximum of (2k+1) and minimum of 1 rectangle space being unoptimised.

        Which is completely acceptable where the difference between the max unoptimised rectangles is ONE.

'''

from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
import random

n = int(input("How many number of rectangles do you need?: "))

c = canvas.Canvas("pdf_table{4}.pdf", pagesize=(1000,1000))

def generate_rectangles():
    '''
    #This function is called when n is NOT a percect square of some number.
    #A function to generate n number of rectangles.
    #plotting rectangles starts from origin and goes along x axis.
    #i)if we want to generate 8 rectangles then 3x3 grid will be generated and
    #ii)rectangles are plotted inside each grid with random dimensions.
    #iii)Ex:1st rectangle with center (x1,y1) then ,(x2,y1),(x3,y1),etc...
    #2 Rectangles: (x1,y3),(x2,y3),*( x3,y3) THIS RECTANGLE WILL NOT BE PLOTTED*  #line eqn: y3=constant
    #3 Rectangles: (x1,y2),(x2,y2),(x3,y2)                                        #line eqn: y2=constant
    #3 Rectangles: (x1,y1),(x2,y1),(x3,y1)                                        #line eqn: y1=constant
    #iv)Total 8 centers for 8 rectangles.
    '''

    x=[' ']*(k+1)
    k_part = 0

    while (k_part<k+1):
        x[k_part]=int(k_part*(1000/k))
        k_part+=1
    print('.'*100)
    print('.'*100)
    print('Vertical Lines Which Are Rectangles Borders',x)
    y = x

    xy_tups = []
    ci=0
    while (ci<len(x)-1):
        if ci==(len(x)-1):
            xi = (x[ci-1]+x[ci])/2
            yi = (y[ci-1]+y[ci])/2
            xy_tups.append((int(xi),int(yi)))
        else:
            xi = (x[ci]+x[ci+1])/2
            yi = (y[ci]+y[ci+1])/2
            xy_tups.append((int(xi),int(yi)))

        ci+=1

    x_center = []
    for ele in xy_tups:
        x_center.append(ele[0])

    y_center = []
    for ele in xy_tups:
        y_center.append(ele[1])


    print('-'*100)
    print('-'*100)
    print("x center:" ,x_center)
    print('-'*100)
    print('-'*100)
    print("y center",y_center)


    main_coords = []
    break_val = 1
    for ele_y in y_center:
        for ele_x in x_center:

    #for ele_x in x_center:
        #for ele_y in y_center:
            if break_val<n+1:
                w = random.randrange(int(30/k),int(1000/k))
                h = random.randrange(int(30/k),int(1000/k))
                c.rect(ele_x,ele_y,w,h)
                main_coords.append((ele_x,ele_y,w,h))
                break_val+=1

    print('-'*100)
    print('-'*100)
    print('MAIN COORDINATES LIST',main_coords)
    print('-'*100)
    print('-'*100)
    print('Length of the main_coords list',len(main_coords))
    print('-'*100)
    print('-'*100)


    c.save()
    print("Pdf generated....")
    print('.'*100)
    print('.'*100)

i_val = [i for i in range(int(n**0.5+1))][-1]+1
k=i_val
generate_rectangles()
