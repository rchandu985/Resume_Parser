from DataProcessing.PdfExtractor import PdfFileTextExtratcor
from DataProcessing.resume_data_processor import load,resume
from pymongo import MongoClient





input_file=r"incoming_resumes\Dice_Profile_Ashish_Bandgar (1).pdf"

x=PdfFileTextExtratcor.GetPdfFileText(input_file)
y=load.stop_keywords()
z=resume.blocks(x,y)

a=resume.constant_data_seggragator(z,y)
print(a)


db=MongoClient()
tb=db['local']
c=tb['test']
c.insert_one(a)
