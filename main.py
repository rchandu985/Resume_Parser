from pypdf import PdfReader
from model_keys import ResumeKeys
import json
import re
from pymongo import MongoClient
class PdfExtratcor:

    def __init__(self) -> None:
        pass

    def PdfFile(file_path):
        reader = PdfReader(file_path)

        return reader
    def TotalPages(file_path):
        return PdfExtratcor.PdfFile(file_path)._get_num_pages()
    
    def GetPdfFileText(file_path):

        text=""
        
        PdfFile=PdfExtratcor.PdfFile(file_path)

        get_total_pages=PdfExtratcor.TotalPages(file_path)
        
        for page_no in range(int(get_total_pages)):



            page = PdfFile.pages[page_no]
            text+="\n"+page.extract_text()
        
        return text.lower()



    def GetResumeBlocks(resume_text:str,stop_keywords):
        resume_text=resume_text.replace(":","").replace("","")
        
        final_data={}
        #print(resume_text)
        

        def get_exist_stop_keywords():

            keywords=[]
            rsm=resume_text.replace(":","")
            for kw in rsm.splitlines():
                    kw=re.sub(r'\s+', ' ', kw)
                    if  kw.startswith(' ') or kw.endswith(" "):
                        kw=kw.strip()
                    if kw in stop_keywords:
                        
                        keywords.append(kw)
                    #print(kw)
                       
            #exit()
            keywords__=[]
            for kws in keywords:
                if keywords.count(kws)<=1 and kws not in keywords__:
                    keywords__.append(kws)


            return keywords
        
        kws=get_exist_stop_keywords()
       
        final_data={kw:"" for kw in kws}
        
        v=False
        for rsm in resume_text.splitlines():
            rsm=re.sub(r'\s+', ' ', rsm)
            if  rsm.startswith(' ') or rsm.endswith(" "):
                rsm=rsm.strip()
            if rsm in kws:
                v=True
                c=rsm
                continue
            if v:
                rsm=rsm.replace("","").replace("","").replace("","")
                if not rsm.isspace() and len(rsm)>1:
                    #print(rsm)
                    final_data[c]+="\n"+rsm

        return final_data

input_file="incoming/Dice_Profile_Danyel_Teixeira.pdf"

ResumeText=PdfExtratcor.GetPdfFileText(input_file)
#print(ResumeText)
x=PdfExtratcor.GetResumeBlocks(ResumeText,set(ResumeKeys.StopKeys()))

con=MongoClient()

table=con['local']

table['test'].insert_one(x)