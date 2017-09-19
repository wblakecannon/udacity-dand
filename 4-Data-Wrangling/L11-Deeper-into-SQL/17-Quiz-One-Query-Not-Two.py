# Find the players whose weight is less than the average.
# 
# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.
#
# Multiple query version:
def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute("select avg(weight) as av from players;")
    av = cursor.fetchall()[0][0]  # first column of first (and only) row
    cursor.execute("select name, weight from players where weight < " + str(av))
    return cursor.fetchall()

# One query version:
def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute("select aname, weight from players, (select avg(weight) as av from players) as subq where weight < av;")
    return cursor.fetchall()
