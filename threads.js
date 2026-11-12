const path = require('path');

const express = require('express');

const { Worker } = require('worker_threads');

const app = express();

const port = process.env.PORT || 3000;

app.get("/non-blocking", (req, res) => {
    setTimeout(() => {
        res.send("Non-blocking response after 3 seconds");
    }, 3000);
});

app.get("/blocking", (req, res) => {
    const worker = new Worker(path.join(__dirname, 'worker.js'));
    worker.on('message', (result) => {
        console.log(`Result from worker: ${result}`);
        res.send(`Blocking response with worker result: ${result}`);
    });
    worker.on('error', (err) => {
        console.error(err);
        res.status(500).send('Worker failed');
    });
});


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

