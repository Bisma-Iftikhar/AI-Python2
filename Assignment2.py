# Given a dictionary of products with nested categories, find the product with the highest price
# and print its name and price.
# Example Input:
products = {
 "Electronics": {"Laptop": 1200, "Phone": 800},
 "Clothes": {"Shirt": 50, "Shoes": 100},
 "Grocery": {"Rice": 20, "Milk": 10}
}
m=max([a for i in products.values() for a in i.values()])
print(list((k,j) for i in products.values() for k,j in i.items() if j==m))

# Write a Python function that takes a nested list of arbitrary depth and returns a dictionary with
# the frequency count of each integer in the list.
# Example Input:
lst = [1, [2, [3, 2, 4], 5, 1], 6]
def de(lst, alllist):
 for i in lst:
  if isinstance(i, int):
   alllist.append(i)
  else:
   de(i, alllist)
 return alllist
alllist=de(lst, [])
print(sum(alllist))

initial=["Red on pole","Blue on pole","Green on pole","Green on top"]
goal=["Green on pole","Blue on pole","Red on pole","Red on top"]
operations=[
    {
        "action":"Move Green on table",
        "preconds":["Green on top","Green on pole"],
        "add":["Green on table","Blue on top"],
        "delete":["Green on pole","Green on top"]
    },
    {
        "action":"Move Blue on table",
        "preconds":["Blue on pole","Blue on top"],
        "add":["Blue on table","Red on top"],
        "delete":["Blue on top","Blue on pole"],
    },
    {
        "action": "Move Red on table",
        "preconds": ["Red on pole", "Red on top"],
        "add": ["Red on table","nothing on pole"],
        "delete": ["Red on top", "Red on pole"],
    },
{
        "action": "Move Green on pole",
        "preconds": ["nothing on pole", "Green on table"],
        "add": ["Green on pole","Green on top"],
        "delete": ["nothing on pole", "Green on table"],
},
{
        "action": "Move Blue on pole",
        "preconds": ["Blue on table","Green on top"],
        "add": ["Blue on pole","Blue on top"],
        "delete": ["Green on top", "Blue on table"],
},
{
        "action": "Move Red on pole",
        "preconds": ["Red on table", "Blue on top"],
        "add": ["Red on pole","Red on top"],
        "delete": ["Blue on top", "Red on table"],
},
]


initial=["P on side1","Q on side1","R on side1","S on side1","Lantern on side1",]
goal=["P on side2","Q on side2","R on side2","S on side2","Lantern on side2",]
operation=[
 {
  "action":"Move P and Q, Lantern on side2",
  "preconds":["P on side1","Q on side1","Lantern on side1"],
  "add":["P on side2","Q on side2","Lantern on side2"],
  "delete":["P on side1","Q on side1","Lantern on side1"]
 },
 {
  "action": "Move P and  lantern on side1",
  "preconds": ["P on side2", "Lantern on side2"],
  "add": ["P on side1", "Lantern on side1"],
  "delete": ["P on side2",  "Lantern on side2"]
 },
 {
  "action": "Move P and R, lantern on side2",
  "preconds": ["P on side1",  "Lantern on side1", "R on side1"],
  "add": ["P on side2", "R on side2", "Lantern on side2"],
  "delete": ["P on side1", "R on side1", "Lantern on side1"]
 },
 {  "action":"Move P and S, Lantern on side2",
  "preconds":["P on side1","Lantern on side1","S on side1"],
  "add":["P on side2","S on side2","Lantern on side2"],
  "delete":["P on side1","S on side1","Lantern on side1"]
 },
]



