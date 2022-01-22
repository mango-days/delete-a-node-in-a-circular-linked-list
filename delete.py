# 2 way linked list

class Node :
    def __init__ ( self , data ) :
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def insert ( self , data ) :
        if self.head == None :
            self.head = Node ( data )
            self.head.next = self.head
            self.head.prev = self.head
            print ( self.head.prev.data ,"  ", self.head.data ,"  ", self.head.next.data )
            return
        
        temp = self.head
        while temp :
            if temp.next != self.head : temp = temp.next
            else : break
        
        temp.next = Node ( data )
        temp.next.next = self.head
        temp.next.prev = temp
        
        self.head.prev = temp.next
        print ( temp.next.prev.data ,"  ", temp.next.data ,"  ", temp.next.next.data )
        return
    
    def printList ( self ) :
        
        print ("")
        print ( "nodes inserted as ---" )
        
        if self.head == None : return
        
        print ( "pre", "node" , "next" )

        print ( self.head.prev.data ,"  ", self.head.data ,"  ", self.head.next.data )
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            print ( temp.prev.data ,"  ", temp.data ,"  ", temp.next.data )
            temp = temp.next
        return
    
    def find ( self , data ) :
        if self.head == None : return
        
        index = 1
        temp = self.head
        while temp :
            if temp.data == data : return index
            elif temp.next != self.head : temp = temp.next
            else : return None
            index += 1
    
    def size ( self ) :
        if self.head == None : return 0
        
        count = 0
        temp = self.head
        while temp :
            count += 1
            if temp.next != self.head : temp = temp.next
            else : return count
    
    def delete ( self , data ) :
        
        print ("")
        print ( "after deleting node with data", data, "---")

        data_index = self.find ( data )
        if data_index == None : return

        count = 1
        temp = self.head
        while count != data_index :
            temp = temp.next
            count += 1
        prev = temp.prev
        prev.next = temp.next
        temp.next.prev = prev
        
        if  data_index == 1 : self.head = self.head.next
        self.printList ()
        return
    
Obj = DoubleLinkedList ()

print ( "inserting nodes ---" )
print ( "pre", "node" , "next" )
for index in range (9) : Obj.insert (index+1)

Obj.printList()

Obj.delete ( 1 )
Obj.delete ( 3 )
Obj.delete ( 5 )
Obj.delete ( 7 )
Obj.delete ( 9 )