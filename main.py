from math import sqrt
from random import *

# ----------------------------- Ex 6 -----------------------------


def sum_square_difference():
    sum_square = 0
    square_sum = 0

    for i in range(1, 101, 1):
        sum_square += i**2
        square_sum += i

    square_sum *= square_sum

    return square_sum - sum_square


# print("The difference is: ", sum_square_difference())


# ----------------------------- Ex 2 -----------------------------
sum_even_fib = 2


# Skriv funktion som lägger i hop två tal och skriver ut dem


def add(var1, var2):
    new = var1 + var2
    print("new value", new)


def is_prime(number):
    if number == 1:
        return True
    for k in range(2, int(sqrt(number)) + 1):
        if number % k == 0:
            return False

    return True

# Skriv en rekursiv funktion som lägger ihop två tal (fibonacci) och skriver ut det nya talet


def fibonacci(var1, var2):
    new = var1 + var2
    if new < 100000000000000:
        if is_prime(new):
            print(new)
        fibonacci(var2, new)


# fibonacci(1, 1)
# print(is_prime(12))


# ----------------------------- Ex 7 -----------------------------

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2


def is_sum_1000(a, b, c):
    return a + b + c == 1000


def product_p_triplet():
    for i in range(1, 1000, 1):
        for j in range(i, 1000, 1):
            for k in range(j, 1000, 1):
                if is_pythagorean_triplet(i, j, k) and is_sum_1000(i, j, k):
                    return i*j*k


# print(product_p_triplet())

# ----------------------------- Ex 4 -----------------------------
# Find greatest palindrome that is the product of two three-digit numbers

def find_greatest_three_digit_palindrome():
    largest_palindrome = 0
    component1 = 0
    component2 = 0
    for i in range(999, 800, -1):
        for j in range(999, 800, -1):
            product = i*j
            if is_palindrome(product):
                if product > largest_palindrome:
                    largest_palindrome = product
                    component1 = i
                    component2 = j

    print("The greatest 3-digit palindrome is: ", largest_palindrome, "Components: ", component1, " ", component2)


def is_palindrome(product):
    st_product = str(product)
    return st_product == st_product[::-1]


# find_greatest_three_digit_palindrome()


# ----------------------------- Ex 4 -----------------------------
number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def find_greatest_thirteen_adjacent_numbers():
    greatest_number = 0
    number_singles = [int(x) for x in str(number)]
    for i in range(0, len(number_singles)-13, 1):
        product = 1

        for j in range(0, 13, 1):
            product *= number_singles[i+j]

        if greatest_number < product:
            greatest_number = product

    print(greatest_number)


# find_greatest_thirteen_adjacent_numbers()

# ----------------------------- Horse race -----------------------------
def horse_race(number_of_dices, win_condition):

    olle = 0
    rigel = 0
    sui = 0
    filip = 0

    win_cond = win_condition

    while olle < win_cond and rigel < win_cond and sui < win_cond and filip < win_cond:
        dice_sum = randint(1, 6) + randint(1, 6)
        if 1 <= dice_sum <= 3:
            olle += 1
        elif 4 <= dice_sum <= 6:
            rigel += 1
        elif 7 <= dice_sum <= 9:
            sui += 1
        elif 10 <= dice_sum <= 12:
            filip += 1

    print("Horse results:", "Olle:", olle, "Rigel:", rigel, "SUI:", sui, "Filip:", filip)


# horse_race(1, 10)


# ----------------------------- Personal number control number -----------------------------
def find_control_number(personal_number):
    print(len(personal_number))
    personal_number_as_ints = []

    # Multiply respectively by 2 and 1
    for i in range(0, len(personal_number), 1):
        if i % 2 == 0:
            personal_number_as_ints.append(int(personal_number[i])*2)
        else:
            personal_number_as_ints.append(int(personal_number[i]))

    print("PNi", personal_number_as_ints)
    # Sum all numbers
    sum = 0
    for number in personal_number_as_ints:
        str_num = str(number)
        for c in str_num:
            sum += int(c)

    print("sum:", sum)
    # Find control number
    if sum % 10 == 0:
        print("Control number is 0")
    else:
        print("Control number is:", (10 - (sum % 10)))


