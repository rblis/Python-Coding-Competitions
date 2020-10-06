n = int(input().split()[0])
opus = [int(x) for x in input().split()]
#C++ 
#include <iostream>
#include <vector>
# using namespace std;
# struct node{
#     int value;
#     int index;
# };
# int main(){
#     int n = 0;
#     cin >> n;
#     vector<node*> opus(n);
#     for(int k = 0; k < n; k++){
#         node* nod = new node;
#         nod->index = k+1;
#         cin >> nod->value;
#         opus[k] = nod;
#     }
#     int index = 0;
#     while(n > 1){
#         index = (index+(opus[index]->value)-1)%n;
#         opus.erase(opus.begin()+index);        
#         n--;
#         if(index == n){
#             index = 0;
#         }
#     }
#     cout << opus[0]->index;
# }

'''
Original Brute Force too slow
index, new_index, count = 0,0,(opus[0]-1)
while n > 1:
    while count > 0:        
        index += 1        
        if index == len(opus):
            index = 0
        if opus[index] != -1:
            count -= 1
    n -= 1
    opus[index] = -1
    new_index = index+1 if (index+1) < len(opus) else 0
    while(opus[new_index] == -1):
        new_index = new_index+1 if (new_index+1) < len(opus) else 0
    count = opus[new_index]-1
    index=new_index    
print(new_index+1)


Link List Brute Force too slow
class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.left = None
        self.right = None

n = int(input().split()[0])
links, head = Node(0,0), None
for index, value in enumerate(input().split()):
    if index == 0:
        links.index = int(index)
        links.value = int(value)
        head = links
    elif index == (n-1):
        nnode = Node(int(index), int(value))
        links.right = nnode
        nnode.left = links
        nnode.right = head
        head.left = nnode
    else:
        nnode = Node(int(index), int(value))
        links.right = nnode
        nnode.left = links
        links = links.right
links = head
while n > 1:
    count = links.value-1
    for x in range(0,count):
        links = links.right

    links.right.left = links.left
    links.left.right = links.right
    links = links.right
    n-=1

print(links.index+1) 

'''        
        