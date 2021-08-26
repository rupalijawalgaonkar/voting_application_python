#voting application in python
import random
num=int(input("Enter number of candidates: ")) #3
cand=input(f'Enter {num} candidates now:\n').split() #[list of names]
print("Candidates are: ",cand)
print("Voting is live....please wait for the results...")
print("Voting has been finished.... and wait is over")
print("Here are the results")
votes=[52,94,85]
for x in range(0,num):
    c=random.randrange(1,100,3)
    votes.append(c)
for i in range(num):
    print(cand[i],':',votes[i]) #cand[0]:votes[0]
print("Hence the winner is...")
maximum=max(votes) #94
count=0
for r in range(num):
    if votes[r]==maximum:
        count=r #count =1
print(cand[count],':',maximum)
