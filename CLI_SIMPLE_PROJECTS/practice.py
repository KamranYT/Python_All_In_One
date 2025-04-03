from graphics import *
import time

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 20


def erase_objects(win, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = win.getMouse().getX()
    mouse_y = win.getMouse().getY()

    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find things that overlap with our eraser
    for obj in win.items:
        if obj != eraser:
            if isinstance(obj, Rectangle):
                if (
                    obj.getP1().getX() <= right_x
                    and obj.getP2().getX() >= left_x
                    and obj.getP1().getY() <= bottom_y
                    and obj.getP2().getY() >= top_y
                ):
                    obj.setFill("white")


# There is no need to edit code beyond this point


def main():
    win = GraphWin("Drawing Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE  # Figure out how many columns of cells we need

    # Make a grid of squares based on the number of rows and columns.
    # The rows and columns along with our cell size help determine where
    # each individual cell belongs in our grid!
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = (
                left_x + CELL_SIZE
            )  # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = (
                top_y + CELL_SIZE
            )  # The bottom coordinate of the cell is CELL_SIZE pixels away from the top

            # Create a single cell in the grid
            cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            cell.setFill("blue")
            cell.draw(win)

    # Wait for initial click
    win.getMouse()

    # Create eraser
    last_click = win.getMouse()
    eraser = Rectangle(
        Point(last_click.getX(), last_click.getY()),
        Point(last_click.getX() + ERASER_SIZE, last_click.getY() + ERASER_SIZE),
    )
    eraser.setFill("pink")
    eraser.draw(win)

    # Move the eraser and erase
    while True:
        mouse = win.getMouse()
        eraser.move(
            mouse.getX() - eraser.getP1().getX(), mouse.getY() - eraser.getP1().getY()
        )
        erase_objects(win, eraser)
        time.sleep(0.05)


if __name__ == "__main__":
    main()
