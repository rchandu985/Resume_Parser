from pyresparser import ResumeParser
import re
class extracted_data_processing:
    
    segregated_data={}
    
    def total_experience_parser(data,keys):
        extracted_data_processing.segregated_data.update({"Total_Work_Experience":None})
        state=True
        while state:
            for k in keys:
                for f_data in data[k]:
                    if "total experience" in f_data.lower() or "years of overall experience" in f_data.lower() or "overall experience" in f_data.lower() or "total_experience" in f_data.lower() or "total work experience"  in f_data.lower() or "Years of experience".lower() in f_data.lower() or "Years experience".lower() in f_data.lower():
                        for f in f_data:
                            if f.isdigit():
                                #print('esp',f_data)
                                extracted_data_processing.segregated_data.update({"Total_Work_Experience":int(f)})
                                state=False


    def profile_source_parser(data,keys):
        extracted_data_processing.segregated_data.update({"Profile_Source":[]})
        for k in  keys:
            for f_data in data[k]:
                if "www." in f_data.lower():
                    extracted_data_processing.segregated_data[" "].append(f_data)
   
        
    def personal_data(data,keys,file=None):

        for k in  keys:
                for f_data in data[k]:
                    
                    if "_" in f_data:
                        f_data=f_data.replace("_"," ")
                        
                    if "date of birth" in f_data.lower() or "dob" in f_data.lower() or "born date" in f_data.lower() or "borned on" in f_data.lower() or "borned at" in f_data.lower():
                        for f_data in data[k][data[k].index(f_data)::]:
                            match = re.search(r"(\d+-\d+-\d+)",f_data)
                            if match:
                                extracted_data_processing.segregated_data["Personal_Information"].update({"date_of_birth":match.group(1)})
                                break
                            else:
                                match = re.search(r"(\d+/\d+/\d+)",f_data)
                                if match:
                                    extracted_data_processing.segregated_data["Personal_Information"].update({"date_of_birth":match.group(1)})
                                    break
            

                        
    
    def gender_processing(data,keys):
        
        extracted_data_processing.segregated_data["Personal_Information"].update({"Gender":None})

        for k in keys:
            for f_data in data[k]:                   
                if "male" in f_data.lower() :
                    
                    extracted_data_processing.segregated_data["Personal_Information"].update({"Gender":"Male"})
                    break
                elif "female" in f_data.lower():
                    extracted_data_processing.segregated_data["Personal_Information"].update({"Gender":"Female"})

                    break
        
    def skills_processor(data,keys,file):
        pass
                  
    def passport_details(data,keys):
        p_keys=["Passport Available".lower(),"passport status","passport","passport information","passport info"]                
        extracted_data_processing.segregated_data.update({"Passport_Status":None})
        
        dynamo_keys={"yes":"YES","no":"NO","available":"YES","not available":"NO"}

        for ks in keys:
            if ks in p_keys:
                for vrf in data[ks]:
                    if vrf.lower()=="yes" or vrf.lower()=="no" or vrf.lower()=="available" or vrf.lower()=="not availble":
                        extracted_data_processing.segregated_data.update({"Passport_Status":dynamo_keys[vrf.lower()]})
                        break
                    
    def visa_details(data,keys):
        p_keys=["visa Available".lower(),"visa status","visa","visa info","visa information",]                
        extracted_data_processing.segregated_data.update({"Visa_Status":None})
        
        dynamo_keys={"yes":"YES","no":"NO","available":"YES","not available":"NO"}
        
        for ks in keys:
            if ks in p_keys:
                for vrf in data[ks]:
                    if vrf.lower()=="yes" or vrf.lower()=="no"or vrf.lower()=="available" or vrf.lower()=="not availble":
                        extracted_data_processing.segregated_data.update({"Visa_Status":dynamo_keys[vrf.lower()]})
                        break
    
    def immigration_status(data,keys):
        im_keys=["immigration","immigration status","immigration information","immigration info"]                
        extracted_data_processing.segregated_data.update({"Immigration_Status":None})
        
        dynamo_keys={"yes":"YES","no":"NO","available":"YES","not available":"NO"}
        
        for ks in keys:
            if ks in im_keys:
                for vrf in data[ks]:
                    if vrf.lower()=="yes" or vrf.lower()=="no"or vrf.lower()=="available" or vrf.lower()=="not availble":
                        extracted_data_processing.segregated_data.update({"Immigration_Status":dynamo_keys[vrf.lower()]})
                        break
    
    def salary_details(data,keys):
        
        extracted_data_processing.segregated_data.update({"Salary_Details":None})

        for ks in keys:
            if ks in data[keys]:
                for s in ks:
                    if "salary" in s.lower() or "ctc" in s.lower():
                        extracted_data_processing.segregated_data.update({"Salary_Details":s})

        
    
    
    def process(data:dict,file):
        
        get_keys=list(data.keys())
        
        extracted_data_processing.total_experience_parser(data,get_keys)
        extracted_data_processing.personal_data(data,get_keys,file)
        extracted_data_processing.gender_processing(data,get_keys)
        extracted_data_processing.passport_details(data,get_keys)
        extracted_data_processing.visa_details(data,get_keys)
        extracted_data_processing.immigration_status(data,get_keys)
        extracted_data_processing.profile_source_parser(data,get_keys)

        
        return extracted_data_processing.segregated_data