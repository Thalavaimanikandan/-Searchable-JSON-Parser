import re        
class JSONSearchable:
    def __init__(self, data):
        self.data=data
    
    def parse(json_string):
        try:
          for old,new in [("true","True"),("false","False"),("null","None")]:
            json_string=json_string.replace(old,new)
          json_string=json_string.strip()  
          return JSONSearchable (eval(json_string,{ "__builtins__":None },{}))
        except Exception as e:
            print("indentation error:",e)
            return None
       
    def search(self,path):
        parts=re.split(r'\.(?![^\[]*\])',path)
        current_data=self.data
        for value in parts:
            if not value:
                return None
            if "[" in value:
                key,*rest=re.split(r'(\[.*?\])',value) 
                if key:
                    current_data=current_data.get(key)
                    
                for r in rest:
                    if not r:
                        continue
                    if r.startswith("[?"):
                        obj, op, val=re.split(r'(==|!=|>=|<=|>|<)',r[2:-1]) 
                        obj,value=obj.strip(),value.strip().strip('"').lower()
                        if val.replace('.','',1).isdigit():
                            val=float(val)
                        elif val=="true":
                            val=True
                        elif val=="false":
                            val = False
                        elif val=="null":
                            val=None
                                    
                        res=[]
                        for item in current_data:
                            if obj in item:
                                try:
                                    if eval(f"item[obj] {op} val"):
                                            res.append(item)
                                except Exception as e:
                                    print("eval error:",e)
                                   
                        current_data=res                                                                
                                            
                    else:
                        idx=int(r[1:-1])
                        current_data=current_data[idx]
                        if isinstance:
                            return current_data,dict
                        else:
                            return None         
            else:
                
                if isinstance(current_data,dict):
                    current_data=current_data.get(value)  
                elif isinstance(current_data,list):
                    temp=[]
                    for item in current_data:
                        if isinstance(item,dict) and value in item:
                            temp.append(item[value])
                    current_data=temp
                            
                else:
                    return None
                if current_data is None:
                    return None
                
                
        return current_data                      

if __name__=="__main__":
    
    file_path= "json_string.json"
    with open("/home/thalavai-manikandan/Desktop/json/json_string.json", 'r') as f:
     json_string = f.read()
    
    searchable_json = JSONSearchable.parse(json_string)
    if searchable_json is None:
        print("parse fail")
    else:
        print("parse not fail")    

    print("Enter your Queries:")
    while True:
        Query=input("Enter Query:<---").strip()
        if Query.lower() == 'exit':
            print("Existing....")
            break


        my_variable=searchable_json
        if my_variable is not None:
            result=my_variable.search(Query)
            print(Query,"----||---->",result)
    


      
           
    
            
    
    