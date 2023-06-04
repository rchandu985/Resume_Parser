import warnings
warnings.filterwarnings("ignore")
import textract
from resume_parser import resumeparse
#import docx
from model_keys import resume_keys
import re
from data_segration_model import extracted_data_processing
import json
from pdf2docx import Converter
import os

class process_incoming_files:
    availble_files=set()
    def incoming_processing(file):
        text = textract.process(f"incoming/{file}")

        op={}

        key=[]

        for r in str(text).split("\\n"):
            r=r.replace("\\t","").replace("xefx81xb6","").replace("xe2x80x99","").replace("xefx80xa0","").replace("xe2x80x93","").replace("xefx80xa0","")
            if r.endswith(":") or "&" in r:
                r=r.replace(":","").replace("&"," ")
            if r.endswith(" "):
                r=r[:len(r)-1]    
            if r.startswith(" "):
                r=r[1::]
                
            keys=resume_keys.all_keys()
            if r!="" :
                
                if r.lower().replace("_"," ").replace("-"," ") in keys:
                    #print("key",r.lower())
                    op.update({r.lower():[]})
                    
                    key.append(r.lower())
                else:
                    if len(key)>0:
                        #print("data",r)
                        op[key[-1]].append(re.sub(' +', ' ', r).replace("\\t","").replace("\\","").replace("xefx82xb7","").replace("xefx81xb6","").replace("xe2x80x99","").replace("xefx80xa0","").replace("xe2x80x93","").replace("xefx80xa0",""))
                    else:
                        #print("else",r,len(r))
                        pass

        output=extracted_data_processing.process(op,file)
        process_incoming_files.availble_files.add(file)
        #print(output)
        #print(op)
        
        with open(f"output/{file.replace('.docx','')}.json","a") as f:
            f.write(json.dumps([output],indent=4))
    
    def pdf_to_word_convert(file):
        #import aspose.words as aw
        pdf_file=Converter(f"incoming/{file}")
        file_name=file.replace('.pdf','').replace('.PDF','')
        pdf_to_word=pdf_file.convert(f"incoming/{file_name}.docx")

        process_incoming_files.incoming_processing(f"{file_name}.docx")

        process_incoming_files.availble_files.add(file)
        
    def load_file():
        for file in os.listdir("incoming/"):
            if file.endswith("docx"):
                process_incoming_files.incoming_processing(file)
            elif file.lower().endswith("pdf"):
                process_incoming_files.pdf_to_word_convert(file)
    def remove_processed_files():
        for file in process_incoming_files.availble_files:
            try:
                os.remove(f"incoming/{file}")
            except:
                continue
process_incoming_files.load_file()
#process_incoming_files.remove_processed_files()




""