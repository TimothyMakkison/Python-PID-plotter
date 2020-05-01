dt = 0.1
goal = 10
iterations = 100


def pid_data(kp,ki,kd):
    integral = 0
    priorerror = 0
    velocity = 0

    current = 0
    array = [current]
    for i in range(iterations):
        error = goal - current

        integral += dt * error
        differential = (error- priorerror)/dt
        priorerror = error

        change = kp * error + ki * integral + kd * differential
        velocity += change
        current += velocity * dt
        array.append(current)
    return array



#Add a new array for a new line
pid_settings = [[0.5, 0.1, 0.05], 
                [0.4 ,0,0],
                [0.01,0.1,0],
                ]





import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
plt.axhline(y=10, color='r', linestyle='-')

for i in pid_settings:
    plt.plot(pid_data(i[0],i[1],i[2]), label = f'{i[0]}, {i[1]}, {i[2]}')

plt.ylim(-5,15)
plt.legend()

plt.show()