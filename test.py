from pyresparser import ResumeParser
import warnings
from resume_parser import resumeparse
warnings.filterwarnings("ignore", category=UserWarning)
import json


"""data = ResumeParser('incoming/Naukri_Rameshbabu[6y_6m].pdf').get_extracted_data()
with open("test1.json","w") as ff:
    ff.write(json.dumps(data,indent=4))"""
data = resumeparse.read_file('incoming/Naukri_Rameshbabu[6y_6m].pdf')
with open("resume_parser.json","w") as ff:
    ff.write(json.dumps(data,indent=4))