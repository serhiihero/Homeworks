# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name.
# Find those who are on all blacklists.

casino_blacklist = {"Albina Notaga", "Serena Obligato", "Fredderic Nous", "John Dow", "Ferdinand Joun"}
poker_blacklist = {"Jessica Helloub", "Albina Notaga", "Diason Bert", "Okla Denisson", "John Dow"}
alcohol_blacklist = {"Serena Obligato", "John Dow", "Fredderic Nous", "Daniels Robinson", "Albina Notaga"}
blacklisted_everywhere = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(blacklisted_everywhere)
