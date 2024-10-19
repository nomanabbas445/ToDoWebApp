def Get_TODO(file_Path):
    with open(file_Path,"r") as file_local:
       todoList_local = file_local.readlines() 
       return todoList_local
   
def Set_TODO(file_Path,writeToDo):
    
    with open(file_Path,"w") as file_local:
        file_local.writelines(writeToDo)
    
