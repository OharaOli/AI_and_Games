"""
A mancala bot that gives random legal moves to play
"""

import random

legal_moves = []

class Board:

    north_score = 0
    south_score = 0

    north_row = [7, 7, 7, 7, 7, 7, 7]
    south_row = [7, 7, 7, 7, 7, 7, 7]

    # Initiliases board from a message string if given
    def Board(self, message_str=None):

        if message_str:
            self.parseMessage(message)

    # Set up the board from an array in form of:
    # [player_one_score, pit, pit, pit, pit, pit, pit, pit,
    #  pit, pit, pit, pit, pit, pit, pit, player_two_score]
    def updateBoard(self, board_array):
        self.north_score = int(board_array[7])
        self.south_score = int(board_array[15])

        # need to reverse north row so it stored from perspective of north player
        self.north_row = [int(x) for x in board_array[0:7]]
        self.south_row = [int(x) for x in board_array[8:15]]

    # Checks if a move is legal given a player
    def checkMoveLegal(self, pit_no, player):
        # print(player)
        if player == "North":
            if self.north_row[pit_no - 1] > 0:
                # print("N False")
                return True
            else:
                # print("N True")
                return False
                
        elif player == "South":
            if self.south_row[pit_no - 1] > 0:
                # print("s False")
                return True
            else:
                # print("s True")
                return False
                

def minimax():
    global legal_moves

    if(legal_moves):
        f = open("legalmoves.txt", "a")
        for i in range(len(legal_moves)):
            f.write(str(legal_moves[i]) + " ")
        f.write("\n")
        f.close()

"""
Parses a message from the game engine and updates a given board with it

Returns a tuple containing
        "YOU" if it is your turn to play OR,
        "OPP" if opponent to play OR,
        "END" if game had ended
        AND
        the updated board
"""
def parseMessage(message_str, board, player):
    message = message_str.split(";")

    if message[0] == "CHANGE":
        board.updateBoard(message[2].split(","))
        if message[3] == "YOU":
            return "YOU", board
        else:
            return "OPP", board
    elif message[0] == "START":
        # this should never happen but it is here for the sake of completeness
        pass
    elif message[0] == "END":
        return "END", board


"""
Creates a move message with a random, legal move on a given Board for a given Player
"""
def createMoveMessage(board, player):
    # Keep trying random moves until one of them is legal
    while True:
        move_no = random.randint(1,7)
        moves = [1,2,3,4,5,6,7]
        global legal_moves
        legal_moves = []

        for i in range(len(moves)):
            if(board.checkMoveLegal(moves[i], player)):
                legal_moves.append(moves[i])

        if board.checkMoveLegal(move_no, player):
            return "MOVE;" + str(move_no)


def main():

    #Clear file which stores legal moves
    f = open("legalmoves.txt", "w")
    f.write("The legal moves possible are : \n")
    f.close()

    board = Board()
    player = "North"

    # get first message to check if we are north or south player
    message_str = input()
    message = message_str.split(";")
    if message[1] == "South":
        player = "South"
        print(createMoveMessage(board, player))

    while True:
        message_str = input()
        message, board = parseMessage(message_str, board, player)
        if message == "YOU":
            print(createMoveMessage(board, player))
        elif message == "OPP":
            pass
        elif message == "END":
            exit(0)
        minimax()


if __name__ == "__main__":
    main()