# personal_number_input = input()
# find_control_number(personal_number_input)


# ----------------------------- Newton-(Rhapson) method -----------------------------
def f(x):
    return x**3 - 5*(x**2) + 3


def f_prime(x, h):
    return (f(x + h) - f(x - h))/(2*h)


def new_x(x):
    if -0.0000001 <= f(x) < 0.0000001:
        print("x", x, "f(x)", f(x))
        return
    new = x - (f(x) / f_prime(x, 0.001))
    new_x(new)


# new_x(0)
# new_x(1)
# new_x(10)


# ----------------------------- Stone-Scissor-bag -----------------------------
def game():
    players = []
    player_scores = [0, 0]
    moves = ["stone", "scissor", "bag"]
    win_condition = 3

    players.append("Kim")
    players.append("Joe")

    while win_condition not in player_scores:
        p1_move = moves[randint(0, 2)]
        p2_move = moves[randint(0, 2)]

        if wins_over(p1_move) == p2_move:
            player_scores[0] += 1
        elif wins_over(p2_move) == p1_move:
            player_scores[1] += 1

    print("Scores are:", players[0], player_scores[0], players[1], player_scores[1])
    return player_scores


def wins_over(move):
    if move == "stone":
        return "scissor"
    elif move == "bag":
        return "stone"
    elif move == "scissor":
        return "bag"


def stone_scissor_paper():
    wins1 = 0
    wins2 = 0

    for i in range(0, 1000):
        scores = game()
        if scores[0] > scores[1]:
            wins1 += 1
        else:
            wins2 += 1

    print("W1", wins1, "w2", wins2, "P1 wins the percentage of the games:", float(wins1/1000))


# stone_scissor_paper()


# ----------------------------- Probability of dice differance -----------------------------

def prob_dice():
    hits = 0
    n_loops = 1000000

    for i in range(0, n_loops, 1):
        if abs((randint(1, 6) - randint(1, 6))) == 3:       # dice1 - dice2
            hits += 1

    print("Probability is", hits/n_loops)


# prob_dice()


# ----------------------------- Guess the fruit? -----------------------------
def fruit_guess():
    frukter = ["äpple", "aprikos", "avokado", "banan",
     "björnbär",
     "blodapelsin",
     "blåbär",
     "svarta vinbär",
     "körsbär",
     "klementin",
     "kokosnöt",
     "tranbär",
     "röda vinbär",
     "drakfrukt",
     "dadlar",
     "durian",
     "fikon",
     "gojibär",
     "grapefrukt",
     "vindruva",
     "guava",
     "kiwi",
     "kumquat",
     "citron",
     "lime",
     "lychee",
     "mandarin",
     "mango",
     "nektarin",
     "apelsin",
     "pomelo",
     "papaya",
     "passionsfrukt",
     "persika",
     "päron",
     "physalis",
     "ananas",
     "plommon",
     "hallon",
     "satsuma",
     "stjärnfrukt",
     "jordgubbe", "vattenmelon"]

    current_fruit = frukter[randint(0, len(frukter))]
    # current_fruit = choice(frukter)
    guesses = 0

    while guesses < 10:
        # Hints
        if guesses == 3:
            print("Ordets längd", len(current_fruit))

        if guesses == 5:
            print("Första bokstaven är: ", current_fruit[0])

        # Game mechanic
        guess = str(input("Gissa frukten:"))
        if guess.lower() == current_fruit:
            print("Du vann!")
            return
        else:
            print("Försök igen ;)")

        guesses += 1

    print("Inga försök kvar...")


# fruit_guess()


# ----------------------------- Guess the number? -----------------------------
def number_guess(upper_bound):

    c_num = randint(0, upper_bound)
    number_of_guesses = 10

    counter = 0
    while 0 < number_of_guesses:
            guess = int(input("What do you guess?"))

            if guess < 0:
                print("Bara positiva tal!")
            else:
                if guess == c_num:
                    print("Du vann")
                    return
                elif guess < c_num:
                    print("Gissa lite högre")
                else:
                    print("Gissa lite lägre")

            counter += 1
            print("Gissningar kvar:", number_of_guesses - counter)
            print("------------------------------------------------------------------")


number_guess(100)

