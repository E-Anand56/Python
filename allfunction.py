class function():
    subfields=["Machine Learning ","Neural Networks","Vision","Robotics","Speech Processing ","Natural Language Processing "]
    def SubfieldsInAI():
        print("Sub-fields in AI are: ")
        for temp in subfields:
            print(temp)

    def OddEven():
        if num%2==0:
            print("even")
            msg="even"
        else:
            print("odd")
            msg="odd"
        return msg

    def mrgelegibility():
        if (cate=="male") and (age>=21):
            print("eligible for marriage")
            msg="eligible for marriage"
        elif(cate=="female") and (age>=18):
            print("eligible for marriage")
            msg="eligible for marriage"
        else:
            print("not eligible for marriage")
            msg="not eligible for marriage"
        return msg

    cate=input("enter a category:")
    age=int(input("enter a age:"))
    msg=mrgelegibility()

    def triangle():
        area=(height1*breath)/2 
        print(f"Area:{area}")
        Perimeter_formula= height1+height2+breath 
        print(f"Perimeter_formula:{Perimeter_formula}")

    

    
    
        
    
    