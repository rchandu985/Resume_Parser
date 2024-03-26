import json

class load:
    def stop_keywords():
        #stk >> stop keywords
        stk_file=open(r"stop_keywords\groups.json","r+")
        stk=json.load(stk_file)

        return stk#[{},{}]


class resume:
    
    def constant_data_seggragator(resume_data:dict,stk:dict):

        final_data={}

        for s in stk:

            s_data:list=stk[s]
            final_data.update({s:{}})
            
            for rd in resume_data:

                if rd in s_data:
                    
                    final_data[s].update({rd:resume_data[rd]})
        
        return final_data






    def blocks(resume_text:str,stk:dict):

        ref_data={}

        ref_blocks=[]

        stw_refernce_key=[]

        for rsm in resume_text.splitlines():
            #print(rsm)

            for key in stk:
                #stw >> stop words
                stw:list=stk.get(key)

                if rsm in stw:
                    stw_refernce_key.append({key:rsm})
                    ref_blocks.append(rsm)
                    ref_data.update({rsm:""})
            
            if len(ref_blocks)>0:

                ref_data[ref_blocks[-1]]+="\n"+rsm
        

        return ref_data

        


