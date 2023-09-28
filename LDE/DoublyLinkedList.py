from Node import Node

class DoublyLinkedList:
    '''Constructor'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.element_num = 0

    '''Check if empty, boolean return value'''
    def is_empty(self):
        return self.element_num == 0

    def get_size(self):
        return self.element_num

    '''Gets the value by position inserted (i-nth element)'''
    def get_element(self, pos):
        if self.is_empty() or (pos < 1) or (pos > self.get_size()):
            return "Posição inválida ou lista vazia"

        aux = Node()
        aux = self.head

        for _ in range(1, pos):
            aux = aux.get_next()

        return aux.get_content()

    '''Searches for the 1st element with this one given value and returns it's position'''
    def get_first_occurrence(self, data):
        if self.is_empty():
            return "Lista Vazia"

        aux = Node()
        aux = self.head
        counter = 1

        while aux is not None:
            if aux.get_content() == data:
                return counter
            aux = aux.get_next()
            counter += 1

        return "Valor não encontrado"

    '''Inserts node at head/beginning of list'''
    def insert_at_head(self, searched_value):
        new_node = Node()

        #Insert at head
        new_node.set_content(searched_value)
        new_node.set_next(self.head)
        new_node.set_previous(None)

        if self.is_empty():
            self.tail = new_node
        else:
            self.head.set_previous(new_node)

        self.head = new_node
        self.element_num += 1

        return True

    '''Inserts at middle'''
    def insert_at_middle(self, pos, data):
        if (pos < 1) or (pos > self.get_size() + 1):
            return "Posição Inválida"

        if pos == 1:
            self.insert_at_head(data)
            return True

        counter = 1

        new_node = Node()
        new_node.set_content(data)

        #Locate pos where new_node'll be inserted into
        aux_node = Node()
        aux_node = self.head

        while (counter < pos - 1) and (aux_node is not None):
            aux_node = aux_node.get_next()
            counter += 1

        if aux_node is None:    #Invalid pos
            return "Posição Inválida"

        #Inserting the new element after aux
        new_node.set_previous(aux_node)
        new_node.set_next(aux_node.get_next())

        #Setting new_node as the previous
        (aux_node.get_next()).set_previous(new_node)

        aux_node.set_next(new_node)

        self.element_num += 1
        return True

    '''Insert at tail/end of list'''
    def insert_at_tail(self, data):
        new_node = Node()
        new_node.set_content(data)
        new_node.set_next(None)

        self.tail.set_next(new_node)

        new_node.set_previous(self.tail)
        self.tail.set_next(new_node)
        self.tail = new_node

        self.element_num += 1
        return True

    '''Insert an element in the specified position. Returns True if it managed to do it, False if not.
    General Function for inserting (would be public)'''
    def insert_element(self, pos, data):
        if self.is_empty() and (pos != 1):
            return "Lista Vazia"

        #Insert at beginning/head
        if pos == 1:
            return self.insert_at_head(data)
        #Insert at end/tail
        elif pos == (self.element_num + 1):
            return self.insert_at_tail(data)
        #Insert in the middle
        else:
            return self.insert_at_middle(pos, data)
    
    '''Removes element from head/beginning (case of single-element list)'''
    def remove_from_head_unitary(self):
        data = self.head.get_content()

        self.head = None
        self.tail = None
        self.element_num -= 1

        return data

    '''Removes element from head/beginning'''
    def remove_from_head(self):
        first_elem = self.head
        
        #Saves the data for returning
        data = first_elem.get_content()

        #Removes the 1st elem from list (first_elem)
        #Making the next elem the new head
        self.head = first_elem.get_next()
        (first_elem.get_next()).set_previous(None)

        self.element_num -= 1

        #Retuns data for convenience
        return data

    '''Removes first ocurrence of element from middle of list (by pos)'''
    def remove_from_middle(self, pos):
        first_elem = self.head
        pos_iterator = 1

        #Iterates 'till it finds the node that'll be removed
        while (pos_iterator <= pos - 1) and (first_elem != None):
            first_elem = first_elem.get_next()
            pos_iterator += 1

        if pos_iterator == None:
            return "Posição Inválida"

        #Sets up ptrs to previous and next (and data for returning)
        data = first_elem.get_content()
        (first_elem.get_previous()).set_next(first_elem.get_next())
        (first_elem.get_next()).set_previous(first_elem.get_previous())

        self.element_num -= 1

        return data

    '''Removes from list's tail'''
    def remove_from_tail(self):
        first_elem = self.tail
        data = first_elem.get_content()

        (self.tail.get_previous()).set_next(None)
        self.tail = self.tail.get_previous()

        self.element_num -= 1

        return data

    '''Removes first occurrence of an element from a given position, returning it for convenience, unless invalid'''
    def remove_element(self, pos):
        #If empty
        if(self.is_empty()):
            return "Lista Vazia"

        #Remove from head (case of single-element list)
        if (pos == 1) and (self.get_size() == 1):
            return self.remove_from_head_unitary()
        #General removing-from-head routine
        elif pos == 1:
            return self.remove_from_head()
        #Remove from tail
        elif pos == self.get_size():
            return self.remove_from_tail()
        else:
            #From middle
            return self.remove_from_middle(pos)

    '''Func that returns the element in a specified position arg'''
    def search_element_by_pos(self, pos):
        if(pos < 1) or (pos > self.get_size()):
            return "Posição inválida"

        aux_node = self.head

        for _ in range(1, pos):
            aux_node = aux_node.get_next()

        return aux_node.get_content()

    '''Func that returns a list of positions in which the value can be found'''
    def search_value_ocurrences(self, value):
        if self.is_empty():
            return [] #Empty list

        aux_node = self.head
        found_positions = []

        position = 1 #Starting pos

        while aux_node is not None:
            if aux_node.get_content() == value:
                found_positions.append(position)

            aux_node = aux_node.get_next()
            position += 1

        return found_positions #The pos list