import re

def top_resources(logs, top=10):
    results = {}
    for line in logs.split('\n'):
        if len(line.strip()) > 0:
            m = re.search(r"\[(.*)\] \"(.*)\" (\d{3}) (\d*)", line)
            [method, resource, protocol] = m.group(2).split(' ')
            status, bytes = int(m.group(3)), int(m.group(4))
            if method == 'GET' and status == 200:
                if resource not in results:
                    results[resource] = (0, 0)
                results[resource] = (results[resource][0] + 1, #occurrences
                                     results[resource][1] + bytes) #bytes
    return sorted(results.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))[0:top]
