import psutil

#aapko kaam karna hai ki user se cpu threshold lo
#current cpu percentage check karo
#agar current cpu percentage threshold se jyada hai to email karo


def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU threshold "))

    current_cpu = psutil.cpu_percent(interval=1)

    print("Current CPU %: ", current_cpu)

    if current_cpu > cpu_threshold:
        print("CPU Alert : Email sent to the admin")
    else:
        print("CPU usage is within the threshold.")

check_cpu_threshold()