from Utils import Utils

linked_list = Utils([2, 7, 18, 31, 33, 200]).get_linked_list()
linked_list_two = Utils([4, 6, 8, 10, 11, 24, 30]).get_linked_list()

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]

'''
Use 2 pointers (p and q) which will each initially point to the head node 
of each linked list. 

There will be another pointer, s, that will point to the smaller 
value of data of the nodes that p and q are pointing to. 

Once s points to the smaller value of the data of nodes that
p and q point to, p or q will move on to the next node in their 
respective linked list. 

If s and p point to the same node, p moves forward;
otherwise q moves forward. The final merged linked list will be made from 
the nodes that s keeps pointing to.
'''



def merge_sorted(self, llist):
  # Step 0: Initialize the 3 variables to their start values.
  p = self.head
  q = llist.head
  s = None

  # Step 2: Check if either list is empty
  # if a list is empty can return early as no merging is possible.
  # This step is optional if we state the lists cannot be empty.
  # if not p:
  #     return q
  # if not q:
  #     return p

  # Step 3: Initialize s to its first value and
  # adjust the value of p or q accordingly.
  # It is important to note that this takes place
  # outside of the while loop.
  if p and q:
      # p has the smaller value so s is updated to point to the node
      # p is pointing to originally
      # p pointer is updated to reference the next node in its list
      if p.data <= q.data:
          s = p
          p = s.next
      else:
      # q has the smaller value so s updated to point to the node
      # q is pointing to originally
      # q pointer is updated to reference the next node in its list
          s = q
          q = s.next
      # s is currently pointing to the node with the smallest number
      # in the entire list, it must be the new head
      new_head = s

  # Step 4: The main loop where we
  # compare p and q and based on which is smaller, update s
  while p and q:
      if p.data <= q.data:
          s.next = p
          s = p
          p = s.next
      else:
          # when q is the node with smaller value

          # Step 4A: Update the structure of the linked list,
          # the merging step.
          # node s is joined to node q
          s.next = q

          # Step 4B: Update both pointers s and q to point to their new nodes.

          # node s is updated to point to node q
          # we don't lose the node s was previously pointing to
          # because it is connected to the new_head node or is the new_head
          # in first iteration of loop
          s = q
          # The q pointer is update to the next node on its list
          q = s.next


  # Step 5: Either p or q has reached the end of its list and
  # the loop has stopped.
  # When one list reaches the end of the list, the non-empty list contains
  # the next value of the merged list.
  if not p:
      s.next = q
  if not q:
      s.next = p

  self.head = new_head

  return self.head
#
# We pass llist which is the second linked list that we are going to merge with the linked list on which the class method merge_sorted is called. As discussed in the algorithm, p and q will initially point to the heads of each of the two linked lists (lines 3-4). On line 5, we declare s and assign None to it.
#
# On lines 7-10, we handle the case if one of the linked lists is empty. If not p evaluates to true, it means that the first linked list is empty; therefore, we return q on line 8. Similarly, we check for the second linked list by using q which points to the head of the second linked list (llist). If it’s empty, then we return p.
#
# Next, we’ll code the main idea of our algorithm. On line 12, we will proceed if both p and q are not None. If p and q are not None, then we compare the data of the nodes they are pointing to. If p.data is less than q.data, then s will point to p (line 14). On the other hand, if q.data is less than p.data, s will point to q (line 17). Also, as shown in the algorithm, p and q will move along if s points to the node they were previously pointing to. Therefore, based on whichever condition is true, we update p and q accordingly by pointing it to s.next (line 15 and line 18). Now you can note that the node with the lesser value of p and q will be the first node of our merged linked list. Therefore, we set it as the new_head on line 19.
#
# Let’s go ahead and break down the code in the following while loop (lines 20-28):
#
# The while loop will run until either p or q becomes None. Again, we’ll execute the corresponding block of code based on the condition in the if-statement. If p.data is less than or equal to q.data, then we want to point s to what p is pointing to and move p along its respective linked list. Therefore, we save what p is pointing to by assigning it to s.next (line 22). On line 23, we update the value of s to p because p.data is less than or equal to q.data. Now we make p move along by pointing it to the next node of s (line 24).
#
# Lines 26-28 are the mirror image of lines 22-34 except that they will be executed if q.data is less than p.data. Also, they’ll make s point to whatever q was pointing to and will make q move along its linked list.
#
# Now let’s discuss the following portion of the code (lines 29-33):
#
# The code will reach this point after the while loop terminates which implies either p or q or both p and q have become None. We check using the conditions on line 29 and line 31 that we have reached the None for which of the linked lists. If we have reached the end of p, i.e., the condition on line 29 becomes true, we make the next of s point to q. This means that s will now point to the remaining llist. This will complete the entire chain of our merged linked list. In the same way, we check if q has reached the end of the linked list or not and update s.next accordingly (line 32).
#
# Finally, on line 35, we return updated self.head (new_head) from the method which is the head node of our merged linked list made from llist and the linked list on which this class method is called.
#
# As we have discussed the merge_sorted method, we’ll verify the method by making it part of the LinkedList class:

