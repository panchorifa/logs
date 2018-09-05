const re = /\[(.*)\]\s"(.*)"\s(\d{3})\s(\d*)/

const topResources = (logs, top=10) => {
  const results = {}
  for(let line of logs.split('\n')) {
    if(line.trim().length) {
      const [,, req, status, bytes,,] = re.exec(line.trim())
      const [method, resource,] = req.split(' ')
      if(method === 'GET' && status === '200') {
        if(!(resource in results)) {
          results[resource] = {bytes: 0, occurrences: 0}
        }
        results[resource] = {
          bytes: results[resource].bytes + parseInt(bytes),
          occurrences: results[resource].occurrences + 1
        }
      }
    }
  }
  const sortedLogs = Object.keys(results).sort( (a, b) => {
    if(results[b].occurrences > results[a].occurrences) return 1
    if(results[b].occurrences < results[a].occurrences) return -1
    if(results[b].bytes > results[a].bytes) return 1
    if(results[b].bytes < results[a].bytes) return -1
    if(b > a) return -1
    return 1
  })
  return sortedLogs.map(k => {return {[k]: results[k]}}).slice(0, top)
}

module.exports = topResources
