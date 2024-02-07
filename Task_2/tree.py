import turtle

def draw_tree(branch_length, level):
    if level <= 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_tree(branch_length / 1.414, level - 1) 
        turtle.right(90)
        draw_tree(branch_length / 1.414, level - 1)
        turtle.left(45)
        turtle.backward(branch_length)

def initialize_turtle():
    turtle.up()
    turtle.left(90)
    turtle.backward(300)
    turtle.down()
    turtle.speed('fastest')
    turtle.hideturtle()

def main():
    recursion_level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))  
    initialize_turtle()
    draw_tree(150, recursion_level)  
    turtle.done()
    
main()