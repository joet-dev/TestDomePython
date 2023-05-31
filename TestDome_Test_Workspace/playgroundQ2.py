def find_all_hobbyists(hobby, hobbies):
    
    res = [] 
    
    for person in hobbies: 
        for person_hobby in hobbies[person]: 
            if person_hobby == hobby: 
                res.append(person)
                break
            
    return res

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
    
    print(find_all_hobbyists('Fashion', hobbies))