''' 
this module contains files to assist with the completion and testing of Assignment 1B CTPS 2025
'''

def move(robot_position, object_positions):
    '''
    Moves a robot position one tile towards the first object in the object positions list.

    Inputs:
        robot_position: The position described as an (x, y) tuple.
        object_positions: A list of (x, y) tuples describing the position of each object.

    Returns:
        The new robot position after moving one tile towards the first object.
    
    '''

    # select object to move towards
    object_position = object_positions[0]
    
    # computing displacement
    (x_r, y_r) = robot_position
    (x_o, y_o) = object_position
    displacement_x = x_o - x_r
    displacement_y = y_o - y_r
    
    # moving
    if displacement_y > 0:
        return (x_r, y_r + 1)
    elif displacement_x < 0:
        return (x_r - 1, y_r)
    elif displacement_y < 0:
        return (x_r, y_r - 1)
    elif displacement_x > 0:
        return (x_r + 1, y_r)




def collect(robot_position, object_positions):
    '''
    Removes an object from the object_positions list as the robot collects the object. 
    Robot must be in the same location as one of the objects.

    Inputs:
        robot_position: The position described as an (x, y) tuple.
        object_positions: A list of (x, y) tuples describing the position of each object.

    Returns:
        The new object positions lsit after collecting an object.
    
    '''

    
    new_positions = object_positions.copy()
    new_positions.remove(robot_position)
    return new_positions



def initialise_positions(rng_seed, n_objects):
    '''
    Initialises positions for the robot and objects at the start of a simulation.

    Inputs:
        rng_seed: A seed to use for random number generation. Seeding ensures repeatable results.
        n_objects: An integer stating the number of objects to create.

    Returns:
        robot_position: The position described as an (x, y) tuple.
        object_positions: A list of (x, y) tuples describing the position of each object.
    
    '''


    
    # importing random module and setting rng_seed
    import random
    random.seed(rng_seed)

    # creating object positions list
    object_positions = set()
    while len(object_positions) < n_objects:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        object_positions.add((x, y))
    object_positions = list(object_positions)

    # randomly initialising robot position
    while True:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        robot_position = (x, y)
        if robot_position not in object_positions:
            break
    
    # visualise board
    """
    if visualise:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        object_x_coordinates = [ x for (x,y) in object_positions ]
        object_y_coordinates = [ y for (x,y) in object_positions ]
        scat = ax.scatter(robot_position[0], robot_position[1], c = "b")
        scat2 = ax.scatter(object_x_coordinates, object_y_coordinates, c = "r", marker = '*')
        ax.set_xlim(-0.5, 99.5)
        ax.set_ylim(-0.5, 99.5)
        ax.set_xlabel('x-coordinate')
        ax.set_ylabel('y-coordinate')
        ax.set_title('Initial robot and object positions')
        """
    
    return robot_position, object_positions



def animate_robot(robot_position_list, object_positions_list):
    import IPython.display
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    
    iterations = len(robot_position_list)
    
    # Create a Plotting surface so that we can visualize the resulting position
    fig, ax = plt.subplots()
    robot_position = robot_position_list[0]
    object_positions = object_positions_list[0]
    object_x_coordinates = [ x for (x,y) in object_positions ]
    object_y_coordinates = [ y for (x,y) in object_positions ]
    
    scat = ax.scatter(robot_position[0], robot_position[1], c = "b")
    scat2 = ax.scatter(object_x_coordinates, object_y_coordinates, c = "r", marker = '*')
    ax.set_xlim(-1, 100)
    ax.set_ylim(-1, 100)

    # This function performs one time step of the simulation and then updates the plot to show the x,y coordinates of the new positions
    def animate(i):
        #ax.set_title(f't = {i} seconds')
        scat.set_offsets(robot_position_list[i])
        object_positions = object_positions_list[i]
        if object_positions:
            scat2.set_offsets(object_positions)
        else:
            scat2.set_offsets([None,None])

        return (scat, scat2)

    # We are going to create a video animation of the simulation that runs for 1000 iterations, one video frame per iteration, displayed at 20 frames per second
    robot_animation = animation.FuncAnimation(fig, animate, frames=iterations, interval=50)
    plt.close(fig)
    video = robot_animation.to_jshtml()
    #video = robot_animation.to_html5_video()
    html = IPython.display.HTML(video)
    IPython.display.display(html)


# need marking code here for correctness
