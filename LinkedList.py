#!/usr/bin/python

class Node:
  def __init__(self, value):
    self.next = None
    self.data = value

class SLinkedList:

  def __init__(self):
    self.head = None

  def getNewNode(self, Value):
    return Node( Value )

  def PrintList( self ):
    current = self.head
    while current is not None:
      print( current.data, current ) 
      current = current.next

  def Prepend( self, Value ):
    temp = self.getNewNode( Value )    
    temp.next = self.head
    self.head = temp

  def Append( self, Value ):
    newNode = self.getNewNode( Value ) 
    if self.head is None:
      self.head = newNode
      return

    current = self.head
    while ( current.next ):
      current = current.next
    current.next = newNode

  def Search( self, Value ):
    current = self.head
    status = False
    while ( current ):
      print (current.data)
      if ( current.data == Value ):
        status = True
      current = current.next
    return status

  def InsertAtPosition( self, Position, Value ):
    Counter = 1    
    current = self.head
    newNode = self.getNewNode( Value ) 
    if self.head is None:
      self.head = newNode
      return

    while( current ):
      if (Counter == Position):
        newNode.next=current.next
        current.next = newNode
        return
      current = current.next
      Counter =  Counter + 1
    
  def DeleteNode( self, Key ):
    status = False
    current = self.head
    while (current):
      if ( current.next.data == Key ):
        current.next = current.next.next
        status = True
        break
      current = current.next
    return status

  def SearchRecursive(  self, Key, Current ):
    if ( Current.data == Key ):
      return True

    if ( Current.next is None ):
      return False
        
    return self.SearchRecursive ( Key, Current.next )        


list1 = SLinkedList(  )
list1.Prepend( 13 )
list1.Prepend( 14 )
list1.Append( 10 )
list1.Append( 20 )
list1.InsertAtPosition( 1, 7 )
SearchStatus = list1.Search( 173 )
DeletionStatus = list1.DeleteNode( 20 )
SearchStatusRecursive = list1.SearchRecursive( 10, list1.head )

print (list1.PrintList())





 
 
