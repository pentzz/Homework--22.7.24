# Task 1
import statistics

data: bool = True
t: list = []
zero: int = 0
while len(t) < 12:
    try:
        temp: int = int(input(f"Please enter the temperature of month {len(t) + 1}: "))
        if temp > 40 or temp < -5:
            data = False
            break
        else:
            if temp == 0:
                if zero == 1:
                    print("You are probably put a wrong input (0) please Try again.")
                    zero = 0
                    continue
                zero = zero + 1
                t.append(temp)
            else:
                zero = 0
                t.append(temp)
    except Exception as e:
        print(f"{e}\nPlease enter a valid temperature! (number)")
        continue
print(f"Correct data!" if data else f"Data wrong!")
if data:
    print(f"The average temperature is: {statistics.mean(t):.2f}\n"
          f"The max temperature is: {max(t)}\n"
          f"The min temperature is: {min(t)}")

# Task 2
sub: str = input("-=Welcome to the UN vote=-\n"
                 "Please enter the subject you want: ")
all_votes: list[int] = []  # כל ההצבעות
last_ag: int = 0
while len(all_votes) < 44:
    try:
        vote: int = int(input("Please enter your vote: "))
        if vote >= 1 and vote <= 4:
            if vote == 4:
                print(f"The vote has been canceled.\nCountry number {len(all_votes)+1} had VETO for {sub}.")
                all_votes.clear()
                break
            all_votes.append(vote)
            last_ag: int = len(all_votes) if vote == 2 else last_ag
        else:
            print("Please enter a valid number (1-4).")
            continue
    except Exception as e:
        print(f"Error,{e}\nTry again..")
if len(all_votes) == 44:
    votes_for: list[int] = [_ for _ in all_votes if _ == 1]
    votes_ag: list[int] = [_ for _ in all_votes if _ == 2]
    votes_av: list[int] = [_ for _ in all_votes if _ == 3]
    print(f"None of the countries vote for {sub}" if not votes_for
          else f"The number of countries voted FOR {sub} is {len(votes_for)}")
    print(f"None of the countries vote against {sub}" if not votes_ag
          else f"The number of countries voted AGAINST {sub} is {len(votes_ag)}")
    print(f"None of the countries avoided {sub}" if not votes_av
          else f"The number of countries AVOIDED {sub} is {len(votes_av)}")
    print(f"The first country that voted FOR {sub} is country number: {all_votes.index(1)+1}" if votes_for
          else f"None of the countries voted for : {sub}")
    print(f"The last country that voted AGAINST {sub} is country number: {last_ag}" if votes_ag
          else f"None of the countries voted against : {sub}")
