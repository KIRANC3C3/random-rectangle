from fpdf import FPDF, HTMLMixin
#from r1 import outr1
import random
x=int(input("how many pdf's do you need?"))
y=int(input("how many tables do you need?"))


class PDF(FPDF, HTMLMixin):
    pass
for i in range(x):
    pdf = PDF()
    pdf.add_page()
    # specify font
    pdf.set_font('helvetica', '', 16)
    #pdf.cell(0,0, 'A cell with some words')
    for j in range(y):

         pdf.write_html("""
         <table  width = 30%>
                  <thead>
                     <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
                     <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
                     
                    <tr>
                      <th align="left" width="30%">X</th>
                      <th align="left" width="70%">Y</th>
                    </tr>
                  </thead>
                <tbody>
                    <tr>
                      <td>1</td>
                      <td>2</td>
                    </tr> 
                    <tr>
                      <td>3</td>
                      <td>4</td>
                    </tr>
                </tbody>  
         </table>           
         
                   
         </section>
         """)
                      

    pdf.output('pdf_table{}.pdf'.format(i),'F')
x_val=[1,3]
y_val=[2,4]

total_pdfs= [ ]
for k in range(x):
    srt1="pdf_table{}.pdf".format(k)
    total_pdfs+=[srt1]
print("Total number of pdf's with their coordinates:"+ str(total_pdfs))


