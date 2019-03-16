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

list1 = SLinkedList(  )
list1.Prepend( 13 )
list1.Prepend( 14 )
list1.Append( 10 )
list1.Append( 20 )
list1.PrintList()
status = list1.Search( 173 )
print (status)





 
 
