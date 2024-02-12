from plotille import Figure


def generate_plot(x_pts: list[float], y_pts: list[float]) -> None:
    fig = Figure()
    fig.color_mode = "byte"
    fig.height = 15
    fig.width = 90
    fig.plot(X=x_pts, Y=y_pts, lc=25, label="Trajectory")
    print(fig.show(legend=True))
