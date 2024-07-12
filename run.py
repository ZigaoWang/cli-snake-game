import Game


def main():
    menu = Game.Menu()
    score_board = Game.ScoreBoard()
    play = Game.Play("█", "░")

    while True:
        menu.start

        if menu.selected_item == 0:
            try:
                play.start
            except:
                pass
            score_board.add_score(play.score[:])
        elif menu.selected_item == 1:
            score_board.start
        else:
            break


if __name__ == "__main__":
    main()
