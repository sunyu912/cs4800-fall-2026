import random
from sklearn import svm

prev1 = 1
prev2 = 2

input_data = [
    [1, 2],
    [2, 3],
    [3, 1]
]

output_data = [
    3,
    1,
    2
]

model = svm.SVC()

while True:
    player = int(input("1=Rock, 2=Paper, 3=Scissors: "))

    # The model to apply to the computer player
    # predict the next play from the human player
    model.fit(input_data, output_data)
    predicted_play = model.predict([[prev1, prev2]])[0]
    print("Predicted Play: ", predicted_play)
    computer = 1
    if predicted_play == 1:
        computer = 2
    elif predicted_play == 2:
        computer = 3

    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")
    elif (
        (player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)
    ):
        print("You win!")
    elif player in [1, 2, 3]:
        print("You lose!")
    else:
        print("Invalid input.")

    # update the human player records
    input_data.append([prev1, prev2])
    output_data.append(player)
    prev1 = prev2
    prev2 = player
