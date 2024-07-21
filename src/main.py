import time

from GUI import GUI


def main():

    gui = GUI(1200, 600)

    gui.menu()
    while not gui.game.is_over:
        # Clear Elements
        gui.canvas.delete("all")
        # Update state
        gui.game.update()
        # Draw elements
        gui.draw()

        time.sleep(0.04)

        gui.root.update_idletasks()
        gui.root.update()

    gui.game_over()
    print("Game over.")


if __name__ == "__main__":
    main()
