const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        reject('Promise 1 rejected');
    }, 3000);
});

const p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        // resolve('Promise 2 resolved');
        reject('Promise 2 rejected');
    }, 3000);
});

const p3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        reject('Promise 3 rejected');
    }, 1000);
});

Promise.any([p1, p2, p3])
    .then((results) => {
        console.log(results);
    })
    .catch((error) => {
        console.error('One of the promises rejected:', error);
    });


