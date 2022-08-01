# o = open("newfile.txt","r")
# print(o.name)
# print(o.mode)
# o.close


# using context manger




# with open("newfile.txt","r") as o :
    
    # contents = o.read()
    # mycontent = o.readlines()

# print(mycontent)
# for n in mycontent:
    # print(n)
    # mycontent = o.read(10)
    # print(mycontent)



# with open("newfile.txt","r") as o :
#     size_of_content = 30
#     mycontent = o.read(size_of_content)
#     while len(mycontent)>0:
#         print(mycontent,end="/")
#         mycontent=o.read(size_of_content)

with open("newfile2.txt","w") as g :
    g.write("<h1> welcome</h1>\n")
    g.write("<h2> welcome</h2>\n")
    g.write("<h3> welcome</h3>")
    g.write("<h4> welcome</h4>")
    g.write("<h5> welcome</h5>")