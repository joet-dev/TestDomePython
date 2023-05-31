class CategoryTree:

    # class Node: 
    #     def __init__(self, category, parent):
    #         self.category
    #         self.parent
    #         self.children
            
    def __init__(self):
        self.dictParents = {'root': []}
        self.categorySet = set()

    def add_category(self, category, parent):
        if category in self.categorySet: 
            raise KeyError(category + " already exists.")
        
        if parent == None: 
            self.dictParents['root'].append(category)
        elif parent in self.dictParents['root'] and parent in self.dictParents.keys(): 
            self.dictParents[parent].append(category)
        elif parent in self.dictParents['root']:
            self.dictParents[parent] = self.dictParents.get(self.dictParents[parent], [category])
        else: 
            raise KeyError(parent + " does not exist.")

        self.categorySet.add(category)
        
    # Return an array containing the direct children of the specified category. 
    def get_children(self, parent):
        if parent not in self.dictParents.keys(): 
            raise KeyError(parent + " does not exist.")
               
        return self.dictParents[parent]

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))