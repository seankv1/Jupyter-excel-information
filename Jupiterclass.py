import tkinter as tk
import xlwt

root = tk.Tk()
root.geometry("400x300")
root.title("Data form")
root.resizable(0,0)

cid_label = tk.Label(root, text = "Student Id", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "Student Name", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "Address", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "State", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "City", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "Grade", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "Gender", font = ('calibre',10, 'bold') )
cid_label = tk.Label(root, text = "Age", font = ('calibre',10, 'bold') )


cid_var = tk.StringVar()
cname_var = tk.StringVar()
caddr_var = tk.StringVar()
cstate_var = tk.StringVar()
ccity_var = tk.StringVar()
cgrade_var = tk.StringVar()
cgender_var = tk.StringVar()
cage_var = tk.StringVar()


cid_entry = tk.Entry(root, textvariable = cid_var, font=('calibre',10,'normal'))
cname_entry = tk.Entry(root, textvariable = cname_var, font=('calibre',10,'normal'))
caddr_entry = tk.Entry(root, textvariable = cstate_var, font=('calibre',10,'normal'))
cstate_entry = tk.Entry(root, textvariable = ccity_var, font=('calibre',10,'normal'))
ccity_entry = tk.Entry(root, textvariable = cgrade_var, font=('calibre',10,'normal'))
cgrade_entry = tk.Entry(root, textvariable = cgender_var, font=('calibre',10,'normal'))
cid_entry = tk.Entry(root, textvariable = cage_var, font=('calibre',10,'normal'))



cid_label.grid(row=0, column=0)
cid_entry.grid(row=0, column=1)

cname_label.grid(row=1, column=0)
cname_entry.grid(row=1, column=0)

caddr_label.grid(row=2, column=0)
caddr_entry.grid(row=2, column=0)

cstate_label.grid(row=3, column=0)
cstate_entry.grid(row=3, column=0)

ccity_label.grid(row=4, column=0)
ccity_entry.grid(row=4, column=0)

cgrade_label.grid(row=5, column=0)
cgrade_entry.grid(row=5, column=0)

cgender_label.grid(row=6, column=0)
cgender_entry.grid(row=6, column=0)

cage_label.grid(row=7, column=0)
cage_entry.grid(row=7, column=0)

def submit():
    cid = cid_var.get()
    cname = cname_var.get()
    caddr = caddr_var.get()
    cstate = cstate_var.get()
    ccity = ccity_var.get()
    cstate = cstate_var.get()
    cgrade = cgrade_var.get()
    cgender = cgender_var.get()
    cage = cage_var.get()

    workbook =xlwt.Workbook()

    sheet = workbook.add_sheet("StudentInfo")
    sheet.write(0,0, "Student Details Info")
    sheet.write(1,0,"Student ID")
    sheet.write(2,0,"Name")
    sheet.write(3, 0, "Address")
    sheet.write(4, 0, "State")
    sheet.write(5, 0, "City")
    sheet.write(6, 0, "Grade")
    sheet.write(7, 0, "Gender")
    sheet.write(8, 0, "Age")


    sheet.write(1,1,cid)
    sheet.write(2,1,cname)
    sheet.write(3, 1, caddr)
    sheet.write(4, 1, cstate)
    sheet.write(5, 1, ccity)
    sheet.write(6, 1, cgrade)
    sheet.write(7, 1, cgender)
    sheet.write(8, 1, cage)


    workbook.save("mystudents.xls")

    cid_var.set("")
    cname_var.set("")
    caddr_var.set("")
    cstate_var.set("")
    ccity_var.set("")
    cgrade_var.set("")
    cgender_var.set("")
    cage_var.set("")

sub_button = tk.Button(root, text = 'Submit the Data', command = submit)
sub_button.grid (row =9, column = 1)
root.mainloop()

