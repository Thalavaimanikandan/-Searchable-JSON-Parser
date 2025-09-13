import re        
class JSONSearchable:
    def __init__(self, data):
        self.data=data
    
    def parse(json_string):
        try:
          for old,new in [("true","True"),("false","False"),("null","None")]:
            json_string=json_string.replace(old,new)
          return JSONSearchable (eval(json_string,{ "__builtins__":None },{}))
        except Exception as e:
            ("indentation error:",e)
            return None
       
    def search(self,path):
        parts=re.split(r'\.(?![^\[]*\])',path)
        current_data=self.data
        for value in parts:
            if not value:
                return "null"
            if "[" in value:
                key,*rest=re.split(r'(\[.*?\])',value) 
                if key:
                    current_data=current_data.get(key)
                    if isinstance:
                        return current_data,list
                    else:
                        return "null"
                for r in rest:
                    if not r:
                        continue
                    if r.startswith("[?"):
                        obj,op,val=re.split(r'(==,!=,>,<,>=,<=)') 
                        obj,value=obj.strip(),value.strip().strip('"') 
                        res=[]
                        for item in current_data:
                            if isinstance:
                                return current_data,list
                            else:
                                return res
                                if obj in item:
                                    right=float(value)
                                    if value:
                                      value.replace('.','',1).isdigit()
                                    elif value=="true":
                                        return True
                                    elif value=="false":
                                        return False
                                    elif value=="null":
                                        return "null"
                                    else:
                                        return value
                                    if eval(f"item[obj] {op} right"):
                                        res.append(item)
                        current_data= res          
                    else:
                        idx=int(r[1:-1])
                        current_data=current_data[idx]
                        if isinstance:
                            return current_data,dict
                        else:
                            return "null"
            else:
                current_data=current_data.get(value)  
                if isinstance(current_data,dict):
                    pass
                elif isinstance(current_data,list):
                    pass
                else:
                    return "null"
                
                
        return current_data                       

if __name__=="__main__":
    json_data = """
    {
        "store": "Main Street Books",
        "inventory": [
        { "type": "book", "title": "The Great Gatsby", "price": 12.50, "in_stock": true },
        { "type": "book", "title": "Moby Dick", "price": 15.00, "in_stock": false },
        { "type": "magazine", "title": "Tech Today", "price": 5.99, "in_stock": true }
        ],
        "location": {
        "city": "New York",
        "postcode": "10001"
        }
    }
    """   

    searchable_json = JSONSearchable.parse(json_data)

    for Queries in [
        "store",
        "inventory[0].title",
        "inventory[?in_stock==true]",
        "inventory[?price<15.0].title",
        "location.country"
    ]:
     my_variable=searchable_json
     if my_variable is not None:
            result = my_variable.search(Queries)
            print(Queries)
            print(result)
    
    