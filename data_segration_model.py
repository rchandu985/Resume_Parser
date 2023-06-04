from pyresparser import ResumeParser
import re
class extracted_data_processing:
    
    segregated_data={}
    
    def experience_parser(data,keys):
        e_p_keys=["Work History".lower(),'internship experience',"employment experience",'work experience','professional experience','freelance experience','professional experience',"technical experience"]
        extracted_data_processing.segregated_data.update({"Work_Experience":[]})
        for k in  keys:
            for f_data in data[k]:
                if "experience" in f_data.lower():
                    extracted_data_processing.segregated_data["Work_Experience"].append(f_data)

            if k in e_p_keys:
                extracted_data_processing.segregated_data["Work_Experience"]+=data[k]
        
        #extracted_data_processing.segregated_data.update({"Work_Experience":list(set(extracted_data_processing.segregated_data["Experience"]))})
        
        #print(extracted_data_processing.segregated_data)
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
                    extracted_data_processing.segregated_data["Profile_Source"].append(f_data)
   
    def certifications(data,keys):
        extracted_data_processing.segregated_data.update({"Certifications":[]})
        
        c_keys=["certifications","EDUCATIONAL PUBLICATION CERTIFICATION".lower(),"education certification","education certifications","EDUCATIONAL PUBLICATION CERTIFICATIONS".lower(),"certifications and training"]
        
        if "certifications" in keys or "certifications and training"  in keys or "EDUCATIONAL PUBLICATION CERTIFICATION".lower() in keys or "EDUCATIONAL PUBLICATION CERTIFICATIONS".lower() or "education certification" in keys or "education certifications" in keys:
            for ks in keys:
                if ks in c_keys:
                    for c in data[ks]:
                        if "certified" in c.lower() or "certification" in c.lower() or "certificate" in c.lower() and "mainten" not in c.lower() and "create" not in c.lower() and "generate" not in c.lower() and "fixing" not in c.lower() and "renew" not in c.lower():
                            extracted_data_processing.segregated_data['Certifications'].append(c)
        
        
        for k in  keys:
            for f_data in data[k]:
                if f_data.lower() not in c_keys:
                    if "certified" in f_data.lower() or "certification" in f_data.lower()  or "certificate" in f_data.lower() and "mainten" not in f_data.lower() and "create" not in f_data.lower() and "generate" not in f_data.lower() and "renew" not in f_data.lower() and "fixing" not in f_data.lower():
                        extracted_data_processing.segregated_data["Certifications"].append(f_data)
        extracted_data_processing.segregated_data.update({"Certifications":list(set(extracted_data_processing.segregated_data["Certifications"]))})
    
    def personal_data(data,keys,file=None):
        extracted_data_processing.segregated_data.update({"Personal_Information":{}})
        p_data = ResumeParser(f"incoming/{file}").get_extracted_data()
        #print(p_data)
        extracted_data_processing.segregated_data['Personal_Information'].update({'name':p_data['name'] , "date_of_birth":None,'email': p_data['email'], 'mobile_number': p_data['mobile_number']})

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
        
    def skill_processor(data,keys,file):
        sk_keys=['skills',
        "other skills",
        "other abilities",
        'career related skills',
        'professional skills',
        'specialized skills',
        'technical skills',
        'computer skills',
        'personal skills',
        'language competencies and skills']
        
        extracted_data_processing.segregated_data.update({"Skills_1":{},"Skills_2":[]})

        for s_K_k in sk_keys:
            if s_K_k in keys:
                for f_data in data[s_K_k]:
                    if "years" in f_data.lower() or "year" in f_data.lower() :
                        f_data=f_data.replace("_","").replace("(","").replace(")","").replace(":","").replace(" ","").replace("-","")
                        #print(f_data)

                        for exp in f_data:
                            if exp.isdigit():
                                k=f_data.split(exp,1)[1]
                                #print(k)
                                idx=f_data.index(exp)
                                if k.lower() == "years" or k.lower()=="year":
                                    
                                    extracted_data_processing.segregated_data['Skills_1'].update({f_data[:idx].lower():int(exp)})
                                    extracted_data_processing.segregated_data['Skills_2'].append(f_data[:idx].lower())
                                    break
                                elif f_data[idx+1]==".":
                                    if f_data[idx+3::]=="years" or f_data[idx+2::]=="year":
                                        extracted_data_processing.segregated_data['Skills_1'].update({f_data[:idx].lower():int(exp)})
                                        extracted_data_processing.segregated_data['Skills_2'].append(f_data[:idx].lower())

                                        break
                                else:
                                    #print('new',f_data,exp,f_data[idx+1])
                                    pass
                                    
                    else:
                        extracted_data_processing.segregated_data['Skills_1'].update({f_data:"NA"})
                        extracted_data_processing.segregated_data['Skills_2'].append(f_data.lower())

        p_data = ResumeParser(f"incoming/{file}").get_extracted_data()
        
        '''for skls in p_data['skills']:
            k=list(extracted_data_processing.segregated_data['Skills_1'].keys())

            if skls not in k: 
                extracted_data_processing.segregated_data['Skills_1'].update({skls:"NA"})
                extracted_data_processing.segregated_data['Skills_2'].append(skls.lower())
        
        extracted_data_processing.segregated_data.update({"Skills_2":list(set(extracted_data_processing.segregated_data['Skills_2']))})
        '''
        


    def summary_parser(data,keys):
        extracted_data_processing.segregated_data.update({"Summary":[]})
        s_keys=["summary","professional summary",'career summary','summary of qualifications',"executive summary"]
        for k in s_keys:
            if k  in keys :
                extracted_data_processing.segregated_data['Summary']+=data[k]
        
        #extracted_data_processing.segregated_data.update({"Summary":list(set(extracted_data_processing.segregated_data['Summary']))})
              
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
    
    
    def work_preferences(data,keys):
        w_p_keys=["preferences","work preferences","work priority","priority"]
        
        extracted_data_processing.segregated_data.update({"Work_Preference":[]})

        for ks in keys:
            if ks in w_p_keys:
                extracted_data_processing.segregated_data['Work_Preference']+=data[ks]
        extracted_data_processing.segregated_data.update({"Work_Preference":extracted_data_processing.segregated_data['Work_Preference']})
    
    def project_details(data,keys):
        p_d_keys=["PROJECT DETAILS".lower(),
        "projects",
        "projects information",
        "projects info","PROJECT PROFILE".lower()]
        extracted_data_processing.segregated_data.update({"Project_Details":[]})

        for ks in keys:
            if ks in p_d_keys:
                extracted_data_processing.segregated_data['Project_Details']+=data[ks]
        #extracted_data_processing.segregated_data.update({"Project_Details":list(set(extracted_data_processing.segregated_data['Project_Details']))})
    def salary_details(data,keys):
        
        extracted_data_processing.segregated_data.update({"Salary_Details":None})

        for ks in keys:
            if ks in data[keys]:
                for s in ks:
                    if "salary" in s.lower() or "ctc" in s.lower():
                        extracted_data_processing.segregated_data.update({"Salary_Details":s})

        
    
    
    def process(data:dict,file):
        
        get_keys=list(data.keys())
        
        extracted_data_processing.certifications(data,get_keys)
        extracted_data_processing.experience_parser(data,get_keys)
        extracted_data_processing.total_experience_parser(data,get_keys)
        extracted_data_processing.personal_data(data,get_keys,file)
        extracted_data_processing.gender_processing(data,get_keys)
        extracted_data_processing.skill_processor(data,get_keys,file)
        extracted_data_processing.summary_parser(data,get_keys)
        extracted_data_processing.passport_details(data,get_keys)
        extracted_data_processing.visa_details(data,get_keys)
        extracted_data_processing.immigration_status(data,get_keys)
        extracted_data_processing.profile_source_parser(data,get_keys)
        extracted_data_processing.work_preferences(data,get_keys)
        extracted_data_processing.project_details(data,get_keys)

        extracted_data_processing.segregated_data.update({"Resume_Body":[data]})
        
        return extracted_data_processing.segregated_data