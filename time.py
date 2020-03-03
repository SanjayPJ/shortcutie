import time

localtime = time.localtime();

result = time.strftime("%I:%M:%S %p", localtime)

print(result)

time.sleep(2)
