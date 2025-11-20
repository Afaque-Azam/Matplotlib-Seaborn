import matplotlib.pyplot as plt

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
tendulkar =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

with plt.xkcd():
    plt.plot(years, kohli, color = 'orange', label = "Virat Kohli")
    plt.plot(years, sehwag, color = 'green', label = "Virender Sehwag")
    plt.plot(years, tendulkar, color = 'blue', label = "Sachin Tendulkar")
    
    plt.xlabel("Year")
    plt.ylabel("Runs Scored")
    plt.title("Performance Comparison")
    plt.grid(True)
    plt.legend()
    
    plt.show()