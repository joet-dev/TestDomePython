def group_by_owners(files):

    res = {}
    
    for file in files: 
        if files[file] in res.keys(): 
            res[files[file]].append(file)
        else: 
            res[files[file]] = res.get(files[file], [file])
      
    return res



if __name__ == "__main__":    

    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   

    print(group_by_owners(files))