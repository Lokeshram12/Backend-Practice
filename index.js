const express = require('express')
const app = express()
const port = 3000

app.get('/sample', (req, res) => {
  res.send('Hello World from sample!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
