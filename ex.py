f = open("grammar","w")

'''
<item>
        1 <tag>
          out.operand="1";
        </tag>
      </item>
'''

for i in range(0,501):
    f.write("<item>")
    f.write(str(i) + "<tag>")
    f.write("out.operand=\""+str(i)+"\"")
    f.write("</tag>")
    f.write("</item>")
    f.write("\n")