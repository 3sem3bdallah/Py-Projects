from statistics import mode, median
import scipy.stats as stats
import matplotlib.pyplot as plt

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data):
    return mode(data)

def calculate_range(data):
    return max(data) - min(data)

def calculate_mid_range(data):
    return (max(data) + min(data)) / 2

def calculate_mad(data, mean):
    return sum(abs(x - mean) for x in data) / len(data)

def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def calculate_std_dev(variance):
    return variance ** 0.5

def calculate_coefficient_of_variation(mean, std_dev):
    return (std_dev / mean) * 100

def calculate_quartiles(data):
    sorted_data = sorted(data)
    n = len(data)
    Q1 = median(sorted_data[:n//2])
    Q3 = median(sorted_data[(n+1)//2:])
    return Q1, Q3

def calculate_interquartile_range(Q1, Q3):
    return Q3 - Q1

def calculate_lower_fence(Q1, IQR):
    return Q1 - 1.5 * IQR

def calculate_upper_fence(Q3, IQR):
    return Q3 + 1.5 * IQR

def plot_data(data):
    sorted_data = sorted(data)
    n = len(data)
    
    # Frequency distribution
    thisdict = {}
    for value in data:
        if value in thisdict:
            thisdict[value] += 1
        else:
            thisdict[value] = 1
    list2 = list(thisdict.keys())
    list1 = list(thisdict.values())
    
    # Pie Chart
    list3 = [(freq / n) * 100 for freq in list1]
    plt.pie(list3, labels=list2, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(list2))))
    plt.title("Pie Chart")
    plt.show()
    
    # Bar Chart
    plt.figure(figsize=(6,4))
    plt.bar(list2, list1, color="skyblue", edgecolor="black")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Bar Chart")
    plt.tight_layout()
    plt.show()
    
    # Scatter Plot
    plt.scatter(list2, list1, color="blue", marker="o", s=50)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Scatter Plot")
    plt.tight_layout()
    plt.show()
    
    # Box Plot
    Q1, Q3 = calculate_quartiles(data)
    IQR = calculate_interquartile_range(Q1, Q3)
    lower_fence = calculate_lower_fence(Q1, IQR)
    upper_fence = calculate_upper_fence(Q3, IQR)
    
    outliers = [x for x in data if x > upper_fence or x < lower_fence]
    
    plt.boxplot(data, vert=False, patch_artist=True)
    plt.scatter(outliers, [0]*len(outliers), color="red")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Box Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    data = list(map(int, input("Enter numbers separated by space:\n").split()))

    # Calculate statistics
    mean = calculate_mean(data)
    median_value = calculate_median(data)
    mode_value = calculate_mode(data)
    data_range = calculate_range(data)
    mid_range = calculate_mid_range(data)
    mad = calculate_mad(data, mean)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(variance)
    coeff_of_var = calculate_coefficient_of_variation(mean, std_dev)
    Q1, Q3 = calculate_quartiles(data)
    IQR = calculate_interquartile_range(Q1, Q3)
    lower_fence = calculate_lower_fence(Q1, IQR)
    upper_fence = calculate_upper_fence(Q3, IQR)

    # Display statistics
    print(f"\nMean: {mean:.2f}")
    print(f"Median: {median_value:.2f}")
    print(f"Mode: {mode_value}")
    print(f"Range: {data_range}")
    print(f"Mid Range: {mid_range:.2f}")
    print(f"M.A.D: {mad:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Coefficient of Variation: {coeff_of_var:.2f} %")
    print(f"Lower Quartile (Q1): {Q1}")
    print(f"Upper Quartile (Q3): {Q3}")
    print(f"Interquartile Range (IQR): {IQR}")
    print(f"Lower Fence: {lower_fence}")
    print(f"Upper Fence: {upper_fence}")

    # Plot data
    plot_data(data)

if __name__ == "__main__":
    main()