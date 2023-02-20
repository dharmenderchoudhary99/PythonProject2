import pywhatkit  as pw

txt="""Python i a awesome language having huge libraries
It is used in web, ml, ai , data scientist field"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END ")